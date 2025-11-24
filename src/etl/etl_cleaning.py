import pandas as pd
import numpy as np

def run_etl():
   
    # Se carga el dataset
    df = pd.read_csv("Dataset/credit_risk_dataset.csv")

    # Vemos la forma original del dataset
    print("Shape original:", df.shape) 

    # Normalizar nombres de columnas
    df.columns = df.columns.str.lower()

    # Rellenar valores nulos básicos según tipo
    df['person_emp_length'].fillna(df['person_emp_length'].median(), inplace=True)
    df['loan_int_rate'].fillna(df['loan_int_rate'].median(), inplace=True)

    # Si hay nulos en income, eliminarlos del dataset
    df = df[df['person_income'].notna()]

    # Conversión de tipos
    df['loan_status'] = df['loan_status'].astype(int)

    
    # Detección de outliers
    df = df[df['person_income'] < df['person_income'].quantile(0.99)]
    df = df[df['loan_amnt'] < df['loan_amnt'].quantile(0.99)]

    # CREACIÓN DE NUEVAS VARIABLES
    df["gasto_mensual"] = df["person_income"] * np.random.uniform(0.55, 0.75, len(df))
    df["ahorro_mensual"] = df["person_income"] - df["gasto_mensual"]
    df["indice_endeudamiento"] = df["loan_amnt"] / df["person_income"]

    grade_map = {"A": 5, "B": 4, "C": 3, "D": 2, "E": 1}
    df["loan_grade_score"] = df["loan_grade"].map(grade_map)

    df["score_crediticio"] = (
        df["loan_grade_score"] * 15 +
        df["cb_person_cred_hist_length"] * 2 +
        (1 - df["cb_person_default_on_file"].map({"Y": 1, "N": 0})) * 30 +
        (1 - df["loan_int_rate"] / df["loan_int_rate"].max()) * 25
    )

    df["score_crediticio"] = 100 * (
        (df["score_crediticio"] - df["score_crediticio"].min()) /
        (df["score_crediticio"].max() - df["score_crediticio"].min())
    )

    # Guardar dataset limpio
    df.to_csv("Dataset/credit_risk_dataset_clean.csv", index=False)

    # Vemos la forma final del dataset
    print("\nShape final:", df.shape)

    return df
