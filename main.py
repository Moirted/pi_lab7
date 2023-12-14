import unittest


def arabic_to_roman(number):
    if not 1 <= number <= 3999:
        raise ValueError("Число должно быть в диапазоне от 1 до 3999 включительно")

    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_numeral = ''
    for value, numeral in roman_numerals.items():
        while number >= value:
            roman_numeral += numeral
            number -= value

    return roman_numeral


class TestArabicToRoman(unittest.TestCase):

    def test_valid_arabic_numbers(self):
        test_cases = {
            1: 'I',
            4: 'IV',
            9: 'IX',
            21: 'XXI',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            3999: 'MMMCMXCIX'
        }

        for arabic, roman in test_cases.items():
            with self.subTest(arabic=arabic, roman=roman):
                self.assertEqual(arabic_to_roman(arabic), roman)

    def test_invalid_arabic_number(self):
        with self.assertRaises(ValueError) as context:
            arabic_to_roman(0)
        self.assertEqual(str(context.exception), "Число должно быть в диапазоне от 1 до 3999 включительно")

        with self.assertRaises(ValueError) as context:
            arabic_to_roman(4000)
        self.assertEqual(str(context.exception), "Число должно быть в диапазоне от 1 до 3999 включительно")

    def test_large_arabic_number(self):
        arabic_number = 2023
        roman_number = arabic_to_roman(arabic_number)
        self.assertEqual(roman_number, 'MMXXIII')

    def test_random_arabic_numbers(self):
        test_cases = {
            3998: 'MMMCMXCVIII',
            25: 'XXV',
            888: 'DCCCLXXXVIII',
            369: 'CCCLXIX'
        }

        for arabic, roman in test_cases.items():
            with self.subTest(arabic=arabic, roman=roman):
                self.assertEqual(arabic_to_roman(arabic), roman)


if __name__ == '__main__':
    unittest.main()
"""
    try:
        # arabic_number = int(input("Введите арабское число (от 1 до 3999): "))
        roman_number = arabic_to_roman(55)
        print(f"Римская запись числа {55}: {roman_number}")
    except ValueError as e:
        print(f"Ошибка: {e}")
"""
