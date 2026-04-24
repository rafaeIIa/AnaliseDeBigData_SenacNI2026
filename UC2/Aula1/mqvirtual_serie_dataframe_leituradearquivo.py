import pandas as pd

# # Ler o arquivo Excel para um DataFrame
# df = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')     # Caso o arquivo não esteja na mesma pasta, copiar o caminho completo e acrescentar mais uma /, ou "../" (com uma parte do caminho em comum)
# # OU
# df = pd.read_excel('base_invest.xlsx', sheet_name=0)

# # Exibir as primeiras 5 linhas do DataFrame
# print(df.head())

# # Exibir as 5 últimas linhas do Dataframe
# print(df.tail())

# notas = pd.Series([9.5, 8.0, 7.5, 9.0], index=['João', 'Maria', 'Pedro', 'Ana'])

# print(notas)

# # Daqui, podemos realizar consultas mais específicas:
# print(notas['Maria']) # Acessando a nota de Maria
# print(notas['Pedro']) # Acessando a nota de Pedro
# print(notas.mode())
# print(notas.median())
# print(notas.mean()) # Calculando a média das notas
# print(notas[notas > 8]) # Filtrando notas maiores que 8
# print(notas.describe()) # Estatísticas descritivas das nota (count, mean, max, var, std, 25%, 50%, 75%)
# Outros comanddos: .min / .max / .count / .var / .std (desvio de padrão) / .describe (25%, 50% - mediana,75%) / .sum / .groupby / .pencentile / .quantile / .loc / .iloc / .query / .head / .tail

# notas_ajustadas = notas * 1.10
# print(notas_ajustadas)

# # Criar uma segunda Series para comparar
# notas_exame_final = pd.Series([10.0, 7.5, 8.0, 9.5], index=['João', 'Maria', 'Pedro', 'Ana'])
# # Calcular a diferença entre as notas
# diferenca = notas_exame_final - notas_ajustadas
# print(diferenca)

# 30/03/2026
#Atividade prática

# Você recebeu um conjunto de dados de uma empresa de tecnologia voltada para aplicações
# de investimentos. O objetivo é responder algumas perguntas importantes:
# 1- Quais são as máximas e mínimas de operação de compra e venda das transações?
# 2- Qual CNPJ tem o ativo de maior valor?
# 3- Qual valor total em transações de cada participante?
# Usando os conceitos de DataFrame e os comandos que aprendemos, crie um script que
# carregue os dados e responda a essas perguntas

# 1- Quais são as máximas e mínimas de operação de compra e venda das transações?
# print(notas[notas > 8]) # Filtrando notas maiores que 8

# df = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes') 
# max_min= df['operacao']
# max_min_compra = max_min == 'compra'
# max_min_venda = max_min == 'venda'

# max_min_compra= df ['preco']

# print(max_min_compra.max())
# print(max_min_compra.min())

# print(max_min_venda.max())
# print(max_min_venda.min())

#________________________________
###RESOLUÇÃO DOUGLAS###
# df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
# df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

# # Pergunta 1: Quais são as máximas e mínimas de operação de compra e venda das transações? ---
# # variável nova    tabela[filtro]
# df_compra = df_transacoes[df_transacoes['operacao'] == 'compra']
# #
# df_venda = df_transacoes[df_transacoes['operacao'] == 'venda']
# print(df_compra)    #Boa prátic: printar para verificar se o códig está dando certo
# print(df_venda)

# max_compra_preco = df_compra['preco'].max()
# min_compra_preco = df_compra['preco'].min()
# max_venda_preco = df_venda['preco'].max()
# min_venda_preco = df_venda['preco'].min()

# print("--- Preços máximos e mínimos das operações ---")
# print(f"Preço máximo de compra: {max_compra_preco}")
# print(f"Preço mínimo de compra: {min_compra_preco}")
# print(f"Preço máximo de venda: {max_venda_preco}")
# print(f"Preço mínimo de venda: {min_venda_preco}")
# print("\n")

#________________________________
# # 2- Qual CNPJ tem o ativo de maior valor?
df = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')  

#________________________________
###RESOLUÇÃO DOUGLAS###
df_transacoes = pd.read_excel('base_invest.xlsx', sheet_name='Transacoes')
df_ativo = pd.read_excel('base_invest.xlsx', sheet_name='Ativo')

df_transacoes['valor_total'] = df_transacoes['quantidade'] * df_transacoes['preco']
valor_por_ativo = df_transacoes.groupby('id_ativo')['valor_total'].sum()
id_ativo_maior_valor = valor_por_ativo.idxmax()
cnpj_maior_valor = df_ativo[df_ativo['id_ativo'] == id_ativo_maior_valor]['cnpj'].iloc[0]

