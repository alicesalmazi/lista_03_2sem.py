# 9. Ranking de Campeonato (Matriz de Resultados)
# Enunciado: Dada uma matriz T x T onde m[i][j] é o número de gols do time i 
# contra o time j (e m[j][i] o inverso), compute pontos (vitória=3, empate=1), 
# saldo e ordene o ranking por pontos, saldo e gols pró.
# Entrada (exemplo): matriz 4x4 com placares
# Saída (exemplo): 1º Time 3 (7 pts, saldo +5), etc.

def rankingCampeonato(matriz):
    pontosTimes = {}
    saldoTimes = {}
    golsTimes = {}
    tamanho = len(matriz)
    
    for i in range(tamanho):
        pontos = 0
        golsPro = 0
        golsContra = 0
        for j in range(tamanho):
            if j == i:
                continue
            elif matriz[i][j] > matriz[j][i]:
                pontos += 3
            elif matriz[i][j] == matriz[j][i]:
                pontos += 1

            golsContra += matriz[j][i]
            golsPro += matriz[i][j]

        pontosTimes[f"Time {i + 1}"] = pontos
        golsTimes[f"Time {i + 1}"] = golsPro
        saldoTimes[f"Time {i + 1}"] = golsPro - golsContra

    ranking = sorted(
        pontosTimes.keys(),
        key = lambda t: (pontosTimes[t], saldoTimes[t], golsTimes[t]),
        reverse = True
    )

    for posicao, time in enumerate(ranking, start = 1):
        print(f"{posicao}º {time} ({pontosTimes[time]} pts, saldo {saldoTimes[time]}, gols pró {golsTimes[time]}).")