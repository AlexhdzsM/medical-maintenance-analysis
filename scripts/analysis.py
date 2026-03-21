import os
import pandas as pd

# Obtener ruta base del proyecto
base_path = os.path.dirname(os.path.dirname(__file__))

# Construir ruta al CSV
file_path = os.path.join(base_path, "data", "data.csv")

df = pd.read_csv(file_path)

print(df.head())

print("\nConteo por tipo de equipo:")
print(df["equipment_type"].value_counts())

print("\nPromedio downtime:")
print(df["downtime_hours"].mean())

print("\nDowntime total por equipo:")
print(df.groupby("equipment_type")["downtime_hours"].sum())

print("\nCasos por técnico:")
print(df["technician"].value_counts())

print("\nDowntime por técnico:")
print(df.groupby("technician")["downtime_hours"].sum())
