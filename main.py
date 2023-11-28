def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def main():
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            if es_primo(numero):
                print(f"{numero} es un número primo.")
            else:
                print(f"{numero} no es un número primo.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()
