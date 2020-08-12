# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 21:42:14 2017

@author: alan.mazeto
"""

class Tree(object):
    def __init__(self, valor):
        self.info = valor
        self.filhos = []
    
    def setFilhos(self, no):
        self.filhos.append(no)
    
    def showFilhos(self):
        for filho in self.filhos:
            filho.showNome()
            
    def showNome(self):
        print(self.info)        
            
num3 = Tree("3")

num5 = Tree("5")
num8 = Tree("8")
num9 = Tree("9")

num4 = Tree("4")
num1 = Tree("1")
num2 = Tree("2")
num10 = Tree("10")

num11 = Tree("11")
num12 = Tree("12")
num13 = Tree("13")
num14 = Tree("14")

num3.setFilhos(num5)
num3.setFilhos(num8)
num3.setFilhos(num9)

num5.setFilhos(num4)
    