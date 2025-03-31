N = 7
P = []

for i in range(0, N):
    row = [1] * (i + 1)
    for j in range(i + 1):
        if j != 0 and j != i:
            row[j] = P[i - 1][j - 1] + P[i - 1][j]

    P.append(row)

for r in P:
    print(r)

#второе решение задачи
def pascal_triangle(num_rows):
    if num_rows <= 0:
        print("Должна быть минимум одна строка")
        return

    # Вычислим последнюю строку для определения ширины
    last_row_calc = [1]
    for _ in range(num_rows - 1):
        last_row_calc = [sum(pair) for pair in zip([0] + last_row_calc, last_row_calc + [0])]

    max_width = len(" ".join(map(str, last_row_calc)))

    # Генерируем и печатаем строки
    row = [1]
    for _ in range(num_rows):
        row_str = " ".join(map(str, row))
        # Печатаем строку, центрируя её
        print(row_str.center(max_width))
        row = [sum(pair) for pair in zip([0] + row, row + [0])]
