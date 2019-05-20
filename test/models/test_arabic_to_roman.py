from src.models.arabic_to_roman import ArabicToRomanConverter


class TestArabicToRomanConverter:

    def setup_method(self):
        self.converter = ArabicToRomanConverter()

    def test_convert__should_convert_1_to_I(self):
        actual = self.converter.convert(1)
        assert actual == 'I'

    def test_convert__should_convert_2_to_II(self):
        actual = self.converter.convert(2)
        assert actual == 'II'

    def test_convert__should_convert_3_to_III(self):
        actual = self.converter.convert(3)
        assert actual == 'III'

    def test_convert__should_convert_4_to_IV(self):
        actual = self.converter.convert(4)
        assert actual == 'IV'

    def test_convert__should_convert_5_to_V(self):
        actual = self.converter.convert(5)
        assert actual == 'V'

    def test_convert__should_convert_6_to_VI(self):
        actual = self.converter.convert(6)
        assert actual == 'VI'

    def test_convert__should_convert_7_to_VII(self):
        actual = self.converter.convert(7)
        assert actual == 'VII'

    def test_convert__should_convert_8_to_VIII(self):
        actual = self.converter.convert(8)
        assert actual == 'VIII'

    def test_convert__should_convert_9_to_IX(self):
        actual = self.converter.convert(9)
        assert actual == 'IX'

    def test_convert__should_convert_10_to_X(self):
        actual = self.converter.convert(10)
        assert actual == 'X'

    def test_convert__should_convert_14_to_XIV(self):
        actual = self.converter.convert(14)
        assert actual == 'XIV'

    def test_convert__should_convert_19_to_XIX(self):
        actual = self.converter.convert(19)
        assert actual == 'XIX'

    def test_convert__should_convert_24_to_XXIV(self):
        actual = self.converter.convert(24)
        assert actual == 'XXIV'

    def test_convert__should_convert_29_to_XXIX(self):
        actual = self.converter.convert(29)
        assert actual == 'XXIX'

    def test_convert__should_convert_333_to_CCCXXXIII(self):
        actual = self.converter.convert(333)
        assert actual == 'CCCXXXIII'

    def test_convert__should_convert_494_to_CDXCIV(self):
        actual = self.converter.convert(494)
        assert actual == 'CDXCIV'

    def test_convert__should_convert_639_to_DCXXXIX(self):
        actual = self.converter.convert(639)
        assert actual == 'DCXXXIX'

    def test_convert__should_convert_949_to_CMXLIX(self):
        actual = self.converter.convert(949)
        assert actual == 'CMXLIX'

    def test_convert__should_convert_999_to_CMXCIX(self):
        actual = self.converter.convert(999)
        assert actual == 'CMXCIX'

    def test_convert__should_convert_1492_to_MCDXCII(self):
        actual = self.converter.convert(1492)
        assert actual == 'MCDXCII'

    def test_convert__should_convert_1985_to_MCMLXXXV(self):
        actual = self.converter.convert(1985)
        assert actual == 'MCMLXXXV'

    def test_convert__should_convert_2019_to_MMXIX(self):
        actual = self.converter.convert(2019)
        assert actual == 'MMXIX'

    def test_convert__should_convert_4994_to_M_VCMXCIV(self):
        actual = self.converter.convert(4994)
        assert actual == 'M(V)CMXCIV'

    def test_convert__should_convert_7447_to_V_MMCDXLVII(self):
        actual = self.converter.convert(7447)
        assert actual == '(V)MMCDXLVII'

    def test_convert__should_convert_9999_to_M_XCMXCIX(self):
        actual = self.converter.convert(9999)
        assert actual == 'M(X)CMXCIX'
