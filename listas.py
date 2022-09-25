# Listas
nota1 = 7.9
nota2 = 9.7
nota3 = 8.2

notas = [7.9, 9.7, 8.2] # Lista

lista = [] # Lista vazia
lista = list() # Lista vazia também
lista = [26, 'Igor', 3.14, False]
lista_de_listas = [26, [1, 2, 3]]

#Indexação

lista = [10, 'Igor', -3.14, True]

print(lista[0]) # O primeiro elemento da lista
print(lista[1]) # O segundo elemento da lista
print(lista[2])
print(lista[3])

print(lista[-1]) # O último elemento da lista
print(lista[-2]) # O penúltimo elemento da lista
print(lista[-3]) # O antepenúltimo elemento da lista
print(lista[-4])

#Slices (fatiamento)

lista = [10, 50, 30, 20, 25, 60, 5]

print(lista[0:3]) # Começa no índice 0 e vai até o menor do que 3
print(lista[3:6]) # Começa no índice 3 e vai até o menor do que 6
print(lista[0:]) # Começa no índice 0 e vai até o último índice
print(lista[2:6:2]) # Começa no índice 2 e vai até o menor do que 6 e pulando de 2 em 2

# Percorrer todos os elementos de uma lista

# Utilizando os prórpios elementos da lista
for elemento in lista:
    print(elemento)

# Utilizando o tamanho da lista
print('Comprimento da lista: ', len(lista)) # len() traz a quantidade de elementos que tem na lista

for i in range(len(lista)):
    print(i) # imprime o indice
    print(lista[i]) # imprime o valor no indice

# Métodos de Listas

lista = [1, 3, 12, 8, 2]

print('Antes do append:', lista)
# método é uma função que está atrelada a uma variável

# append - adicionar um elemento ao final da lista

lista.append(3) # é como se fosse uma "função" que está dentro de uma variável
# adicionou o 3 no final da lista
print('Depois do append:', lista)

# insert - adiciona um elemento na posição que você quiser e qual elemento que você quer adicionar

lista.insert(2, 10) # 2 é o indice onde que adicionar e 10 é o valor do elemento que será adicionado
print('Depois do insert:', lista)

# extend - método para juntar duas listas

lista2 = [1, 2, 3]

lista.extend(lista2) # vai pegar os elemento da lista2 e colocar no final da lista lista
print('Depois do extend:', lista)

# Métodos para remover elementos

# pop - remover o elemento que você especificar ou se você não especificar ele vai remover o último elemento da lista

lista.pop() # remover o ultimo elemento
print('Lista após o pop:', lista)

lista.pop(0) # remove o elemento que está no índice 0
print('Lista após o pop:', lista)

# remove - remover o primeiro valor que você especificar

lista.remove(3) # remove o primeiro valor 3 que está na lista
print('Lista após o remove:', lista)

# count - método para contar quantas vezes um elemento que você especificar aparece na sua lista

print('Quantidade de 2 na lista:', lista.count(2))

# index - método para informar o índice de um determinado elemento dentro da lista

print('Indice do elemento 12 na lista:', lista.index(12))

# sort - método para ordenar a lista de forma crescente

lista.sort()

print(lista)

lista.sort(reverse=True) # ordenar de forma decrescente

print(lista)


# Funções para Listas

# len() - saber quantos elementos tem na lista, ou seja, seu tamanho

print('A lista tem:', len(lista),'elementos')

# sum - somar todos os elementos da lista

print('A soma total dos elementos da lista é:', sum(lista))

# max - retorna o maior valor da lista

print('O maior elemento da lista é:', max(lista))

# min - retorna o menor valor da lista

print('O menor elemento da lista é:', min(lista))