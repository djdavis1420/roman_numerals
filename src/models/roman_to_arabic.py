class RomanToArabicConverter:
    def __init__(self, roman_numeral):
        self.roman_numeral = roman_numeral
        self.arabic_number = 0

    def convert(self):
        self.arabic_number = 1
