def es_primo_palindromo(numero):
    # Verifica si el número es menor o igual a 1, en cuyo caso no es primo ni palíndromo
    if numero <= 1:
        return False
    
    # Verifica si el número es divisible por algún número en el rango de 2 a la raíz cuadrada del número más 1
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    # Convierte el número en una cadena y verifica si es igual a su inverso (es un palíndromo)
    return str(numero) == str(numero)[::-1]

def test_es_primo_palindromo():
    # Casos de prueba para la función es_primo_palindromo
    assert es_primo_palindromo(2) == True  # 2 es un número primo y un palíndromo
    assert es_primo_palindromo(4) == False  # 4 no es un número primo ni un palíndromo
    assert es_primo_palindromo(17) == False  # 17 es primo pero no es un palíndromo
    assert es_primo_palindromo(131) == True  # 131 es un número primo y un palíndromo
    assert es_primo_palindromo(121) == False  # 121 no es un palíndromo
    assert es_primo_palindromo(757) == True  # 757 es un número primo y un palíndromo

# Ejecuta las pruebas si el script se ejecuta directamente
if __name__ == "__main__":
    test_es_primo_palindromo()

