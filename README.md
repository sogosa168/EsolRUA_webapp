# EsolRUA_webapp
Este proyecto es parte del curso Desarrollo de Web Apps con Python y Shiny para el Análisis en Energías Renovables. En este repositorio se muestra el desarrollo de una aplicación web interactiva para analizar datos meteorológicos proporcionados por las estaciones RUOA y Esolmet en Temixco, Morelos con el objetivo de analizar el recurso y posible potencial de la energía solar y mini eólica en Temixco, Morelos. La webapp integra bases de datos y visualizaciones interactivas....

El proyecto está organizado de la siguiente manera:

```plaintext
├── data/
├── docs/
├── img/
├── notebooks/
├── src/
├── venv/
├── .gitignore
└── README.md
```

A continuación, se detalla el propósito de cada carpeta y archivo.

1. **data/** - Conjuntos de datos  
   En esta carpeta se almacenan los archivos de datos utilizados en el proyecto, principalmente en formatos csv o SQLite. Los datos provienen de las bases RUOA y Esolmet, con mediciones meteorológicas (temperatura, humedad, radiación solar, viento, entre otras.) desde 2017 hasta la actualidad.

   **Ejemplos de archivos:**  
   - `2016_RUOA_HR.csv`: Archivo csv de base de datos RUOA con resolución temporal de 1 hora.  
   - `2010_ESOLMET.csv`: Archivo csv de base de datos ESOLMET con resolución temporal de 1 hora.

2. **docs/** - Documentación  
   Esta carpeta contiene la documentación técnica y de usuario del proyecto.

   **Archivos principales:**  
   - `manual_usuario.md`: Guía paso a paso para instalar y usar la webapp.  
   - `documentacion_tecnica.md`: Detalles técnicos sobre la estructura del código y dependencias.  
   - `instalacion.md`: Instrucciones para configurar el entorno y ejecutar la webapp.  
   - `esolmet_RUOA.md`: Explicaciones sobre las bases de datos RUOA y Esolmet y su estructura.

3. **img/** - Recursos gráficos  
   Aquí se almacenan imágenes y gráficos relevantes. Las subcarpetas y archivos que se muestran son :

   **Subcarpetas y archivos:**  

   - `logo.png`: Logotipo institucional.  
   - `capturas_dashboard/`: Capturas de la interfaz de usuario.  
   - `graficos_preliminares/`: Gráficos generados durante el análisis exploratorio.

4. **notebooks/** - Notebooks de Jupyter  
   Contiene notebooks de Jupyter (.ipynb) utilizados para el análisis exploratorio, pruebas de visualización y procesamiento previo de datos.

   **Los notebooks que se muestran son:**  
   - `exploracion_datos.ipynb`: Exploración inicial de los datos, estadísticas descriptivas y limpieza.  
   - `analisis_001.ipynb`: Se realiza el tronco del análisis de la información utilizando estadística, funciones de correlación, funciones para determinar potencial renovable, entre otros. Consecuentemente, se sintetizan los resultados para que puedan utilizarse en la web app.  
   - `prototipos_graficos.ipynb`: Pruebas de visualizaciones con Plotly y Matplotlib antes de definirlos en la web app.

5. **src/** - Código fuente  
   Esta carpeta contiene el código fuente de la webapp para gestionar la lógica de la aplicación, el procesamiento de datos y la generación de gráficos.

   **Archivos principales:**  
   - `main.py`: Código principal de la aplicación. Define la interfaz de usuario y el servidor utilizando Shiny.  
   - `procesamiento_datos.py`: Funciones para cargar, limpiar y procesar los datos de RUOA y Esolmet.  
   - `visualizaciones.py`: Funciones para generar gráficos interactivos con Plotly o Matplotlib.

   **El flujo de ejecución se realiza de la siguiente manera:**  
   1. `main.py` llama a las funciones de `procesamiento_datos.py` y `visualizaciones.py`.  
   2. Los datos se procesan y se generan gráficos interactivos.  
   3. La webapp muestra los resultados a través de la interfaz.

6. **venv/** - Entorno virtual  
   Este entorno virtual contiene todas las dependencias instaladas para ejecutar el proyecto.

   **Las carpetas dentro de `venv` son:**  
   - `Include/`: Contiene los archivos de encabezado (headers) necesarios para construir algunos paquetes instalados.  
   - `Lib/`: Contiene todos los paquetes instalados y sus dependencias.  
   - `Scripts/`: Contiene los scripts ejecutables, como el comando `pip` y el propio intérprete de Python dentro del entorno virtual.  
   - `pyvenv.cfg`: Es el archivo de configuración que identifica este entorno como virtual e indica la versión de Python usada.

   **Ojo:** La carpeta `venv/` está incluida en el archivo `.gitignore`, por lo que no se subirá al repositorio en caso de un push request. Al momento de clonar el proyecto inicialmente asegúrate de recrear el entorno virtual y las dependencias usando:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

7. **.gitignore** - Archivo de exclusiones  
   Este archivo define qué archivos o carpetas no se subirán al repositorio de GitHub. En este caso:

   ```plaintext
   __pycache__/
   *.sqlite3
   *.parquet
   .DS_Store
   venv/
   .env
   .ipynb_checkpoints/
   ```

---

## Configuración del proyecto

### Requisitos previos
- **Python 3.x instalado.**  
- Clonar este repositorio:
  ```bash
  git clone https://github.com/sogosa168/EsolRUA_webapp.git
  cd EsolRUA_webapp
  ```

---

## Instalación

1. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: .\venv\Scripts\activate
   ```

2. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar la aplicación:**
   ```bash
   python src/main.py
   ```

---

## Ejecución de la webapp  
Por defecto, la aplicación estará disponible en:  
`http://localhost:8000`

---

## Funcionalidades principales
- Visualización del historial de temperaturas, humedad, viento y radiación.  
- Análisis interactivo mediante gráficos dinámicos.  
- Evaluación del potencial solar y eólico en Temixco.

---

## Colaboración  
Cualquier contribución es bienvenida. Por favor, realiza un fork del repositorio, haz tus cambios y envía un pull request, se analizará previamente la contribución.

---

## Licencia  
**MIT License**
