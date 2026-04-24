# PK: Primary Key
# FK: Foreign Key - quando uma chave não é daquela tabela (ex: pegar a chave Id_forn da tabela Forneedore e levar para Produto. a tabela produtos, será FK)
# Cardinalidade: como as ligações acontecem (1:1; 1:n; n:1, n:n) normlmente, quando n:n, gera-se uma nova tabela

######################

import mysql.connector

# 1. Conectar ao banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="vendas_online"
)

# 2. Criar um objeto cursor para executar as queries
cursor = conexao.cursor()

# 3. Definir a query
query = "SELECT * FROM produtos"

# 4. Executar a query
cursor.execute(query)

# 5. Obter os resultados
resultados = cursor.fetchall()

# 6. Exibir os resultados
for linha in resultados:
    print(linha)

# # 7. Fechar a conexão
# cursor.close()
# conexao.close()

# ######################

# import mysql.connector

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

# # Usando a função
# query_produtos = "SELECT * FROM produtos WHERE preco > 100"
# dados_filtrados = obter_dados_do_banco(query_produtos)

# if dados_filtrados:
#     for produto in dados_filtrados:
#         print(produto)
