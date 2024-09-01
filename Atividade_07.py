lista = []

add = input("Deseja adicionar itens na lista? S/N")

while add == "S":

 item = input("Digite o item da lista de compras: ")
 lista.append(item)
 add = input("Deseja adicionar mais itens na lista? S/N ")


print("Lista de compras: ", lista)