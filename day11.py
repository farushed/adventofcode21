filename = "day11_input.txt"
# filename = "example.txt"


def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [list(map(int, list(line.strip()))) for line in lines]

def flash(grid, y, x):
    new = 0
    if grid[y][x] > 9:
        new += 1
        grid[y][x] = 0
        if x > 0:
            grid[y][x-1] += 1 if grid[y][x-1] != 0 else 0
            new += flash(grid, y, x-1)
        if x < len(grid[y])-1:
            grid[y][x+1] += 1 if grid[y][x+1] != 0 else 0
            new += flash(grid, y, x+1)
        if y > 0:
            grid[y-1][x] += 1 if grid[y-1][x] != 0 else 0
            new += flash(grid, y-1, x)
        if y < len(grid)-1:
            grid[y+1][x] += 1 if grid[y+1][x] != 0 else 0
            new += flash(grid, y+1, x)
            
        if x > 0 and y > 0:
            grid[y-1][x-1] += 1 if grid[y-1][x-1] != 0 else 0
            new += flash(grid, y-1, x-1)
        if x < len(grid[y])-1 and y < len(grid)-1:
            grid[y+1][x+1] += 1 if grid[y+1][x+1] != 0 else 0
            new += flash(grid, y+1, x+1)
        if x < len(grid[y])-1 and y > 0:
            grid[y-1][x+1] += 1 if grid[y-1][x+1] != 0 else 0
            new += flash(grid, y-1, x+1)
        if x > 0 and y < len(grid)-1:
            grid[y+1][x-1] += 1 if grid[y+1][x-1] != 0 else 0
            new += flash(grid, y+1, x-1)
    return new

def part1():
    grid = read()

    total_flashes = 0
    for i in range(100):
        for y, row in enumerate(grid):
            for x, el in enumerate(row):
                grid[y][x] += 1

        for y, row in enumerate(grid):
            for x, el in enumerate(row):
                total_flashes += flash(grid, y, x)
    print(total_flashes)

def part2():
    grid = read()

    i = 1
    finished = False
    while not finished:
        for y, row in enumerate(grid):
            for x, el in enumerate(row):
                grid[y][x] += 1

        for y, row in enumerate(grid):
            for x, el in enumerate(row):
                flashes = flash(grid, y, x)
                if flashes == 100:
                    print(i, grid)
                    finished = True
        i += 1
                

if __name__ == "__main__":
    # part1()
    part2()