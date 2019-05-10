class RomanToArabicConverter:
    VALUES = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }

    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.arabic_number = 0

    def convert(self):
        numeral = self.roman_numeral
        for char in numeral:
            for key, value in self.VALUES.items():
                if char == key:
                    self.arabic_number += value
