# Análisis Estratégico del Marketplace Brasileño Olist mediante Data Analytics

## Proyecto Final de Data Analytics

**Autor:** Claudia Soler de la Cruz
---

# Índice

1. Resumen Ejecutivo
2. Introducción
3. Objetivos del Proyecto
4. Descripción del Proyecto
5. Metodología
6. Exploración Inicial de los Datos
7. Limpieza y Transformación de los Datos
8. Feature Engineering y Construcción del Dataset Analítico
9. Análisis Exploratorio de los Datos
10. Análisis Estadístico
11. Dashboard en Power BI
12. Principales Hallazgos de Negocio
13. Recomendaciones Estratégicas
14. Limitaciones del Proyecto
15. Líneas Futuras de Trabajo
16. Conclusiones
17. Bibliografía

---

# 1. Resumen Ejecutivo

El presente proyecto desarrolla un análisis integral del marketplace brasileño **Olist** mediante técnicas de **Data Analytics** y **Business Intelligence**, con el objetivo de comprender el comportamiento de compra de los clientes, evaluar el rendimiento operativo de la plataforma e identificar oportunidades de mejora desde una perspectiva estratégica.

Para ello se ha seguido un flujo completo de trabajo propio de un proyecto de analítica de datos, comenzando con la exploración y validación de múltiples fuentes de información, continuando con la limpieza y transformación de los datos, el desarrollo de nuevas variables mediante técnicas de *Feature Engineering*, la construcción de un dataset analítico y la realización de un análisis exploratorio y estadístico que permitiera extraer conocimiento útil para la toma de decisiones.

El proyecto se ha desarrollado utilizando Python como lenguaje principal para el tratamiento y análisis de los datos, apoyándose en librerías especializadas como Pandas, NumPy, Matplotlib y Seaborn. Finalmente, los resultados obtenidos se han integrado en un dashboard interactivo desarrollado en Power BI, diseñado específicamente para proporcionar una visión ejecutiva del negocio mediante indicadores clave de rendimiento (KPIs) y visualizaciones orientadas a facilitar la interpretación de los resultados.

El análisis realizado evidencia que Olist constituye un marketplace consolidado, con más de **99.000 pedidos**, una facturación superior a **15,8 millones de reales brasileños** y una operación logística altamente eficiente, caracterizada por un elevado porcentaje de entregas realizadas dentro del plazo previsto.

Asimismo, el estudio pone de manifiesto que el crecimiento del negocio durante el periodo analizado se encuentra impulsado principalmente por el incremento del volumen de pedidos, mientras que una parte significativa de la facturación procede de un grupo reducido de pedidos de elevado valor económico. Del mismo modo, se identifican oportunidades de negocio relacionadas con estrategias de *cross-selling*, optimización logística y expansión comercial en regiones con menor presencia dentro del marketplace.

Como resultado final, el proyecto proporciona una herramienta de análisis capaz de transformar datos operativos en información estratégica para apoyar la toma de decisiones por parte de la Dirección General.

---

# 2. Introducción

En los últimos años el comercio electrónico ha experimentado un crecimiento sostenido que ha transformado la forma en que empresas y consumidores interactúan. La digitalización de los procesos de compra ha generado un volumen cada vez mayor de información que, adecuadamente tratada y analizada, constituye una fuente de conocimiento de enorme valor para comprender el comportamiento de los clientes, optimizar los procesos internos y mejorar la competitividad empresarial.

En este contexto, el análisis de datos se ha convertido en un elemento estratégico dentro de las organizaciones, permitiendo convertir grandes volúmenes de información en conocimiento útil para la toma de decisiones. La aplicación de técnicas de Data Analytics y Business Intelligence facilita no solo la descripción del comportamiento histórico del negocio, sino también la identificación de patrones, tendencias y oportunidades de mejora que difícilmente podrían detectarse mediante métodos tradicionales.

El presente proyecto se centra en el estudio del marketplace brasileño **Olist**, una plataforma de comercio electrónico que conecta pequeños y medianos vendedores con diferentes canales de venta online. El conjunto de datos utilizado recoge información detallada sobre pedidos, clientes, productos, pagos y procesos logísticos realizados entre los años **2016 y 2018**, permitiendo analizar el funcionamiento global del marketplace desde múltiples perspectivas.

A diferencia de un análisis meramente descriptivo, este trabajo aborda el proyecto siguiendo una metodología completa de análisis de datos, abarcando todas las fases habituales de un proyecto profesional de Data Analytics: exploración inicial, validación de la calidad de los datos, limpieza, transformación, generación de nuevas variables, análisis exploratorio, análisis estadístico y comunicación de resultados mediante un dashboard interactivo.

El objetivo final no consiste únicamente en describir el comportamiento histórico del marketplace, sino en obtener conclusiones que puedan resultar útiles para la gestión estratégica del negocio. Para ello se analizan aspectos relacionados con la evolución de las ventas, el comportamiento de compra de los clientes, la estructura económica de los pedidos, la distribución geográfica de la demanda, el rendimiento logístico y la eficiencia del sistema de pagos, proporcionando una visión global del funcionamiento de la plataforma.

Finalmente, el proyecto culmina con el desarrollo de un dashboard interactivo en Power BI orientado a la Dirección General, diseñado para facilitar el seguimiento de los principales indicadores del negocio mediante una interfaz intuitiva, visual y enfocada a la toma de decisiones.

---

# 3. Objetivos del Proyecto

El objetivo principal de este proyecto consiste en realizar un análisis estratégico del marketplace brasileño Olist mediante técnicas de Data Analytics, transformando datos operativos en información de valor para apoyar la toma de decisiones empresariales.

Para alcanzar este objetivo general se plantean los siguientes objetivos específicos:

- Explorar la estructura y calidad de los distintos conjuntos de datos proporcionados por Olist.
- Detectar posibles problemas relacionados con valores nulos, duplicados, inconsistencias y errores de integridad referencial.
- Llevar a cabo un proceso completo de limpieza y transformación de los datos que permita construir un dataset consistente y preparado para el análisis.
- Diseñar e implementar nuevas variables mediante técnicas de *Feature Engineering* con el fin de enriquecer la información disponible y facilitar posteriores análisis de negocio.
- Analizar la evolución temporal de las ventas y del volumen de pedidos para identificar tendencias de crecimiento del marketplace.
- Estudiar el comportamiento de compra de los clientes desde diferentes perspectivas temporales, geográficas y económicas.
- Analizar la composición de los pedidos y el peso relativo de las distintas categorías de productos dentro del negocio.
- Evaluar el rendimiento logístico del marketplace mediante indicadores relacionados con tiempos de entrega, retrasos y cumplimiento de las fechas estimadas.
- Comprobar la consistencia entre los importes registrados en los pedidos y los pagos realizados por los clientes.
- Analizar estadísticamente las principales variables económicas y logísticas del dataset para identificar distribuciones, relaciones entre variables y posibles valores atípicos.
- Diseñar un dashboard interactivo en Power BI que permita monitorizar los principales indicadores del negocio mediante una interfaz orientada a la Dirección General.
- Extraer conclusiones estratégicas y proponer recomendaciones que puedan contribuir a mejorar el rendimiento comercial y operativo del marketplace.

---

# 4. Descripción del Proyecto

