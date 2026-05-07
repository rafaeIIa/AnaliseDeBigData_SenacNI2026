import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

###### IMPORTAÇÃO E LIMPEZA ######

# Importando o .csv, definindo o separador (;) e encoding
df_intervencao_pocos = pd.read_csv('intervencao_em_pocos_2025-2026.csv', sep=',', encoding='latin1')

# Criando a cópia do arquivo que será utilizada ao longo da limpeza e cálculos estatíscos
df_intervencao_pocos_copy = df_intervencao_pocos.copy()

# Definindo as primeiras e últimas 5 linhas para visualização
print(df_intervencao_pocos_copy.head())
print(df_intervencao_pocos_copy.tail())

# Definindo o tipo de dado das colunas para verificar o que precisa ser modificado
print(df_intervencao_pocos_copy.info())

# Renomeando maior parte das colunas
df_intervencao_pocos_copy.columns = ['id_poco', 'nome_poco_estado', 'Campo', 'Bacia', 'Operador_atual',
'Operador_epoca', 'Ambiente', 'Sonda', 'Objetivo', 'Data_início', 'Data_término', 'Dias_em_intervenção']

#### INÍCIO DA LIMPEZA ######

# Alterando o tipo de dado das colunass para data e definindo parâmetros
df_pocos_copy['data_inicio'] = pd.to_datetime(df_pocos_copy['data_inicio'], dayfirst=True, errors='coerce')
df_pocos_copy['data_conclusao'] = pd.to_datetime(df_pocos_copy['data_conclusao'], dayfirst=True, errors='coerce')
df_pocos_copy['data_primeira_descoberta'] = pd.to_datetime(df_pocos_copy['data_primeira_descoberta'], dayfirst=True, errors='coerce')
df_pocos_copy['profundidade(m)'] = pd.to_numeric(df_pocos_copy['profundidade(m)'], errors='coerce')

# # Verificando o total de linhas por coluna com valor NULO
# print(df_pocos_copy.isnull().sum())

# # Verificando o total de linhas por coluna COM ESPAÇO/VAZIO 
# espacos_vazios = (df_pocos_copy == ' ').sum()
# print(espacos_vazios)   # Resultado de espaços vazios = 0

# # Preenchendo espaços vazios das colunas de tipo texto
# colunas_str = ['id_poco', 'id_bloco', 'localizacao_bacia', 'regiao_bacia', 'estado', 'ambiente',
# 'operador', 'pre_sal', 'notificacao_descoberta', 'fluido_notificacao_descoberta']

# df_pocos_copy[colunas_str] = df_pocos_copy[colunas_str].fillna('Não informado')   

# print(df_pocos_copy) 
# print(df_pocos_copy.describe())
