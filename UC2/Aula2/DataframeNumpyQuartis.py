# import numpy as np      # Foram utilizadas as duas bibliotecas para teste

# # Dados de exemplo
# # dados = np.array([12, 15, 17, 20, 22, 25, 28, 30, 35, 40])

# print(dados)        # retorna dessa forma no terminal: '[12 15 17 20 22 25 28 30 35 40]', sem virgula, é um ARRAY

# # Calcular quartis
# q1 = np.percentile(dados, 25) # O 1º quartil representa 25% dos dados       
# q2 = np.percentile(dados, 50) # A Mediana é o mesmo que o quartil de 50%
# q3 = np.percentile(dados, 75) # O 3º quartil representa 75% dos dados

# # Exibir os resultados
# print(f"Primeiro quartil (Q1): {q1}")
# print(f"Segundo quartil (Q2, Mediana): {q2}")
# print(f"Terceiro quartil (Q3): {q3}")

import pandas as pd

# Carregar a planilha 'Transacoes' para um DataFrame
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
# # Exibir as primeiras 5 linhas para verificar os dados
# print(df_transacoes.head())

# # Calcule o Q1, Q2 (Mediana) e Q3 para a coluna 'preco' (QUANTILE - PANDAS / PERCENTILE - NUMPY)
# q1_preco = df_transacoes['preco'].quantile(0.25)
# q2_preco = df_transacoes['preco'].quantile(0.50)    # 32.843430000000005 é a mediana, por isso aparece com tantas casas decimais. Pode ser arredondada no final, mas durante o processo não. Tendência central
# q3_preco = df_transacoes['preco'].quantile(0.75)

# print(f"Preço Q1: {q1_preco}")
# print(f"Preço Mediana (Q2): {q2_preco}")
# print(f"Preço Q3: {q3_preco}")

# Selecione a linha com índice 2 (iloc)
# print(df_transacoes.iloc[2])
# Selecione a linha com id_participante igual a 101 (query)
# print(df_transacoes.query("id_participante == 101"))            # mais interessante para fazer filtros exatos (== 101), tem esse formato específico, pois vem do SQL. Deve ser nesse formato entre ""

# print(df_transacoes.loc[df_transacoes['preco']>32.8])

# import pandas as pd
# import matplotlib.pyplot as plt
# # Contar a frequência de cada tipo de operação
# contagem_operacao = df_transacoes['operacao'].value_counts()
# # Criar um gráfico de barras
# contagem_operacao.plot(kind='bar', title='Tipos de Operação')
# # Mostrar o gráfico
# plt.show()