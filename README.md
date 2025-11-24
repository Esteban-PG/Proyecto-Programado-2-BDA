# Proyecto-Programado-2-BDA

Análisis de Big Data para la Toma de Decisiones,

## Objetivos del proyecto

- Implementar un flujo completo de **ETL (Extract, Transform, Load)**.
- Limpiar y enriquecer un dataset de riesgo crediticio con variables derivadas.
- Almacenar los datos limpios en una base de datos **PostgreSQL**.
- Calcular **KPIs financieros y de riesgo** relevantes para la toma de decisiones.
- Construir **dashboards interactivos** en Power BI para explorar el portafolio de créditos.
- Documentar el proceso técnico de principio a fin.

---

## Flujo general de la solución

1. **Extract**

   - Se carga el dataset crudo de riesgo crediticio desde un archivo CSV.

2. **Transform**

   - Limpieza de datos:
     - Tratamiento de valores nulos en variables como `person_emp_length`, `loan_int_rate`, etc.
     - Eliminación de outliers en `person_income` y `loan_amnt`.
     - Conversión de tipos de datos (por ejemplo, `loan_status` a entero).
   - Enriquecimiento:
     - Cálculo de **gasto mensual** y **ahorro mensual**.
     - Cálculo de **índice de endeudamiento** (`loan_amnt / person_income`).
     - Asignación de un **score** a la calificación del préstamo (`loan_grade_score`).
     - Normalización de un **score_crediticio** en escala 0–100.

3. **Load**

   - Los datos limpios se guardan en un CSV limpio.
   - Estos mismos datos se cargan en PostgreSQL en la tabla `credit_risk`.

4. **Procesamiento analítico**

   - Un script en Python calcula diversos **KPIs de riesgo y liquidez** (morosidad, endeudamiento, ahorro, score, etc.).
   - Los análisis se realizan directamente sobre los datos almacenados en PostgreSQL.

5. **Visualización (Power BI)**
   - Power BI se conecta a la base de datos `credit_risk_db`.
   - Se construyen dashboards con KPIs, segmentaciones por edad, ingresos, finalidad del préstamo y calificación del crédito.

---

## Tecnologías utilizadas

- **Python** (ETL y análisis)
  - `pandas`
  - `sqlalchemy`
  - `psycopg2-binary`
- **Base de datos**: PostgreSQL
- **Visualización**: Power BI
- **Control de versiones**: Git / GitHub
