## Autor: Andres Rafael Escala Acosta
import math as math
import numpy as np
from tabulate import tabulate
import os

## Este codigo es para calcular el valor de Y en la compansion
#de una senal con varios niveles

def imprimirValorNivel(valorNivel):
    nivelCompansion = np.size(valorNivel)
    column, row = nivelCompansion, 2 ##dimensiones del array
    A = [[0]*row for _ in range(column)] ##Se inicializa el array con ceros
    # print(A)
    for i in range(0,nivelCompansion):
        for j in range(0,2):
            if j == 0:
                A[i][j] = "Ym"+str(i)
            else:
                A[i][j] = valorNivel[i]
    ## Se imprimira la tabla con los valores de compansion
    print(tabulate(A, headers=["Nivel en compansion", "Valor del nivel"]))

def leyMiu(ym,niveles):
    valorNivel = []
    miu = float(input('\nIngrese el valor de Miu!\n\nMiu: '))
    for i in range(0,niveles):
        mmp = math.fabs(ym[i]) ##valor absoluto de m/mp
        sgn = np.sign(ym[i]) ## funcion sgn(m)
        leyMiu = (sgn/(1+math.log(1+miu))*math.log(1+(miu*mmp)))
        valorNivel.append(leyMiu)
    imprimirValorNivel(valorNivel)

def leyA(ym,niveles):
    valorNivel = []
    vA = float(input('\nIngrese el valor de A!\n\nA: '))
    cond1 = 1/vA
    for i in range(0,niveles):
        mmp = math.fabs(ym[i]) ##valor absoluto de m/mp
        sgn = np.sign(ym[i]) ## funcion sgn(m)
        if mmp <= cond1:
            leyA1 = (vA*(1+math.log(vA)))*(mmp)
            valorNivel.append(leyA1)
        elif cond1 <= mmp and mmp <= 1:
            leyA2 = (sgn/(1+math.log(vA))*(1+math.log(vA*mmp)))
            valorNivel.append(leyA2)
    # else:
    #     print("error")
    #     main()
    imprimirValorNivel(valorNivel)

def indices(valorNC,mp):
    niveles = int(input('\nIngrese la cantidad de niveles!\n\nNiveles: '))
    ym = []
    for i in range(0,niveles):
        ym.append((i*valorNC)/mp)
    print('\nPara usar la ley Miu escriba: Miu\nPara usar la ley A escriba: A\n')
    ley = input("\nOpcion: ")
    
    if ley == "Miu":
        leyMiu(ym,niveles)
    elif ley == "A":
        leyA(ym,niveles)
    else:
        print("\nError!!!!!")
        main()


def cuantizacionLineal():
    vL = int(input('\nIngrese el valor de L!\n\nL: '))
    mp = float(input('\nIngrese el valor de mp en decimal (maximo 6 decimales). Ej: 0.333333\n\nMp: '))
    print('\nSi se toman parte positiva o parte negativa ingrese: 1, si se toman valores positivos y negativos ingrese: 2')
    ejeY = input('\nOpcion: ')
    if ejeY == '1':
        #Una sola amplitud
        valorNC = mp/vL 
    elif ejeY == '2':
        #Ambas amplitudes
        valorNC = 2*(mp/vL)
    else:
        print('\nOpcion Incorrecta!')
        cuantizacionLineal()
    indices(valorNC,mp)

def main():
    print("\n\t---Script para Cuantizacion Lineal y Compansion---\n")
    print("\n\t\t\tAutor: Andres Rafael Escala Acosta\n")
    cuantizacionLineal()

if __name__ == "__main__":
    os.system("cls")
    main()