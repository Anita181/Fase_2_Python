import pandas as pd
df = pd.read_csv("estudiantes.csv")
print("Datos originales:")
print(df)
df_python = df[df["Curso"] == "Python"] #filtrar columna
print(df_python)
df_ordenado = df_python.sort_values(by="Edad", ascending=False) #organizar determinada columna de mayor a menor
print(df_ordenado)
df_ordenado.to_csv("python_ordenado.csv", index=False) #para guardar la tabla nueva en un archivo aparte


