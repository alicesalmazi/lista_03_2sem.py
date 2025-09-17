# Lista 03 - Implementação de Algoritmos (decisão, repetição, vetores e matrizes)
from lib.boletimEscolar import estatisticaBoletimTurma
from lib.CaixaLimitado import caixaLimitado
from lib.controleEstoque import controleEstoque
from lib.jogoForca import jogoForca
from lib.assentosSala import assentosSala
from lib.bingo import bingo
from lib.temperaturas import analiseTemperatura
from lib.sudoku import sudoku
from lib.ranking import rankingCampeonato
from lib.atendimento import atendimento
from limpeza import limpeza

# 1.
print(estatisticaBoletimTurma(6, [7.5, 9.0, 4.0, 6.5, 8.0, 5.0]))
limpeza()
print(estatisticaBoletimTurma(8, [5.73, 1.34, 9.69, 2.07, 6.95, 5.89, 9.0, 7.39]))
limpeza()
print(estatisticaBoletimTurma(5, [8.04, 8.8, 5.79, 3.29, 2.83]))
limpeza()

# 2.
print(caixaLimitado(480, {100:2, 50:1, 20:5, 10:10}))
limpeza()
print(caixaLimitado(380, {100:2, 50:1, 20:5, 10:10}))
limpeza()
print(caixaLimitado(280, {100:2, 50:1, 20:5, 10:10}))
limpeza()

# 3.
print(controleEstoque({"A":10, "B":3}, "E A 5, S B 2, S A 20"))
limpeza()
print(controleEstoque({"A":10, "B":3}, "E A 5, S B 2"))
limpeza()

# 4.
print(jogoForca("PYTHON", ["P", "A", "O", "X", "T", "H", "N"]))
limpeza()
print(jogoForca("PPYTHON", ["P", "A", "O", "X", "T", "H", "N"]))
limpeza()
print(jogoForca("ALICE", ["A", "R", "j", "H", "3", "Ç", "O", "L", "I", "C", "E"]))
limpeza()

# 5.
print(assentosSala())
limpeza()

# 6.
sequenciaSorteada = ([63, 64, 42, 6, 27, 44, 30, 23, 70, 71, 
    21, 56, 17, 49, 13, 1, 33, 39, 4, 61, 
    37, 7, 72, 60, 48, 5, 20, 52, 29, 3, 
    16, 19, 32, 53, 58, 26, 43, 62, 50, 47, 
    55, 34, 18, 57, 51, 66, 73, 2, 74, 11, 
    68, 54, 9, 75, 24, 69, 41, 67, 10, 25, 
    40, 36, 15, 65, 35, 22, 12, 59, 14, 8, 
    46, 75, 45, 28, 72
])
print(bingo(5, sequenciaSorteada))
limpeza()

# 7.
print(analiseTemperatura([28, 31, 33, 29, 30, 34], 30))
limpeza()

# 8.
matriz = [
    [5,3,4, 6,7,8, 9,1,2],
    [6,7,2, 1,9,5, 3,4,8],
    [1,9,8, 3,4,2, 5,6,7],

    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,5,3, 7,9,1],
    [7,1,3, 9,2,4, 8,5,6],

    [9,6,1, 5,3,7, 2,8,4],
    [2,8,7, 4,1,9, 6,3,5],
    [3,4,5, 2,8,6, 1,7,9]
]
print(sudoku(matriz))
limpeza()

matrizInvalida = [
    [5,3,4, 6,7,8, 9,1,2],
    [6,7,2, 1,9,5, 3,4,8],
    [1,9,5, 3,4,2, 5,6,7],  

    [8,5,9, 7,6,1, 4,2,3],
    [4,2,6, 8,5,3, 7,9,1],
    [7,1,3, 9,2,4, 8,5,6],

    [9,6,1, 5,3,7, 2,8,4],
    [2,8,7, 4,1,9, 6,3,5],
    [3,4,5, 2,8,6, 1,7,9]
]
print(sudoku(matrizInvalida))
limpeza()

# 9.
times = [
    [0, 2, 1],  # Time 1 fez 2 contra T2, 1 contra T3
    [0, 0, 3],  # Time 2 fez 0 contra T1, 3 contra T3
    [2, 0, 0]   # Time 3 fez 2 contra T1, 0 contra T2
]
rankingCampeonato(times)
limpeza()

# 10.
print(atendimento("CHEGA Ana, CHEGA Bia, PRIORITARIO João, ATENDE, ATENDE"))
limpeza()