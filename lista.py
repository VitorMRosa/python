saladaDeFrutas = ["Leite em pó"]

saladaDeFrutas.append("maçã")

saladaDeFrutas.insert(0,"laranja")

saladaDeFrutas.remove("Leite em pó")

Fruta = saladaDeFrutas.pop()

x = saladaDeFrutas.copy()
print(x)

x.append("maça")

senhas = [10,20,30,40]

senhas.insert(0,senhas.pop())

senhas.reverse()

senhas.sort(reverse = True)



print(min(senhas))
print(max(senhas))

print(senhas)


print(saladaDeFrutas)