
import math

# Solicita as medidas dos catetos ao usuário
cateto_a = float(input("Digite a medida do cateto a: "))
cateto_b = float(input("Digite a medida do cateto b: "))

# Calcula a hipotenusa
hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)

# Calcula o perímetro
perimetro = cateto_a + cateto_b + hipotenusa

# Calcula a área
area = (cateto_a * cateto_b) / 2

# Exibe os resultados
print("Perímetro: ", perimetro)
print("Área: ", area)



