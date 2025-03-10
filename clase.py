# %%
def hola_persona ( frase :str, name:str="mundo") -> None:
    print(f"Hola {name} "+ frase)

def hola_persona2 (name):
    print(f"Hola {name}")
# %%
hola_persona("cruel", name=3)
hola_persona2(3) #Regresa un NONType puesto que no regresa nada.


# %%
