# -*- coding: utf-8 -*-

#---------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Orlando
#
# Created:     29/07/2014
# Copyright:   (c) Orlando 2017
# Licence:     <your licence>
#---------------------------------------------------------------
#!/usr/bin/env python

#_______________________________________________________________

# para executar este arquivo

# IPython (console + editor)
# run 'C:/Orlando/python/exemplos_e_exercicios/estruturas1.py'

# Spyder
#   F5

# PyScripter
# ao salvar este arquivo, definir:      Edit/File Format/UTF-8
#   Ctrl F9


#_______________________________________________________________


peso = 30

altura = 2 * 3.

hellow_word = 'Hello World !'

latinas = 'computação'
gregas = "αβδλε"

new_string = latinas + gregas # concatenação de strings


def soma(v1, v2):
    return v1 + v2
#
# soma(2, 3)
# soma("2", "3")


# if
#
def maior_1(a, b):
    if a > b:
        return True
    else:
        return False
#
# maior_1(2, 3)


# igualdade de dois valores
#
def m_equal(a, b):
    return a == b
#
# m_equal(2, 3)


def m_abs(x):
    'valor absoluto de um número real'
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0
#
# m_abs(3)


#
# tipos: int, bool, float, str, bytes, list


# valores são tipados
# a função type retorna o tipo de um valor:
#
# type(2)               retorna         <class 'int'>
# type('2')             retorna         <class 'str'>
# type("2222")          retorna         <class 'str'>
# type(2.)              retorna         <class 'float'>


# como verificar o tipo de um valor:
# type(valor)

# como converter um inteiro em um binário
# bin(3)

# como converter um float em inteiro
# int(3.4)

def m_test_type(valor, tipo):
    'verifica o tipo de um valor'
    if type(valor) == tipo:
        print("o tipo é: ", tipo)
    else:
        print("tipo inválido")
#
# m_test_type(3.0,float)
# m_test_type([1,2,3],list)
# m_test_type([1,2,3],int)


# como validar parâmetros

def maior(a, b):
    'selecionar o maior de dois números inteiros'
    if not (type(a) == int):
        print("excessão 1:", a,  "possui tipo inválido")
        return
    if not type(b) == int:
        print("excessão 2:", b,  "possui tipo inválido")
        return
    return a > b

def print_maior(a, b):
    print("o maior número é ", maior(a, b))


# exemplos de funções recursivas


def fatorial(n):
    'fatorial de um número inteiro'
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
#
# fatorial(6)


def fibn(n):
    'retorna o fibonacci de um número inteiro'
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibn(n - 1) + fibn(n - 2)
#
# fibn(5)

# para executar uma cell: Ctrl Return
#%%

print('hello')

#%%

#_______________________________________________________________


# exercicios


# Escreva em Python uma função para cada algoritmo a seguir:
#
# 1) elevar um número ao quadrado
#
# 2) somar três números e concatenar três strings
#
# 3) multiplicar dois números inteiros, validando o tipo dos
#    parâmetros
#
# 4) selecionar o maior de dois números inteiros dados
#
# 5) selecionar o maior de três números


# Escreva em Python uma função "recursiva" para cada
# algoritmo a seguir
#
# 6) calcular o produto dos naturais de 1 até um número dado
#
# 7) dado n, calcular a soma dos inteiros de 1 a n
#
# 8) dado n, calcular a soma de
#    1/2 + 1/4 + 1/8 + ... + 1/2^n + ...
#
# 9) dado n, calcular o número e (a base dos logaritmos
#    neperianos; e = 2,718 281 828 ) até a n-ésima parcela:
#    e = 1/0! + 1/1! + 1/2! + 1/3! + ... + 1/n! + ...

def fat(n):
    if n == 0:
        return 1
    else:
        return n * fat(n - 1)
        
def nep(n):
    if n == 0:
        return 1 / fat(0)
    else:
        return 1 / fat(n) + nep(n - 1)
    
#
# *10) sen x = x - (x^3 / 3!) + (x^5 / 5!) - (x^7 / 7!) + ...
#
# *11) cos x = 1 - (x^2 / 2!) + (x^4 / 4!) - (x^6 / 6!) + ...
#
# 12) 1 + (1/2) + (1/3) + (1/4)...

def half(n):
    if n == 1:
        return 1
    else:
        return 1 / n + half(n - 1)
        
# 13) 1 + (1/4) + (1/8) + (1/16)...

def four(n):
    if n == 1:
        return 1
    else:
        return (1 / (2 ** n)) + four(n-1) 
        
    
