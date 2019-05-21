#!/C/Users/djdav/Development/Python/roman_numerals/venv/Scripts/python


from src.models.arabic_to_roman import ArabicToRomanConverter
from src.models.roman_to_arabic import RomanToArabicConverter


def console_app():
    input_string = input("Enter a valid Roman Numeral or Arabic Number.\nInput: ")
    convert(input_string)


def convert(input_string):
    try:
        number = int(input_string)
        converter = ArabicToRomanConverter()
        result = converter.convert(number)
        print("Output: " + result)
    except ValueError:
        converter = RomanToArabicConverter()
        result = converter.convert(input_string)
        print("Output: " + str(result))


console_app()
