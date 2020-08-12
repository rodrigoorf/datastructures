# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:45:42 2017

@author: Rodrigo
"""

class List:
    def __init__(self, info, next=None):
        self.info = info
        self.next = next
        
    def set_info(self, info):
        self.info = info
        
    def setNext(self, next):
        self.next = next
            
n1 = List(2)
n2 = List(3)
n3 = List(8)
n4 = List(10)

n1.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)

def show_list(nr):
        if(nr.next == None):
            return [nr.info]
        else:
            return [nr.info] + show_list(nr.next)
            
def first(nr):
    return nr.info
    
def rest(nr):
    return nr.next
    
def length(nr):
    if(nr.next == None):
        return 1
    else:
        return 1 + length(rest(nr))
        
def search(nr, el):
    if(nr.info == el):
        return el
    elif(nr.info == None):
        return -1
    else:
        return search(rest(nr), el) + 1

