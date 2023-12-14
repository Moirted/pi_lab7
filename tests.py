import unittest
import main


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
                self.assertEqual(main.arabic_to_roman(arabic), roman)

    def test_invalid_arabic_number(self):
        with self.assertRaises(ValueError) as context:
            main.arabic_to_roman(0)
        self.assertEqual(str(context.exception), "Число должно быть в диапазоне от 1 до 3999 включительно")

        with self.assertRaises(ValueError) as context:
            main.arabic_to_roman(4000)
        self.assertEqual(str(context.exception), "Число должно быть в диапазоне от 1 до 3999 включительно")

    def test_large_arabic_number(self):
        arabic_number = 2023
        roman_number = main.arabic_to_roman(arabic_number)
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
                self.assertEqual(main.arabic_to_roman(arabic), roman)
