'''Функция на вход должна принимать список чисел и возвращать True,
если список можно переупорядочить так, что он станет арифметической прогрессией
(во всех остальных случаях — False).

Арифметическая прогрессия — такая последовательность,
в которой разница между любыми двумя последовательными элементами одинакова.'''

def arithmetic_progress(arr):
    n = len(arr)
    if n <= 1:
        return True
    min_val, max_val = min(arr), max(arr)
    if min_val == max_val:
        return True
    if (max_val - min_val) % (n - 1) != 0:
        return False
    d = (max_val - min_val) // (n - 1)
    elements = set(arr)
    for i in range(n):
        if (min_val + i * d) not in elements:
            return False
    return True