import os
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# CARGA DE DATOS
# ==============================

def load_data():
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "data", "data.csv")
    return pd.read_csv(file_path)


# ==============================
# ANÁLISIS
# ==============================

def basic_analysis(df):
    print("\nPrimeras filas:")
    print(df.head())

    print("\nConteo por tipo de equipo:")
    print(df["equipment_type"].value_counts())

    print("\nPromedio downtime general:")
    print(df["downtime_hours"].mean())

    print("\nDowntime total por equipo:")
    print(df.groupby("equipment_type")["downtime_hours"].sum())

    print("\nCasos por técnico:")
    print(df["technician"].value_counts())

    print("\nDowntime por técnico:")
    print(df.groupby("technician")["downtime_hours"].sum())

    print("\nCosto por equipo:")
    print(df.groupby("equipment_type")["cost"].sum())

    print("\nPromedio downtime por equipo:")
    print(df.groupby("equipment_type")["downtime_hours"].mean())


def failure_analysis(df):
    print("\nTipo de falla por equipo:")
    tabla = pd.crosstab(df["equipment_type"], df["failure_type"])
    print(tabla)
    return tabla


# ==============================
# VISUALIZACIÓN
# ==============================

def plot_bar(data, title, ylabel):
    data.plot(kind="bar")
    plt.title(title)
    plt.xlabel("Equipo")
    plt.ylabel(ylabel)
    plt.xticks(rotation=0, ha='right')
    plt.tight_layout()
    plt.show()


def plot_all(df, failure_table):
    plot_bar(
        df.groupby("equipment_type")["downtime_hours"].sum(),
        "Downtime total por equipo",
        "Horas"
    )

    plot_bar(
        df.groupby("equipment_type")["cost"].sum(),
        "Costo total por equipo",
        "Costo"
    )

    plot_bar(
        df.groupby("equipment_type")["downtime_hours"].mean(),
        "Promedio de downtime por equipo",
        "Horas promedio"
    )

    plot_bar(
        failure_table,
        "Tipo de falla por equipo",
        "Cantidad de fallas"
    )


# ==============================
# MAIN
# ==============================

def main():
    df = load_data()

    basic_analysis(df)
    failure_table = failure_analysis(df)

    plot_all(df, failure_table)


if __name__ == "__main__":
    main()