numPri = int(input("Digite um numero: "))
divisao = (2,3,5,7)
if numPri < 0 or numPri == 1:
    print("Seu numero não é primo.")
elif numPri == 2 or numPri == 3 or numPri == 5 or numPri == 7 :
    print(" O numero é primo.")
else:
    for i in (divisao):
        if numPri % i == 0:
            print ("Não é primo!")
            break
        
        else: 
            numPri % i != 0
            print("é primo!")
            break
            
       
                
            
        
                