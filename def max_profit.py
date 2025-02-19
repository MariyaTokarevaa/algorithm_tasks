'''Необходимо написать функцию, которая будет определять наиболее "выгодную сделку" по акциям.
На вход подаётся список чисел.
Каждое число представляет собой цену акции, числа расположены в хронологическом порядке изменения цен.

↩️Функция должна возвращать кортеж из трёх чисел – 2 индекса
(элементов-цен покупки и продажи для наиболее выгодной сделки)
и выручку (разницу между ценой продажи и покупки).

😟Если прибыльная сделка невозможна, то кортеж должен содержать одно число – 0.'''

def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    buy = sell = min_index = 0
    for i, price in enumerate(prices):
        if price < min_price:
            min_price, min_index = price, i
        elif price - min_price > max_profit:
            max_profit = price - min_price
            buy, sell = min_index, i
    return (buy, sell, max_profit) if max_profit else (0,)
