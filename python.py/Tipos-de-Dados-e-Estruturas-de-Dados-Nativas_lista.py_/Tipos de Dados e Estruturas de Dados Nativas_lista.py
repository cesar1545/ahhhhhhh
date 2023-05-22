#Como declarar uma lista
'''
lista  = []
lista2 = [1,2,3,4,5]
'''
#Como ler uma lista
'''
lista  = ["UM",2.0,3]    #Uma lista pode conter diferentes tipos de dados
x = lista[0]             #A contagem dos itens sempre começam em zero
print(lista[0])
print(lista[1])
print(lista[2])
#print(lista[3])         #Retorna um erro, pois este índice não existe
'''

lista  = ["UM",2.0,3] #Lista usada nos exemplos

#len() -> É uma função nativa do Python, não uma lista. Ela retorna o tamanho de um objeto.
''' 
print(len(lista))
'''

#append()
'''
lista.append('Quatro')
print(lista[3])
print(len(lista))
'''

#clear
'''
lista.clear()
print(len(lista))
#print(lista[0]]) #Não existem mais itens
'''

#copy
'''
x = lista.copy()
print(x[1])
'''

#count()
'''
print(lista.count(2.0))
'''

#extend()
'''
lista.extend('Quatro')
print(lista[3])
'''

#index()
'''
print(lista.index(3))
'''

#insert()
'''
lista.insert(0,'um')
print(lista[0])
'''

#pop()
'''
lista.pop(1)
print(lista[1])
'''

#remove()
'''
lista.remove(2.0)
print(lista[1])  #As posições seguintes são arrastadas uma casa para trás
'''

#reverse()
'''
lista.reverse()
print(lista[0])
'''

#sort()
'''
lista = [5,1,2,3,4]
lista.sort()
print(lista[0])
'''

#Listas podem ter outras listas dentro delas
'''
lista3 = [[1,2,3],[4,5,6]]
print(lista3[0][1])
'''

#Referência
'''
append()	   Adiciona um elemento ao final da lista
clear()	       Remove todos os elementos da lista
copy()	       Retorna uma cópia da lista
count()	       Retorna a quantidade de elementos com determinado valor
extend()	   Adiciona um item da lista, ou um iterável, ao final da lista
index()	       Retorna o índice de posição de um elemento com aquele valor
insert()	   Adiciona um elemento em determinada posição
pop()	       Remove o elemento da posição informada
remove()	   Remove o primeiro item com aquele valor
reverse()	   Inverte a ordem da lista
sort()	       Organiza a lista
'''