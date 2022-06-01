termos = int(input("Informe quantos termos da sequencia Fibonacci deseja?\n"))

while(termos !=0):
    x = 0
    y = 1
    contador = 0

    if termos == 1:
        print("\n",x)

    elif termos == 2:
        print("\n",x,"\n",y)

    elif termos == 3:
        print("\n",x,"\n",y,"\n",x+y)

    else:
        print("\nSequencia Fibonacci:")

        while (contador < termos):
            print(x)
            z = x + y
            x = y
            y = z
            contador += 1

    termos = int(input("Digite qual a nova sequencia Fibonacci. Caso digite 0 sera encerrado o codigo\n"))
print("Tchau obrigado por utilizar esse Script")