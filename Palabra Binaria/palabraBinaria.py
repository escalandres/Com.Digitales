## Autor: Andres Rafael Escala Acosta
## Conversion a palabra binaria en Compansion Analogica

import os
##Creamos la tabla de segmentos
#Dato0: segmento 0-7, #Dato1: binario, #Dato2 y Dato3: intervalo de voltaje(mV), #Dato 4: Tamano paso (mV)
# seg0=[0,"000",  0,      7.8124, 0.4882]
# seg1=[1,"001",  7.8125, 15.624, 0.4882]
# seg2=[2,"010",  15.625, 31.24,  0.9765]
# seg3=[3,"011",  31.25,  62.4,   1.9531]
# seg4=[4,"100",  62.5,   124,    3.9062]
# seg5=[5,"101",  125,    249,    7.8125]
# seg6=[6,"110",  250,    499,    15.625]
# seg7=[7,"111",  500,    1000,   31.25]

tablaSegmentos = [[0,"000",0,7.8124,0.4882],[1,"001",  7.8125, 15.624, 0.4882],
    [2,"010",  15.625, 31.24,  0.9765],[3,"011",  31.25,  62.4,   1.9531],
    [4,"100",  62.5,   124,    3.9062],[5,"101",  125,    249,    7.8125],
    [6,"110",  250,    499,    15.625],[7,"111",  500,    1000,   31.25]]

tablaPasos = [[0,"0000"],[1,"0001"],[2,"0010"],[3,"0011"],[4,"0100"],[5,"0101"],
    [6,"0110"],[7,"0111"],[8,"1000"],[9,"1001"],[10,"1010"],[11,"1011"],
    [12,"1100"],[13,"1101"],[14,"1110"],[15,"1111"],]

def palabraBin():
    voltajeMax = float(input('\nIngrese el voltaje maximo en volts!\n\nVoltaje max (V): '))
    variacion = input('\n\nSi la variacion es positiva, ingrese 1; si es negativa, ingrese 0\n\nVariacion: ')
    amplitudVoltaje = 0
    print('\nEl dato de la muestra (amplitud) es en numero decimal o en porcentaje?')
    datoMuestra = input('\nSi es numero decimal: ingrese 0; si es en porcentaje: ingrese 1\n\nDato muestra: ')
    if datoMuestra == '0':
        voltajeMuestra = float(input('\n\nIngrese el voltaje muestra en volts!\n\nVoltaje muestra (V): '))
        amplitudVoltaje = voltajeMax / voltajeMuestra
    elif datoMuestra == '1':
        amplitudVoltaje = float(input('\n\nIngrese la amplitud en volts (sin el %)!\n\nAmplitud(%): '))
    else:
        print("\nError, intentelo de nuevo!\n")
        palabraBin()
    voltajePico = 1000 #mV max de la tabla
    amplitudMuestra = voltajePico * amplitudVoltaje/100
    print('\nValor Intervalo: {0} mV\n'.format(amplitudMuestra))
    diferenciaIntervalo = 0
    segmento = 0
    segmentoBinario = ""
    for i in range(0,7):
        if(amplitudMuestra>=tablaSegmentos[i][2] and amplitudMuestra<=tablaSegmentos[i][3]):
            diferenciaIntervalo = amplitudMuestra - tablaSegmentos[i][2]
            segmento = i
            segmentoBinario = tablaSegmentos[i][1]

    nivel = int((diferenciaIntervalo)/tablaSegmentos[segmento][4])
    print("\nNivel paso: {0}\n".format(nivel))
    nivelBinario = tablaPasos[nivel][1]
    palabraBinaria = ""+variacion+segmentoBinario+nivelBinario
    print("\nLa palabra binaria es: "+palabraBinaria+"\n\n")

def main():
    print("\n\t---Script para calcular la palabra binaria---\n")
    print("\n\t\t\tAutor: Andres Rafael Escala Acosta")
    palabraBin()

if __name__ == "__main__":
    os.system("cls")
    main()
