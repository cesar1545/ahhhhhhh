#Isso é um comentário e não será executado

'''
Isto é um comentário e não será executado
--------------------------------------------------------------------------------------------------------------
'''

#Funcionamento de comentários
'''
print("Esse executa")
#print("Esse não")
'''

#Nomenclatura de variáveis
'''
Correto: aluno, saldo, valor, altura1, altura2, altura3
Errado:  Aluno, 1saldo, valor@#
'''

#Atribuição de valor
'''
Ordem:
Variável <- = <- Valor
x = 1
'''

#Tipos de dados
'''
inteiro = 1              #inteiro -1, 2, 0, 1000000, -1000000
float = 2.3              #float 1.2, -1.5
String = 'Olá'           #String 'Treinamento Python' ou "Treinamento Python"
boolean = True ou False  #bool
objeto = Cachorro()      #veremos mais tarde
'''

#Verificando tipos
'''
x = 1
print(type(x))
'''

#Input
'''
nome = input()
print(nome)

nome = input("Digite seu nome: ")
print(nome)

y = input("Digite um número: ")
x = 2 * int(y)
print(x)

y = int(input("Digite um número: "))
x = 2 * y
print(x)
'''

#Observações
'''
x = 0
print(x)
y = 1
print(1)
x = y    #Uma variável pode receber o valor da outra
print(x)

x = 0
x = "Oi" #Uma variável pode mudar seu tipo quando recebe nova atribuição
'''

#Print composto
'''
nome = input("Digite seu nome: ") 
print("Olá " + nome + "!") #Você pode combinar uma String com o valor de uma variável
'''