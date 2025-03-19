"""
Arnau Piñero Masegosa

Modulo que define funciones con numeros primos.

# Pruevas unitarias al estilo doctest
>>> esPrimo(4)
False

>>> esPrimo(-2)
True
"""


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # Comprueba las pruebas unitarias.


def esPrimo(numero):
    """"
    Retorna True si el numero introducido"
    es primo o False en caso contrario.

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """

    for prova in range(2, numero):
        if numero % prova == 0:
            return False
    
    return True


def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que el número ingresado.
    
    >>> primos(10)
    (2, 3, 5, 7)
    """
    primos_menores = [i for i in range(2, numero) if esPrimo(i)]
    return tuple(primos_menores)


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    >>> descompon(315)
    (3, 3, 5, 7)
    """

    factores = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        else:
            divisor += 1
            if not esPrimo(divisor):
                divisor += 1
    return tuple(factores)


def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de dos números.

    >>> mcm(12, 15)
    60
    """
    
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) | set(factores2)
    mcm = 1
    for factor in factores_comunes:
        potencia1 = factores1.count(factor)
        potencia2 = factores2.count(factor)
        mcm *= factor ** max(potencia1, potencia2)
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de dos números.

    >>> mcd(12, 15)
    3
    """

    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) & set(factores2)
    mcd = 1
    for factor in factores_comunes:
        potencia1 = factores1.count(factor)
        potencia2 = factores2.count(factor)
        mcd *= factor ** min(potencia1, potencia2)
    return mcd


def mcmN(*args):
    """
    Devuelve el mínimo común múltiplo de un número arbitrario de argumentos.

    >>> mcmN(12, 15, 20)
    60
    """

    resultado = args[0]
    for arg in args[1:]:
        resultado = mcm(resultado, arg)
    return resultado

def mcdN(*args):
    """
    Devuelve el máximo común divisor de un número arbitrario de argumentos.

    >>> mcdN(12, 15, 20)
    1
    """
    
    resultado = args[0]
    for arg in args[1:]:
        resultado = mcd(resultado, arg)
    return resultado