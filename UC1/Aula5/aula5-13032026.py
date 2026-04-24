# carro=False
# combustivel=False

# # Qual a condição pra que este carro funcione?
# #   not(F)==V        not(F)==V
# if not carro and not combustivel: # <<< ambas as condições são verdadeiras: é o que eu quero
#     print("Meu fusquinha está rodando.")
# else:
#     print("Não sobrou nada pro fusquinha.")

# print('*'*15)

# if not carro and not combustivel: # <<< ambas as condições são verdadeiras: é o que eu quero
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada pro fusquinha.")
# else:
#     print('Erro de execução.')

# print('*'*15)

#Melhorias: 

# semana = int(input("Informe o dia da semana:")) 
 
# if semana == 1:  
#     print("Domingo") 
# elif semana == 2: 
#     print("Segunda-feira") 
# elif semana == 3: 
#     print("Terça-feira") 
# elif semana == 4: 
#     print("Quarta-feira") 
# elif semana == 5: 
#     print("Quinta-feira") 
# elif semana == 6: 
#     print("Sexta-feira") 
# elif semana == 7: 
#     print("Sábado") 
# else: # O 'else' funciona como o 'default' 
#     print("Dia inválido")

# #MATCH CASE:
# mes = int(input("Informe o mês:"))
 
# match mes: 
#     case 1: 
#         print("Janeiro") 
#     case 2: 
#         print("Fevereiro") 
#     case 3: 
#         print("Março") 
#     case 6: 
#         print("Junho") 
#     case _: # O underline ( _ ) funciona como o 'default' ou 'else' 
#         print("Mês inválido")

######################13DE_MARÇO###########################

# >>> WHILE

# loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito

# while loolap > 300:
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=0

# while loolap > 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=300

while loolap >= 300:
    loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
    print('Mas não vou mesmo!!!')

# print('Estarei lá!')


#######

# LISTAS:

# nomes = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']

# nome1 = nomes[0]

# print(nomes[-1])
# print(nomes[-2])
# print(nomes[-3])
# print(nomes[-4])
# print(nome1)

# primeira_parte=nomes[0:3]
# print(primeira_parte)
# segunda_parte=nomes[3:6]
# print(segunda_parte)

# print(len(nomes))


# # >>> usando laço de repetição 'for'
# for i in range(5):
#     try:
#  # i representa o número atual da repetição (0, 1, 2...)
#         print(f"Número {i + 1} de 5:")
#         num = float(input("Digite um número: "))
 
#         dobro = num * 2
#         triplo = num * 3
#         quádruplo = num * 4
 
#         print(f" Resultado: Dobro={dobro}, Triplo={triplo}, Quádruplo={quádruplo}\n")
 
#     except ValueError:
#         print("Entrada inválida. Tente novamente.")

# >>> Usando laço de repetição ' WHILE '
# >>> WHILE

# loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito

# while loolap > 300:
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=0

# while loolap > 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')
# ##

# loolap=300

# while loolap >= 300:
#     loolap=float(input('Qual o valor do evento (inteira)?')) #Dependnedo do input, cai num loop infinito
#     print('Mas não vou mesmo!!!')

# print('Estarei lá!')


nomes = ['Matheus','Alice','Caio','Larissa','Miguel','Rafael']

# lista1=[]
# tupla1=()
# set1=() #ou set={} #não tem ordem
# dict1={:} #é mais organizado. Rótulo/chave:valor ex: "Idade:19" .json

#TUPLAS:
nomes_tupla=tuple(nomes)
print(nomes_tupla)
#SET
nomes_set=set(nomes)
print(nomes_set)
#DICIONÁRIOS
nomes_dict={'nome1':'Matheus',
            'nome2': 'Alice',
            'nome3': 'Caio',
            'nome4': 'Larissa',
            'nome5': 'Miguel',
            'nome6': 'Rafael'}
print(nomes_dict)
