import pandas as pd
import numpy as np

def run_analysis():

    print("========== INICIANDO ANÁLISIS ==========\n")

    # =========================
    # 1. Cargar dataset limpio
    # =========================
    df = pd.read_csv("Dataset/credit_risk_dataset_clean.csv")
    print("Dataset limpio cargado correctamente.")
    print("Shape:", df.shape)

    # =========================
    # 2. KPI: Tasa de morosidad
    # =========================
    tasa_morosidad = df["loan_status"].mean() * 100

    # =========================
    # 3. KPI: Índice de riesgo promedio
    # =========================
    indice_riesgo_promedio = df["indice_endeudamiento"].mean()

    # =========================
    # 4. KPI: Ahorro mensual promedio
    # =========================
    ahorro_promedio = df["ahorro_mensual"].mean()

    # =========================
    # 5. KPI: Endeudamiento promedio (% del ingreso)
    # =========================
    endeudamiento_promedio = df["indice_endeudamiento"].mean() * 100

    # =========================
    # 6. KPI: Score crediticio promedio
    # =========================
    score_promedio = df["score_crediticio"].mean()

    # =========================
    # 7. KPI: Ingreso promedio
    # =========================
    ingreso_promedio = df["person_income"].mean()

    # =========================
    # 8. KPI: Tendencia de ahorro por grupo de edad
    # =========================
    df["grupo_edad"] = pd.cut(df["person_age"],
                              bins=[18, 25, 35, 45, 60, 100],
                              labels=["18-25", "26-35", "36-45", "46-60", "60+"])

    ahorro_por_edad = df.groupby("grupo_edad")["ahorro_mensual"].mean()

    # =========================
    # 9. KPI: Endeudamiento por rango de ingresos
    # =========================
    df["rango_ingresos"] = pd.cut(df["person_income"],
                                  bins=[0, 20000, 40000, 60000, 100000, 1000000],
                                  labels=["0-20k", "20k-40k", "40k-60k", "60k-100k", "100k+"])

    endeudamiento_por_ingresos = df.groupby("rango_ingresos")["indice_endeudamiento"].mean()

    # =========================
    # 10. KPI: Score por loan_grade
    # =========================
    score_por_grade = df.groupby("loan_grade")["score_crediticio"].mean()

    # =========================
    # 11. Imprimir KPIs
    # =========================
    print("\n========== RESULTADOS ==========\n")
    print(f"Tasa de morosidad: {tasa_morosidad:.2f}%")
    print(f"Índice de riesgo promedio (endeudamiento): {indice_riesgo_promedio:.4f}")
    print(f"Ahorro mensual promedio: {ahorro_promedio:,.2f}")
    print(f"Endeudamiento promedio (% del ingreso): {endeudamiento_promedio:.2f}%")
    print(f"Score crediticio promedio: {score_promedio:.2f}")
    print(f"Ingreso mensual promedio: {ingreso_promedio:,.2f}\n")

    print("Ahorro promedio por grupo de edad:")
    print(ahorro_por_edad, "\n")

    print("Endeudamiento por rango de ingresos:")
    print(endeudamiento_por_ingresos, "\n")

    print("Score crediticio promedio por Loan Grade:")
    print(score_por_grade, "\n")

    # =========================
    # 12. Devolver resultados en un diccionario
    # =========================
    resultados = {
        "tasa_morosidad": tasa_morosidad,
        "indice_riesgo_promedio": indice_riesgo_promedio,
        "ahorro_promedio": ahorro_promedio,
        "endeudamiento_promedio": endeudamiento_promedio,
        "score_promedio": score_promedio,
        "ingreso_promedio": ingreso_promedio,
        "ahorro_por_edad": ahorro_por_edad,
        "endeudamiento_por_ingresos": endeudamiento_por_ingresos,
        "score_por_grade": score_por_grade
    }
    
    return resultados
