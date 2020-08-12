# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 21:42:05 2017

@author: Rodrigo
"""
from operator import itemgetter
#Huffman: código -> Árvore binária

#ler arquivo txt OK
#percorrer o arquivo caracter por caracter OK
#contar a frequência de cada caracter OK
#ordenar do mais frequente para o menos frequente OK
#bolar um método de criar uma árvore bottom-up
#popular a árvore de baixo para cima, começando pelos menores valores

class Huffman(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
    def filhos(self):
        return((self.left, self.right))

def teste():
    arquivo = open("C:\\Users\\Rodrigo\\Desktop\\teste.txt")
    prox = arquivo.read()
    texto = {}
    for i in prox:
        texto[i] = 0
    for i in prox:
        texto[i] += 1
    asd = sorted(texto.items(), key=itemgetter(1), reverse=False)
    return asd
    
