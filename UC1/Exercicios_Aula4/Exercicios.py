# 2. Quantidade de Caixas de Azulejos:
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento,
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em
# todas as suas paredes (considere que não será descontada a área ocupada por portas e
# janelas). Cada caixa de azulejos possui 1,5 m²

# # Parede_maior= int(input("Digite a largura da parede maior: "))
# # Parede_menor= int(input("Digite a largura da parede menor: "))
# # h= int(input("Digite a altura da cozinha: "))
# # Paredes_cozinha= ((Parede_maior*h)+(Parede_menor*h))*2
# # Qtd_azulejos= Paredes_cozinha/1.5

# # print(f"A quantidade de caixas de azulejos necessárias é: {Qtd_azulejos}")


# 3. Rendimento do Taxista:
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a
# média do consumo em km/L e o lucro (líquido) do dia.

# preco_combustivel= 6.15
# km_inicial= int(input("A kilometragem inicial é: "))
# km_final= int(input("A kilometragem final é: "))
# consumo_do_carro= 8/1
# qtd_km_rodados= km_final-km_inicial
# valor_recebido= int(input("Insira o valor recebido: "))
# qtd_combustivel_gasto= qtd_km_rodados/consumo_do_carro
# valor_gasto_combustivel= qtd_combustivel_gasto*preco_combustivel
# lucro= valor_recebido - valor_gasto_combustivel

# if lucro > 0:
#     print(f"O lucro líquido do dia é de {lucro}")

# else:
#     print("Não houve lucro") 

# print(f"\nA média do consumo do carro é de {consumo_do_carro} km/L.")
# print(f"Quantidade de combustivel gasto: {qtd_combustivel_gasto}\nValor gasto com combustivel: R${valor_gasto_combustivel}")
# print(f"A quantidade de combustivel gasto e valor são: {qtd_combustivel_gasto}L e R${valor_gasto_combustivel}")
# print(f"O valor total recebido dos passageiros é: {valor_recebido}")


# 4. Código de Origem do Produto:
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região
# de sua procedência, conforme a tabela abaixo:
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser
# encarado como “Importado”.

try:
    codigo= input("Digite o código do produto: ")
    
    match codigo:
        case 1:
            procedencia= "Sul"
        case 2:
            procedencia= "Norte"
        case 3:
            procedencia= "Leste"
        case 4:
            procedencia= "Oeste"
        case 5|6:
            procedencia= "Nordeste"
        case 7|8|9:
            procedencia= "Sudeste"
        case 10:
            procedencia= "Centro Oeste"
        case 11:
            procedencia= "Noroeste"
        case _:
            print("O produto é importado")

    print(f"A região de procedência do código {codigo} é: {procedencia}")

except ValueError:
    print("Erro. Digite um número válido")

