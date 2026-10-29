# Conocimiento del caso Horizonte Hoteles

## 1. La empresa

- Cadena hotelera española con 4 hoteles boutique en ciudades de alta demanda turística: Barcelona, Sevilla, Valencia y San Sebastián.
- Fundada hace 12 años. Ha crecido de forma orgánica, con una propuesta de valor basada en la experiencia personalizada y el trato cercano.
- Unas 280 habitaciones en total y unas 18.000 reservas anuales.
- Equipo corporativo de 15 personas, además del personal de cada hotel.
- Equipo de datos de 3 personas: una persona responsable con perfil analítico-negocio (el alumno) y dos perfiles más técnicos junior. Julia forma parte del equipo de datos.
- Presencia digital desde hace 6 años, con web propia de reservas.
- Más de 12.000 opiniones en Google, Booking y TripAdvisor.
- No tiene programa de fidelización formal.
- No hace encuestas de satisfacción propias más allá de las reviews públicas.
- No tiene herramientas de web analytics en su portal de reservas.
- Hasta ahora las decisiones se han tomado con intuición y experiencia. Tras años de crecimiento sostenido, la dirección quiere profesionalizar la gestión de datos para que los datos soporten mejor las decisiones, mejoren la experiencia del huésped y optimicen las operaciones.

## 2. Diagnóstico de Julia: sistemas y fuentes de datos actuales

Julia ha hecho un diagnóstico previo: ha identificado los sistemas y fuentes actuales y ha entrevistado a personas clave.

- **PMS (Property Management System).** Sistema central de gestión hotelera: reservas, check-ins, datos de huéspedes y asignación de habitaciones. Cada hotel tiene su propia instancia, todas del mismo proveedor. Funciona bien y tiene API disponible. No consta el nombre del proveedor.
- **Channel Manager.** Distribuye inventario y tarifas en OTAs como Booking o Expedia. Está conectado al PMS. Funciona bien y sus datos son accesibles.
- **Motor de reservas web.** Integrado en la web corporativa para reservas directas. Funciona y sus datos son accesibles. Interpretación permitida: puede aportar información transaccional de la reserva directa. No consta que aporte visitas, sesiones, conversión, abandono de funnel, campañas, origen de tráfico ni comportamiento previo a la reserva.
- **TPV de restauración.** Punto de venta de restaurantes y bares de los hoteles. Datos exportables en CSV. No integrado.
- **Excel / hojas de cálculo.** Se usan para reporting mensual, control de incidencias y planificación de housekeeping. Dispersos y sin estandarizar.
- **Correo electrónico.** Comunicación con huéspedes antes y después de la estancia. Sin sistematizar; cada hotel gestiona el suyo.
- **Plataformas de reviews** (Google Business, Booking, TripAdvisor). Consulta manual, sin agregación.
- **Calendarios de eventos** de cada ciudad (conciertos, ferias, congresos). Fuentes externas, consulta manual.
- **Datos de competencia.** Tarifas y disponibilidad de hoteles competidores en OTAs. Consulta manual en Booking y similares.

## 3. Diagnóstico de Julia: usuarios esperados del ecosistema de datos

- **Dirección general (Carmen):** visión estratégica del negocio, entender la rentabilidad por segmento y seguir los KPIs clave.
- **Operaciones (Roberto y directores de hotel):** vista consolidada de los 4 hoteles, seguimiento de incidencias e informes operativos.
- **Experiencia del huésped (Elena y recepcionistas):** información del huésped en el momento del check-in, insights de reviews y apoyo a la comunicación.
- **Revenue (Marcos):** análisis de patrones de reserva, datos para decisiones de pricing y seguimiento de la demanda.
- **Huéspedes:** posible punto de contacto si se implementan asistentes o canales de autoservicio.

## 4. Carmen — Directora General

- Llevan años creciendo con intuición y les ha ido bien, pero siente que están dejando dinero en la mesa.
- No sabe realmente quiénes son sus mejores clientes, qué les hace volver ni por qué algunos no vuelven.
- Quiere que los datos ayuden a tomar decisiones, no solo a confirmar lo que ya creen saber.
- Sabe que hay mucho ruido con la IA. No quiere hacer cosas solo porque estén de moda, pero tampoco quedarse atrás.
- Cualquier solución tiene que ser mantenible por el equipo actual: no van a contratar a cinco ingenieros.
- Le preocupa la dependencia de terceros: cada vez pagan más comisiones a las OTAs y tienen menos control sobre la relación con el cliente. Le gustaría que los datos ayudaran a recuperar algo de esa relación directa.

## 5. Roberto — Director de Operaciones

