'''Представьте, что у вас есть "таблица" accounts, где:  accounts[i][j] — это сумма,
которую некий j-й клиент имеет на счете в i-м банке.

Ваша задача — найти самый "богатого" клиента, то есть "столбец" с максимальной суммой всех счетов.

🎯 Задача:
Напишите функцию find_richest(accounts: list[list[int]]) -> int,
которая принимает таблицу accounts и возвращает максимальную сумму по столбцам.

Пример:
accounts = [[1, 2, 5], [3, 6, 1]]

Разберем этот случай:
*  Сумма accounts[0][0] + accounts[1][0] = 1 + 3 = 4.
*  Сумма accounts[0][1] + accounts[1][1] = 2 + 6 = 8.
*  Сумма accounts[0][2] + accounts[1][2] = 5 + 1 = 6.

Самый богатый клиент имеет состояние 8.
➡️ Ваша функция для [[1,2,5],[3,6,1]] должна вернуть 8.

Еще пример:
accounts = [[10, 5, 100], [20, 15, 0]]
*   Портфель 0: 10 + 20 = 30
*   Портфель 1: 5 + 15 = 20
*   Портфель 2: 100 + 0 = 100
Результат: 100'''


def find_richest(accounts: list[list[int]]) -> int:
    if not accounts or not accounts[0]:
        return 0

    num_clients = len(accounts[0])
    max_wealth = 0

    for client_index in range(num_clients):
        current_client_wealth = 0
        for bank_account in accounts:
            current_client_wealth += bank_account[client_index]

        if current_client_wealth > max_wealth:
            max_wealth = current_client_wealth

    return max_wealth
