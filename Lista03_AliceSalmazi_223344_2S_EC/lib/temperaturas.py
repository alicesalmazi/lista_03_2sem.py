# 7. Análise de Temperaturas com Maior Sequência Quente
# Enunciado: Dado um vetor de temperaturas diárias, calcule média, dias acima 
# da média e a maior sequência consecutiva acima de um limiar L.
# Entrada (exemplo): temps: 28, 31, 33, 29, 30, 34, L=30
# Saída (exemplo): media=30.83, acima_media=3, maior_sequencia_acima_L=2.

def analiseTemperatura(temps, L):
    mediaa = media(temps)
    acimaMediaa = acimaMedia(temps, mediaa)
    maiorSequenciaa = maiorSequencia(temps, L)

    return f"Média = {mediaa:.2f}, acima da média = {acimaMediaa}, maior sequência = {maiorSequenciaa}."

def media(temps):
    return sum(temps)/ len(temps)

def acimaMedia(temps, mediaa):
    return sum(1 for i in temps if i > mediaa)

def maiorSequencia(temps, L):
    atualSequencia = 0
    maiorSequencia = 0
    for i in temps:
        if i > L:
            atualSequencia += 1
            if atualSequencia > maiorSequencia:
                maiorSequencia = atualSequencia
        else: 
            atualSequencia = 0
    return maiorSequencia