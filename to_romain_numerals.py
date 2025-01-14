''' напишите функцию,
которая на вход принимает любое целое число и
возвращает его в римском представлении (как строку).'''
def roman_to_integer(s):
    # Словарь для сопоставления римских цифр с их значениями
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Проходим по строке римской цифры с конца к началу
    for char in reversed(s):
        current_value = roman_dict[char]
        
        # Если текущее значение меньше предыдущего, вычитаем его
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        # Обновляем предыдущее значение
        prev_value = current_value
    
    return total

# Пример использования
roman_numeral = input()
result = roman_to_integer(roman_numeral)
print(result) 


