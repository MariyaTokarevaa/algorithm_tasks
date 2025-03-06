import time

def get_nod(a, b):
    '''функция нахождения наибольшего общего делителя (НОД) для двух натуральных чисел a и b.
    алгоритм Евклида'''
    while a !=  b:
        if a > b:
            a-=b
        else:
            b-=a
    return a

#print('НОД =', get_nod(int(input('a = ')), int(input('b = '))))


def test_nod(func):
    '''Тестируем функцию на корректность работы'''
    a=28
    b=35
    res = func(a,b)
    if res == 7:
        print('#test 1 - ok')
    else:
        print('#test 1 - fail')

    '''ТЕСТ2'''
    a=100
    b=1
    res = func(a,b)
    if res == 1:
        print('#test 2 - ok')
    else:
        print('#test 2 - fail')

    '''ТЕСТ3'''
    a=2
    b=1000
    st=time.time()
    res = func(a,b)
    et=time.time()
    dt=et-st
    if res == 2 and dt<1:
        print('#test 3 - ok')
    else:
        print('#test 3 - fail')


#   test_nod(get_nod)

def fast_get_nod(a,b):
    '''Быстрое вычисление НОД для чисел а и b'''
    if a<b:
        a,b=b,a
    while b>0:
        a,b=b,a%b
    return a

# test_nod(fast_get_nod)