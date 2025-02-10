 
# Documentación técnica

Este documento detalla cómo funciona el backend (datos y la infraestructura que permiten que la aplicación funcione) de la webapp y los módulos que componen el proyecto.

## Estructura del proyecto
- `src/main.py`: Archivo principal de la aplicación.
- `src/procesamiento_datos.py`: Módulo para cargar y limpiar datos.
- `src/visualizaciones.py`: Funciones que generan gráficos interactivos.

## Dependencias
- `shiny`: Para la interfaz web interactiva.
- `pandas`: Para la manipulación de datos.
- `plotly`: Para la creación de gráficos interactivos.
- `sqlite3`: Para el manejo de bases de datos.

## Lógica de la aplicación
1. Se cargan los datos desde `data/` usando `procesamiento_datos.py`.
2. Los datos se procesan y filtran según las necesidades/objetivo que se pida en la visualizacion..
3. Los resultados se muestran mediante gráficos interactivos usando Plotly.
