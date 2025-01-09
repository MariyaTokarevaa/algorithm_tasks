'''Нужно написать функцию, которая на вход принимает строку,
 разбивает её на пары символов и возвращает список таких строковых пар.
Если в изначальной строке нечётное количество элементов, то  недостающим
вторым символ последней пары делаем _.'''

#решение 1
def split_string(string):
    data += '_'
    return [''.join(t) for t in zip(data[::2], data[1::2])]

#решение 2
def solution(s):
    if len(s) == 1:
        return [s+'_']
    if not s:
        return []
    return [s[:2]] + solution(s[2:])

#решение 3
def split_into_pairs(s: str) -> list[str]:
    pairs = []
    length = len(s)

    for i in range(0, length, 2):
        if i + 1 < length:
            pairs.append(s[i:i + 2])
        else:
            pairs.append(s[i] + '_')

    return pairs