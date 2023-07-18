X1 = 0
X2 = 0
def main():
    Xa = float(input("qual o valor de a?: ").replace(",", "."))
    Xb = float(input("qual o valor de b?: ").replace(",", "."))
    Xc = float(input("qual o valor de c?: ").replace(",", "."))
    delta = callDelta(Xa,Xb,Xc)
    print(delta)
    deltaif = ifDelta(delta,Xa,Xb,Xc)
    print(deltaif)
    print(f"O valor de X1 é {deltaif[0]:.2f}")
    print(f"O valor de X2 é {deltaif[1]:.2f}")
    
def callDelta(Xa,Xb,Xc):
    delta = (Xb**2) - 4 * Xa * Xc
    return delta
def ifDelta(delta,Xa,Xb,Xc):
        if delta <0 :
            print("O valor é inexistente pois não é possivel tirar raiz de um delta negativo.")
        elif delta == 0 :
                X1 = (-Xb + delta ** 0.5) / 2 * Xa
                print(f"O resultado é {X1} pois delta é igual 0.  ")
        elif delta > 0 :
            X1 = (-Xb + delta ** 0.5 )/ 2 * Xa
            X2 = (-Xb - delta ** 0.5 ) / 2 * Xa

        return X1,X2

        
main()

   


