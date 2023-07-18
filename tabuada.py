numero2 = float(input("Qual o numero que você deseja ver a tabuada:"))
for i in range (11):
    numero3 = numero2 * i
    print(f"{numero2:.0f}" , "+" , i , "=", f"{numero3:.0f}")
numero = 0
for i in range(11):
    numero = numero + 1
    for j in range(11):
        resposta = numero * j
        print(f"{numero}" , "+" , j ,"=", f"{resposta}")

   
 

