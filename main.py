def pedir_valor(frase):
    valor = float(input(frase))
    return valor

def calcular_desconto(preco, cupom):
    valor_final = preco - cupom
    return valor_final

def mostrar_recibo(total):
    print(f"O valor com desconto é: R$ {total}")
    
print("Bem-vindo à Loja Simples!")
p = pedir_valor("Digite o preço do produto: ")
d = pedir_valor("Digite o valor do desconto: ")

resultado = calcular_desconto(p, d)
mostrar_recibo(resultado)
