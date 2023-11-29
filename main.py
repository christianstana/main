def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def test_es_primo():
    assert es_primo(2) ==

if __name__ == "__main__":
    test_es_primo()

