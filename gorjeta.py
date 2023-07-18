

def main(): 
    reais = reais_to_float(input("Quanto deu a conta? "))
    percent = percent_to_float(input("Qual a porcentagem da gorgeta? "))
    tip = reais * percent
    print(f"Deixe R${tip:.2f}")

    return reais,percent


def reais_to_float(d): 
    d.replace("R$","")
    try:
        d = float(d)
    except:
        print("valor informmado não é numerico!")
        quit()
    return d

    
def percent_to_float(p):
    p.replace("%","")
    try:
        p = float(p)
        p = p / 100
    except:
        print("valor informmado não é numerico!")
        quit()
    return p

   


    

main()
