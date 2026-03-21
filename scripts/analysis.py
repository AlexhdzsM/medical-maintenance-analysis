import pandas as pd

# Cargar datos
df = pd.read_csv("../data/data.csv")

# Mostrar primeras filas
print("Primeras filas:")
print(df.head())

# Info general
print("\nInfo:")
print(df.info())

# Conteo por tipo de equipo
print("\nEquipos más frecuentes:")
print(df["equipment_type"].value_counts())

# Promedio de tiempo de inactividad
print("\nPromedio downtime:")
print(df["downtime_hours"].mean())
