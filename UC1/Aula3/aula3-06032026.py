# # ## ESTRUTURAS DE DECISÃO IF/ELIF/ELSE

# # # chover=True                 ## Se chover
# # # rafa_presenca=None          ## variável vazia

# # # if chover== True:           ## Se chover
# # #     rafa_presenca=False     ## rafa não estará presente
# # # else:                       ## Se for diferente (não chover)
# # #     rafa_presenca=True      ## rafa estará presente

# # # placar_time1=None
# # # placar_time2=None
# # # resultado=None

# # # if placar_time1>placar_time2: #IDENTAÇÃO
# # #         resultado= 'Time 1 ganhou!'     
# # # elif placar_time1<placar_time2:
# # #         resultado='Time 2 ganhou!'
# # # else:
# # #         resultado= 'Empate!'

# # # x= 21
# # # y= 10
# # # print("x é maior que Y?", x>y)
# # # print("x é igual a Y?", x==y)

# # # tem_carteira=True
# # # idade=17
# # # tem_carro=False
# # # pode_dirigir=(idade>=18 and tem_carteira)and bebe==False ##parenteses não obrigatório. Nesse caso foi usado apenas para evidenciar
# # # print("Pode irigir?", pode_dirigir)
# # # print("Pode dirigir e tem carro?", pode_dirigir or tem_carro)

# # frase= "Python é divertido"
# # print(frase.upper())
# # print(frase.lower())
# # nova_frase=frase.replace("divertido","poderoso") #entre "" a ordem é o que você quer mudar pelo novo termmo/palavra
# # print(nova_frase)

# contador=0
# contador+=5         #INCREMENTO
# contador-=2         #DECREMENTO
# contador*=3
# contador/=3         #Evitar divisão, pois normalmente ocorrem alguns erros
# print("Valor final do contador:", contador)

# itens_carrinho=0
# itens_carrinho=itens_carrinho+1  ##NÃO SE PODE ACRESCENTAR/REALIZAR OPERAÇÕES AO VAZIO, APENAS SUBSTITUIR
# print(itens_carrinho)

a=int(input("Digite uma nota:")) 
b=20
c=30
media=(a+b+c)/3
print("Média:", media)
print("A média é maior que 15 e menor que 25?",15<media<25)

# nota=int(input("Nota:"))
# print(nota)
