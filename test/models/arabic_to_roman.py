from src.models.arabic_to_roman import ArabicToRomanConverter


class TestArabicToRomanConverter:

    def test_arabic_to_roman__should_convert_1_to_I(self):
        converter = ArabicToRomanConverter(1)
        actual = converter.convert()
        assert actual == 'I'

    def test_arabic_to_roman__should_convert_2_to_II(self):
        converter = ArabicToRomanConverter(2)
        actual = converter.convert()
        assert actual == 'II'

    def test_arabic_to_roman__should_convert_3_to_III(self):
        converter = ArabicToRomanConverter(3)
        actual = converter.convert()
        assert actual == 'III'

    def test_arabic_to_roman__should_convert_4_to_IV(self):
        converter = ArabicToRomanConverter(4)
        actual = converter.convert()
        assert actual == 'IV'

    def test_arabic_to_roman__should_convert_5_to_V(self):
        converter = ArabicToRomanConverter(5)
        actual = converter.convert()
        assert actual == 'V'

    def test_arabic_to_roman__should_convert_6_to_VI(self):
        converter = ArabicToRomanConverter(6)
        actual = converter.convert()
        assert actual == 'VI'

    def test_arabic_to_roman__should_convert_7_to_VII(self):
        converter = ArabicToRomanConverter(7)
        actual = converter.convert()
        assert actual == 'VII'

    def test_arabic_to_roman__should_convert_8_to_VIII(self):
        converter = ArabicToRomanConverter(8)
        actual = converter.convert()
        assert actual == 'VIII'

    def test_arabic_to_roman__should_convert_9_to_IX(self):
        converter = ArabicToRomanConverter(9)
        actual = converter.convert()
        assert actual == 'IX'

    def test_arabic_to_roman__should_convert_10_to_X(self):
        converter = ArabicToRomanConverter(10)
        actual = converter.convert()
        assert actual == 'X'

    def test_arabic_to_roman__should_convert_14_to_XIV(self):
        converter = ArabicToRomanConverter(14)
        actual = converter.convert()
        assert actual == 'XIV'

    def test_arabic_to_roman__should_convert_19_to_XIX(self):
        converter = ArabicToRomanConverter(19)
        actual = converter.convert()
        assert actual == 'XIX'

    def test_arabic_to_roman__should_convert_24_to_XXIV(self):
        converter = ArabicToRomanConverter(24)
        actual = converter.convert()
        assert actual == 'XXIV'

    def test_arabic_to_roman__should_convert_29_to_XXIX(self):
        converter = ArabicToRomanConverter(29)
        actual = converter.convert()
        assert actual == 'XXIX'

    def test_arabic_to_roman__should_convert_333_to_CCCXXXIII(self):
        converter = ArabicToRomanConverter(333)
        actual = converter.convert()
        assert actual == 'CCCXXXIII'

    def test_arabic_to_roman__should_convert_494_to_CDXCIV(self):
        converter = ArabicToRomanConverter(494)
        actual = converter.convert()
        assert actual == 'CDXCIV'

    def test_arabic_to_roman__should_convert_639_to_DCXXXIX(self):
        converter = ArabicToRomanConverter(639)
        actual = converter.convert()
        assert actual == 'DCXXXIX'

    def test_arabic_to_roman__should_convert_949_to_CMXLIX(self):
        converter = ArabicToRomanConverter(949)
        actual = converter.convert()
        assert actual == 'CMXLIX'

    def test_arabic_to_roman__should_convert_999_to_CMXCIX(self):
        converter = ArabicToRomanConverter(999)
        actual = converter.convert()
        assert actual == 'CMXCIX'

    def test_arabic_to_roman__should_convert_1492_to_MCDXCII(self):
        converter = ArabicToRomanConverter(1492)
        actual = converter.convert()
        assert actual == 'MCDXCII'

    def test_arabic_to_roman__should_convert_1985_to_MCMLXXXV(self):
        converter = ArabicToRomanConverter(1985)
        actual = converter.convert()
        assert actual == 'MCMLXXXV'

    def test_arabic_to_roman__should_convert_2019_to_MMXIX(self):
        converter = ArabicToRomanConverter(2019)
        actual = converter.convert()
        assert actual == 'MMXIX'

    def test_arabic_to_roman__should_convert_4994_to_M_VCMXCIV(self):
        converter = ArabicToRomanConverter(4994)
        actual = converter.convert()
        assert actual == 'M(V)CMXCIV'

    def test_arabic_to_roman__should_convert_7447_to_V_MMCDXLVII(self):
        converter = ArabicToRomanConverter(7447)
        actual = converter.convert()
        assert actual == '(V)MMCDXLVII'

    def test_arabic_to_roman__should_convert_9999_to_M_XCMXCIX(self):
        converter = ArabicToRomanConverter(9999)
        actual = converter.convert()
        assert actual == 'M(X)CMXCIX'
