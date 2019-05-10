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

        for index, value in enumerate(numeral):
            if index == len(self.roman_numeral) - 1:
                self.arabic_number += self.VALUES.get(value)
            elif index < len(self.roman_numeral) - 1:
                value_at_current_index = self.VALUES.get(value)
                value_at_next_index = self.VALUES.get(numeral[index + 1])
                if value_at_current_index < value_at_next_index:
                    self.arabic_number -= value_at_current_index
                elif value_at_current_index >= value_at_next_index:
                    self.arabic_number += value_at_current_index