# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 18:58:06 2017

@author: Bruno
"""

import numpy as np
import random
import csv
import os

def somaPeso(indi,largura):
    peso = 0
    for i in range(largura):
        if(indi[i] == 1):
            peso = peso + float(vetor[i][1])
    return peso

def diminuirPeso(indi,largura,peso_maximo):
    while(somaPeso(indi,largura) > peso_maximo):
        t = random.randint(0,largura-1)
        while(indi[t] == 0):
            t = random.randint(0,largura-1)
        indi[t] = 0
    return indi  
            
def individuo(largura, peso_maximo):
    indiv = [random.randint(0,1) for i in range(largura)]
    if(somaPeso(indiv,largura) > peso_maximo):
        indiv = diminuirPeso(indiv,largura,peso_maximo)
    return indiv
            
def Populacao(largura,peso_maximo):
    return[individuo(largura,peso_maximo) for i in range(num)]

def fitness(individuo):
    fit = 0
    for i in range(largura):
        if(individuo[i] == 1):
            fit+=float(vetor[i][0])
    return fit

def crossover(population, selecionados):
    for i in range(len(population)-pressao):
        corte = random.randint(0,largura-1)
        pais = random.sample(selecionados,2)
        
        population[i][:corte] = pais[0][:corte]
        population[i][corte:] = pais[1][corte:]
        
    return population

def selecao(population):
    indi = [(fitness(i),i) for i in population]
    indi = [i[1] for i in sorted(indi)]
    population = indi
    selecionados = indi[(len(indi)-pressao):]
    population = crossover(population,selecionados)
    return population

def mutacao(population):
    for i in range(len(population)-pressao):
         if(random.random() <= taxa_mutacao):
            corte = random.randint(0,largura-1)
            if(population[i][corte] == 1):
                population[i][corte] = 0
            else:
                population[i][corte] = 1
         diminuirPeso(population[i], largura, peso_maximo)
    return population

def resultado(population):
    population = [(fitness(i),i) for i in population]
    population = [i[1] for i in sorted(population, reverse = True )]
    print("\nPopulação final: ")
    print(population)
    print("\nNumero de itens: ")
    print(largura)
    print("\nCapacidade Maxima da mochila: ")
    print(peso_maximo)
    print("\nO melhor individuo foi:\n%s"%(population[0]))
    print("Fitness:\n%s"%(fitness(population[0])))
    print("\n")
    print ("O pior individuo foi: \n%s"%(population[9]))
    print ("Fitness \n%s"%(fitness(population[9])))
    print("\n")

print("============== Problema Da Mochila Binária ==============")
print("1 - Mochila 1")
print("2 - Mochila 2")
print("3 - Mochila 3")
print("4 - Mochila 4")
print("5 - Mochila 5")
print("6 - Mochila 6")
print("7 - Mochila 7")
print("8 - Mochila 8")
print("9 - Mochila 9")
print("10 - Mochila 10")
opcao = int(input('Escolha qual mochila analisar: \n'))

num = 10 # tamanho da populacao
pressao = 3 #num de inviduos usados para se reproduzir
taxa_mutacao = 0.2 #quantidade de mutacoes q vao ocorrer
geracoes = 100 #condicao de parada

if(opcao==1):
    print("============== Resolvendo a Mochila 1 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f1_l-d_kp_10_269.txt'), delimiter = ' ')

    vetor = np.ones((10,2),dtype = int)
    for line in arq:
        if(line[1] == '269'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==2):
    print("============== Resolvendo a Mochila 2 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f2_l-d_kp_20_878.txt'), delimiter = ' ')

    vetor = np.ones((20,2),dtype = int)
    for line in arq:
        if(line[1] == '878'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==3):
    print("============== Resolvendo a Mochila 3 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f3_l-d_kp_4_20.txt'), delimiter = ' ')

    vetor = np.ones((4,2),dtype = int)
    for line in arq:
        if(line[1] == '20'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==4):
    print("============== Resolvendo a Mochila 4 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f4_l-d_kp_4_11.txt'), delimiter = ' ')

    vetor = np.ones((4,2),dtype = int)
    for line in arq:
        if(line[1] == '11'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==5):
    print("============== Resolvendo a Mochila 5 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f5_l-d_kp_15_375.txt'), delimiter = ' ')

    vetor = np.ones((15,2),dtype = int)
    for line in arq:
        if(line[1] == '375'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==6):
    print("============== Resolvendo a Mochila 6 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f6_l-d_kp_10_60.txt'), delimiter = ' ')

    vetor = np.ones((10,2),dtype = int)
    for line in arq:
        if(line[1] == '60'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==7):
    print("============== Resolvendo a Mochila 7 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f7_l-d_kp_7_50.txt'), delimiter = ' ')

    vetor = np.ones((7,2),dtype = int)
    for line in arq:
        if(line[1] == '50'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==8):
    print("============== Resolvendo a Mochila 8 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f8_l-d_kp_23_10000.txt'), delimiter = ' ')

    vetor = np.ones((23,2),dtype = int)
    for line in arq:
        if(line[1] == '10000'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)
    
if(opcao==9):
    print("============== Resolvendo a Mochila 9 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f9_l-d_kp_5_80.txt'), delimiter = ' ')

    vetor = np.ones((5,2),dtype = int)
    for line in arq:
        if(line[1] == '80'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)

if(opcao==10):
    print("============== Resolvendo a Mochila 10 ==============")
    arq = csv.reader(open('C:/Users/Alex/Downloads/Binario/low-dimensional/f10_l-d_kp_20_879.txt'), delimiter = ' ')

    vetor = np.ones((20,2),dtype = int)
    for line in arq:
        if(line[1] == '879'):
            largura = int(line[0])
            peso_maximo = int(line[1])
            i = 0
            continue
        vetor[i][0] = float(line[0])
        vetor[i][1] = float(line[1])
        i = i+1
    population = Populacao(largura, peso_maximo)
    print("\nPopulação inicial: \n%s"%(population))

    for i in range(geracoes):
        population = selecao(population)
        population = mutacao(population)
    resultado(population)

os.system("pause")