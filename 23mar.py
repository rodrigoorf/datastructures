# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:04:34 2017

@author: orlando
"""

# Métodos de lista

# first/head
# rest/tail
# length
# insert_n
# insert_left
# insert_right
# remove_n
# remove_left
# remove_right
# update_n
# search
# show_info
# void
# show_list

l1 = [7, 5, 0, -2, 4]
l2 = ["manga", "abacate", "laranja"]
l3 = [["Maria", "maria@gmail.com", 987651318], ["Nicolau", "nicky@yahoo.com", 912347367], ["Bob", "bbg2@gmail.com", 998078734]]

def first(lst):
    return lst[0]

def rest(lst):
    return lst[1:]

def length(lst):
    if lst == []:
        return 0
    else:
        return 1 + length(rest(lst))
    
def search(lst, n):
    if lst == []:
        return False
    if first(lst) == n:
        return True
    else:
        return search(rest(lst), n)
    
def search_p(lst, n):
    if not search(lst, n):
        return -1
    if first(lst) == n:
        return 0
    else:
        return search_p(rest(lst), n) + 1
    
def update(lst, pos, n):
    
            
        

# (a) Implementar os métodos da "estrutura de lista"
#   - usando recursividade sempre que necessário
#   - recebendo como parâmetro uma lista do Python

# (b) Criar uma lista do Python com todos os estudantes
#     da turma, registrando:
#   - nome do estudante
#   - telefone
#   - e-mail
#   - número de matrícula

# (c) Usar os métodos que você implementou no item (a)
#     para manipular a lista que você criou no item (b)