# 5. Matriz de Ocupação (Assentos de Sala)
# Enunciado: Dada uma matriz R x C (0=livre, 1=ocupado), implemente: 
# reservar assento, liberar assento e verificar blocos contíguos de k 
# lugares livres na mesma fila. Imprima um mapa final.
# Entrada (exemplo): R=3,C=5, matriz inicial com alguns 1s; operações: 
# reservar(1,2), liberar(0,4), existe_bloco(k=3)
# Saída (exemplo): mapa final e existe_bloco=True.

import random

def assentosSala():
    numCadeiras = cadeiras()
    R = numCadeiras[0]
    C = numCadeiras[1]
    matriz = []
    
    for i in range(numCadeiras[0]):
        matriz.append([random.randint(0,1) for j in range(C)])

    print([f"{linha}\n" for linha in matriz])

    while True:
        reserva = reservarLugar(R, C)
        if reserva == None:
            break
        elif matriz[reserva[0]][reserva[1]] == 0:
            matriz[reserva[0]].pop(reserva[1])
            matriz[reserva[0]].insert(reserva[1], 1)
            break
        else:
            print("Cadeira já está ocupada!")

    while True:
        liberar = liberarLugar(R, C)
        if liberar == None:
            break
        elif matriz[reserva[0]][reserva[1]] == 1:
            matriz[reserva[0]].pop(reserva[1])
            matriz[reserva[0]].insert(reserva[1], 0)
            break
        else:
            print("Cadeira não está ocupada!")
    

    verificar = verificarLugar(R, C, matriz)
        

    linhasMatriz = [", ".join(map(str, linha)) for linha in matriz]

    return f"{'\n'.join(linhasMatriz)}\nBlocos livres: {verificar}"

def cadeiras():
    listaAux = []
    while True:
        try: 
            if not listaAux:
                R = int(input("Digite um número para R (Linha): "))
                listaAux.append(R)
            C = int(input("Digite um número para C (Coluna): "))
            listaAux.clear()
            break
        except ValueError:
            print("Digite um valor válido!")

    return R, C 

def reservarLugar(R, C):
    listaAux = []

    while True:
            try:
                if not listaAux:
                    decisaoReservar = input("Deseja reservar (S/N)? ")
                    if decisaoReservar.upper() == "N":
                        return None
                    elif decisaoReservar.upper() == "S":
                        listaAux.append(decisaoReservar)
                    else:
                        print("Digite 'S' ou 'N'!")
            
                if len(listaAux) == 1 :
                    reservarNum1 = int(input("Digite o número da linha: "))
                    if reservarNum1 >= 0 and reservarNum1 < R:
                        listaAux.append(reservarNum1)
                    else:
                        print("Essa linha não existe!")
                if len(listaAux) == 2 :
                    reservarNum2 = int(input("Digite o número da coluna: "))
                    if reservarNum2 >= 0 and reservarNum2 < C:
                        break
                    else:
                        print("Essa coluna não existe!")
            except ValueError:
                print("Digite um valor válido!")
    return [reservarNum1, reservarNum2]

def liberarLugar(R, C):
    listaAux = []

    while True:
            try:
                if not listaAux:
                    decisaoLiberar = input("Deseja liberar (S/N)? ")
                    if decisaoLiberar.upper() == "N":
                        return None
                    elif decisaoLiberar.upper() == "S":
                        listaAux.append(decisaoLiberar)
                    else:
                        print("Digite 'S' ou 'N'!")
            
                if len(listaAux) == 1 :
                    liberarNum1 = int(input("Digite o número da linha: "))
                    if liberarNum1 >= 0 and liberarNum1 < R:
                        listaAux.append(liberarNum1)
                    else:
                        print("Essa linha não existe!")
                if len(listaAux) == 2 :
                    liberarNum2 = int(input("Digite o número da coluna: "))
                    if liberarNum2 >= 0 and liberarNum2 < C:
                        break
                    else:
                        print("Essa coluna não existe!")
            except ValueError:
                print("Digite um valor válido!")
    return [liberarNum1, liberarNum2]

def verificarLugar(R, C, matriz):
    while True:
        try:
            lugaresVagos = int(input("Digite um número para verificar blocos contíguos de lugares livres na mesma fila: "))
            if lugaresVagos > C:
                print("Número maior do que a quantidade de cadeiras.")
            elif lugaresVagos < C and lugaresVagos >= 0: 
                break
        except ValueError:
            print("Digite um valor válido!")

    for i in range(R):
        for j in range(C - lugaresVagos + 1):
            bloco = matriz[i][j : j + lugaresVagos]
            if all(cadeira == 0 for cadeira in bloco):
                return True
    return False

print(assentosSala())
