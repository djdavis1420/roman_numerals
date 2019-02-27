roman_numerals = {
    '(X)': 10000,
    'M(X)': 9000,
    '(V)': 5000,
    'M(V)': 4000,
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1
}


def romanize(num):
    values = roman_numerals.items()
    number = num
    numeral = ''

    while number != 0:
        for key, value in values:
            while number >= value:
                numeral += str(key)
                number -= value

    return numeral
