from etl.etl_cleaning import run_etl

def main():
    import os
    print("Python está ejecutando desde:", os.getcwd())

    print("========== INICIANDO ETL ==========\n")
    df_clean = run_etl()
    print("\n========== ETL COMPLETADO ==========\n")

if __name__ == "__main__":
    main()
