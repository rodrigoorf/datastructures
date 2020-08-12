# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 12:12:01 2017

@author: Rodrigo
"""
#com risadinha
from datetime import datetime
import random

lista = random.sample(range(1, 1000000), 100000)
l = [2, 3, 5, 7, 9, 35, 678, 86, 123, 54, 8765]

def getTempoExecBubble():
    inicio = datetime.now()
    bubbleSort(lista)
    fim = datetime.now()
    print('Duração: {}'.format(fim - inicio))
    
def getTempoExecQuick():
    inicio = datetime.now()
    quickSort(lista, 0, len(lista) - 1)
    fim = datetime.now()
    print('Duration: {}'.format(fim - inicio))
    
def getTempoExecInsertion():
    inicio = datetime.now()
    insertionSort(lista)
    fim = datetime.now()
    print('Duration: {}'.format(fim - inicio))
    
def getTempoExecShell():
    inicio = datetime.now()
    shellSort(lista)
    fim = datetime.now()
    print('Duration: {}'.format(fim - inicio))

def bubbleSort(l):
    if len(l) <= 1:
        lst = l
    else:
        for j in range(0, len(l)):
            for i in range(0, len(l)-1):
                if l[i] > l[i+1]:
                    temp = l[i+1]
                    l[i+1] = l[i]
                    l[i] = temp
        lst = l
    return lst
    
#função pro quicksort
def partition(l,inicio,fim):
    i = (inicio - 1)
    x = l[fim]
 
    for j in range(inicio, fim):
        if l[j] <= x:
 
            i = i+1
            #inverte as posições
            l[i],l[j] = l[j],l[i]
 
    # mesma coisa aqui, depois do loop
    l[i+1],l[fim] = l[fim],l[i+1]
    return (i+1)
 
def quickSort(l,inicio,fim):
 
    tamanho = fim - inicio + 1
    pilha = [0] * (tamanho) #transforma tudo num array do tamanho da lista
     #graças a deus pq ninguém merece 
    topo = -1
 
    topo += 1
    pilha[topo] = l
    topo += 1
    pilha[topo] = fim
 
    while topo >= 0:
        fim = pilha[topo]
        topo -= 1
        inicio = pilha[topo]
        topo = topo - 1 
        # Pivô
        pivo = partition(l, inicio, fim) # faz a famosa inversão (na outra função)
        # esquerda #FORATEMER
        if pivo-1 > inicio:
            topo += 1
            pilha[topo] = l
            topo = topo + 1
            pilha[topo] = pivo - 1
 
        # direita #BORATEMER
        if pivo+1 < fim:
            topo += 1
            pilha[topo] = pivo + 1
            topo += topo + 1
            pilha[topo] = fim
    return l #FUNCIONOU PORRA
        
def insertionSort(l):
    for i in range(1, len(l)):
        key = l[i]
        k = i
        while k > 0 and key < l[k-1]:
            l[k] = l[k-1]
            k -= 1
        l[k] = key
    return l
    
def shellSort(l):
    h = 1
    n = len(l)
    while h > 0:
        for i in range(h, n):
            c = l[i]
            j = i
            while j >= h and c < l[j - h]:
                l[j] = l[j - h]
                j = j - h
                l[j] = c
        h = int(h / 2.2)
    return l
    
    #sem risadinha