import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Continuando exatamente de onde paramos na aula passada (histograma), vamos calcular os quartis e verificar se a média está dentro da faixa interquartil (entre Q1 e Q3).
# def obter_dados_do_banco(query):
#     try:
#         conexao = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="",
#             database="vendas_online"
#         )
#         cursor = conexao.cursor()
#         cursor.execute(query)
#         resultados = cursor.fetchall()
#         return resultados
#     except mysql.connector.Error as erro:
#         print(f"Erro ao conectar ao MySQL: {erro}")
#         return None
#     finally:
#         if 'conexao' in locals() and conexao.is_connected():
#             cursor.close()
#             conexao.close()

# query_produtos = "SELECT * FROM Produtos"
# dados_filtrados = obter_dados_do_banco(query_produtos) # <<<< Aqui você chama a função para obter os dados do banco e armazenar o que será convertido em um DataFrame do Pandas. 

# df_produtos = pd.DataFrame(dados_filtrados, columns=['id', 'nome_produto', 'preco', 'categoria']) # Consulta em SQL já convertida
# print(df_produtos.head()) # Verificar os dados carregados no DataFrame

# precos_array = df_produtos['preco'].to_numpy() # Convertendo a coluna 'preco' do DataFrame para um array NumPy

# precos_array_final = np.array(precos_array).astype(float) # Convertendo os preços para float, por estarem vindo do banco de dados como string (ex: Decimal('1250.00'))
# print(precos_array_final) # Verificar os preços convertidoos; estando tudo OK, podemos utilizar o array pra iniciar a análise estatística e visualização dos dados.

#Quando não conseguir fazer a conexão com o XAMPP, tentar da seguinte forma:

df_pedidos = pd.read_csv('vendas_pedidos.csv')

print(df_pedidos)

df_produtos = pd.read_csv('vendas_produtos.csv')
precos_array = df_produtos['preco'].values

print(precos_array)

df_relacionado = pd.merge(df_produtos, df_pedidos, on='id_pedido', how='inner')

print(df_relacionado)

media= np.mean(precos_array)
mediana= np.median(precos_array)

q1 = np.percentile(precos_array, 25)
q2 = np.percentile(precos_array, 50)
q3 = np.percentile(precos_array, 75)

print(f"\nPrimeiro Quartil (Q1): R$ {q1:.2f}")
print(f"Segundo Quartil (Mediana/Q2): R$ {q2:.2f}")
print(f"Terceiro Quartil (Q3): R$ {q3:.2f}")

if q1 <= media <= q3:
    print("\nA média está DENTRO da faixa interquartil (entre Q1 e Q3).")
else:
    print("\nA média está FORA da faixa interquartil (fora de Q1 e Q3).")

plt.axvline(x=q1, color='green', linestyle='--', label=f'Q1: R$ {q1:.2f}')    #ax:eixo v: vertical estilos de linha: -: contínua / --: tracejado / .: pontilhado / label: leganda
plt.axvline(x=q3, color='orange', linestyle='--', label=f'Q3: R$ {q3:.2f}')
plt.axvline(x=media, color='red', linestyle='-', label=f'Média: R$ {media:.2f}')
plt.axvline(x=mediana, color='purple', linestyle='-', label=f'Mediana: R$ {mediana:.2f}')
plt.legend()    #deve ser mencionado quando usa-se "label". Se quisr colocar a informação "dentro" do grafico, deve-se usar um modelo apropriado
plt.show()

# ###################################################
# Calcular Q1 e Q3
Q1 = np.percentile(precos_array, 25)
Q3 = np.percentile(precos_array, 75)

# Calcular IQR
IQR = Q3 - Q1

# Calcular Limites
limite_superior = Q3 + (1.5 * IQR)  #não é máximo/mínimo outlier está abaixo
limite_inferior = Q1 - (1.5 * IQR)  #outlier está acima

print(f"\n--- Limites de Outliers (Preços dos Produtos) ---")
print(f"Q1 (25%): R$ {Q1:.2f}")
print(f"Q3 (75%): R$ {Q3:.2f}")
print(f"IQR: R$ {IQR:.2f}")
print(f"Limite Superior (LS): R$ {limite_superior:.2f}")
print(f"Limite Inferior (LI): R$ {limite_inferior:.2f}")

# Identificação de Outliers Superiores e Inferiores
outliers_superiores = df_produtos[df_produtos['preco'] > limite_superior]
outliers_inferiores = df_produtos[df_produtos['preco'] < abs(limite_inferior)]  #abs: corruptela (filtra apenas termos absolutos, nem sempre é viável)

# Exibir Outliers Superiores Ordenados (Decrescente)
print(f"\n--- Outliers Superiores ({len(outliers_superiores)} produtos) ---")
print(outliers_superiores[['nome_produto', 'preco']].sort_values(by='preco', ascending=False))

# Exibir Outliers Inferiores Ordenados (Crescente)
print(f"\n--- Outliers Inferiores ({len(outliers_inferiores)} produtos) ---")
print(outliers_inferiores[['nome_produto', 'preco']].sort_values(by='preco', ascending=True))

# Garante que os DataFrames de outliers não estão vazios antes de plotar
if not outliers_inferiores.empty or not outliers_superiores.empty:
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) # 1 linha, 2 colunas
    
    # 1ª Posição: Outliers Inferiores (Crescente)
    axes[0].bar(outliers_inferiores['nome_produto'], outliers_inferiores['preco'])
    axes[0].set_title('Outliers Inferiores (Preços Mais Baixos)')
    axes[0].set_ylabel('Preço (R$)')
    axes[0].tick_params(axis='x', rotation=45, labelsize=8)
    axes[0].grid(axis='y', linestyle='--')
    
    # 2ª Posição: Outliers Superiores (Decrescente)
    # Ordenamos novamente para garantir a visualização correta
    outliers_superiores_plot = outliers_superiores.sort_values(by='preco', ascending=False)
    axes[1].bar(outliers_superiores_plot['nome_produto'], outliers_superiores_plot['preco'])
    axes[1].set_title('Outliers Superiores (Preços Mais Altos)')
    axes[1].set_ylabel('Preço (R$)')
    axes[1].tick_params(axis='x', rotation=45, labelsize=8)
    axes[1].grid(axis='y', linestyle='--')
    
    plt.tight_layout() # Ajusta automaticamente os parâmetros de subplot para dar preenchimento
    plt.show()

else:
    print("\nNão houve outliers superiores ou inferiores para plotar.")