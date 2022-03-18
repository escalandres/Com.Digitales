## Autor: Andres Rafael Escala Acosta
## Script para calcular el Signal-to-Quantization Noise Ratio SQNR
import math as math
import numpy as np
import os

def sqnr():
    mp = float(input('\nIngrese valor de mp!\n\nmp: '))
    L = float(input('\nIngrese valor de L!\n\nL: '))
    valores = int(input('\nIngrese la cantidad de valores\n\nValores: '))
    vector = []
    m2 = 0
    for i in range(0,valores):
        dato = float(input('\nDato {0}\n: ').format(i+1))
        vector.append(dato)
    for i in range(0,valores):
        m2 = m2 + math.pow(vector[i],2)
    So = m2/valores 
    No = (math.pow(mp,2))/(3*math.pow(L,2))
    if So > No:
        print("\nSo es mayor que No, se respeta\nSo = {0}\nNo = {1}\n".format(So,No))
    else:
        print("\nSo es menor que No, no se respeta\nSo = {0}\nNo = {1}\n".format(So,No))

def main():
    print("\n\t---Script para calcular el ruido---\n")
    print("\n\t\t\tAutor: Andres Rafael Escala Acosta\n")
    sqnr()

if __name__ == "__main__":
    os.system("cls")
    main()