## 4.1 Contexto del proyecto

El presente trabajo desarrolla un proyecto integral de análisis de datos aplicado al marketplace brasileño **Olist**, una plataforma de comercio electrónico que conecta pequeños y medianos vendedores con diferentes canales de venta online.

El objetivo del proyecto consiste en transformar un conjunto de datos operativos en información estratégica que permita comprender el comportamiento del negocio, identificar patrones de compra, evaluar el rendimiento logístico de la plataforma y proporcionar una herramienta de apoyo a la toma de decisiones mediante un dashboard interactivo desarrollado en Power BI.

A diferencia de un análisis puramente descriptivo, el proyecto sigue el flujo completo habitual de un proceso de Data Analytics, comenzando con la exploración de los datos originales y finalizando con la construcción de un modelo analítico preparado para la visualización y comunicación de resultados.

Todo el desarrollo se ha realizado utilizando Python como lenguaje principal para el tratamiento y análisis de los datos, complementándose con Power BI para la construcción del cuadro de mando final.

---

## 4.2 Descripción del conjunto de datos

El proyecto utiliza el conocido dataset público **Brazilian E-Commerce Public Dataset by Olist**, disponible a través de Kaggle.

Este conjunto de datos recoge información real sobre pedidos realizados entre los años **2016 y 2018**, incluyendo información relacionada con clientes, pedidos, artículos vendidos, pagos, productos y categorías.

Con el objetivo de enriquecer el análisis temporal, se incorporó además un segundo dataset correspondiente al calendario oficial de festivos nacionales de Brasil, permitiendo estudiar el posible impacto de los días festivos sobre el comportamiento de compra de los clientes.

Los principales conjuntos de datos utilizados durante el proyecto fueron los siguientes:

| Dataset | Descripción |
|----------|-------------|
| Customers | Información de clientes y localización geográfica. |
| Orders | Información general de cada pedido y fechas del proceso logístico. |
| Order Items | Productos incluidos en cada pedido y costes de envío. |
| Payments | Métodos de pago, cuotas e importe pagado. |
| Products | Información de los productos vendidos. |
| Product Categories | Traducción de categorías de producto. |
| Holidays | Calendario oficial de festivos nacionales de Brasil. |

La integración de estas fuentes permitió construir un dataset analítico único con información económica, logística, temporal y geográfica para cada pedido.

---

## 4.3 Arquitectura del proyecto

Con el fin de facilitar la organización, reutilización y mantenimiento del código, el proyecto se estructuró siguiendo una arquitectura modular.

```text
Proyecto_Final_Data_Analytics/

data/
    raw/
    interim/
    processed/

notebooks/

src/

dashboard/

reports/

README.md

requirements.txt
```

Cada carpeta cumple una función específica dentro del flujo de trabajo:

- **raw** contiene los datos originales sin modificar.
- **interim** almacena los datasets ya limpiados y preparados para posteriores transformaciones.
- **processed** contiene el dataset analítico definitivo junto con diferentes tablas resumen generadas durante el análisis.
- **notebooks** documenta paso a paso todo el desarrollo del proyecto.
- **src** agrupa las funciones reutilizables empleadas durante el procesamiento y análisis de los datos.
- **dashboard** incluye el archivo Power BI y los recursos gráficos utilizados durante el diseño.
- **reports** almacena la documentación final del proyecto.

Esta estructura facilita la reproducibilidad del análisis y permite separar claramente los datos, el código y la documentación.

---

## 4.4 Herramientas utilizadas

El proyecto se desarrolló utilizando herramientas ampliamente empleadas en proyectos profesionales de análisis de datos.

| Herramienta | Utilidad |
|-------------|----------|
| Python | Procesamiento y análisis de datos |
| Pandas | Manipulación de datos |
| NumPy | Operaciones numéricas |
| Matplotlib | Visualización |
| Seaborn | Visualización estadística |
| Jupyter Notebook | Desarrollo del análisis |
| Visual Studio Code | Desarrollo del proyecto |
| Git | Control de versiones |
| GitHub | Publicación del proyecto |
| Power BI | Dashboard interactivo |

---

## 4.5 Flujo general del proyecto

El desarrollo siguió un flujo secuencial propio de un proyecto de Data Analytics.

1. Exploración inicial de los datos.
2. Validación de calidad.
3. Limpieza y transformación.
4. Feature Engineering.
5. Construcción del dataset analítico.
6. Análisis exploratorio.
7. Análisis estadístico.
8. Desarrollo del dashboard en Power BI.
9. Elaboración del informe final.

Cada una de estas etapas constituye un bloque independiente del proyecto y se documenta detalladamente en los capítulos posteriores.

---

# 5. Metodología

## 5.1 Enfoque metodológico

El proyecto se desarrolló siguiendo una metodología estructurada basada en las principales fases presentes en los procesos profesionales de Data Analytics.

En lugar de abordar directamente la construcción de visualizaciones o indicadores, se priorizó la calidad de los datos y la construcción de un modelo analítico consistente, garantizando que todas las conclusiones obtenidas estuvieran sustentadas sobre información previamente validada.

Este enfoque permitió minimizar posibles sesgos derivados de problemas de calidad de datos y asegurar la trazabilidad completa del proceso de análisis.

---

## 5.2 Exploración inicial de los datos

La primera fase consistió en realizar una exploración detallada de todos los conjuntos de datos originales.

Durante esta etapa se analizaron aspectos como:

- dimensiones de cada dataset;
- tipos de datos;
- estructura de las tablas;
- claves primarias y foráneas;
- distribución de valores nulos;
- duplicados;
- relaciones entre tablas;
- primeras estadísticas descriptivas.

El objetivo de esta fase fue comprender la estructura general del modelo de datos antes de realizar cualquier transformación.

---

## 5.3 Limpieza y transformación

Una vez analizados los datos originales, se procedió a su limpieza y normalización.

Las principales tareas desarrolladas fueron:

- conversión de fechas al formato datetime;
- homogeneización de tipos de datos;
- eliminación de columnas innecesarias;
- revisión de duplicados;
- comprobación de integridad referencial;
- validación de valores negativos e inconsistentes;
- revisión de variables logísticas;
- preparación del calendario de festivos.

Durante esta fase se decidió conservar determinadas inconsistencias presentes en el dataset original, documentándolas mediante nuevas variables en lugar de eliminarlas, con el objetivo de preservar la fidelidad respecto a la información original.

---

## 5.4 Feature Engineering

Una de las fases más relevantes del proyecto fue el desarrollo de nuevas variables derivadas.

Entre ellas destacan:

- variables temporales;
- indicadores logísticos;
- variables económicas;
- agregados por pedido;
- categorías principales;
- indicadores binarios;
- segmentación económica;
- segmentación por número de artículos;
- variables relacionadas con festivos.

Estas transformaciones permitieron convertir múltiples tablas relacionales en un único dataset analítico preparado para el análisis de negocio.

---

## 5.5 Análisis Exploratorio de Datos (EDA)

Con el dataset final construido, se desarrolló un análisis exploratorio orientado a comprender el comportamiento general del marketplace.

Se estudiaron aspectos relacionados con:

- evolución temporal de ventas y pedidos;
- comportamiento horario y semanal;
- categorías de producto;
- distribución geográfica;
- métodos de pago;
- composición de los pedidos;
- rendimiento logístico;
- impacto de los festivos.

