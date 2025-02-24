# %%

import pandas as pd
#%%
f= './data/raw/RUOA/2016_RUOA_HR.csv'
df=pd.read_csv(f, skiprows=[0,2,3], index_col=0,parse_dates=True, dayfirst=True)
columnas= df.columns
def verificar_tipos_variables(cols=columnas):
    for columna in cols:
        assert type(columna) is int, f"La {columna} no es entera"
    print("todas las columnas pasaron la prueba de tipos")


#vamos a ver unit test, la proxima clase, para automatizarlas despues