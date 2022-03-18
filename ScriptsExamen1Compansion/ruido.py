## Autor: Andres Rafael Escala Acosta
## Script para calcular el ruido
import math as math
import numpy as np
import os

def ruido():
    mp = float(input('\nIngrese valor de mp!\n\nmp: '))
    L = float(input('\nIngrese valor de L!\n\nL: '))
    No = (math.pow(mp,2))/(3*math.pow(L,2))
    print("\nEl valor de la potencia del ruido es de {0}\n".format(No))

def main():
    print("\n\t---Script para calcular el ruido---\n")
    print("\n\t\t\tAutor: Andres Rafael Escala Acosta\n")
    ruido()

if __name__ == "__main__":
    os.system("cls")
    main()