El objetivo de esta fase fue identificar patrones, tendencias y oportunidades de negocio.

---

## 5.6 Análisis Estadístico

Posteriormente se realizó un análisis estadístico de las principales variables económicas y logísticas.

Se calcularon:

- estadísticas descriptivas;
- media y mediana;
- asimetría;
- curtosis;
- correlaciones;
- detección de valores atípicos mediante el método IQR;
- comparación entre segmentos económicos;
- análisis logístico por cumplimiento de plazos.

Esta fase permitió complementar los resultados obtenidos durante el análisis exploratorio mediante técnicas estadísticas que aportan una mayor solidez a las conclusiones del proyecto.

---

## 5.7 Desarrollo del Dashboard

Como fase final se diseñó un dashboard interactivo en Power BI dirigido a la Dirección General.

El cuadro de mando se estructuró en dos páginas complementarias:

- **Executive Business Overview**, orientada a proporcionar una visión global del rendimiento del marketplace mediante indicadores ejecutivos y métricas comerciales.

- **Customer & Operations Insights**, centrada en el análisis del comportamiento de compra de los clientes y del rendimiento logístico de la plataforma.

La separación en dos páginas permitió mantener un diseño limpio, facilitar la navegación y evitar la sobrecarga de información, proporcionando distintos niveles de análisis según las necesidades del usuario.

---

## 5.8 Comunicación de resultados

Finalmente, todos los resultados obtenidos se documentaron mediante el presente informe técnico.

La combinación del análisis desarrollado en Python con el dashboard interactivo en Power BI permite transformar un conjunto de datos operativos en una herramienta de apoyo a la toma de decisiones basada en evidencia, facilitando la interpretación de los principales indicadores del negocio y la identificación de oportunidades estratégicas para el marketplace.
 
---
 
# 6. Exploración Inicial de los Datos

## 6.1 Objetivo de la exploración

La primera fase del proyecto consistió en realizar una exploración exhaustiva de los distintos conjuntos de datos proporcionados por Olist con el fin de comprender su estructura, evaluar su calidad y detectar posibles problemas que pudieran afectar a las fases posteriores del análisis.

Antes de realizar cualquier transformación, era necesario conocer el contenido de cada tabla, identificar las relaciones existentes entre ellas y verificar que la información disponible fuera suficiente para construir un modelo analítico consistente.

Esta fase permitió establecer una visión global del modelo de datos y sirvió como base para definir las tareas de limpieza y transformación desarrolladas posteriormente.

---

## 6.2 Carga de los datos

Los datos originales se almacenaban en formato CSV y fueron cargados utilizando la librería **Pandas**, manteniendo inicialmente su estructura original para evitar introducir modificaciones prematuras.

El proyecto utilizó siete tablas principales procedentes del dataset público de Olist, complementadas con un calendario oficial de festivos nacionales de Brasil.

Tras la carga de los datos se verificó correctamente la lectura de todos los archivos, comprobando el número de registros, columnas y tipos de datos asociados a cada uno de ellos.

---

## 6.3 Análisis estructural del modelo de datos

Como primer paso se analizó la estructura de cada uno de los datasets.

Para cada tabla se revisaron aspectos como:

- número de observaciones;
- número de variables;
- tipos de datos;
- variables identificadoras;
- posibles claves primarias;
- variables categóricas y numéricas;
- variables temporales.

Este análisis permitió comprender la función de cada tabla dentro del modelo relacional y planificar posteriormente la integración de la información.

Asimismo, se identificaron las principales relaciones existentes entre los diferentes datasets, verificando que el modelo seguía una estructura relacional coherente donde la tabla de pedidos actuaba como elemento central sobre el que se integraba el resto de la información.

---

## 6.4 Evaluación de la calidad de los datos

Una vez comprendida la estructura del modelo, se procedió a evaluar la calidad de la información disponible.

Durante esta fase se analizaron los siguientes aspectos:

### Valores nulos

Se calculó el número y porcentaje de valores ausentes presentes en cada variable.

Los resultados mostraron que la mayoría de columnas presentaban una elevada completitud, concentrándose los principales valores nulos en variables relacionadas con el proceso logístico, como las fechas de entrega o determinadas variables económicas derivadas.

Posteriormente se comprobó que estos valores ausentes respondían al propio comportamiento del negocio, ya que la mayor parte pertenecían a pedidos cancelados, no disponibles o todavía no entregados.

Por este motivo, estos registros no fueron considerados errores de calidad, sino situaciones reales que debían conservarse para mantener la representatividad del dataset.

---

### Duplicados

Se revisó la existencia de registros duplicados tanto a nivel de fila completa como en las variables candidatas a clave primaria.

El análisis confirmó que las tablas principales no presentaban duplicados en sus identificadores, mientras que las repeticiones observadas en las tablas de artículos y pagos correspondían al propio diseño del modelo relacional, donde un pedido puede contener varios artículos o varios registros de pago.

---

### Tipos de datos

También se revisaron los tipos de datos asignados automáticamente durante la carga de los archivos.

Se detectaron varias variables temporales almacenadas como texto, así como columnas identificadoras que requerían conservarse como variables de tipo carácter para evitar la pérdida de información.

Esta revisión permitió planificar posteriormente la conversión de tipos realizada durante la fase de limpieza.

---

### Integridad referencial

Se verificó la consistencia entre las diferentes tablas mediante la comprobación de las claves primarias y foráneas.

El análisis confirmó una elevada integridad del modelo de datos.

Únicamente se detectaron dos registros de artículos cuyo identificador de producto no aparecía en la tabla de productos, así como un pedido sin información asociada en la tabla de pagos.

Dado el reducido impacto de estas incidencias sobre el volumen total del dataset, se decidió conservar dichos registros documentando su existencia durante el análisis.

---

## 6.5 Principales hallazgos de la exploración

La exploración inicial permitió obtener una visión clara de la calidad y estructura de los datos antes de iniciar cualquier transformación.

Entre los principales resultados obtenidos destacan:

- El modelo relacional presentaba una estructura consistente y bien definida.
- La tabla **Orders** constituía el núcleo principal del análisis, sobre el que posteriormente se integraría el resto de la información.
- Los valores nulos observados respondían principalmente a situaciones reales del proceso logístico y no a errores de calidad de datos.
- No se detectaron problemas relevantes de duplicidad en las claves principales.
- La integridad referencial era muy elevada, con únicamente incidencias puntuales de escaso impacto.
- Fue posible planificar una estrategia de limpieza conservadora, evitando eliminar información que pudiera resultar relevante para el análisis posterior.

En conjunto, esta primera fase permitió concluir que el dataset presentaba un nivel de calidad suficiente para continuar con el proceso de preparación de los datos.

---

# 7. Limpieza y Transformación de los Datos

## 7.1 Objetivo de la limpieza

Una vez evaluada la calidad del modelo de datos, se inició el proceso de limpieza y transformación con el objetivo de construir un conjunto de datos homogéneo, consistente y preparado para el análisis.

Esta etapa no tuvo como finalidad modificar el comportamiento original del negocio, sino corregir aspectos relacionados con el formato de la información, mejorar la coherencia entre tablas y facilitar la integración de los distintos datasets.

