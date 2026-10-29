"""
Simulador de entrevistas · Caso Horizonte Hoteles (BC1 MDA14Oct · ISDI)
Autores: Martín Bellido y Miguel Taboada

Secrets necesarios (en Streamlit Cloud → Settings → Secrets):
    OPENAI_API_KEY = "sk-..."
    APP_PASSWORD   = "..."
    OPENAI_MODEL   = "gpt-4.1-mini"   # opcional; este es el valor por defecto
"""

import hmac
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import streamlit as st
from openai import OpenAI

# ---------------------------------------------------------------------------
# Configuración (cambia aquí los límites si lo necesitas)
# ---------------------------------------------------------------------------
MAX_TURNOS = 30          # preguntas máximas por conversación
MAX_CARACTERES = 800     # longitud máxima de cada pregunta
MODELO_POR_DEFECTO = "gpt-4.1-mini"

PERSONAJES = {
    "Julia": "Equipo de datos",
    "Carmen": "Directora General",
    "Roberto": "Director de Operaciones",
    "Elena": "Experiencia del Huésped",
    "Marcos": "Revenue",
}

BASE = Path(__file__).parent
ZONA = ZoneInfo("Europe/Madrid")

st.set_page_config(page_title="Horizonte Hoteles · Simulador BC1", page_icon="🏨")


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def cabecera():
    st.title("🏨 Horizonte Hoteles")
    st.markdown("**Simulador de entrevistas · Business Case 1 · MDA14Oct**")
    st.caption("ISDI · Creado por Martín Bellido y Miguel Taboada")


def cargar_system_prompt() -> str:
    # Se lee en cada ejecución (son archivos pequeños) para que cualquier
    # cambio subido a GitHub se aplique sin reiniciar la app.
    instrucciones = (BASE / "instrucciones.md").read_text(encoding="utf-8")
    conocimiento = (BASE / "conocimiento.md").read_text(encoding="utf-8")
    return f"{instrucciones}\n\n---\n\n# CONOCIMIENTO DEL CASO\n\n{conocimiento}"


@st.cache_resource
def cliente_openai() -> OpenAI:
    return OpenAI(api_key=st.secrets["OPENAI_API_KEY"], timeout=60, max_retries=2)


def exportar_markdown(mensajes: list) -> str:
    ahora = datetime.now(ZONA).strftime("%d/%m/%Y %H:%M")
    lineas = [
        "# Horizonte Hoteles · Entrevistas BC1 MDA14Oct",
        f"Exportado el {ahora}",
        "",
    ]
    for m in mensajes:
        if m["role"] == "user":
            lineas += ["---", "", f"**Pregunta a {m['personaje']}:** {m['content']}", ""]
        else:
            lineas += [m["content"], ""]
    return "\n".join(lineas)


# ---------------------------------------------------------------------------
# Acceso con contraseña
# ---------------------------------------------------------------------------
if not st.session_state.get("autenticado"):
    cabecera()
    with st.form("login"):
        clave = st.text_input("Contraseña", type="password")
        entrar = st.form_submit_button("Entrar")
    if entrar:
        if hmac.compare_digest(clave.strip(), str(st.secrets["APP_PASSWORD"])):
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta.")
    st.stop()


# ---------------------------------------------------------------------------
# Estado de la sesión
# ---------------------------------------------------------------------------
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []

mensajes = st.session_state.mensajes
turnos = sum(1 for m in mensajes if m["role"] == "user")


# ---------------------------------------------------------------------------
# Barra lateral
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("¿Con quién hablas?")
    personaje = st.radio(
        "Personaje",
        list(PERSONAJES),
        format_func=lambda n: f"{n} · {PERSONAJES[n]}",
        label_visibility="collapsed",
    )
    st.divider()
    st.caption(f"Preguntas en esta conversación: {turnos}/{MAX_TURNOS}")
    st.download_button(
        "⬇️ Descargar conversación",
        data=exportar_markdown(mensajes),
        file_name=f"horizonte_entrevistas_{datetime.now(ZONA):%Y%m%d_%H%M}.md",
        mime="text/markdown",
        disabled=not mensajes,
    )
    if st.button("🔄 Reiniciar conversación"):
        st.session_state.mensajes = []
        st.rerun()
    st.caption("Descarga la conversación antes de reiniciar o cerrar la pestaña: no se guarda en ningún sitio.")


# ---------------------------------------------------------------------------
# Página principal
# ---------------------------------------------------------------------------
cabecera()
st.markdown(
    "Puedes entrevistar a **Julia, Carmen, Roberto, Elena y Marcos** para descubrir "
    "la situación actual y las necesidades de datos de la empresa. Elige a la persona "
    "en el panel lateral y pregunta. Puedes cambiar de interlocutor cuando quieras: "
    "la conversación se mantiene.\n\n"
    "El simulador no da la solución ni vuelca el diagnóstico de golpe: tendrás que "
    "investigar preguntando. Martín y Miguel están observando, con mirada pedagógica "
    "pero implacable."
)
st.caption(
    f"Máximo {MAX_TURNOS} preguntas por conversación y {MAX_CARACTERES} caracteres por pregunta. "
    "No introduzcas datos personales."
)

for m in mensajes:
    if m["role"] == "user":
        with st.chat_message("user"):
            st.caption(f"→ {m['personaje']}")
            st.markdown(m["content"])
    else:
        with st.chat_message("assistant", avatar="🏨"):
            st.markdown(m["content"])

if turnos >= MAX_TURNOS:
    st.warning(
        "Has llegado al máximo de preguntas de esta conversación. "
        "Descárgala y pulsa «Reiniciar conversación» para empezar otra."
    )

pregunta = st.chat_input(
    f"Pregunta a {personaje}…",
    max_chars=MAX_CARACTERES,
    disabled=turnos >= MAX_TURNOS,
)

if pregunta and pregunta.strip():
    pregunta = pregunta.strip()

    with st.chat_message("user"):
        st.caption(f"→ {personaje}")
        st.markdown(pregunta)

    # Mensajes para la API: system prompt fijo (aprovecha la caché de OpenAI)
    # y la etiqueta del personaje activo dentro de cada pregunta.
    api_mensajes = [{"role": "system", "content": cargar_system_prompt()}]
    for m in mensajes + [{"role": "user", "content": pregunta, "personaje": personaje}]:
        if m["role"] == "user":
            api_mensajes.append(
                {"role": "user", "content": f"[Personaje activo: {m['personaje']}]\n{m['content']}"}
            )
        else:
            api_mensajes.append({"role": "assistant", "content": m["content"]})

    respuesta = None
    with st.chat_message("assistant", avatar="🏨"):
        try:
            stream = cliente_openai().chat.completions.create(
                model=st.secrets.get("OPENAI_MODEL", MODELO_POR_DEFECTO),
                messages=api_mensajes,
                stream=True,
            )

            def trozos():
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        yield chunk.choices[0].delta.content

            respuesta = st.write_stream(trozos())
        except Exception as e:  # noqa: BLE001
            print(f"[ERROR OpenAI] {type(e).__name__}: {e}")  # visible en los logs de Streamlit Cloud
            st.error(
                "No he podido obtener respuesta en este momento. Espera unos segundos y "
                "vuelve a enviar la pregunta. Si el problema continúa, avisa a tus profesores."
            )

    # Solo se guarda el intercambio si hubo respuesta: si falla, el alumno puede reintentar.
    if isinstance(respuesta, str) and respuesta.strip():
        mensajes.append({"role": "user", "content": pregunta, "personaje": personaje})
        mensajes.append({"role": "assistant", "content": respuesta})
        st.rerun()
