n = int(input("inserisci un numero: "))
while True:
    for i in range(n, -1, -1):
        print(i)
        continua = input("vuoi continuare?" "(si/no)")
    if continua == "no":
        print("ciclo terminato")
        
        
        