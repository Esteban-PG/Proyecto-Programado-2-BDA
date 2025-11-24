import os

from etl.etl_cleaning import run_etl
from analysis.analysis_kpis import run_analysis

def main():

    clean_path = "Dataset/credit_risk_dataset_clean.csv"

    if not os.path.exists(clean_path):
        print("No existe dataset limpio. Ejecutando ETL...")
        run_etl()
    else:
        print("Dataset limpio ya existe. Saltando ETL.")
        
    run_etl()
    resultados = run_analysis()

if __name__ == "__main__":
    main()
