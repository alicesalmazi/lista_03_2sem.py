# 10. Fila de Atendimento (Simulação)
# Enunciado: Implemente uma fila com operações textuais: CHEGA nome, ATENDE, 
# PRIORITARIO nome (entra na frente). Ao final, imprima a ordem de atendimentos 
# e quem ficou sem ser atendido.
# Entrada (exemplo): CHEGA Ana, CHEGA Bia, PRIORITARIO João, ATENDE, ATENDE
# Saída (exemplo): atendidos: João, Ana; na fila: Bia.

def atendimento(string):
    comandos = string.split(", ")
    comandosFinais = [comando.split() for comando in comandos]
    contadorComandos = 0
    contadorPrioritario = 0
    fila = []
    atendidos = []

    for parte in comandosFinais:
        if parte[0] == "PRIORITARIO":
            fila.insert(contadorPrioritario, parte[1])
            contadorPrioritario += 1
        elif parte[0] == "CHEGA":
            fila.append(parte[1])
        elif parte[0] == "ATENDE":
            if fila:
                atendidos.append(fila.pop(0))
    
    return f"Atendidos: {", ".join(atendidos)}; na fila: {", ".join(fila)}."