import pandas as pd
df = pd.read_csv("estudiantes.csv")
print("Datos originales:")
print(df)
df_limpio = df.dropna()
print("\nDatos después de eliminar filas con valores vacíos:")
print(df_limpio)
promedio = df_limpio.groupby("Curso")["Edad"].mean()
print("\nEdad promedio por curso (datos limpios):")
print(promedio)
promedio_df = promedio.reset_index()  # convierte la Serie en DataFrame
promedio_df.to_csv("promedio_limpio.csv", index=False)  # guarda en archivo
