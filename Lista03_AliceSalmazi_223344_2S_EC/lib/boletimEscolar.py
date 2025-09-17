import math as m

# 1. Boletim da Turma com Estatísticas
# Enunciado: Leia as notas (0 a 10) de N alunos em uma lista. Calcule média da turma, 
# maior e menor nota, desvio-padrão (pode usar fórmula própria) e quantos alunos ficaram 
# acima da média. Mostre também a distribuição em faixas: [0–2), [2–4), [4–6), [6–8), [8–10].
# Entrada (exemplo): N=6 e notas: 7.5 9.0 4.0 6.5 8.0 5.0
# Saída (exemplo):
# media=6.67, maior=9.0, menor=4.0, acima_media=3
# faixas: [0-2)=0, [2-4)=0, [4-6)=2, [6-8)=2, [8-10]=2

def estatisticaBoletimTurma(N, notas):
    mediaTurma = sum(notas) / N
    maiorNota = max(notas)
    menorNota = min(notas)
    alunosAcimamedia = 0 
    listAuxiliar = []
    
    for nota in notas:
        # Calcular desvio
        desvioIndividual = nota - mediaTurma
        quadradoDesvios = m.pow(desvioIndividual, 2)
        listAuxiliar.append(quadradoDesvios)
        # Ver acima da média
        if nota > mediaTurma:
            alunosAcimamedia += 1
    
    varianciaDesvio = sum(listAuxiliar) / N
    desvioPadrao = m.pow(varianciaDesvio, 0.5)

    saida = [f"Média das notas= {mediaTurma:.2f};",f"Maior nota = {maiorNota};",f"Menor nota = {menorNota};",
        f"Notas acima da média = {alunosAcimamedia};",f"Desvio-padrão = {desvioPadrao:.2f};",
        f"""Faixas: [0-2) = {sum(0 <= nota < 2 for nota in notas)}
        [2-4) = {sum(2 <= nota < 4 for nota in notas)},
        [4-6) = {sum(4 <= nota < 6 for nota in notas)},
        [6-8) = {sum(6 <= nota < 8 for nota in notas)},
        [8-10] = {sum(8 <= nota <= 10 for nota in notas)}."""]

    return "\n".join(saida)