Siempre que fue posible se optó por una estrategia conservadora, preservando la información original y documentando aquellas incidencias que formaban parte del funcionamiento real del marketplace.

---

## 7.2 Conversión de tipos de datos

Una de las primeras tareas realizadas consistió en homogeneizar los tipos de datos de todas las variables.

Las principales transformaciones incluyeron:

- conversión de las fechas al formato `datetime`;
- normalización de variables de texto;
- conversión de identificadores y códigos postales a tipo carácter;
- revisión de variables numéricas enteras y decimales.

Esta estandarización facilitó posteriormente el cálculo de variables temporales, indicadores logísticos y métricas económicas.

---

## 7.3 Tratamiento de valores nulos

El análisis realizado durante la fase anterior permitió comprobar que la mayor parte de los valores ausentes tenían una explicación operativa.

Por este motivo se decidió no realizar imputaciones artificiales.

Los principales casos fueron:

- fechas de entrega inexistentes en pedidos cancelados;
- tiempos logísticos no disponibles para pedidos no entregados;
- variables económicas sin información asociada debido a la ausencia de registros en la tabla de artículos.

Mantener estos valores ausentes permitió conservar la integridad del proceso de negocio y evitar la introducción de sesgos en los análisis posteriores.

---

## 7.4 Validaciones realizadas

Además de la limpieza de formatos, se desarrolló un conjunto de validaciones orientadas a detectar posibles inconsistencias en los datos.

Entre las comprobaciones realizadas destacan:

- validación de claves primarias;
- comprobación de integridad referencial;
- búsqueda de valores negativos;
- detección de importes iguales a cero;
- revisión de fechas inconsistentes;
- comprobación de duplicados;
- validación de variables económicas y logísticas.

Estas verificaciones permitieron garantizar que las transformaciones posteriores se realizaran sobre una base de datos consistente.

---

## 7.5 Principales incidencias detectadas

Durante esta fase se identificaron varias situaciones que, aunque inicialmente podían interpretarse como errores, finalmente fueron consideradas parte del comportamiento real del sistema.

Entre ellas destacan:

### Pedidos sin información de artículos

Se identificaron aproximadamente **775 pedidos** presentes en la tabla **Orders** que no disponían de registros asociados en la tabla **Order Items**.

Como consecuencia, estos pedidos carecen de información económica y no pueden clasificarse dentro de la segmentación por valor económico.

Dado que representan únicamente alrededor del **0,8 %** del total de pedidos, se decidió conservarlos en el dataset analítico y excluirlos únicamente de aquellas visualizaciones donde la segmentación económica era imprescindible.

---

### Pedido sin información de pago

Se detectó un único pedido sin registros asociados en la tabla de pagos.

Debido a su impacto prácticamente nulo sobre el conjunto de datos, el registro se mantuvo sin realizar imputaciones.

---

### Inconsistencias temporales

Se identificaron **1.359 pedidos (1,37 %)** cuya fecha de entrega al transportista era anterior a la fecha de aprobación del pedido.

Tras revisar una muestra representativa de estos registros, se observó que la mayoría correspondían a diferencias horarias muy reducidas o posibles inconsistencias derivadas del sistema original de registro.

En lugar de eliminar dichos pedidos, se decidió crear la variable **carrier_before_approval**, permitiendo documentar esta situación y mantener la trazabilidad de la información original.

---

## 7.6 Resultado de la fase de limpieza

Como resultado del proceso de limpieza y transformación se obtuvo un conjunto de datos consistente, homogéneo y preparado para las fases posteriores de integración y enriquecimiento mediante técnicas de Feature Engineering.

Todas las decisiones adoptadas durante esta etapa se orientaron a preservar la representatividad del negocio, evitando modificaciones innecesarias sobre la información original y garantizando la máxima trazabilidad del proceso de preparación de los datos.
 
---
 
# 8. Feature Engineering y Construcción del Dataset Analítico

## 8.1 Objetivo del Feature Engineering

Una vez finalizado el proceso de limpieza y validación de los datos, se inició la fase de *Feature Engineering*, cuyo objetivo fue enriquecer la información disponible mediante la creación de nuevas variables que permitieran realizar un análisis de negocio más completo.

Los datasets originales de Olist contienen información distribuida en distintas tablas relacionales, lo que dificulta la realización de análisis globales. Por ello, fue necesario integrar las diferentes fuentes de información y generar nuevas variables derivadas capaces de representar aspectos temporales, económicos, logísticos y comerciales del marketplace.

El resultado de esta fase fue la construcción de un dataset analítico único, donde cada fila representa un pedido y cada columna describe alguna de sus características relevantes para el análisis.

---

## 8.2 Integración de las fuentes de datos

La construcción del dataset analítico se realizó tomando como punto de partida la tabla **Orders**, considerada el eje central del modelo de datos.

Sobre ella se incorporó progresivamente información procedente del resto de tablas mediante diferentes operaciones de unión (*joins*), integrando:

- Información demográfica de los clientes.
- Productos y artículos incluidos en cada pedido.
- Costes de envío.
- Información agregada de pagos.
- Categoría principal del pedido.
- Calendario de festivos nacionales de Brasil.

Todas las uniones se realizaron utilizando las claves primarias y foráneas previamente validadas durante la fase de limpieza, garantizando la consistencia del modelo analítico.

---

## 8.3 Variables temporales

Uno de los primeros bloques de variables generadas fue el relacionado con la dimensión temporal.

A partir de la fecha de compra de cada pedido se obtuvieron nuevas variables que permiten analizar el comportamiento del marketplace desde diferentes perspectivas cronológicas.

Entre ellas destacan:

- Año de compra.
- Mes de compra.
- Día del mes.
- Hora de compra.
- Día de la semana.
- Trimestre.
- Fecha de compra sin componente horario.

Estas variables constituyen la base de los análisis temporales desarrollados posteriormente tanto en Python como en el dashboard de Power BI.

---

## 8.4 Variables logísticas

Con el objetivo de evaluar el rendimiento operativo del marketplace, se generaron diferentes indicadores relacionados con el proceso logístico.

Las principales variables creadas fueron:

- Tiempo transcurrido entre la compra y la aprobación del pedido.
- Tiempo entre la aprobación y la entrega al transportista.
- Tiempo total de entrega al cliente.
- Tiempo estimado de entrega.
- Días de retraso respecto a la fecha comprometida.

Asimismo, se construyeron diferentes indicadores binarios que permiten identificar automáticamente pedidos:

- entregados;
- cancelados;
- no disponibles;
- entregados fuera de plazo.

Estas variables resultaron fundamentales para evaluar posteriormente la eficiencia logística del marketplace.

---

## 8.5 Variables económicas

Con el fin de obtener una visión económica completa de cada pedido se desarrolló un conjunto de variables agregadas a partir de la información contenida en las tablas de artículos y pagos.

Entre las principales métricas generadas destacan:

- Número total de artículos por pedido.
- Número de productos distintos.
- Valor total de los productos.
- Coste total de envío.
- Valor medio de los artículos.
- Precio máximo del pedido.
- Valor total del pedido.
- Valor medio por artículo.
- Ratio entre coste de envío y valor del pedido.
- Diferencia entre el importe pagado y el valor calculado del pedido.

