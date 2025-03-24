from collections import Counter
'''Имеется список целых чисел. Нужно написать функцию, которая попарно будет удалять одинаковые числа из списка (либо его копии) и вернёт кортеж вида (pair_count, alone_count), где

🔸pair_count — количество удаленных дублей
🔸alone_count — количество оставшихся элементов 
'''


def count_pairs(nums):
    pair_count = sum(count // 2 for count in Counter(nums).values())
    alone_count = sum(count % 2 for count in Counter(nums).values())
    return pair_count, alone_count