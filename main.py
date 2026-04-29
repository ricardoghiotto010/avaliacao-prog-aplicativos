def pedir_valor(frase):
    valor = float(input(frase))
    return valor

def calcular_desconto(preco, cupom):
    valor_final = preco - cupom
    return valor_final