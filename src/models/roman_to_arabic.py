class RomanToArabicConverter:
    VALUES = {
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
