def count_neighbor(data, i, j):
    count = 0
    rows = len(data)
    cols = len(data[0])
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ni, nj = i + dx, j + dy
            if 0 <= ni < rows and 0 <= nj < cols:
                count += data[ni][nj]
    return count

def lifegame_rule(cur, neighbor):
    if cur == 1:
        return 1 if 2 <= neighbor <= 3 else 0
    else:
        return 1 if neighbor == 3 else 0

import ita

def lifegame_step(data):
    n, m = len(data), len(data[0])
    new_data = ita.array.make2d(n, m)
    for i in range(n):
        for j in range(m):
            neighbor = count_neighbor(data, i, j)
            new_data[i][j] = lifegame_rule(data[i][j], neighbor)
    return new_data

def lifegame(data, steps):
    results = ita.array.make1d(steps)
    current = data
    for step in range(steps):
        results[step] = current
        current = lifegame_step(current)
    return results

import ita.plot

ani = lifegame(ita.lifegame_glider(), 10)
ita.plot.animation_show(ani)
