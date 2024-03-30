# %%
import pandas as pd
df = pd.read_csv('Dados/covid.csv', sep=',')
df.head(5)




# %%
df.columns




# Tratamento de nomes
# %%
nomes = {
    'USMER': 'usmr', 
    'MEDICAL_UNIT': 'unidade_medica',
    'SEX': 'sexo', 
    'PATIENT_TYPE': 'tipo_paciente', 
    'DATE_DIED': 'data_obito', 
    'INTUBED': 'intubado',
    'PNEUMONIA': 'pneumonia', 
    'AGE': 'idade', 
    'PREGNANT': 'gravidez', 
    'DIABETES': 'diabetes', 
    'COPD': 'doenca_pulmonar_obstrutiva', 
    'ASTHMA': 'asma', 
    'INMSUPR': 'imunossuprimido',
    'HIPERTENSION': 'hipertensao', 
    'OTHER_DISEASE': 'outras_doencas', 
    'CARDIOVASCULAR': 'cardiovascular', 
    'OBESITY': 'obesidade',
    'RENAL_CHRONIC': 'doenca_renal_cronica', 
    'TOBACCO': 'fumante', 
    'CLASIFFICATION_FINAL': 'classificacao', 
    'ICU':'uti'
}

df = df.rename(columns=nomes)
df.head(5)


# %%
