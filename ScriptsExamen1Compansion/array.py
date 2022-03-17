import numpy as np
from tabulate import tabulate

y = []
for i in range(0,8):
    y.append(i)
print('array')
for i in range(0,8):
    print('Y: {0}'.format(y[i]))
h = np.sign(-4.5)
i = np.sign(0)
j = np.sign(5.5)

print("\nH: {0}, I: {1}, J:{2}".format(h,i,j))
ym = [0,0.41070,0.62067,0.74344,0.83055,0.89811,0.95332,1]
#A = []
vA = np.size(ym)
column, row = vA, 2
A = [[0]*row for _ in range(column)]
print(A)

for i in range(0,vA):
    for j in range(0,2):
        if j == 0:
            #A.insert([i,j],"Ym0")
            A[i][j] = "Ym"+str(i)
        else:
            #A.insert([i,j],ym[i])
            A[i][j] = ym[i]
print(tabulate(A, headers=["Nivel en compansion", "Valor del nivel"]))

print("\n\n")
niveles = 8
jm = []
for i in range(0, niveles):
    jm[i]=0
# column, row = 1 , 8 ##dimensiones del array
# ym = [[0]*row for _ in range(column)] ##Se inicializa el array con ceros
print(ym)