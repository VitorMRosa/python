media = int(input("quantas notas você quer fazer a média:"))
soma = 0
for i in range(media) :
    nota = float(input("Digite a nota:"))
    soma = soma +  nota
soma = soma / media
print(f"A média é :{soma}")

