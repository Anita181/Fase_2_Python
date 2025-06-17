import pandas as pd  # Importamos la librería pandas

# Leemos el archivo CSV
df = pd.read_csv("datos.csv")

# Mostramos los datos originales
print("Datos originales:")
print(df)

# Eliminamos las filas que tienen datos vacíos
df_limpio = df.dropna()

# Mostramos los datos ya limpios
print("\nDatos después de eliminar filas con valores vacíos:")
print(df_limpio)

# Guardamos la tabla limpia en un nuevo archivo
df_limpio.to_csv("datos_limpios.csv", index=False)
