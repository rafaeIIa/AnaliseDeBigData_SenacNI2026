def desconto_usuario(valor_final,valor_compra):
    """
    Função para fornecer desconto ao cliente em
    caso de aniversário ou outros contextos
    """
    faz_aniversario= input("Hoje é seu aniversário? Responda com SIM ou NAO")
    
    if faz_aniversario== "SIM":
        desconto= valor_compra*0.15
        valor_final= valor_compra-desconto
        print(f"Você ganhou um desconto de {desconto}!")
    
    elif faz_aniversario== "NAO": 
        valor_final=valor_compra
        print("Compra sem desconto")
        return (valor_final,valor_compra)

    else:
        print("Resposta inválida. Digite apenas SIM ou NAO")
