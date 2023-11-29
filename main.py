def es_primo_palindromo(numero):
    # Verifica si el número es menor o igual a 1, en cuyo caso no es primo ni palíndromo
    if numero <= 1:
        return False
    
    # Verifica si el número es divisible por algún número en el rango de 2 a la raíz cuadrada del número más 1
    for i in range(2,
