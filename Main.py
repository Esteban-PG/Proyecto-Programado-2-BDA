import pandas as pd
import numpy as np
import os

# =========================
# 1. Cargar el Dataset
# =========================

print("Directorio actual:", os.getcwd())

df = pd.read_csv("/Dataset/credit_risk_dataset.csv")


print("Shape original:", df.shape)
print("Primeras filas:")
print(df.head())

# =========================
# 2. Normalizar nombres de columnas
# =========================

df.columns = df.columns.str.lower()

# =========================
# 3. Revisar y manejar valores nulos
# =========================

print("\nValores nulos por columna:")
print(df.isnull().sum())

# Rellenar valores nulos básicos según tipo
df['person_emp_length'].fillna(df['person_emp_length'].median(), inplace=True)
df['loan_int_rate'].fillna(df['loan_int_rate'].median(), inplace=True)

# Si hay nulos en income, eliminarlos (variable crítica)
df = df[df['person_income'].notna()]

# =========================
# 4. Conversión de tipos
# =========================

df['loan_status'] = df['loan_status'].astype(int)

# =========================
# 5. Detección de outliers (ingresos y préstamos)
# =========================

df = df[df['person_income'] < df['person_income'].quantile(0.99)]
df = df[df['loan_amnt'] < df['loan_amnt'].quantile(0.99)]

# =========================
# 6. CREACIÓN DE NUEVAS VARIABLES
# =========================

# ---- Gasto mensual (simulado entre 55% y 75% del ingreso) ----
df["gasto_mensual"] = df["person_income"] * np.random.uniform(0.55, 0.75, len(df))

# ---- Ahorro mensual ----
df["ahorro_mensual"] = df["person_income"] - df["gasto_mensual"]

# ---- Índice de endeudamiento ----
df["indice_endeudamiento"] = df["loan_amnt"] / df["person_income"]

# ---- Score crediticio proxy (0 a 100) ----
# Fórmula basada en:
# - historial de default
# - longitud del historial crediticio
# - tasa de interés
# - grado del préstamo

# Convertir loan_grade (A,B,C,D,E) → valor numérico
grade_map = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
df["loan_grade_score"] = df["loan_grade"].map(grade_map)

# Score final (puedes ajustar pesos)
df["score_crediticio"] = (
    df["loan_grade_score"] * 15 +
    df["cb_person_cred_hist_length"] * 2 +
    (1 - df["cb_person_default_on_file"].map({"Y": 1, "N": 0})) * 30 +
    (1 - df["loan_int_rate"] / df["loan_int_rate"].max()) * 25
)

# Normalizar a 0–100
df["score_crediticio"] = 100 * (df["score_crediticio"] - df["score_crediticio"].min()) / (df["score_crediticio"].max() - df["score_crediticio"].min())

# =========================
# 7. Guardar dataset limpio
# =========================

df.to_csv("Dataset/credit_risk_dataset_clean.csv", index=False)

print("\nArchivo limpio guardado como:")
print("Dataset/credit_risk_dataset_clean.csv")

print("\nShape final:", df.shape)
