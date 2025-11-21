from etl.etl_cleaning import run_etl
from analysis.analysis_kpis import run_analysis

def main():

    df_clean = run_etl()

    resultados = run_analysis()

if __name__ == "__main__":
    main()
