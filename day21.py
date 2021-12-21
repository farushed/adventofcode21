from time import perf_counter_ns
import itertools
import functools

filename = "day21_input.txt"
# filename = "example.txt"

class Die:
    def __init__(self, start=1, max_val=100):
        self.value = start
        self.max_val = max_val
        self.rolls = 0
    
    def __repr__(self):
        return f"Die with value {self.value} and {self.rolls} rolls"

    def roll(self):
        prev = self.value
        self.value += 1
        self.rolls += 1
        if self.value > self.max_val:
            self.value -= self.max_val
        return prev
    
    def roll_multiple(self, count):
        sum = 0
        for i in range(count):
            sum += self.roll()
        return sum

class Player:
    def __init__(self, start_pos=1, *, max_pos=10, winning_score=1000):
        self.pos = start_pos
        self.max_pos = max_pos
        self.winning_score = winning_score
        self.score = 0

    def __repr__(self):
        return f"Player at {self.pos} with score {self.score}"
    
    def move(self, steps):
        self.pos += steps
        while self.pos > self.max_pos:
            self.pos -= self.max_pos
        
        self.score += self.pos

        return self.pos
    
    def has_won(self):
        return self.score >= self.winning_score

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [int(l.strip().split(": ")[-1]) for l in lines]

def part1():
    starts = read()
    players = [Player(s) for s in starts]
    die = Die()

    for player in itertools.cycle(players):
        player.move(die.roll_multiple(3))
        if player.has_won():
            break
    
    # print(players, die)
    print(min(p.score for p in players)*die.rolls)

def part2():
    starts = read()

    print(p1_turn(starts[0], 0, starts[1], 0))



@functools.cache
def p1_turn(p1_pos, p1_score, p2_pos, p2_score):
    # if p1_score >= 21:
    #     return 1, 0
    if p2_score >= 21:
        return 0, 1

    wins1, wins2 = 0, 0
    for rolls in itertools.product((1, 2, 3), repeat=3):
        p1_newpos = p1_pos + sum(rolls)
        while p1_newpos > 10: p1_newpos -= 10
        w1, w2 = p2_turn(p1_newpos, p1_score+p1_newpos, p2_pos, p2_score)
        wins1 += w1
        wins2 += w2
    return wins1, wins2

@functools.cache
def p2_turn(p1_pos, p1_score, p2_pos, p2_score):
    if p1_score >= 21:
        return 1, 0
    # if p2_score >= 21:
    #     return 0, 1

    wins1, wins2 = 0, 0
    for rolls in itertools.product((1, 2, 3), repeat=3):
        p2_newpos = p2_pos + sum(rolls)
        while p2_newpos > 10: p2_newpos -= 10
        w1, w2 = p1_turn(p1_pos, p1_score, p2_newpos, p2_score+p2_newpos)
        wins1 += w1
        wins2 += w2
    return wins1, wins2

if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")