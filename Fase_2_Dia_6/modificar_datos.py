import pandas as pd
df = pd.read_csv("estudiantes.csv")
print("Datos originales:")
print(df)
df.loc[ df["Curso"].isna(), "Curso" ] = "Python (pendiente)" #para modificar un valor que este vacio
print("\nDatos modificados:")
print(df)
df.to_csv("estudiantes_modificados.csv", index=False)
