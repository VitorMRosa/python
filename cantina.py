print("--------------CARDÁPIO----------------")
print("| Código |    Descrição      | Valor |")
print("|  100   |   Cachorro-quente | 9,00  |")
print("|  101   |   Cachorro duplo  | 11,00 |")
print("|  102   |       X-Egg       | 12,00 |")
print("|  103   |      X-Salada     | 13,00 |")
print("|  104   |      X-Bacon      | 14,00 |")
print("|  105   |      X-Tudo       | 17,00 |")
print("|  106   |    Refrigerante   |  5,00 |")
total = 0

CantinaItens = {"100":{"descriçao":"Cachoro-Quente","preço":9.00} ,
                "101": {"descriçao":"Cachorro Duplo","preço":11.00},
                "102": {"descriçao":"X-Egg","preço":12.00},
                "103": {"descriçao":"X-Salada","preço":13.00} ,
                "104": {"descriçao":"X-Egg","preço":14.00},  
                "105": {"descriçao":"X-tudo","preço":17.00},
                "106": {"descriçao":"Refrigerante","preço":5.00} }


while True:
    pedido = input("Digite o código do produto ou 0 para sair: ")
    
    if pedido == "0":
        resposta = input("Você deseja terminar sua compra? \n sim/não.\n ").lower()
        if resposta == "Sim":
            break
        else:
            continue
            

    
    elif pedido == "100":
        total = total + CantinaItens[["100"]["preço"]]
        print(f"Você pediu um cachorro-quente no valor de" ,"R$",CantinaItens["100"])

    elif pedido == "101":
        total = total + CantinaItens[["101"]["preço"]]
        print(f"Você pediu um cachorro duplo no valor de" ,"R$", CantinaItens["101"])
    
    elif pedido == "102":
        total = total + CantinaItens[["102"]["preço"]]
        print(f"Você pediu um X-egg no valor de" ,"R$", CantinaItens["102"])
        
    elif pedido == "103":
        total = total + CantinaItens[["103"]["preço"]]
        print(f"Você pediu um X-salada no valor de","R$", CantinaItens["103"])
        
    elif pedido == "104":
        total = total + CantinaItens[["104"]["preço"]]
        print(f"Você pediu um X-bacon no valor de" ,"R$", CantinaItens["104"])
        
    elif pedido == "105":
        total = total + CantinaItens[["105"]["preço"]]
        print(f"Você pediu um X-tudo no valor de" ,"R$",CantinaItens["105"])
        
    elif pedido == "106":
        total = total + CantinaItens[["106"]["preço"]]
        print(f"Você pediu um refrigerante no valor de","R$", CantinaItens["106"])
    else:
        print("Código de produto inválido!")
        continue
    print(f"Total da compra: R$ {total:.2f}")
    
print("Você pediu")
print(f"Total da compra: R$ {total:.2f}")

