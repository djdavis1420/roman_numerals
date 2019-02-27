from src.roman_numerals import romanize


def test_romanize__should_convert_1_to_I():
    num = 1
    actual = romanize(num)
    assert actual == 'I'


def test_romanize__should_convert_2_to_II():
    num = 2
    actual = romanize(num)
    assert actual == 'II'


def test_romanize__should_convert_3_to_III():
    num = 3
    actual = romanize(num)
    assert actual == 'III'


def test_romanize__should_convert_4_to_IV():
    num = 4
    actual = romanize(num)
    assert actual == 'IV'


def test_romanize__should_convert_5_to_V():
    num = 5
    actual = romanize(num)
    assert actual == 'V'


def test_romanize__should_convert_6_to_VI():
    num = 6
    actual = romanize(num)
    assert actual == 'VI'


def test_romanize__should_convert_7_to_VII():
    num = 7
    actual = romanize(num)
    assert actual == 'VII'


def test_romanize__should_convert_8_to_VIII():
    num = 8
    actual = romanize(num)
    assert actual == 'VIII'


def test_romanize__should_convert_9_to_IX():
    num = 9
    actual = romanize(num)
    assert actual == 'IX'


def test_romanize__should_convert_10_to_X():
    num = 10
    actual = romanize(num)
    assert actual == 'X'


def test_romanize__should_convert_14_to_XIV():
    num = 14
    actual = romanize(num)
    assert actual == 'XIV'


def test_romanize__should_convert_19_to_XIX():
    num = 19
    actual = romanize(num)
    assert actual == 'XIX'


def test_romanize__should_convert_24_to_XXIV():
    num = 24
    actual = romanize(num)
    assert actual == 'XXIV'


def test_romanize__should_convert_29_to_XXIX():
    num = 29
    actual = romanize(num)
    assert actual == 'XXIX'


def test_romanize__should_convert_333_to_CCCXXXIII():
    num = 333
    actual = romanize(num)
    assert actual == 'CCCXXXIII'


def test_romanize__should_convert_494_to_CDXCIV():
    num = 494
    actual = romanize(num)
    assert actual == 'CDXCIV'


def test_romanize__should_convert_639_to_DCXXXIX():
    num = 639
    actual = romanize(num)
    assert actual == 'DCXXXIX'


def test_romanize__should_convert_949_to_CMXLIX():
    num = 949
    actual = romanize(num)
    assert actual == 'CMXLIX'


def test_romanize__should_convert_999_to_CMXCIX():
    num = 999
    actual = romanize(num)
    assert actual == 'CMXCIX'


def test_romanize__should_convert_1492_to_MCDXCII():
    num = 1492
    actual = romanize(num)
    assert actual == 'MCDXCII'


def test_romanize__should_convert_1985_to_MCMLXXXV():
    num = 1985
    actual = romanize(num)
    assert actual == 'MCMLXXXV'


def test_romanize__should_convert_2019_to_MMXIX():
    num = 2019
    actual = romanize(num)
    assert actual == 'MMXIX'


def test_romanize__should_convert_4994_to_M_VCMXCIV():
    num = 4994
    actual = romanize(num)
    assert actual == 'M(V)CMXCIV'


def test_romanize__should_convert_7447_to_V_MMCDXLVII():
    num = 7447
    actual = romanize(num)
    assert actual == '(V)MMCDXLVII'


def test_romanize__should_convert_9999_to_M_XCMXCIX():
    num = 9999
    actual = romanize(num)
    assert actual == 'M(X)CMXCIX'


