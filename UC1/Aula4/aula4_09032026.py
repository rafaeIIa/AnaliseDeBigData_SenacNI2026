
# carro=True
# combustivel=True

# #Qual a condição para que este carro funcione?

# if carro and combustivel: #<<<ambas as condições são verdadeiras
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada pro fusquinha.")


# if carro==True and combustivel==True:
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada pro fusquinha.")
# else:
#     print("Erro de execução.")

# #Se começar com ambos "False":

# carro=False
# combustivel=False

# if not carro and not combustivel: 
#     print("Meu fusquinha está rodando.")
# elif carro==False or combustivel==False:
#     print("Não sobrou nada pro fusquinha.")
# else:
#     print("Erro de execução.")

# #Melhorias
# semana = 3
# if semana == 1:
#  print("Domingo")
# elif semana == 2:
#  print("Segunda-feira")
# elif semana == 3:
#  print("Terça-feira")
# elif semana == 4:
#  print("Quarta-feira")
# elif semana == 5:
#  print("Quinta-feira")
# elif semana == 6:
#  print("Sexta-feira")
# elif semana == 7:
#  print("Sábado")
# else: # O 'else' funciona como o 'default'
#  print("Dia inválido")

# #MATCH CASE a diferença é apenas a eficiência

# mes=6

# match mes: 
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 6:
#         print("Junho")
#     case _: #O underline funciona como o 'default' ou 'else'
#         print("Mes inváldo.")

# try:
#     numero_mes = int(input("Digite um número de 1 a 12: "))
#     match numero_mes:
#         case 1:
#             print("O número 1 corresponde a Janeiro.")
#         case 2:
#             print("O número 2 corresponde a Feveriro.")
#         case 3:
#             print("O múmero 3 corresponde a Março.")
#         case 4:
#             print("O número 4 corresponde a Abril.")
#         case 5:
#             print("O número 5 corresponde a Maio.")
#         case 6:
#             print("O número 6 corresponde a Junho.")
#         case 7:
#             print("O número 7 corresponde a Julho.")
#         case 8:
#             print("O número 8 corresponde a Agosto.")
#         case 9:
#             print("O número 9 corresponde a Setembro.")
#         case 10:
#             print("O número 10 corresponde a Outubto.")
#         case 11:
#             print("O número 11 corresponde a Novembro.")
#         case 12:
#             print("O número 12 corresponde a Dezembro.")
#         case _:
#             print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")

# except:
#     print("Entrada inválida. Por favor, digite um número inteiro.")


try:
    mes = int(input("Digite um número de 1 a 12: "))
    match mes:
        case 1:
            print("Janeiro.")
        case 2:
            print("Feveriro.")
        case 3:
            print("Março.")
        case 4:
            print("Abril.")
        case 5:
            print("Maio.")
        case 6:
            print("Junho.")
        case 7:
            print("Julho.")
        case 8:
            print("Agosto.")
        case 9:
            print("Setembro.")
        case 10:
            print("Outubto.")
        case 11:
            print("Novembro.")
        case 12:
            print("Dezembro.")
        case _:
            print(f"Número {numero_mes} inválido. Digite entre 1 e 12.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")
except:
    print("Erro desconhecido.")

# LAÇOS DE REPETICAO

intervalo=range(10)
print(intervalo)

print ('***')

for i in range (10): #dessa forma ele começa do 0
    print(i)

for numero in range (10): #quantidade de algarismos, conta até o penúltimo
    print(numero)

for numero in range (10): 
    print('número')
    print(numero)