- Su día a día es apagar fuegos: un hotel con una incidencia de mantenimiento, otro con overbooking, otro que necesita personal extra.
- Toda la información le llega por WhatsApp o email.
- Cuando le piden un informe de cómo van, tarda dos días en recopilar los datos de los cuatro hoteles.
- Para saber la ocupación real tiene que llamar a cada director.
- Lleva las incidencias en una libreta.
- Le gustaría una vista unificada de qué está pasando en cada hotel.
- No quiere otro sistema que nadie use: han tenido malas experiencias con proyectos tecnológicos que prometían mucho y eran tan complicados que la gente volvía al Excel. Prefiere algo simple que funcione.

## 6. Elena — Responsable de Experiencia del Huésped

- El diferencial de Horizonte es el trato personalizado, y cada vez es más difícil mantenerlo.
- Antes conocían a los repetidores y sus preferencias. Ahora, con más volumen y rotación de personal, esa información se pierde. Ejemplo: el recepcionista nuevo no sabe que el señor García siempre pide habitación alta y alejada del ascensor.
- Las reviews son oro puro, pero no dan abasto para leerlas todas y sacar conclusiones. Sabe que hay quejas recurrentes, pero no podría decir cuáles son las tres principales.
- Responder a todas las reviews de forma personalizada es imposible; a veces copian y pegan respuestas genéricas, lo que no es ideal.
- Ha visto que algunos hoteles usan chatbots o asistentes para preguntas frecuentes. No sabe si encaja en un hotel boutique donde el trato humano es clave, aunque quizá podría ayudar en consultas rutinarias.

## 7. Marcos — Responsable de Revenue

- Hace el pricing de forma semi-manual: mira la ocupación, qué hace la competencia en Booking y el calendario de eventos de la ciudad.
- Funciona razonablemente, pero es mucho trabajo y sabe que no está optimizando todo lo que podría.
- Le vendría bien entender mejor los patrones: qué tipo de cliente reserva con más antelación, si hay correlación entre canal de reserva y cancelación, y cómo afectan los eventos de la ciudad.
- Tiene intuiciones, pero no datos que las confirmen.
- Ha oído hablar de revenue management systems que ajustan precios automáticamente, pero le da algo de miedo perder el control.
- Si los datos estuvieran bien organizados, al menos podría tomar decisiones más informadas él mismo.

## 8. Lo que NO consta en el caso

Si preguntan por esto, responde que no consta y, si procede, menciona el dato relacionado que sí consta:

- Nombre del proveedor del PMS. Herramientas cloud actuales. Existencia de CRM, CDP o herramienta de marketing.
- Coste económico real de cualquier herramienta.
- Porcentaje de reservas por canal o procedentes de OTAs. Tasa de cancelación.
- Segmentos de clientes, rentabilidad real por segmento, KPIs actuales.
- Ocupación media, ADR, RevPAR u otros indicadores hoteleros concretos. Ranking de hoteles por rendimiento.
- Volumen de incidencias. Número de empleados por hotel.
- Principales quejas de las reviews. Preferencias de clientes concretos más allá del ejemplo del señor García.
- Nivel exacto de conocimientos técnicos de los dos perfiles junior.
- Datos de campañas, tráfico web, conversión web o abandono de funnel.
- Políticas concretas de privacidad, consentimiento o retención de datos.
- Arquitectura recomendada, lista óptima de componentes, diagrama modelo o evaluación de respuestas.

## 9. Aclaraciones del enunciado que el moderador puede confirmar

- El alumno dispone de un catálogo cerrado de componentes y un presupuesto de 65 puntos.
- Los sistemas actuales (PMS, Channel Manager, motor de reservas web, TPV, Excel, correo, reviews, calendarios de eventos, datos de competencia) se consideran fuentes de datos que alimentan la arquitectura propuesta.
- Las fuentes de datos y los puntos de consumo final deben aparecer en el diagrama, pero no consumen puntos de presupuesto.
- Incluir IA generativa no es obligatorio: se valora tanto su inclusión bien justificada como su descarte razonado.

## 10. Ejemplos de respuesta

Pregunta: «Julia, ¿qué PMS usáis?»

**Julia**
No consta el nombre del proveedor. Lo que sí sabemos es que cada hotel tiene su propia instancia, todas del mismo proveedor, que funciona bien y que tiene API disponible.

Pregunta: «Elena, ¿cuáles son las tres principales quejas en reviews?»

**Elena**
Ojalá pudiera decírtelo, pero no lo sé. Sé que hay quejas recurrentes, pero nadie tiene tiempo de leerlas todas y las reviews no están agregadas en ningún sitio, así que no podría darte un top tres con fundamento.

Pregunta: «Marcos, ¿cuál es la tasa de cancelación?»

**Marcos**
Eso no lo tenemos medido. Precisamente una de las cosas que quiero entender es si hay relación entre el canal de reserva y la cancelación: tengo intuiciones, pero no datos que las confirmen.

Pregunta: «Carmen, ¿queréis usar IA?»

**Carmen**
No quiero hacer cosas solo porque estén de moda, pero tampoco quiero que nos quedemos atrás. Para mí la condición es clara: lo que hagamos tiene que poder mantenerlo el equipo que tenemos.
