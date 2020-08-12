# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

def func(n):
    if n == 1:
        return 1
    else:
        return 1/n + func(n-1)

def func2(n):
    if n == 1:
        return 1
    else:
        return 1/n**2 + func2(n-1)
    
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1) 