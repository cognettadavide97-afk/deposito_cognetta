while True:
    n = int(input("Inserisci un numero intero positivo: "))
    if n > 0:
        break  # Esce dal ciclo solo se il numero è positivo
    print("Errore: devi inserire un numero maggiore di zero!")

# 2. Somma numeri pari con controllo IF dentro il FOR
somma_pari = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        somma_pari += i
print("Somma dei pari:",somma_pari)

# 3. Numeri dispari usando lo step del range
print("Numeri dispari:")
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

# 4. Controllo numero primo con un contatore di divisori
divisori = 0
for i in range(1, n + 1):
    if n % i == 0:
        divisori += 1

if divisori == 2:
    print(f"{n} è un numero primo.")
else:
    print(f"{n} non è un numero primo.")
