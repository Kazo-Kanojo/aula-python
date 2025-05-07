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
print(f"A quantidade de vogais é {vogais}")'''

soma = 0
numeros = [3,2,7,1,8,9]
for i in range(len(numeros)):
    soma += numeros[i]
    print(f"A soma dos elementos é: {soma} ")


for i in range(len(numeros)):
    if numeros[i]%2 != 0:
        print(i)
    print("não acontece porra nenhuma")