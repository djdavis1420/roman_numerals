class ArabicToRomanConverter:
    VALUES = {
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

    def __init__(self, arabic_number):
        self.arabic_number = arabic_number
        self.roman_numeral = ''

    def convert(self):
        number = self.arabic_number

        for key, value in self.VALUES.items():
            while number >= value:
                self.roman_numeral += key
                number -= value

        return self.roman_numeral
