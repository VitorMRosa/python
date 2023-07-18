idade = int(input("Digite a sua idade: "))
if idade <16 :
    print("Não vota")
elif idade >=18 and idade <= 70:
    print("Voto Obrigatório")
else:
    print("Voto opcional")
