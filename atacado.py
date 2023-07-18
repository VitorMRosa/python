produto = float(input("qual o valor do produto?").replace(",","."))
quantidade = int(input("Qual a quantidade de produtos?" ) )
if quantidade <= 9 :
  valor =  produto * quantidade
  print ("O valor  pagar é :" , valor)
elif quantidade <= 99 :
  desconto = (quantidade * 5) / 100
  valor = desconto - produto
  desconto = (valor * quantidade) * -1
  print("O valor  pagar é :" , desconto)
  print(desconto)
elif quantidade <= 999 :
  desconto = (quantidade * 10) / 100
  valor = desconto - produto
  desconto = (valor * quantidade)
  print("O valor  pagar é :" , desconto)
  print(desconto)
elif quantidade >= 1000 :
  desconto = (quantidade * 15) / 100
  valor = desconto - produto
  desconto = (valor * quantidade) 
  print("O valor  pagar é :" , desconto)
  print(desconto)