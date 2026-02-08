valore = int(input("inserisci numero o stringa: "))
while True:
    if valore % 2 == 0:
        print("è un valore pari")
        loop = input("vuoi inserire un nuovo valore?: (si/no)")
        if loop == "si":
            valore = int(input("inserisci numero o stringa: "))
        else: 
            break
    elif len(valore) % 2== 0:
        loop = input("vuoi inserire un nuovo valore?: (si/no)")
        if loop == "si":
            valore = int(input("inserisci numero o stringa: "))
        else:
            break
    if valore % 2 != 0:
        print("è un valore dispari")
        loop = input("vuoi inserire un nuovo valore?: (si/no)")
        if loop == "si":
            valore = int(input("inserisci numero o stringa: "))
        else:
            break