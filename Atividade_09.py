texto = input("Digite uma frase: ")
letra = input("Digite a letra que deseja contar: ")

quantidade = texto.count(letra)

print("A letra", letra.upper(), "aparece", quantidade, "vezes na frase:", texto)