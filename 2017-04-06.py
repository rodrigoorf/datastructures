# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:40:44 2017

@author: felipe.pires
"""

class Lista:
        
    def __init__(self, elem):
        self.elem = elem
        self.prox = None
    
    def setElem(self, elem):
        self.elem = elem
    
    def setProx(self, prox):
        self.prox = prox
        
    def rest(self):
        return self.prox
    
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
            nz = Lista(elem)
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
        
n1=Lista(2)
n2=Lista(3)
n3=Lista(8)
n4=Lista(10)

n1.setProx(n2)
n2.setProx(n3)
n3.setProx(n4)

class Pilha(Lista):
    def __init__(self, elem):
        Lista.__init__(self, elem)
        self.prox = None
    
    def top(self):
        if(self.prox == None):
            return self
        else:
            return self.rest().top()
        
    def push(self, elem):
        if(self.top() == None):
            return False
        else:
            self.insert_n(elem, self.length())
            return True
        
    def pop(self):
        if(self.top() == None):
            return False
        else:
            self.remove(self.top().elem)
            return True
        
class Fila(Lista):
    
    def __init__(self, elem):
        Lista.__init__(self, elem)
        self.prox = None
        
    def add(self, elem):
        if(self == None):
            return False
        else:
            self.insert_n(elem, self.length())
            return True
        
    
        
L = n1        
    
p1 = Pilha(2)
p2 = Pilha(3)
p3 = Pilha(8)
p4 = Pilha(10)

def showList(no):
    if(no.prox == None):
        return [no.elem]
    else:
        return [no.elem] + showList(no.prox)
    
def first(no):
    return no.elem

def rest(no):
    return no.prox

def length(no):
    if(no.prox == None):
        return 1
    else:
        return 1 + length(rest(no))
    
def search(no, elem):
    if(no.elem == elem):
        return True
    if(no.prox == None):
        return False
    else:
        return search(rest(no), elem)
    
def remove_n(no, elem):
    if(no.prox == None):
        return False
    if(no.prox.elem == elem):
        no.prox = no.prox.prox
        return True
    else:
        return remove_n(rest(no), elem)
    
def insert(no, elem, pos):
    if(pos == 1):
        nz = Lista(elem)
        nz.setProx(no.prox)
        no.setProx(nz)
        return True
    if (no.prox == None):
        return False
    else:
        return insert(rest(no), elem, pos-1)       