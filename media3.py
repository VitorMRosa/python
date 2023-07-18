notas = []
soma = 0
quantia = int(input("Quantas notas você quer fazer a media?: "))
for i in range(quantia):
    notas.append(float(input(f"qual a sua nota {i + 1}?:")))
    
for i in range(quantia):
    
    soma = soma + notas[i]
    media = soma / quantia

for  nota in range(0,len(notas)):
    print(f"A nota {nota + 1} é: {notas[nota]}")
print(f"A media das suas notas é {media:.1f}. ")
    



    
    