Estas variables permitieron analizar posteriormente la estructura económica del negocio y comprobar la consistencia entre pedidos y pagos.

---

## 8.6 Segmentación de los pedidos

Con el objetivo de facilitar el análisis estratégico del negocio se desarrollaron diferentes variables de segmentación.

En primer lugar, los pedidos se clasificaron según su valor económico, obteniendo cuatro segmentos:

- Bajo.
- Medio.
- Alto.
- Muy alto.

Esta clasificación permitió estudiar posteriormente la distribución de la facturación y el comportamiento de los distintos grupos de clientes.

Adicionalmente, también se construyó una segmentación basada en el número de artículos incluidos en cada pedido, facilitando el análisis del tamaño medio de la cesta de compra.

---

## 8.7 Integración del calendario de festivos

Como parte del enriquecimiento del dataset se incorporó un calendario oficial de festivos nacionales de Brasil.

Mediante la fecha de compra de cada pedido fue posible identificar aquellos realizados durante un día festivo, generando las variables:

- Nombre del festivo.
- Nombre normalizado.
- Indicador binario de compra en festivo.

Esta información permitió analizar posteriormente el posible impacto de los festivos sobre el comportamiento de compra de los clientes.

---

## 8.8 Dataset analítico final

Tras completar todas las transformaciones descritas anteriormente se obtuvo un dataset analítico compuesto por **99.441 pedidos** y **51 variables**, preparado para su utilización tanto en el análisis exploratorio como en el análisis estadístico y la construcción del dashboard.

El dataset final integra información procedente de todas las fuentes originales y combina variables descriptivas, temporales, económicas, logísticas, geográficas y comerciales, proporcionando una visión completa del funcionamiento del marketplace.

La construcción de este dataset constituye uno de los principales resultados técnicos del proyecto, ya que transforma un conjunto de tablas relacionales en una única fuente de información preparada para responder preguntas de negocio de forma eficiente.

---

# 9. Análisis Exploratorio de los Datos

## 9.1 Objetivo del análisis exploratorio

Una vez construido el dataset analítico, se desarrolló un Análisis Exploratorio de Datos (EDA) con el objetivo de comprender el comportamiento general del marketplace e identificar patrones, tendencias y relaciones entre las principales variables del negocio.

El análisis exploratorio constituye una fase fundamental dentro de cualquier proyecto de Data Analytics, ya que permite obtener una primera interpretación de los datos antes de aplicar técnicas estadísticas más avanzadas.

Durante esta etapa se combinaron diferentes visualizaciones y métricas descriptivas para estudiar la evolución temporal del marketplace, el comportamiento de compra de los clientes, la distribución económica de los pedidos y el rendimiento operativo de la plataforma.

---

## 9.2 Visión general del negocio

El análisis permitió comprobar que Olist constituye un marketplace consolidado con un elevado volumen de actividad.

Durante el periodo analizado se registraron más de **99.000 pedidos**, correspondientes a **96.096 clientes únicos**, generando una facturación superior a **15,8 millones de reales brasileños**.

El ticket medio alcanzó los **160,58 BRL**, lo que refleja un modelo de negocio basado principalmente en compras de valor intermedio.

Desde el punto de vista operativo, el marketplace presenta un comportamiento altamente eficiente, con un **97,02 % de pedidos entregados correctamente** y un **92,13 % de entregas realizadas dentro del plazo previsto**.

Estos indicadores muestran una operación madura y estable que servirá como punto de partida para el resto del análisis.

---

## 9.3 Evolución temporal del marketplace

El estudio de la evolución mensual permitió identificar una clara tendencia de crecimiento durante el periodo analizado.

A lo largo de 2017 se observa un incremento progresivo tanto del número de pedidos como de las ventas, mientras que durante 2018 el marketplace alcanza una fase de consolidación manteniendo elevados niveles de actividad.

La evolución paralela de ambas variables sugiere que el crecimiento del negocio estuvo impulsado principalmente por el aumento del volumen de pedidos y no únicamente por un incremento del valor medio de las compras.

---

## 9.4 Comportamiento de compra de los clientes

El análisis temporal revela que la actividad de compra se concentra principalmente durante los días laborables.

Los lunes, martes y miércoles registran el mayor número de pedidos, mientras que el sábado constituye el día con menor actividad.

Desde el punto de vista horario, la mayor concentración de compras se produce entre las **10:00 y las 22:00 horas**, con especial intensidad durante la franja de tarde.

Estos resultados sugieren que las compras responden mayoritariamente a comportamientos planificados integrados en la rutina diaria de los consumidores.

---

## 9.5 Estructura económica del marketplace

El estudio del valor económico de los pedidos muestra una distribución claramente asimétrica, donde la mayoría de las compras presentan importes moderados y únicamente un pequeño porcentaje alcanza valores elevados.

La segmentación económica evidencia que aproximadamente la mitad de los pedidos pertenecen al segmento medio, mientras que los segmentos alto y muy alto concentran una parte muy significativa de la facturación.

Este comportamiento confirma que el crecimiento económico del marketplace depende en gran medida de un grupo reducido de pedidos de elevado valor.

---

## 9.6 Composición de los pedidos

Uno de los hallazgos más relevantes del análisis exploratorio fue la elevada concentración de pedidos con un único artículo.

Más del **90 % de las compras** están compuestas por un solo producto, mientras que los pedidos con múltiples artículos representan una proporción considerablemente menor.

Este comportamiento pone de manifiesto que los clientes utilizan la plataforma principalmente para realizar compras concretas, abriendo la posibilidad de desarrollar estrategias de *cross-selling* y *up-selling* destinadas a incrementar el tamaño medio de la cesta de compra.

---

## 9.7 Categorías, métodos de pago y distribución geográfica

El análisis por categorías mostró una importante concentración de las ventas en un reducido grupo de familias de productos.

Las categorías relacionadas con salud, hogar, tecnología y deporte constituyen los principales motores de facturación del marketplace.

En cuanto a los métodos de pago, la tarjeta de crédito representa más de las tres cuartas partes de las transacciones, situándose muy por delante del resto de alternativas disponibles.

Desde una perspectiva territorial, el estado de **São Paulo** concentra aproximadamente el 42 % de los pedidos registrados, seguido por Río de Janeiro y Minas Gerais, reflejando el peso económico de la región sudeste dentro del comercio electrónico brasileño.

---

## 9.8 Rendimiento logístico

El análisis logístico confirma el elevado nivel de eficiencia operativa del marketplace.

La inmensa mayoría de los pedidos son entregados correctamente y más del 92 % llegan dentro del plazo previsto.

Los pedidos cancelados o no disponibles representan únicamente una pequeña fracción del total, mientras que los retrasos afectan a menos del 8 % de las entregas.

Estos resultados evidencian un funcionamiento logístico sólido y una experiencia de compra satisfactoria para la mayor parte de los clientes.

---

## 9.9 Impacto de los festivos

La incorporación del calendario de festivos permitió analizar si existían diferencias significativas en el comportamiento de compra durante estas fechas.

Los resultados muestran que únicamente el **2,72 %** de los pedidos fueron realizados en días festivos y que tanto el ticket medio como el volumen de ventas presentan valores muy similares a los observados en días no festivos.

Por tanto, los festivos nacionales brasileños no parecen ejercer una influencia relevante sobre el comportamiento general de compra.

