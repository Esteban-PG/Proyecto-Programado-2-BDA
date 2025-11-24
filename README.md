# Proyecto-Programado-2-BDA

Análisis de Big Data para la Toma de Decisiones,

CREATE TABLE credit_risk (
person_age INT,
person_income NUMERIC(10,2),
person_home_ownership VARCHAR(20),
person_emp_length NUMERIC(5,2),
loan_intent VARCHAR(50),
loan_grade CHAR(1),
loan_amnt INT,
loan_int_rate NUMERIC(5,2),
loan_status INT,
loan_percent_income NUMERIC(6,3),
cb_person_default_on_file CHAR(1),
cb_person_cred_hist_length INT,
gasto_mensual NUMERIC(10,2),
ahorro_mensual NUMERIC(10,2),
indice_endeudamiento NUMERIC(8,4),
loan_grade_score NUMERIC(5,2),
score_crediticio NUMERIC(6,2)
);

CREATE DATABASE credit_risk_db;

CREATE USER credit_user WITH ENCRYPTED PASSWORD '1010';

GRANT ALL PRIVILEGES ON DATABASE credit_risk_db TO credit_user;
