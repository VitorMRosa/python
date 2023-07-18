media = int(input("quantas notas você quer fazer a média: "))
peso = 0
soma = 0
peso2 = 0
for i in range(1,media + 1,1):
    nota = float(input(f"Qual a nota {i}? "))
    peso = float(input(f"Digite o peso da nota {i}: "))
    soma = soma + nota * peso
    peso2 += peso
    
   
    
    
resul = soma / peso2
print(f"Sua média é {resul:.1f}")

    