# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:56:07 2017

@author: bruno
"""
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np
import csv
import os

arq = csv.reader(open('C:/Users/bruno/Downloads/vinho.txt'), delimiter = ';') 
 
M = np.ones((1599,12),dtype = float)

for line in arq:
    if (line[0] == 'fixed acidity'):
        i = 0
        continue

    M[i][0] = float(line[0])
    M[i][1] = float(line[1])
    M[i][2] = float(line[2])
    M[i][3] = float(line[3])
    M[i][4] = float(line[4])
    M[i][5] = float(line[5])
    M[i][6] = float(line[6])
    M[i][7] = float(line[7])
    M[i][8] = float(line[8])
    M[i][9] = float(line[9])
    M[i][10] = float(line[10])
    M[i][11] = float(line[11])
    i = i+1     

x_treino = np.ones((1119, 6), dtype = float)
y_treino = np.ones((1119, 6), dtype = float)
x_teste = np.ones((480, 6), dtype = float)
y_teste = np.ones((480, 6), dtype = float)

lin = 0
for i in range(0, 1119): #Vai da pos 0 a 1118
    x_treino[lin][0] = M[i][0]
    x_treino[lin][1] = M[i][1]
    x_treino[lin][2] = M[i][2]
    x_treino[lin][3] = M[i][3]
    x_treino[lin][4] = M[i][4]
    x_treino[lin][5] = M[i][5]
    lin = lin + 1
    
lin = 0
for j in range(0, 1119):
    y_treino[lin][0] = M[j][6]
    y_treino[lin][1] = M[j][7]
    y_treino[lin][2] = M[j][8]
    y_treino[lin][3] = M[j][9]
    y_treino[lin][4] = M[j][10]
    y_treino[lin][5] = M[j][11]
    lin = lin + 1
    
lin = 0
for x in range(1119, 1599): #Vai da pos 1119 a 1598
    x_teste[lin][0] = M[x][0]
    x_teste[lin][1] = M[x][1]
    x_teste[lin][2] = M[x][2]
    x_teste[lin][3] = M[x][3]
    x_teste[lin][4] = M[x][4]
    x_teste[lin][5] = M[x][5]
    lin = lin + 1
    
lin = 0
for y in range(1119, 1599):
    y_teste[lin][0] = M[y][6]
    y_teste[lin][1] = M[y][7]
    y_teste[lin][2] = M[y][8]
    y_teste[lin][3] = M[y][9]
    y_teste[lin][4] = M[y][10]
    y_teste[lin][5] = M[y][11]
    lin = lin + 1
    
model = LinearRegression()
model.fit(x_treino, y_treino)
predictions = model.predict(x_teste)
for i, prediction in enumerate(predictions):
    print('predicted: %s \nTarget: %s' % (prediction, y_teste[i]))
    print('R-squared: %.2f' % model.score(x_teste, y_teste))

acidez_fixa = []
acidez_volatil = []
acidez_citrica = []
acucar_residual = []
cloretos = []
dioxido_livre = []
dioxido_total = []
densidade = []
sulfatos = []

ph = []
teor_alcoolico = []
qualidade = []

for i in range(1599):
    teor_alcoolico.append(M[i][10])
    qualidade.append(M[i][11])
    ph.append(M[i][8])
    acidez_fixa.append(M[i][0])
    acidez_volatil.append(M[i][1])
    acidez_citrica.append(M[i][2])
    acucar_residual.append(M[i][3])
    cloretos.append(M[i][4])
    dioxido_livre.append(M[i][5])
    dioxido_total.append(M[i][6])
    densidade.append(M[i][7])
    sulfatos.append(M[i][9])
    
#Gráficos

plt.figure()
plt.title("Qualidade por taxa de sulfatos")
plt.xlabel("Sulfatos")
plt.ylabel("Qualidade")
plt.plot(sulfatos,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por densidade")
plt.xlabel("Densidade")
plt.ylabel("Qualidade")
plt.plot(densidade,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa total de dióxido de enxofre")
plt.xlabel("Dióxido de enxofre total")
plt.ylabel("Qualidade")
plt.plot(dioxido_total,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa de dióxido de enxofre livre")
plt.xlabel("Dióxido de enxofre livre")
plt.ylabel("Qualidade")
plt.plot(dioxido_livre,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa de cloretos")
plt.xlabel("Cloretos")
plt.ylabel("Qualidade")
plt.plot(cloretos,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa de açúcar residual")
plt.xlabel("Açúcar Residual")
plt.ylabel("Qualidade")
plt.plot(acucar_residual,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa de acidez citrica")
plt.xlabel("Acidez Cítrica")
plt.ylabel("Qualidade")
plt.plot(acidez_citrica,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa de acidez volátil")
plt.xlabel("Acidez Volátil")
plt.ylabel("Qualidade")
plt.plot(acidez_volatil,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por taxa de acidez fixa")
plt.xlabel("Acidez Fixa")
plt.ylabel("Qualidade")
plt.plot(acidez_fixa,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por pH")
plt.xlabel("pH")
plt.ylabel("Qualidade")
plt.plot(ph,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

plt.figure()
plt.title("Qualidade por teor alcoólico")
plt.xlabel("Teor alcoólico")
plt.ylabel("Qualidade")
plt.plot(teor_alcoolico,qualidade,'r.')
plt.axis([0,20,0,10])
plt.grid(True)
plt.show()

os.system("pause")