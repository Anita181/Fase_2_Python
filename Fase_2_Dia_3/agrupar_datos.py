import pandas as pd
df = pd.read_csv("estudiantes.csv")
print("Datos originales:")
print(df)
conteo = df.groupby("Curso").count() #para agrupar y contar cuántos valores completos hay por columna en cada grupo.
conteo_2 = df.groupby("Curso").size() #para agrupar y contar cuántas filas totales hay por grupo, sin importar si hay datos vacíos.
print("\nCantidad de estudiantes por curso:")
print(conteo)
print(conteo_2)
conteo.to_csv("conteo_estudiantes.csv", index=False)

