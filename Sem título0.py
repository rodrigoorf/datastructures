# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 21:48:03 2017

@author: rodrigo.freire
"""

class BinTree:
    def __init__(self, info):
        self.filhos = []
        self.llink = None
        self.rlink = None
        self.info = info
        
    def insert_left(self, no, pai):
        self.llink = no
        
    def insert_right(self, no):
        self.rlink = no
        
    def remove_left(self, pai):
        self.llink = None
        
    def remove_right(self, pai):
        self.rlink = None
        
    def getInfo(self):
        return self.info
    
    def getLeft(self):
        return self.llink
    
    def getRight(self):
        return self.rlink
        
    def update(self, info):
        self.info = info
        
    def visitRoot(self, metodo, param):
        metodo(param)
        #print(self.info)
        
    def preorder(self, metodo):
        self.visitRoot(metodo, self)
        if (self.llink != None):
            self.llink.preorder()
            
        if (self.rlink != None):
            self.rlink.preorder()
        
    def postorder(self, metodo):
        if (self.llink != None):
            self.llink.preorder()
        self.visitRoot(metodo, self)
        if (self.rlink != None):
            self.rlink.preorder()
        
    def endorder(self, metodo):
        if (self.llink != None):
            self.llink.preorder()
        if (self.rlink != None):
            self.rlink.preorder()
        self.visitRoot(metodo, self)
            
def imprime(root):
    print(root)