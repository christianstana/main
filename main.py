def es_primo_palindromo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return str(numero) == str(numero)[::-1]

def test_es_primo_palindromo():
    # Test cases for es_primo_palindromo function
    assert es_primo_palindromo(2) == True  # 2 is a prime palindrome
    assert es_primo_palindromo(4) == False  # 4 is not a prime palindrome
    assert es_primo_palindromo(17) == False  # 17 is prime but not a palindrome
    assert es_primo_palindromo(131) == True  # 131 is a prime palindrome
    assert es_primo_palindromo(121) == False  # 121 is not a prime palindrome
    assert es_primo_palindromo(757) == True  # 757 is a prime palindrome

# Run the tests if the script is executed directly
if __name__ == "__main__":
    test_es_primo_palindromo()
