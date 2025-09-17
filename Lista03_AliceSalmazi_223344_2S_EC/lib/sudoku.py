# 8. Sudoku Checker
# Enunciado: Receba uma matriz 9x9 e verifique se é uma solução válida de Sudoku: 
# todos os números de 1 a 9 em cada linha, coluna e subgrade 3x3. Informe o 
# primeiro erro encontrado (linha/coluna/subgrade).
# Entrada (exemplo): matriz 9x9 preenchida
# Saída (exemplo): valida=True ou valida=False, erro=subgrade(1,1).

def sudoku(matriz):
    lista = set(range(1,10))
    resultadoLinha = verificarLinha(matriz, lista)
    if resultadoLinha is not True:
        return resultadoLinha
    resultadoColuna = verificarColuna(matriz, lista)
    if resultadoColuna is not True:
        return resultadoColuna
    resultadoGrade = verificarGrade(matriz, lista)
    if resultadoGrade is not True:
        return resultadoGrade
    
    return "Válida = True"

def verificarLinha(matriz, lista):
    for i, linha in enumerate(matriz):
        if set(linha) != lista:
            return f"Válida = False, erro = linha({i})"
    return True

def verificarColuna(matriz, lista):
    for i in range(9):
        coluna = [matriz[j][i] for j in range(9)]
        if set(coluna) != lista:
            return f"Válida = False, erro = coluna({i})"
    return True

def verificarGrade(matriz, lista):
    
    for linha in (0, 3, 6):
        for coluna in (0, 3, 6):
            subgrade = []
            for i in range(3):
                for j in range(3):
                    subgrade.append(matriz[linha + i][coluna + j])
            if set(subgrade) != lista:
                return f"Válida = False, erro = subgrade({linha//3},{coluna//3})"
    return True