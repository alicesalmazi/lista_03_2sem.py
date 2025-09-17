# Controle de Estoque por Operações
# Enunciado: Dado um vetor com o estoque inicial de produtos e uma sequência de 
# operações no formato "E codigo qtd" (entrada) ou "S codigo qtd" (saída), 
# atualize o estoque. Impeça saídas maiores que o disponível e registre erros. 
# Ao final, imprima o estoque e o total de operações inválidas.
# Entrada (exemplo): estoque inicial {A:10, B:3}, operações: E A 5, S B 2, S A 20
# Saída (exemplo): estoque final {A:15, B:1}, inválidas: 1 (por S A 20).

def controleEstoque(estoque, operacoes):
    operacoesTratadas = ("".join(operacoes.split())).split(",")
    erros = []
    contador = 0

    for operacao in operacoesTratadas:
        for i, caractere in enumerate(operacao):
                if i == 0:
                    if caractere == "E":
                        operador = True
                    elif caractere == "S":
                        operador = False
                    else:
                        erros.append(operacao)
                        contador += 1
                        continue
                elif i == 1:
                    if caractere not in estoque.keys():
                        erros.append(operacao)
                        contador += 1
                        continue
                    else:
                        codigo = caractere
                elif i == 2: 
                    try:
                        qnt = int(operacao[2:])
                        if operador == True:
                            estoque[codigo] += qnt
                        else:
                            if qnt > estoque[codigo]:
                                erros.append(operacao)
                                contador += 1  
                                continue
                            else:
                                estoque[codigo] += qnt
                    except ValueError:
                        erros.append(operacao)
                        contador += 1
                        continue

    return f"Estoque final: {estoque}." if contador == 0 else f"Estoque final: {estoque}, inválidas: {contador} (por {" ".join(operacao[:3]) + operacao[3:]})." 