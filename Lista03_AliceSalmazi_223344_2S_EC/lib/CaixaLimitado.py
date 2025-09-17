# 2. Caixa Eletrônico com Cédulas Limitadas
# Enunciado: Dado um valor de saque e um vetor com as cédulas disponíveis 
# e suas quantidades (ex.: {100:2, 50:3, 20:5, 10:8}), calcule uma combinação 
# que usa a menor quantidade total de cédulas. Se for impossível, informe.
# Entrada (exemplo): saque=380, cédulas: {100:2, 50:1, 20:5, 10:10}
# Saída (exemplo): {100:2, 50:1, 20:1, 10:1}
# Obs.: se não houver solução, imprimir impossivel.

def caixaLimitado(saque, cedulas): 
    listaSaque = {}
    valorAtualSaque = saque

    for valor, qnt in cedulas.items():
        contador = 0
        for i in range(qnt):
            if valorAtualSaque >= valor:
                valorAtualSaque -= valor
                contador += 1
                listaSaque[valor] = contador

    if valorAtualSaque != 0:
        return "Impossível!"
    else:
        return f"{listaSaque}"    