---

## 9.10 Principales conclusiones del análisis exploratorio

El análisis exploratorio permitió identificar los principales patrones de funcionamiento del marketplace antes de realizar el análisis estadístico.

Los resultados muestran un negocio consolidado, caracterizado por un crecimiento sostenido, una elevada eficiencia logística y una estructura económica donde una parte importante de la facturación depende de un grupo reducido de pedidos de alto valor.

Asimismo, el estudio pone de manifiesto oportunidades de mejora relacionadas con el incremento del número medio de artículos por pedido y la expansión comercial hacia regiones con menor presencia dentro del marketplace.

Estas conclusiones constituyen la base sobre la que se desarrolla el análisis estadístico presentado en el capítulo siguiente.
 
---
 
# 10. Análisis Estadístico

## 10.1 Objetivo del análisis estadístico

Tras la realización del análisis exploratorio, se llevó a cabo un análisis estadístico con el objetivo de complementar los resultados obtenidos y aportar una mayor solidez a las conclusiones del proyecto.

Mientras que el Análisis Exploratorio de Datos permitió identificar patrones y tendencias generales del marketplace, el análisis estadístico se centró en estudiar el comportamiento de las principales variables económicas y logísticas desde una perspectiva cuantitativa, evaluando sus distribuciones, relaciones e inconsistencias.

Para ello se emplearon diferentes técnicas descriptivas que permitieron caracterizar el comportamiento del conjunto de datos sin alterar la información original.

---

## 10.2 Calidad y completitud del dataset

El análisis confirmó el elevado nivel de calidad del dataset analítico construido durante las fases anteriores.

La mayoría de variables presentan una cobertura prácticamente completa, concentrándose los valores nulos en variables derivadas del proceso logístico o económico.

En todos los casos, estos valores ausentes responden al propio funcionamiento del marketplace y no a problemas de calidad de datos.

Del mismo modo, las incidencias detectadas durante la fase de limpieza (pedidos sin artículos, pedido sin información de pago o inconsistencias temporales) representan un porcentaje muy reducido del total de registros y no afectan de forma significativa a la representatividad del análisis.

En consecuencia, se decidió mantener dichos registros para preservar la integridad del dataset.

---

## 10.3 Comportamiento económico de los pedidos

Las estadísticas descriptivas muestran que el valor medio de los pedidos alcanza los **160,58 BRL**, mientras que la mediana se sitúa en **105,29 BRL**.

La diferencia existente entre ambas medidas confirma que la distribución del valor de los pedidos presenta una marcada asimetría positiva, donde un reducido número de pedidos de elevado importe incrementa considerablemente el valor medio.

Este mismo comportamiento se observa en otras variables económicas como:

- Valor de los productos.
- Valor total pagado.
- Valor medio por artículo.

Por este motivo, la mediana constituye una medida más representativa del comportamiento habitual de los clientes que la media aritmética.

---

## 10.4 Relaciones entre variables

El análisis de correlación puso de manifiesto una elevada coherencia entre las principales variables económicas del modelo.

Las mayores correlaciones se observaron entre:

| Variables | Correlación |
|------------|------------:|
| Valor total del pedido – Importe pagado | 0,999 |
| Valor total del pedido – Valor de productos | 0,996 |
| Valor de productos – Importe pagado | 0,996 |

Estos resultados indican que el importe abonado por los clientes coincide prácticamente con el valor económico calculado para cada pedido, confirmando la elevada consistencia entre la información procedente de las tablas de pedidos y pagos.

Asimismo, las variables relacionadas con el número de artículos presentan correlaciones considerablemente menores con el valor del pedido, lo que sugiere que el gasto realizado por los clientes depende principalmente del precio unitario de los productos y no del tamaño de la cesta de compra.

---

## 10.5 Análisis de distribuciones y valores atípicos

El estudio de la asimetría y la curtosis confirmó que la mayoría de variables económicas presentan distribuciones fuertemente sesgadas hacia la derecha.

Esta situación resulta habitual en plataformas de comercio electrónico, donde un reducido número de pedidos concentra importes significativamente superiores a la media.

La detección de valores atípicos mediante el método IQR permitió identificar aproximadamente entre un **5 % y un 10 %** de observaciones consideradas extremas según criterios estadísticos.

Sin embargo, tras analizar estos registros se concluyó que representan comportamientos reales del negocio y no errores de calidad de datos.

En consecuencia, todos los valores atípicos fueron conservados dentro del dataset analítico con el objetivo de evitar sesgos en los indicadores económicos del marketplace.

---

## 10.6 Segmentación económica y rendimiento logístico

El análisis por segmentos económicos permitió comprobar que los pedidos de mayor valor generan una parte muy significativa de la facturación total del marketplace.

Aunque los segmentos **alto** y **muy alto** representan una proporción relativamente reducida del número total de pedidos, concentran aproximadamente dos tercios de los ingresos generados durante el periodo analizado.

Desde el punto de vista logístico, también se observó una ligera relación positiva entre el valor económico del pedido y la probabilidad de sufrir retrasos.

No obstante, las diferencias detectadas son moderadas y no comprometen el elevado nivel de eficiencia general del marketplace.

---

## 10.7 Principales conclusiones del análisis estadístico

El análisis estadístico confirma y refuerza las conclusiones obtenidas durante el análisis exploratorio.

Los resultados evidencian un dataset de elevada calidad, una fuerte coherencia entre pedidos y pagos y una estructura económica caracterizada por una distribución asimétrica del valor de los pedidos.

Asimismo, se confirma que la mayor parte de la facturación depende de un reducido grupo de pedidos de elevado importe, mientras que el rendimiento logístico mantiene niveles muy elevados de cumplimiento.

En conjunto, el análisis estadístico aporta una base cuantitativa sólida sobre la que fundamentar las conclusiones estratégicas del proyecto.

---

# 11. Dashboard en Power BI

## 11.1 Objetivo del dashboard

Como fase final del proyecto se desarrolló un dashboard interactivo en **Power BI** con el propósito de transformar los resultados obtenidos durante el análisis en una herramienta de apoyo a la toma de decisiones.

El dashboard está orientado a la **Dirección General**, proporcionando una visión ejecutiva del negocio mediante indicadores clave de rendimiento (KPIs), visualizaciones interactivas y filtros que permiten analizar el comportamiento del marketplace desde distintas perspectivas.

Su diseño responde al principio de ofrecer la máxima cantidad de información relevante con el menor esfuerzo de interpretación posible.

---

## 11.2 Diseño del dashboard

Con el objetivo de evitar la sobrecarga visual y facilitar la navegación, el dashboard se estructuró en dos páginas complementarias.

La primera página, **Executive Business Overview**, ofrece una visión global del rendimiento comercial del marketplace, mientras que la segunda, **Customer & Operations Insights**, profundiza en el comportamiento de los clientes y en el desempeño logístico de la plataforma.

Ambas páginas mantienen una línea visual homogénea basada en una paleta de colores suaves, fondos claros y elementos gráficos consistentes, favoreciendo una experiencia de usuario intuitiva y profesional.

La navegación entre ambas páginas se realiza mediante botones integrados en el propio dashboard, permitiendo alternar fácilmente entre la visión ejecutiva y el análisis operativo.

---

## 11.3 Indicadores clave (KPIs)

