import pandas as pd
df = pd.read_csv("estudiantes.csv")
print("Datos originales:")
print(df)
df_limpio = df.dropna()
print("\nDatos después de eliminar filas con valores vacíos:")
print(df_limpio)
df_limpio.to_csv("estudiantes_limpios.csv", index=False)
# cuántas filas limpias quedaron:
print(f"\nCantidad de estudiantes con datos completos: {len(df_limpio)}")
