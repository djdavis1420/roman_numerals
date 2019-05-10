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

    def test_convert__should_convert_X_to_10(self):
        converter = RomanToArabicConverter('X')
        converter.convert()
        assert converter.arabic_number == 10

    def test_convert__should_convert_L_to_50(self):
        converter = RomanToArabicConverter('L')
        converter.convert()
        assert converter.arabic_number == 50

    def test_convert__should_convert_C_to_100(self):
        converter = RomanToArabicConverter('C')
        converter.convert()
        assert converter.arabic_number == 100

    def test_convert__should_convert_D_to_500(self):
        converter = RomanToArabicConverter('D')
        converter.convert()
        assert converter.arabic_number == 500

    def test_convert__should_convert_M_to_1000(self):
        converter = RomanToArabicConverter('M')
        converter.convert()
        assert converter.arabic_number == 1000
