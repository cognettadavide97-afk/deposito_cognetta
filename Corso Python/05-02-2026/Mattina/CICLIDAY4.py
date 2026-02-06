numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    if numero == 3:
        break
    print (numero)
    
numeri = [1, 2, 3, 4, 5]

for numero in numeri:
    if numero == 3:
        continue
    print (numero)
    
for i in range(5):
    if i == 3:
        pass
    print(i)
    
numeri = [*range(1, 11)]
print(numeri) #output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

