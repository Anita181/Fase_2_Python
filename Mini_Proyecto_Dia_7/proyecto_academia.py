import pandas as pd
df = pd.read_csv("estudiantes_academia.csv")
print("Datos originales:")
print(df)
df_limpio = df.dropna()
print("\nDatos después de eliminar filas con valores vacíos:")
print(df_limpio)
promedio = df_limpio.groupby("Curso")["Edad"].mean()
print(promedio)
promedio_df = promedio.reset_index()  # convierte la Serie en DataFrame
promedio_df.to_csv("edad_promedio.csv", index=False)  # guarda en archivo
df_limpio.to_csv("estudiantes_limpios.csv", index=False)