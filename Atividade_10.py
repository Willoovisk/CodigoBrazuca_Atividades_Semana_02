def primo(numero):
    if numero <=1:
        return False
    for i in range(2, int(numero**0.5)+1):
        if numero % i == 0:
            return False
    return True

a = int(input("Digite o primeiro número do intervalo: "))
b = int(input("Digite o segundo número do intervalo: "))
lista = []
cont = b-a

for i in range(cont):
    if primo(a) == True:
        lista.append(a)
        a = a + 1
    else:
        a = a + 1

print("Os números primos encontrados nesse intervalo são:", lista)

