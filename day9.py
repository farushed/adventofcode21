import operator, functools

filename = "day9_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [list(map(int, list(line.strip()))) for line in lines]

def part1():
    rows = read()

    sum = 0
    for y, row in enumerate(rows):
        for x, el in enumerate(row):
            top = rows[y-1][x] if y > 0 else 10
            bottom = rows[y+1][x] if y < len(rows)-1 else 10
            left = rows[y][x-1] if x > 0 else 10
            right = rows[y][x+1] if x < len(row)-1 else 10
            # if min(el, top, bottom, left, right) == el:
            if el < top and el < bottom and el < left and el < right:
                sum += el + 1
    print(sum)

def further_neighbours(rows, x, y, prev = set()):
    if rows[y][x] == 9:
        return 0, prev

    prev.add((x,y))
    sum = 1
    for nx, ny in ((x, y+1), (x, y-1), (x+1, y), (x-1, y)):
        if (nx,ny) in prev or rows[ny][nx] == 9:
            continue
        fs, fp = further_neighbours(rows, nx, ny, prev)
        sum += fs
    return sum, prev


def part2():
    rows = read()

    # pad around with 9s so we don't have to check for edges
    rows = [[9] + [el for el in row] + [9] for row in rows]
    rows.insert(0, [9]*len(rows[0]))
    rows.append([9]*len(rows[0]))

    all_prev = set()
    basins = []

    for y in range(len(rows)):
        for x in range(len(rows[y])):
            if (x, y) not in all_prev and rows[y][x] != 9:
                s, p = further_neighbours(rows, x, y)
                basins.append(s)
                all_prev.union(p)

    # print(sorted(basins))
    print(functools.reduce(operator.mul, sorted(basins)[-3:]))

if __name__ == "__main__":
    # part1()
    part2()
    