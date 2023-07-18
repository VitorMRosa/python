salarioBruto = float(input("Informe-nos o seu salário:").replace(",","."))
if salarioBruto <= 1903.98 :
    print(salarioBruto , ", não tem mudanças no seu salário")
elif salarioBruto <= 2826.65 :
    aliq = 0.075
    salarioLiq = salarioBruto - (aliq * salarioBruto)
    salarioLiqui = salarioLiq + 142.80 
    print(salarioBruto)
    print(salarioLiqui)
    
