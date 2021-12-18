from time import perf_counter_ns
from dataclasses import dataclass
from itertools import chain, permutations
from copy import deepcopy

filename = "day18_input.txt"
# filename = "example.txt"

@dataclass
class Element:
    value: int
    level: int

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [l.strip() for l in lines]

def explode(snum: list[Element]) -> bool:
    prev_el = None
    for i, el in enumerate(snum):
        if prev_el is None:
            prev_el = el
            continue
        if el.level == prev_el.level and el.level > 4:
            if i-2 >= 0:
                snum[i-2].value += prev_el.value
            snum[i-1] = Element(0, prev_el.level -1)
            if i+1 < len(snum):
                snum[i+1].value += el.value
            del snum[i]
            return True
        prev_el = el
    return False

def split(snum: list[Element]) -> bool:
    for i, el in enumerate(snum):
        val = el.value
        if val >= 10:
            new_level = el.level + 1
            snum[i] = Element(val//2, new_level)
            snum.insert(i+1, Element(int(val/2+0.5), new_level))
            return True
    return False
    
def reduce(snum: list[Element]):
    reduced = False
    while not reduced:
        if explode(snum):
            continue
        if split(snum):
            continue
        reduced = True

def print_as_list(snum: list[Element]):
    bracket_level = 0
    first = True
    for el in snum:
        while bracket_level > el.level:
            print(']', end='')
            bracket_level -= 1
        if not first: print(',', end='')
        else: first = False
        while bracket_level < el.level:
            print('[', end='')
            bracket_level += 1
        print(el.value, end='')
    while bracket_level > 0:
        print(']', end='')
        bracket_level -= 1
    print('\n')

def read_snum(line: str) -> list[Element]:
    level = 0
    snum = []
    for c in line:
        if c == '[':
            level += 1
        elif c == ']':
            level -= 1
        elif c.isnumeric():
            snum.append(Element(int(c), level))
    return snum

def add_snums(snum1: list[Element], snum2: list[Element]) -> list[Element]:
    if not snum1: return snum2
    if not snum2: return snum1

    result = []
    for el in chain(deepcopy(snum1), deepcopy(snum2)):
        el.level += 1
        result.append(el)

    reduce(result)

    return result

def magnitude(snum: list[Element]) -> int:
    snum = deepcopy(snum)
    while len(snum) > 1:
        prev_el = None
        for i, el in enumerate(snum):
            if prev_el is None:
                prev_el = el
                continue
            if el.level == prev_el.level:
                prev_el.level -= 1
                prev_el.value = prev_el.value * 3 + el.value * 2
                del snum[i]
                break
            prev_el = el
    return snum[0].value

def part1():
    lines = read()

    total = []
    for line in lines:
        snum = read_snum(line)
        total = add_snums(total, snum)
    # print_as_list(total)
    print(magnitude(total))

def part2():
    lines = read()

    snums = []
    for line in lines:
        snum = read_snum(line)
        snums.append(snum)

    max = 0
    for snum1, snum2 in permutations(snums, 2):
        total = add_snums(snum1, snum2)
        mag = magnitude(total)
        if mag > max: max = mag
    print(max)

if __name__ == "__main__":
    start = perf_counter_ns()

    print("Part 1:")
    part1()
    print("Part 2:")
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")