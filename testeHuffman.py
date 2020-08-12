# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:51:42 2017

@author: Rodrigo
"""
import heapq
from collections import defaultdict

def codificar(freq):
    heap = [[weight, [letra, '']] for letra, weight in freq.items()] # definição do dicionário através da qtde de letras encontradas
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap) # esquerda
        right = heapq.heappop(heap) # direita
        for pair in left[1:]: # formação do código
            pair[1] = '0' + pair[1] # adiciona 0 caso esquerda
        for pair in right[1:]:
            pair[1] = '1' + pair[1] # adiciona 1 caso direita
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:]) #função push (como se fosse uma pilha)
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p)) # função pop volta ordenada
    
def getTxt(huff, data):
    codigo = {}
    for p in huff:
        codigo[p[0]] = p[1] # colocando cada caracter e seu respectivo código no dicionário
    palavra = ""
    with open('C:\\Users\\Rodrigo\\Desktop\\apressado.txt') as f:
        while True: # formação da codificação
            c = f.read(1) # leitura de caractere por caractere
            if not c: #ao fim
                break #sair
            for key in codigo: # para cada letra encontrada no dicionário de códigos em binário
                if key == c: # adiciona a letra lida na formação da palavra final
                    palavra = palavra + codigo[key]
    print("Compressão: ", palavra)
    arq = open('C:\\Users\\Rodrigo\\Desktop\\resultado.txt', 'w')
    arq.write(palavra) # escrevendo a codificação resultante em um arquivo de texto
    arq.close()
    qtdeBitsOriginal = len(data)
    qtdeBitsNovo = len(palavra)
    ganho = 100 * qtdeBitsNovo / qtdeBitsOriginal * 8 # cálculo do ganho
    print("Ganho: ", ganho / 100,"%") # ganho em %
    
def iniciar():
    arquivo = open('C:\\Users\\Rodrigo\\Desktop\\apressado.txt') # leitura de um arquivo de texto
    data = arquivo.read()
    print ("Texto original: '", data, "'")
    frequenciaLetras = defaultdict(int)
    for letra in data:
        frequenciaLetras[letra] += 1
    huff = codificar(frequenciaLetras)
    getTxt(huff, data)
    arquivo.close()