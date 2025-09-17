# 4. Jogo da Forca (versão sem interface)
# Enunciado: Receba uma palavra secreta e uma lista de tentativas de letras. 
# Mostre a evolução do tabuleiro a cada tentativa e o resultado final 
# (ganhou/perdeu) com o número de erros.
# Entrada (exemplo): palavra "PYTHON"; tentativas: P, A, O, X, T, H, N
# Saída (exemplo):
# _ _ _ _ _ _ → P _ _ _ _ _ → P _ _ _ O _ → ...
# resultado: ganhou, erros=2.

def jogoForca(pSecreta, tentativas):
    contadorErros = 0
    MAXERROS = 6
    atualForca = ["_"] * len(pSecreta)
    saidaForca = []
    listaErros = []

    for tentativa in tentativas:
        if contadorErros >= 6:
            return f"{" → ".join(saidaForca)}.\nResultado: {"Perdeu"}."
        elif tentativa in pSecreta:
            for i, caractere in enumerate(pSecreta):
                if tentativa == caractere:
                    atualForca[i] = caractere
            saidaForca.append("".join(atualForca))
        else:
            listaErros.append(tentativa)
            contadorErros += 1

    if "_" in atualForca:
        return f"{" → ".join(saidaForca)}.\nResultado: Perdeu." if contadorErros == 0 else f"{" → ".join(saidaForca)}.\nResultado: Perdeu, Erros: {len(saidaForca)} ({", ".join(listaErros)})."
    else:
        return f'{" → ".join(saidaForca)}.\nResultado: Ganhou' if contadorErros == 0 else f'{" → ".join(saidaForca)}.\nResultado: Ganhou, Erros: {len(saidaForca)} ({", ".join(listaErros)}).'