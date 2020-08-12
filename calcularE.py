# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:36:17 2017

@author: marcos.o
"""

def fatorial(n):
    'fatorial de n'
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def calcularE(n):
    'calcular o numero e'
    if n == 0:
        return 1 / fatorial(0)
    else:
        return 1 / fatorial(n) + calcularE(n - 1)


def somaA(n):
    if n == 1:
        return 1
    else:
        return 1 / n + somaA(n - 1)
    

def somaB(n):
    if n == 1:
        return 1
    else:
        return (1 / 2**n) + somaB(n - 1) 
    
def length(lst):
    if lst == []:
        return 0
    else:
        return 1 + length(rest(lst))

def rest(lst):
        return lst[1:]
    
def first(lst):
    return lst[0]

    
def search(lst, n):
    if lst[1:] != n:
        return 1 + search(rest(lst), n)
    else:
        return True
    
def update(lst, pos, valor):
    if length(lst) >= pos:
        lst[pos] = valor
        return lst
    else:
        return 'non ecziste'
        
def update2(lst, pos, valor):
        if (length(lst) < pos):
            return "no tiene"
        if pos == 0:
            lst[0] = valor
            return lst
        else:
            return [first(lst)] + update(rest(lst), pos-1, valor)
