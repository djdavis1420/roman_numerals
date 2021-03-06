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

    def __init__(self):
        self.roman_numeral = 0
        self.arabic_number = 0

    def convert(self, roman_numeral):
        self.roman_numeral = roman_numeral
        numeral = self.roman_numeral

        for index, character in enumerate(numeral):
            if index == len(self.roman_numeral) - 1:
                self.arabic_number += self.VALUES.get(character)
            elif index < len(self.roman_numeral) - 1:
                self.__parse_character(numeral, index, character)

        return self.arabic_number

    def __parse_character(self, numeral, index, character):
        value_at_current_index = self.VALUES.get(character)
        value_at_next_index = self.VALUES.get(numeral[index + 1])
        if value_at_current_index < value_at_next_index:
            self.arabic_number -= value_at_current_index
        elif value_at_current_index >= value_at_next_index:
            self.arabic_number += value_at_current_index
