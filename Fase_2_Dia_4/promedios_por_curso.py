import pandas as pd
df = pd.read_csv("estudiantes.csv")
print("Datos originales:")
print(df)
# Agrupa por curso y solo calcula el promedio de la edad
promedio = df.groupby("Curso")["Edad"].mean()
print("\nEdad promedio por curso:")
print(promedio)
promedio_df = promedio.reset_index()  # convierte a DataFrame
promedio_df.to_csv("promedio.csv", index=False)
