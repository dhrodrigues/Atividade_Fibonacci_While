termos = int(input("Qual numero termo?\n"))

x = 0
y = 1
contador = 0

if termos <= 0:
    print("Finalizado")

else:
    print("\nSequencia Fibonacci:")
    while (contador < termos):
        print(x)
        z = x + y
        x = y
        y = z
        contador += 1