hipotenusa = 0
perimetro = 0
area = 0

def main():
    a = float(input("Qual o valor do cateto A:").replace(",","."))
    b = float(input("Qual o valor do cateto B:").replace(",","."))
    hipotenusa = callHipotenusa(a,b)
    perimetro = callPerimetro(a,b,hipotenusa)
    area = calArea(a,b)
    print(perimetro)
    print(area)

def callHipotenusa(a,b):
   
    hipotenusa  = ((a ** 2) + (b ** 2))
    hipotenusa = hipotenusa ** 0.5
    return hipotenusa


def callPerimetro(a,b,hipotenusa):
    perimetro = (a + b + hipotenusa)
    return perimetro
    
def calArea(a,b):    
    area = ((a * b ) / 2)
    
    return area

main()