from collections import Counter, defaultdict
import time

filename = "day14_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return lines[0].strip(), [l.strip().split(" -> ") for l in lines[2:]]

def part1():
    start, rules = read()

    start = list(start)
    for idk in range(10):
        mask = [True for c in start]
        for pair, to_insert in rules:
            i = 0
            while i < len(start)-1:
                # if pair == "CB": print(start[-5:], mask[-5:], i, start[i], start[i+1], start[i]==pair[0] and start[i+1]==pair[1])
                if mask[i] and mask[i+1]:
                    if start[i] == pair[0] and start[i+1] == pair[1]:
                        start.insert(i+1, to_insert)
                        mask.insert(i+1, False)
                    # print(start, i, pair)
                i += 1
    counter = Counter(start)
    print(max(counter.values()) - min(counter.values()))
              
def part2():
    start, rules = read()
    first_letter, last_letter = start[0], start[-1]

    zero_pairs = {rule[0]: 0 for rule in rules}
    pairs = zero_pairs.copy()
    for i in range(len(start)-1):
        pairs[start[i:i+2]] += 1

    new_pair_rules = zero_pairs.copy()
    for rule in rules:
        new_pair_rules[rule[0]] = rule[0][0]+rule[1], rule[1]+rule[0][1]

    for idk in range(100000):
        new_pairs = zero_pairs.copy()
        for rule in new_pair_rules:
            num = pairs[rule]
            if num > 0:
                new_pairs[new_pair_rules[rule][0]] += num
                new_pairs[new_pair_rules[rule][1]] += num
        pairs = new_pairs

    freqs = defaultdict(lambda: 0)
    freqs[first_letter], freqs[last_letter] = -1, -1
    for el, freq in pairs.items():
        freqs[el[0]] += freq
        freqs[el[1]] += freq
    freqs = {a: b//2 for a, b in freqs.items()}
    freqs[first_letter] += 1
    freqs[last_letter] += 1

    print(max(freqs.values()) - min(freqs.values()))


if __name__ == "__main__":
    start = time.perf_counter()
    # part1() # leaving the brute force here, but doing part2() with a range(10) in the loop will be *much* faster
    part2()
    end = time.perf_counter()
    print(f"{end-start} seconds taken")