La selección de los KPIs se realizó priorizando aquellos indicadores que permiten evaluar de forma inmediata la situación general del negocio.

La primera página incorpora seis indicadores principales:

- Número total de pedidos.
- Número de clientes.
- Ventas totales.
- Ticket medio.
- Porcentaje de pedidos entregados.
- Porcentaje de pedidos retrasados.

Por su parte, la segunda página incluye indicadores centrados en el rendimiento operativo:

- Tiempo medio de entrega.
- Adelanto medio respecto a la fecha estimada.
- Coste medio de envío.
- Porcentaje de pedidos realizados en festivos.

Estos indicadores resumen los aspectos más relevantes del negocio y permiten detectar rápidamente posibles desviaciones en el rendimiento del marketplace.

---

## 11.4 Visualizaciones

Las visualizaciones fueron seleccionadas atendiendo tanto al tipo de información representada como a la facilidad de interpretación por parte del usuario final.

Entre ellas destacan:

- Gráfico combinado para representar la evolución mensual de pedidos y ventas.
- Gráficos de barras horizontales para comparar categorías y estados.
- Gráficos de anillos para mostrar la distribución por métodos de pago y segmentos económicos.
- Gráficos de columnas para analizar el comportamiento temporal de los clientes.
- Visualizaciones comparativas para evaluar el rendimiento logístico entre pedidos entregados en plazo y retrasados.

Cada gráfico responde a una pregunta de negocio concreta y complementa la información proporcionada por los KPIs.

---

## 11.5 Interactividad

El dashboard incorpora diferentes segmentadores que permiten filtrar dinámicamente la información.

Entre ellos destacan:

- Año.
- Mes.
- Estado.
- Categoría de producto.

Estos filtros permiten adaptar el análisis a distintos escenarios sin necesidad de modificar el modelo de datos.

Asimismo, todas las visualizaciones interactúan entre sí, facilitando la exploración del comportamiento del marketplace desde múltiples perspectivas.

---

## 11.6 Valor añadido del dashboard

El dashboard constituye la culminación del proyecto de Data Analytics.

Mientras que Python permitió realizar el tratamiento, análisis y validación de los datos, Power BI proporciona una herramienta visual capaz de comunicar los resultados de forma clara e intuitiva.

De este modo, el dashboard transforma un conjunto complejo de datos operativos en información fácilmente interpretable para la Dirección General, facilitando el seguimiento de los principales indicadores del negocio y apoyando la toma de decisiones basada en datos.

---

# 12. Principales Hallazgos de Negocio

El análisis realizado a lo largo del proyecto permitió identificar una serie de conclusiones de especial relevancia para la gestión estratégica del marketplace.

En primer lugar, Olist presenta un elevado nivel de madurez operativa, reflejado tanto en el volumen de actividad como en sus indicadores logísticos. El marketplace supera los **99.000 pedidos**, mantiene una facturación superior a **15,8 millones de BRL** y alcanza un porcentaje de entregas correctas superior al **97 %**, evidenciando un funcionamiento estable y eficiente.

En segundo lugar, el crecimiento observado durante el periodo analizado está impulsado principalmente por el incremento del volumen de pedidos y no por un aumento significativo del valor medio de las compras. Este comportamiento refleja una expansión sostenida de la demanda y una consolidación progresiva del marketplace.

Desde el punto de vista económico, el análisis pone de manifiesto que una parte muy significativa de la facturación depende de un grupo reducido de pedidos de elevado importe. Los segmentos **alto** y **muy alto**, aunque representan una proporción menor del total de pedidos, concentran aproximadamente dos tercios de los ingresos generados por la plataforma.

Asimismo, se observa que más del **90 %** de los pedidos contienen un único artículo, lo que sugiere la existencia de oportunidades para incrementar el valor medio de la cesta mediante estrategias de *cross-selling* y *up-selling*.

En relación con el comportamiento de compra, los clientes concentran sus pedidos principalmente durante los días laborables y en horario diurno, reflejando un patrón de consumo planificado más que impulsivo.

Por otra parte, la actividad comercial muestra una fuerte concentración geográfica en la región sudeste de Brasil, especialmente en el estado de **São Paulo**, lo que podría representar una oportunidad de expansión hacia regiones con menor penetración del marketplace.

Desde una perspectiva logística, el análisis confirma un elevado nivel de eficiencia. La mayoría de los pedidos se entregan antes de la fecha comprometida y los retrasos afectan únicamente a una pequeña proporción del total. No obstante, los pedidos de mayor valor presentan una ligera mayor probabilidad de sufrir retrasos, lo que podría justificar un seguimiento específico de este segmento.

Finalmente, la incorporación del calendario de festivos demuestra que los días festivos nacionales apenas modifican el comportamiento de compra de los clientes, por lo que su capacidad explicativa sobre las ventas resulta limitada.

En conjunto, los resultados obtenidos reflejan un marketplace consolidado, con procesos operativos robustos, un crecimiento sostenido y diversas oportunidades para mejorar tanto la rentabilidad como la experiencia del cliente mediante estrategias comerciales y logísticas basadas en el análisis de datos.
 
---
 
# 13. Recomendaciones Estratégicas

A partir de los resultados obtenidos durante el análisis se identifican diversas oportunidades de mejora que podrían contribuir a incrementar el rendimiento comercial y operativo del marketplace.

Si bien las recomendaciones propuestas no pretenden sustituir un análisis específico del negocio, sí constituyen posibles líneas de actuación basadas en la evidencia obtenida a partir de los datos.

---

## 13.1 Incrementar el valor medio de la cesta de compra

El análisis muestra que más del **90 % de los pedidos contienen un único artículo**, lo que indica que la mayoría de los clientes realizan compras muy concretas.

Este comportamiento representa una oportunidad para implementar estrategias orientadas a incrementar el número medio de productos por pedido, tales como:

- recomendaciones automáticas de productos complementarios;
- promociones por compra conjunta;
- descuentos por volumen;
- campañas de *cross-selling* y *up-selling*.

Un incremento moderado del tamaño medio de la cesta tendría un impacto directo sobre la facturación sin necesidad de aumentar el número de clientes.

---

## 13.2 Potenciar la fidelización de clientes de alto valor

El análisis de segmentación económica demuestra que los segmentos **alto** y **muy alto** generan una parte muy significativa de la facturación del marketplace.

Aunque representan un porcentaje relativamente reducido del total de pedidos, constituyen un grupo estratégico para el crecimiento del negocio.

En este contexto, podrían plantearse acciones como:

- programas de fidelización;
- beneficios exclusivos;
- promociones personalizadas;
- campañas específicas para clientes de elevado gasto.

La retención de este perfil de clientes puede generar un impacto considerable sobre los ingresos del marketplace.

---

## 13.3 Optimizar el seguimiento de pedidos de elevado importe

El análisis logístico revela que los pedidos de mayor valor presentan una probabilidad ligeramente superior de sufrir retrasos.

Aunque las diferencias observadas son moderadas, el impacto potencial sobre la satisfacción del cliente puede ser significativo debido al elevado valor económico de estas compras.

Como medida preventiva, podría implantarse un sistema de monitorización específica para este tipo de pedidos, permitiendo actuar de forma temprana ante posibles incidencias logísticas.

---

