from time import perf_counter_ns
from copy import deepcopy

filename = "day25_input.txt"
# filename = "example.txt"

class Seafloor:
    def __init__(self, map):
        self.map = map
        assert all(len(r) == len(map[0]) for r in map)
        self.xmax = len(map[0])-1
        self.ymax = len(map)-1

    def step(self):
        # horribly inefficient but sure
        modified = False
        new_map = deepcopy(self.map)
        for x in range(len(self.map[0])):
            for y in range(len(self.map)):
                nx = x + 1
                if nx > self.xmax:
                    nx = 0
                if self.map[y][x] == '>' and self.map[y][nx] == '.':
                    new_map[y][x] = '.'
                    new_map[y][nx] = '>'
                    modified = True
        self.map = new_map

        new_map = deepcopy(self.map)
        for y in range(len(self.map)):
            for x in range(len(self.map[0])):
                ny = y + 1
                if ny > self.ymax:
                    ny = 0
                if self.map[y][x] == 'v' and self.map[ny][x] == '.':
                    new_map[y][x] = '.'
                    new_map[ny][x] = 'v'
                    modified = True
        self.map = new_map

        return modified

    def __str__(self):
        return "\n".join("".join(r) for r in self.map)


def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [list(l.strip()) for l in lines]

def part1():
    map = read()
    s = Seafloor(map)
    print(s)

    step_num = 0
    while s.step():
        step_num += 1
    print(s)
    print(step_num+1)

def part2():
    pass # :)

if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    # part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")