######      LISTA / SET / TUPLA / DICIONÁRIO        #####
# lista1 = [100,22,43,23,675,23,12,55]
#  INDICES   0  1  2   3  4  5  6  7 
# for i in lista01:
#     print(i,':', type (i))

# fruta1='morango'
# fruta2='banana'
# lista2= [100,'cem','#$%',20224.3154,True,None,[1,2,3],fruta1,fruta2]

# print(lista2[6][2])

# nomes_att=['Daniela Correia','Luciene Silva','Rafael Fernandes']
# #                  0                 1              2      
# dani=nomes_att[0][8:]
# luciene=nomes_att[1][8:]
# rafael=nomes_att[2][7:]         #para pegar o primeiro nome, inverter a ordem da contage, e dos ':', ex: :7, para imprimir 'Rafael'
# #sobrenomes=[dani,luciene,rafael] usar com print(sobrenomes)
# sobrenomes=[]

#print(sobrenomes)

# for i in nomes_att:
#     for j in nomes_att[0]:
#         sobrenomes.append(nomes_att)
# print(sobrenomes)

#                             #pop remove sem ordem
# nome5='Luciene'
# nome4='Miguel'
# nomes_att.insert(2,nome4)   #adiciona com ordem
# nomes_att.append(nome5)     #adiciona sem ordem
# nomes_att.append(nome5)     
# # nomes_att.remove('Luciene') #remove com ordem

# print(nomes_att.index('Luciene'))
# nomezinhos=nomes_att.copy()     #importante trabalhar com a copia da lista, caso haja algum erro

# nomezinhos=nomes_att.clear()

# print(nomezinhos)


##### TUPLAS #### --- Não editável/Imutável

# pares=(40,20,2,18,14,34,96,30,20,58)
# print(pares[3])
# print(pares[3:])
# print(pares[3:8])
# print(len(pares))
# pares=pares+(44,)
#print(pares)
# lista_pares=list(pares)
# print(lista_pares)
# lista_pares.append(102)
# lista_pares.sort()
# lista_pares=tuple(lista_pares)
# print(lista_pares)

##### SET ###### ---- Não tem ordem e não aceita duplicatas, mais usado em situações em q não interessa a "fonte" da informação
# impares={33,5,17,11,27,11,71,79,99,15}
# print(impares)
# print(type(impares))
# impares_02={11,3,23,83,15,73}
# l_impares=list(impares_02)
# print(intersecao)

#### DICIONARIO ####    mutável, sem duplicatas (chaves devem ser diferentes)
# filme={
#     'nome':'V for Vendetta',
#     'ano':2005,
#     'genero': 'Ação',    #Thriller/Drama
#     'faixa_etaria': 16
# }

# print(filme)
# print(type(filme))

# print(filme.keys())
# print(filme.values())
# print(len(filme))

# filme['duracao']='130min'
# filme['genero']='Thriller/Drama'
# filme['genero']=None
# print(filme)

#20.03.2026

#'''Vamos desenvolver um progtama que leia 5 nome de filmes e armazene nas 4 formas, mostrando as diferenças na prática''

#Coleta dos dados:
dados_entrada=[]
print("Digite 5 nomes de filmes:" )
for i in range(5):
    nome = input(f"Filme {i+1}: ")
    dados_entrada.append(nome) #Usando LISTA para 

print("-"*30)

#Armazenamento e Exibição:
#1. LISTA
lista_filmes=dados_entrada
print(lista_filmes)

# 2. TUPLA: 
tupla_filmes = tuple(dados_entrada) 

# 3. SET:  
set_filmes = set(dados_entrada) 

# 4. DICIONÁRIO: Usando o índice como chave (ex: 1: 'Filme A') 
dicionario_filmes = {} 
for i in range(len(dados_entrada)): # Repetição pelo tamanho da lista 
    # Usando o índice (i+1) como CHAVE e o nome como VALOR 
    dicionario_filmes[i + 1] = dados_entrada[i] 

print(f"LISTA (Flexível): {lista_filmes}") 
print(f"TUPLA (Fixa): {tupla_filmes}") 
print(f"SET (Apenas Únicos): {set_filmes}") 
print(f"DICIONÁRIO (Chave: Valor): {dicionario_filmes}")

