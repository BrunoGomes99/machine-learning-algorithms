# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 09:40:07 2017

@author: Bruno
"""
from pybrain3.tools.shortcuts import buildNetwork
from pybrain3.datasets import SupervisedDataSet
from pybrain3.supervised.trainers import BackpropTrainer
from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import math

ds = SupervisedDataSet(1, 1)

valoresX = []
valoresY = []
rede = []

x = -4
while(x <= 4):
    ds.addSample(x, math.cos(2*x))
    x += 0.05


neuralNet = buildNetwork(1, 100, 1, bias=True)

trainer = BackpropTrainer(neuralNet, ds)

for i in range(2000):
    print("Erro: ", trainer.train())


x = -1*math.pi
while (x < 1*math.pi):
    valoresY.append(math.cos(2*x))
    rede.append(neuralNet.activate([x]))
    valoresX.append(x)
    x += 0.1

plt.plot(valoresX, valoresY)
plt.plot(valoresX, rede, 'r.')
plt.title('Função Cos(2x) x Rede Neural')
plt.legend(('cos(2x)','Rede Neural'))
plt.xlabel('Rede Neural')
plt.ylabel('Valore Reais')
grid(True)
plt.show()