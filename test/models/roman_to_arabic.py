from src.models.roman_to_arabic import RomanToArabicConverter


class TestRomanToArabicConverter:

    def test__should_instantiate_converter_with_roman_numeral_I(self):
        converter = RomanToArabicConverter('I')
        assert converter.roman_numeral == 'I'
        assert converter.arabic_number == 0

    def test_convert__should_convert_I_to_1(self):
        converter = RomanToArabicConverter('I')
        converter.convert()
        assert converter.arabic_number == 1

    def test_convert__should_convert_V_to_5(self):
        converter = RomanToArabicConverter('V')
        converter.convert()
        assert converter.arabic_number == 5
