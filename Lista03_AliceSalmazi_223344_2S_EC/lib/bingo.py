# 6. Bingo – Verificação de Ganhadores
# Enunciado: Gere M cartelas (5x5) com números válidos (faixas por coluna) ou 
# leia-as prontas. Receba a sequência de números sorteados e identifique a 
# primeira cartela vencedora (linha/coluna/diagonal completa).
# Entrada (exemplo): 2 cartelas 5x5 e sorteio: 7, 13, 22, ...
# Saída (exemplo): vencedora=cartela_2, criterio=diagonal_principal, chamadas=18.

import random

def bingo(numCartelas, sequenciaSorteio):
    cartelas = gerarCartelas(numCartelas)
    contador = 0

    for i in sequenciaSorteio:
        cartelas = verificarNumeroCartela(i, cartelas)
        horizontal = verificarHorizontal(cartelas)
        if type(horizontal) != bool:
            if horizontal[0] == True:
                return f"Vencedora: cartela {horizontal[1]}, Critério: Linha {horizontal[2]}, Chamadas: {contador}."
        diagonal = verificarDiagonal(cartelas)
        if type(diagonal) != bool:
            if diagonal[0] == True:
                return f"Vencedora: cartela {diagonal[1]}, Critério: Diagonal {diagonal[2]}, Chamadas: {contador}."
        vertical = verificarVertical(cartelas)
        if type(vertical) != bool:
            if vertical[0] == True:
                return f"Vencedora: cartela {vertical[1]}, Critério: Coluna {vertical[2]}, Chamadas: {contador}."
        contador += 1
    return f"Nenhum ganhador, chamadas: {contador}"

def gerarCartelas(numCartelas):
    cartelas = []
    for i in range(numCartelas):
        linha1 = random.sample(range(1,15), 5)
        linha2 = random.sample(range(16,30), 5)
        linha3 = random.sample(range(31,45), 4)
        linha3.insert(2, 'X')
        linha4 = random.sample(range(46,60), 5)
        linha5 = random.sample(range(61,75), 5)
        
        cartela = []
        for j in range(5):
            linha = [linha1[j], linha2[j], linha3[j], linha4[j], linha5[j]]
            cartela.append(linha)
        cartelas.append(cartela)
    return cartelas

def verificarNumeroCartela(i, cartelas):
    retornoCartelas = []
    for cartela in cartelas:
        cartelaAux = []
        for linha in cartela:
            varAux = []
            for item in linha:
                if item == i:
                    varAux.append('X')
                else:
                    varAux.append(item)
            cartelaAux.append(varAux)
        retornoCartelas.append(cartelaAux)
    return retornoCartelas

def verificarHorizontal(cartelas):
    for i, cartela in enumerate(cartelas):
        for j, linha in enumerate(cartela):
            if all(item == 'X' for item in linha):
                return True, i + 1, j
    return False

def verificarVertical(cartelas):
    for i, cartela in enumerate(cartelas):
        for j in range(5):
            if all(linha[j] == 'X' for linha in cartela):
                return True, i + 1, j + 1
    return False

def verificarDiagonal(cartelas):
    for i, cartela in enumerate(cartelas):
        principal = all(cartela[item][item] == 'X' for item in range(5))
        secundaria = all(cartela[item][4 - item] == 'X' for item in range(5))
            
        if principal:
            return True, i + 1, "principal"
        elif secundaria:
            return True, i + 1, "secundaria"
    return False