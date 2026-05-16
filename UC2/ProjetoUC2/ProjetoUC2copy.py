import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

###### IMPORTAÇÃO E LIMPEZA ######

# Importando o .csv, definindo o separador (;) e encoding
df_intervencao_pocos = pd.read_csv('intervencao_em_pocos_2025-2026.csv', sep=',', encoding='utf-8')

# Criando a cópia do arquivo que será utilizada ao longo da limpeza e cálculos estatíscos
df_intervencao_pocos_copy = df_intervencao_pocos.copy()

# # # Definindo as primeiras e últimas 5 linhas para visualização
# # print(df_intervencao_pocos_copy.head())
# # print(df_intervencao_pocos_copy.tail())

# # # Definindo o tipo de dado das colunas para verificar o que precisa ser modificado
# # print(df_intervencao_pocos_copy.info())

# Renomeando maior parte das colunas
df_intervencao_pocos_copy.columns = ['Nome_poco_anp', 'Nome_poco_operador', 'Campo', 'Bacia', 'Operador_atual', 'Operador_epoca', 'Ambiente', 
'Sonda', 'Objetivo', 'Data_inicio','Data_termino', 'Dias_em_intervencao']

# # #### INÍCIO DA LIMPEZA ######

# Alterando o tipo de dado das colunass para data e definindo parâmetros
df_intervencao_pocos_copy['Data_inicio'] = pd.to_datetime(df_intervencao_pocos_copy['Data_inicio'], dayfirst=True, errors='coerce')
df_intervencao_pocos_copy['Data_termino'] = pd.to_datetime(df_intervencao_pocos_copy['Data_termino'], dayfirst=True, errors='coerce')

# Verificando o total de linhas por coluna com valor NULO
# # # print(df_intervencao_pocos_copy)
# # # print(df_intervencao_pocos_copy.isnull().sum())

# Verificando o total de linhas por coluna COM ESPAÇO/VAZIO 
espacos_vazios = (df_intervencao_pocos_copy == ' ').sum()
# # print(espacos_vazios)   # Resultado de espaços vazios = 3 na coluna Operador_epoca

# # # Preenchendo espaços vazios das colunas de tipo texto
df_intervencao_pocos_copy['Operador_epoca'] = df_intervencao_pocos_copy['Operador_epoca'].str.strip().replace('', 'Não informado')

# # # Transformando valor nulo/NaN em 'Não informado'
df_intervencao_pocos_copy['Operador_epoca'] = df_intervencao_pocos_copy['Operador_epoca'].fillna('Não informado')

# # # Recalculando os espaços vazios após as correções
espacos_vazios_atualizado = (df_intervencao_pocos_copy == ' ').sum()

# print(f"--- Nova contagem de espaços vazios:\n",espacos_vazios_atualizado)

#### VERIFICANDO NOVO ARQUIVO ######
df_intervencao_pocos_copy.to_excel("df_intervencao_pocos_copy.xlsx")    #### Sem espaços vazios, encoding correto e tipo dedos

####
# # # # # print(df_intervencao_pocos_copy)
# # # # # print(df_intervencao_pocos_copy.info())
# # # # # print(df_intervencao_pocos_copy.isnull().sum())
print(df_intervencao_pocos_copy.describe())
