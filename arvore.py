# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

class Organograma:
    
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
        print(self.filhos)
     
    def rest(self):
        return self.prox
        
    def searchFilho(self, nome):
        for i in self.filhos:
            if (nome == self.filhos[i.showNome]):
                return i
            else:
                return "Não encontrado"
     
    def length(self):
        if(self.prox == None):
            return 1
        else:
            return 1 + self.rest().length()
         
    def show_list(self):
        if (self.prox == None):
            return [self.elem]
        else:
            return [self.elem] + self.rest().show_list()
             
    def insert_n(self, elem, pos):
        if(pos == 1):
            nz = Organograma(elem)
            nz.setProx(self.prox)
            self.setProx(nz)
            return True
            if (self.prox == None):
                return False
            else:
                return self.rest().insert_n(elem, pos-1)
     
    def remove(self, elem):
        if(self.prox == None):
            return False
        if(self.prox.elem == elem):
            self.setProx(self.prox.prox)
            return True
        else:
            return self.rest().remove(elem)
             
    def update(self, elem, pos):
        if(pos == 0):
            self.setElem(elem)
            return True
        if(self.prox == None):
            return False
        else:
            return self.rest().update(elem, pos-1)
             
    def search_n(self, elem):
        if(self.elem == elem):
            return True
        if(self.prox == None):
            return False
        else:
            return self.rest().search(elem)
            
init = Organograma("PUCPR")
init.addFilho("Pró-Reitoria de Graduação")
init.addFilho("Pró-Reitoria Comuntária e de Extensão")
init.addFilho("Pró-Reitoria de Pesquisa e Pós Graduação")
init.addFilho("Pró-Reitoria Administrativa e de Desenvolvimento")  