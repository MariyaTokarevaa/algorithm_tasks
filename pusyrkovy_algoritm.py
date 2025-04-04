'''Вот идея алгоритма сортировки всплывающего пузырька. Реализуйте его для вводимого списка целых чисел.
Результат выведите на экран в виде последовательности чисел, записанных в одну строчку через пробел.

На вход программе подаются целые числа, записанные в одну строку через пробел.
Необходимо их прочитать и сохранить в списке. Затем, выполнить сортировку полученного списка по возрастанию (неубыванию) методом всплывающего пузырька.
Идея алгоритма проста и показана на рисунке ниже'''

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr