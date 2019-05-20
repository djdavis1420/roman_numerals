from src.models.roman_to_arabic import RomanToArabicConverter


class TestRomanToArabicConverter:

    def setup_method(self):
        self.converter = RomanToArabicConverter()

    def test_convert__should_convert_I_to_1(self):
        actual = self.converter.convert('I')
        assert actual == 1

    def test_convert__should_convert_V_to_5(self):
        actual = self.converter.convert('V')
        assert actual == 5

    def test_convert__should_convert_X_to_10(self):
        actual = self.converter.convert('X')
        assert actual == 10

    def test_convert__should_convert_L_to_50(self):
        actual = self.converter.convert('L')
        assert actual == 50

    def test_convert__should_convert_C_to_100(self):
        actual = self.converter.convert('C')
        assert actual == 100

    def test_convert__should_convert_D_to_500(self):
        actual = self.converter.convert('D')
        assert actual == 500

    def test_convert__should_convert_M_to_1000(self):
        actual = self.converter.convert('M')
        assert actual == 1000

    def test_convert__should_convert_IV_to_4(self):
        actual = self.converter.convert('IV')
        assert actual == 4

    def test_convert__should_convert_VI_to_6(self):
        actual = self.converter.convert('VI')
        assert actual == 6

    def test_convert__should_convert_XX_to_20(self):
        actual = self.converter.convert('XX')
        assert actual == 20
