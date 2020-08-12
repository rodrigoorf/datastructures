# -*- coding: utf-8 -*-
"""
Spyder Editor
 
Este é um arquivo de script temporário.
"""
 
class Arvore(object):
     
    def __init__(self, nome):
        self.nome = nome
        self.filhos = []
         
    def setNome(self, nome):
        self.nome = nome
         
    def showNome(self):
        print(self.nome)
         
    def addFilho(self, filho):
        self.filhos.append(filho)
         
    def showFilhos(self):
        for i in self.filhos:
            print(self.filhos[i].showNome())
            i = i + 1
      
    def rest(self):
        return self.prox
         
    def searchFilho(self, nome):
        for i in self.filhos:
            if (nome == self.filhos[i.showNome]):
                return i
            else:
                return "Não encontrado"
             
init = Arvore("PUCPR")
var1 = Arvore("Pró-Reitoria de Graduação")
var2 = Arvore("Pró-Reitoria Comuntária e de Extensão")
var3 = Arvore("Pró-Reitoria de Pesquisa e Pós Graduação")
var4 = Arvore("Pró-Reitoria Administrativa e de Desenvolvimento")
init.addFilho(var1)
init.addFilho(var2)
init.addFilho(var3)
init.addFilho(var4)