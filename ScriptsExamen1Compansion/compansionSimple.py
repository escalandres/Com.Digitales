## Autor: Andres Rafael Escala Acosta
import math as math
import numpy as np
import os

## Este codigo es para calcular el valor de Y en la compansion
# cuando solamente se quiere un valor concreto

def imprimirValorNivel(valorNivel):
    print("\nValor del nivel es y = {0}\n".format(valorNivel))

def leyMiu(m0,mp):
    valorNivel = 0
    miu = float(input('\nIngrese el valor de Miu!\n\nMiu: '))
    mmp = math.fabs(m0/mp) ##valor absoluto de m/mp
    if mmp <= 1:
        sgn = np.sign(m0) ## funcion sgn(m)
        leyMiu = (sgn/(1+math.log(1+miu))*math.log(1+(miu*mmp)))
        valorNivel = leyMiu
        imprimirValorNivel(valorNivel)
    else:
        print("\nError, no se cumple la condicion!\n")
        main()

def leyA(m0,mp):
    valorNivel = 0
    vA = float(input('\nIngrese el valor de A!\n\nA: '))
    cond1 = 1/vA
    mmp = math.fabs(m0/mp) ##valor absoluto de m/mp
    sgn = np.sign(m0) ## funcion sgn(m)
    if mmp <= cond1:
        leyA1 = (vA/(1+math.log(vA)))*(m0/mp)
        valorNivel = leyA1
    elif cond1 <= mmp and mmp <= 1:
        leyA2 = (sgn/(1+math.log(vA))*(1+math.log(vA*mmp)))
        valorNivel = leyA2
    # else:
    #     print("error")
    #     main()
    imprimirValorNivel(valorNivel)

def cuantizacionNoLineal():
    m0 = float(input('\nIngrese el valor de m0!\n\nm0: '))
    mp = float(input('\nIngrese el valor de mp en decimal (maximo 6 decimales). Ej: 0.333333. Si es entero, solo ponga el entero\n\nMp: '))
    print('\nPara usar la ley Miu escriba: Miu\nPara usar la ley A escriba: A\n')
    ley = input("\nOpcion: ")
    if ley == "Miu":
        leyMiu(m0,mp)
    elif ley == "A":
        leyA(m0,mp)
    else:
        print("\nError!!!!!")
        main()

def main():
    print("\n\t---Script para Cuantizacion Lineal y Compansion---\n")
    print("\n\t\t\tAutor: Andres Rafael Escala Acosta")
    cuantizacionNoLineal()

if __name__ == "__main__":
    os.system("cls")
    main()