'''На вход подаётся последовательность чисел.
Необходимо определить, какое минимальное количество и каких чисел нужно дописать в конец последовательности,
 чтобы она стала симметричной.
 Функция, таким образом, должна возвращать число (количество чисел) и список (какие именно числа).

🔄 Симметричная последовательность — это такая последовательность,
которая читается одинаково справа налево и слева направо. '''


def make_symmetric(seq):
    """
    Находит, что добавить в конец seq, чтобы она стала палиндромом.

    Returns:
        tuple: (количество_элементов_для_добавления, список_элементов)
    """
    n = len(seq)
    # Итерируем по всем возможным точкам начала "хвоста"
    for i in range(n):
        # Проверяем, является ли текущий "хвост" (seq[i:]) палиндромом
        if seq[i:] == seq[i:][::-1]:
            # Если хвост - палиндром, значит, нам нужно добавить
            # перевернутую "голову" (все, что было ДО хвоста)
            head_to_add_reversed = seq[:i][::-1]
            return len(head_to_add_reversed), head_to_add_reversed
    return 0, []
