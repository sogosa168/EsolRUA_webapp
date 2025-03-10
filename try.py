#%%

import pandas as pd
import os

#%%

def verificar(directorio, años=range(2010, 2025)):
    archivos_nombre = [f"data/raw/ESOLMET/{año}_ESOLMET.csv" for año in años]
    #archivos_nombre = [f"data/raw/RUOA/{año}_RUOA_HR.csv" for año in años]

    archivos = [archivo for archivo in archivos_nombre if os.path.exists(archivo)]

    if not archivos:
        print("no se encontraron archivos, o sea, no hay nada que revisar.")
        return  

    columnas_todos = {}         # columnas de cada archivo
    archivos_diferentes = {}    # archivos con estructura diferente

    for archivo in archivos:
        try:
            # leemos
            df = pd.read_csv(archivo, encoding='latin-1', engine='python')

            # vemossi hay un encabezado 'erroneo' (por ejemplo, columnas numéricas)
            encabezado_cols = any(col.isnumeric() for col in df.columns)

            if encabezado_cols:
                # si la primera fila es información extra, se omite
                df = pd.read_csv(archivo, skiprows=1, encoding='latin-1', engine='python', index_col=0)
            
            columnas_todos[archivo] = set(df.columns)  # guardamos  columnas del archivo

        except Exception as e:
            print(f"hay un error al leer el archivo {archivo}: {e}")

    # sencontramos las columnas generales a todos los archivos
    todas_columnas = list(columnas_todos.values())
    columnas_generales = set.intersection(*todas_columnas) if todas_columnas else set()

    # revisamos cuales archivos tienen columnas diferentes a las generales
    for archivo, columnas_actuales in columnas_todos.items():
        if columnas_actuales != columnas_generales:
            columnas_faltantes = columnas_generales - columnas_actuales
            columnas_adicionales = columnas_actuales - columnas_generales

            archivos_diferentes[archivo] = {
                "faltantes": columnas_faltantes if columnas_faltantes else "ninguna",
                "adicionales": columnas_adicionales if columnas_adicionales else "ninguna"
            }

    if archivos_diferentes:
        print("\narchivos con estructura diferente:")
        for archivo, diferencias in archivos_diferentes.items():
            print(f"\narchivo: {archivo}")
            print(f"   columnas que le faltan: {diferencias['faltantes']}")
            print(f"   columnas que tiene de más: {diferencias['adicionales']}")
    else:
        print("todos tienen las mismas columnas.")

verificar(".")


#La entrada sera un diccionario y te regresa si esas columnas que vienen en el dccionario corresponden al tipo devariables que espero no regresa el df solo el diciconario 