## 13.4 Impulsar el crecimiento en regiones con menor penetración

La distribución geográfica de la demanda evidencia una elevada concentración de pedidos en la región sudeste de Brasil, especialmente en el estado de São Paulo.

Este comportamiento resulta coherente con la distribución económica del país, pero también pone de manifiesto la existencia de regiones con menor presencia comercial.

El desarrollo de campañas específicas de captación en estos mercados podría contribuir a diversificar la actividad del marketplace y reducir su dependencia de determinadas áreas geográficas.

---

## 13.5 Continuar monitorizando los principales indicadores del negocio

El dashboard desarrollado en Power BI proporciona una herramienta adecuada para realizar un seguimiento periódico del rendimiento del marketplace.

Se recomienda mantener una monitorización continua de indicadores como:

- volumen de pedidos;
- ventas;
- ticket medio;
- porcentaje de entregas;
- retrasos;
- comportamiento por categorías;
- evolución geográfica de la demanda.

El seguimiento continuo de estos indicadores facilitaría la detección temprana de cambios en el comportamiento del negocio y permitiría adoptar decisiones basadas en datos.

---

# 14. Limitaciones del Proyecto

Aunque el proyecto permite obtener una visión amplia del funcionamiento del marketplace, es importante considerar una serie de limitaciones que condicionan el alcance de los resultados obtenidos.

En primer lugar, el análisis se basa en información histórica correspondiente exclusivamente al periodo comprendido entre **2016 y 2018**.

Por tanto, las conclusiones obtenidas describen el comportamiento del marketplace durante dicho intervalo temporal y no deben extrapolarse automáticamente a la situación actual de la plataforma.

Asimismo, el dataset original presenta determinadas limitaciones derivadas de la información disponible.

Entre ellas destacan:

- aproximadamente **775 pedidos** presentes en la tabla **Orders** no disponen de registros asociados en la tabla **Order Items**, impidiendo calcular determinadas variables económicas;
- existe **un pedido** sin información registrada en la tabla de pagos;
- se detectaron **1.359 pedidos (1,37 %)** cuya fecha de entrega al transportista es anterior a la fecha de aprobación del pedido.

Tras revisar estas incidencias se concluyó que su impacto sobre el volumen total de información era reducido y que, en la mayoría de los casos, respondían a características propias del sistema original.

Por este motivo, se optó por conservar dichos registros y documentarlos adecuadamente durante el proceso de preparación de los datos.

Otra limitación importante es la ausencia de determinadas variables que podrían enriquecer el análisis, como información demográfica detallada de los clientes, datos de rentabilidad, costes logísticos reales, campañas de marketing o información sobre devoluciones.

Finalmente, debe señalarse que el proyecto tiene un carácter fundamentalmente descriptivo y exploratorio.

Aunque se aplican técnicas estadísticas para reforzar las conclusiones obtenidas, no se desarrollan modelos predictivos ni algoritmos de aprendizaje automático, aspectos que podrían abordarse en futuros trabajos.

---

# 15. Líneas Futuras de Trabajo

El presente proyecto constituye una base sólida para el desarrollo de análisis más avanzados relacionados con el funcionamiento del marketplace.

Entre las posibles líneas futuras destacan:

## Desarrollo de modelos predictivos

La construcción del dataset analítico permite desarrollar modelos de Machine Learning orientados a:

- predicción de retrasos;
- predicción del valor futuro de los pedidos;
- predicción del riesgo de cancelación;
- estimación de la demanda.

---

## Segmentación avanzada de clientes

La incorporación de información adicional permitiría desarrollar técnicas de segmentación mediante algoritmos de *clustering*, identificando perfiles homogéneos de clientes y facilitando el diseño de campañas comerciales personalizadas.

---

## Modelos de recomendación

El análisis podría ampliarse mediante sistemas de recomendación de productos basados en compras anteriores, favoreciendo estrategias de *cross-selling* y *up-selling*.

---

## Incorporación de nuevas fuentes de información

La integración de información adicional relacionada con campañas de marketing, costes logísticos, satisfacción del cliente o devoluciones permitiría ampliar considerablemente el alcance del análisis.

---

## Automatización del proceso analítico

Otra línea de mejora consistiría en automatizar la actualización del pipeline completo de datos, permitiendo alimentar automáticamente el dashboard mediante procesos ETL programados y facilitando la monitorización continua del negocio.

---

# 16. Conclusiones

El presente proyecto ha permitido desarrollar un análisis estratégico del marketplace brasileño Olist siguiendo un flujo completo de trabajo propio de un proyecto profesional de Data Analytics.

A lo largo del desarrollo se abordaron todas las fases habituales del ciclo analítico, desde la exploración inicial y validación de los datos hasta la construcción de un dashboard interactivo orientado a la toma de decisiones.

El proceso de preparación de los datos permitió integrar múltiples fuentes de información y construir un dataset analítico compuesto por **99.441 pedidos** y **51 variables**, incorporando información temporal, económica, logística y geográfica en una única estructura preparada para el análisis.

El estudio exploratorio y estadístico permitió comprender el funcionamiento general del marketplace, identificando un negocio consolidado, con un elevado volumen de actividad, una logística altamente eficiente y una fuerte concentración de la facturación en los pedidos de mayor valor.

Asimismo, el análisis puso de manifiesto diversas oportunidades de mejora relacionadas con el incremento del tamaño medio de la cesta de compra, la fidelización de clientes de alto valor y la expansión comercial hacia regiones con menor presencia dentro del marketplace.

Como resultado final del proyecto se desarrolló un dashboard interactivo en Power BI que sintetiza los principales indicadores del negocio mediante una interfaz intuitiva y orientada a la Dirección General.

Este dashboard permite transformar un conjunto complejo de datos operativos en información fácilmente interpretable, facilitando el seguimiento del rendimiento del marketplace y apoyando la toma de decisiones basada en datos.

En conjunto, el proyecto demuestra cómo la aplicación de técnicas de Data Analytics y Business Intelligence permite convertir grandes volúmenes de información en conocimiento útil para comprender el comportamiento de un negocio y apoyar la definición de estrategias orientadas a mejorar su rendimiento.

---

# 17. Bibliografía

Durante el desarrollo del proyecto se utilizaron diversas fuentes de información tanto para la obtención de los datos como para la consulta de documentación técnica relacionada con las herramientas empleadas.

## Fuentes de datos

- Olist. *Brazilian E-Commerce Public Dataset by Olist*. Kaggle.
- Brazilian Public Holidays Dataset.

## Documentación técnica

- McKinney, W. (2022). *Python for Data Analysis* (3rd ed.). O'Reilly Media.
- VanderPlas, J. (2023). *Python Data Science Handbook*. O'Reilly Media.
- Documentación oficial de Pandas. https://pandas.pydata.org/
- Documentación oficial de NumPy. https://numpy.org/
- Documentación oficial de Matplotlib. https://matplotlib.org/
- Documentación oficial de Seaborn. https://seaborn.pydata.org/
- Documentación oficial de Power BI. https://learn.microsoft.com/power-bi/
- Documentación oficial de Git. https://git-scm.com/doc
- Documentación oficial de GitHub. https://docs.github.com/

## Herramientas utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Power BI
- Git
- GitHub
- Visual Studio Code
- Jupyter Notebook