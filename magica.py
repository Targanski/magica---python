lista1 = ['A1','A2','A3','A4','A5','A6','A7']
lista2 = ['B1','B2','B3','B4','B5','B6','B7']
lista3 = ['C1','C2','C3','C4','C5','C6','C7']


print("A  B  C")
for i in range(0,7):
    print(lista1[i],lista2[i],lista3[i])

escolha1 = input("Escolha uma das colunas: ")
print("------------------------------------------")

if escolha1 == 'A' or escolha1 == 'a':
    round1 = lista2+lista1+lista3
elif escolha1 == 'B' or escolha1 == 'b':
    round1 = lista1+lista2+lista3
else:
    round1 = lista1+lista3+lista2

n = 3
round2 = [round1[i::n] for i in range(7)]

lista1 = round2[0]
lista2 = round2[1]
lista3 = round2[2]
print("A  B  C")
for i in range(0,7):
    print(lista1[i],lista2[i],lista3[i])

escolha2 = input("Escolha uma das colunas: ")

print("-------------------------------------------")
if escolha2 == 'A' or escolha2 == 'a':
    round3 = lista2+lista1+lista3
elif escolha2 == 'B' or escolha2 == 'b':
    round3 = lista1+lista2+lista3
else:
    round3 = lista1+lista3+lista2

n = 3
round4 = [round3[i::n] for i in range(7)]


lista1 = round4[0]
lista2 = round4[1]
lista3 = round4[2]
print("A  B  C")
for i in range(0,7):
    print(lista1[i],lista2[i],lista3[i])

escolha3 = input("Escolha uma das colunas: ")
print("A, B ou C?")
print("-------------------------------------------")
if escolha3 == 'A' or escolha3 == 'a':
    round5 = lista2+lista1+lista3
elif escolha3 == 'B' or escolha3 == 'b':
    round5 = lista1+lista2+lista3
else:
    round5 = lista1+lista3+lista2

print(f'Você escolheu > {round5[10]}')

