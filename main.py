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

# Пример использования
try:
    arabic_number = int(input("Введите арабское число (от 1 до 3999): "))
    roman_number = arabic_to_roman(arabic_number)
    print(f"Римская запись числа {arabic_number}: {roman_number}")
except ValueError as e:
    print(f"Ошибка: {e}")
