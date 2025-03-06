'''На улице равномерно выстроены n домов, а каждый дом раскрашен в определённый цвет.
Нам дан список цветов colors, где colors[i] представляет собой цвет i-го дома.

Нужно найти максимальное расстояние между двумя домами с разными цветами.'''


def max_distance_optimized(colors):
    n = len(colors)
    if n < 2:
        return 0

    color_start = colors[0]
    color_end = colors[-1]
    max_dist = 0

    for i, current_color in enumerate(colors):
        if current_color != color_start:
            max_dist = max(max_dist, i)

        if current_color != color_end:
            max_dist = max(max_dist, n - 1 - i)

    return max_dist