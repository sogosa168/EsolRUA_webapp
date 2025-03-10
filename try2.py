import pandas as pd
import os
from typing import Dict, Type

def verificar_cols(directorio: str, expected_columns: Dict[str, Type], años: range = range(2010, 2011)) -> None:
    archivos_nombre = [os.path.join(directorio, f"data/raw/ESOLMET/{año}_ESOLMET.csv") for año in años]
    #archivos_nombre = [os.path.join(directorio, f"data/raw/ESOLMET/esol_{año}.csv") for año in años]
    archivos = [archivo for archivo in archivos_nombre if os.path.exists(archivo)]

    if not archivos:
        print("no se encontraron archivos, o sea, no hay nada que revisar.")
        return  

    for archivo in archivos:
        try:
            # leemos
            df = pd.read_csv(archivo, encoding='latin-1', engine='python')

            # vemossi hay un encabezado 'erroneo' (por ejemplo, columnas numéricas)
            if any(col.isnumeric() for col in df.columns):
                # si la primera fila es información extra, se omite
                df = pd.read_csv(archivo, skiprows=1, encoding='latin-1', engine='python', index_col=0)
            
            columnas_inexistentes = []
            type_errors = []
            
            # vemos que se encuentren las columnas que esperamos exista en el csv
            for col, expected_type in expected_columns.items():
                if col not in df.columns:
                    columnas_inexistentes.append(col)
                else:
                    # y verificamos el el tipo de esa variable sea de tipo flotante, podemos cambiarlo o agregar mas 
                    if expected_type == float:
                        if not pd.api.types.is_float_dtype(df[col]):
                            type_errors.append(f"'{col}' no es de tipo float")
                    
            
            if columnas_inexistentes:
                print(f"\nArchivo: {archivo}")
                print(f"  Faltan las columnas: {columnas_inexistentes}")
            if type_errors:
                print(f"\nArchivo: {archivo}")
                print(f"  Errores de tipo: {type_errors}")
            if not columnas_inexistentes and not type_errors:
                print(f"\nArchivo: {archivo} contiene las columnas y el tipo de variable esperado para cada una.")

        except Exception as e:
            print(f"\nError al procesar el archivo {archivo}: {e}")


columnas_esperadas = {
    "I_dir_Avg": float,
    "I_glo_Avg": float,
    "I_dif_Avg": float,
    "I_uv_Avg": float,
    "AirTC_Avg": float,
    "RH": float,
    "WS_ms_Avg": float,
    "CS106_PB_Avg": float,
}

verificar_cols(".", columnas_esperadas)
