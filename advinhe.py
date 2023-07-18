print("pense um numero!\n 'sim' \n 'não'")
numero1 = 0
numero2 = 0
numero = input("Seu numero é maior que 5?")
if numero == "sim" :
    numero1 = input("Seu numero é par?")
    if numero1 == "não":
        numero2 = input("Seu numero é primo de alguem?(Numero primo)")
        if numero2 == "sim":
            print("Então é o tal do 7!")
            
        elif numero2 == "não":
                numero3 = input("Esse numero é como se o '9' tivesse plantando bananeira?")
                if numero3 == "sim":
                    print("Então é o 6!!!")
                    if numero3 == "não":
                        print("então é o próprio 9!")
        
elif numero1 == "sim" :
    numero2 = input("Seu numero é divisivel por 4?")
    if numero2 == "sim":
        print("Seu Numero é 8!")
    elif numero2 == "não":
        print("Seu numero é 10!")
    else:
        print("Escolha um numero de 1 a 10")

elif numero == "não":
    numero1 = input("Seu numero é sempre o primeiro?")
    if numero1 == "sim":
        print("Então é 0, quer dizer 1!")
    elif numero1 == "não":
        numero2 = input("E o segundo?")
    if numero2 == "sim":
        print("Então é 2!;)")  
    elif numero2 == "não":
        numero3 = input("Esse numero é o dobro do segundo?")
        if numero3 == "sim":
            print("Então o seu numero é 4!")
        elif numero3 == "não":
            numero4 = input("ele é o segundo mais um?")
            if numero4 == "sim":
                print("Então seu numero é 3!")
            elif numero4 == "não":  
                print("Seu numero é 5!")
            else: 
                print("Escolha um numero de 1 a 10")





