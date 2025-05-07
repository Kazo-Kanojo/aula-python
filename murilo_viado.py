'''nome = "danilo"
vogais = 0
for char in nome:
    if char == 'a' or char == 'e' or char =='i' or char == 'o' or char == 'u':
        vogais += 1
print(vogais)


for i in range(11):
    print(i)

for i in range(0,11,2):# (incio, fim , passo))
    print(i)

for i in range(20, 10, -2):
    print(i)

lista = [1, True, 2.3, [], 'Enzo']
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")


lista = [1,True, 2.3,[],'danilo']
for elem in lista:
    print(elem)

lista = [1,True, 2.3,[],'danilo']
for elem in lista:
    elem = 0
print(lista)



for i in range(len(lista)):
    lista[i] = 0
print(lista)


#exercicio print apenas os elementos em indices pares
#print somente as vogais

vogais = 0
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
for i in range(len(lista)):
    if i%2==0:
        print(lista[i])
for i in range(len(lista)):
    print(f"Vou verificar se lista[{i}], ou seja '{lista[i]}', é vogal")
    if lista[i] == 'a' or lista[i] == 'e' or lista[i] == 'i' or lista[i] == 'o' or lista[i] == 'u':
        print("sim")
        vogais += 1
        continue
    print("não")
print(f"A quantidade de vogais é {vogais}")

soma = 0
numeros = [3,2,7,1,8,9]
for i in range(len(numeros)):
    soma += numeros[i]
    print(f"A soma dos elementos é: {soma} ")


for i in range(len(numeros)):
    if numeros[i]%2 != 0:
        print(i)
    print("não acontece porra nenhuma")


media_final = [7,2,3,6,4]
alunos = ['luis', 'joao', 'Ana luiza', 'josé', 'Sofia']

for i in range(len(media_final)):
    if media_final[i] >= 6:
        print(f"O/a {alunos[i]} passou")


#encontre danilo
#Diga qual matéria ele da

profs = ['Ceelso', 'Demetrius', 'aurélio', 'Ana', 'Cidade', 'luis', 'danilo']
materias = ['calculo', 'edge', 'sw&TX', 'story', 'front', 'web', 'pyton']

for i in range(len(profs)):
    if profs[i] == 'danilo':
        print("danilo é o professor mais viado de todos")


profs = ['Celso', 'Demetrius', 'aurélio', 'Ana', 'Cidade', 'luis', 'danilo']
materias = ['calculo', 'edge', 'sw&TX', 'story', 'front', 'web', 'pyton']
for i in range(len(profs)):
    print(f"o/a {profs[i]} da a materia de {materias[i]}")


preco = [3,150,20,1000000000,200,500]
carros = ['kwid','civic','up', 'POLINHO TURBÃO MANUAL', 'opala', 'uno com escada']
maior = preco[0]
indice_maior = 0
for i in range(len(preco)):
   # print(f"vou testar se {preco[i]}, é maior que {maior}")
    if preco[i] > maior:
    #    print(f" Deu certo vou trocar {maior} por {preco[i]}")
        maior = preco[i]
        indice_maior = i
print(f"O carro mais caro é o {carros[indice_maior]}")
'''


for i in range(1,11):
    print(f"tabuada do {i}:")
    for j in range(1,11):
        print(f" a tabuada do {i} * {j} = {j*i}")
