Velocidade = input("Coloque o texto que você quer transformar:")
Vel1 = Velocidade.replace("  " ," ")
VelocidadeRedusida = Vel1.replace(" " , "...")
Vel2 = (f"{VelocidadeRedusida:<1}")
print(Vel2)