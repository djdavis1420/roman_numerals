from src.models.roman_to_arabic import RomanToArabicConverter


class TestRomanToArabicConverter:

    def test__should_instantiate_converter_with_roman_numeral_I(self):
        converter = RomanToArabicConverter('I')
        assert converter.roman_numeral == 'I'
        assert converter.arabic_number == 0
