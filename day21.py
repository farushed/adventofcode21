from time import perf_counter_ns
import itertools, functools
from collections import Counter

filename = "day21_input.txt"
# filename = "example.txt"

possible_rolls = Counter(sum(r) for r in itertools.product((1, 2, 3), repeat=3))

@functools.cache
def play(p1_pos, p1_score, p2_pos, p2_score):
    if p1_score >= 21:
        return 1, 0
    if p2_score >= 21:
        return 0, 1

    wins1, wins2 = 0, 0
    for roll, freq in possible_rolls.items():
        p1_newpos = p1_pos + roll
        while p1_newpos > 10: p1_newpos -= 10
        w2, w1 = play(p2_pos, p2_score, p1_newpos, p1_score+p1_newpos)
        wins1 += w1 * freq
        wins2 += w2 * freq
    return wins1, wins2

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [int(l.strip().split(": ")[-1]) for l in lines]

def part1():
    players = [[pos, 0] for pos in read()]
    die_val = 1
    rolls = 0

    for player in itertools.cycle(players):
        steps = 0
        for _ in range(3):
            steps += die_val
            die_val += 1
            rolls += 1
            if die_val > 100: die_val -= 100

        new_pos = player[0] + steps
        while new_pos > 10: new_pos -= 10
        player[0] = new_pos
        player[1] += new_pos
        if player[1] >= 1000:
            break
    
    print(min(p[1] for p in players)*rolls)

def part2():
    starts = read()

    print(play(starts[0], 0, starts[1], 0))

if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")