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
    # start, rules = read()
    
    # start = list(start)
    # for idk in range(10):
    #     mask = [True for c in start]
    #     insertions = []
    #     for pair, to_insert in rules:
    #         i = 0
    #         while i < len(start)-1:
    #             if start[i] == pair[0] and start[i+1] == pair[1]:
    #                 new_index = i+1
    #                 for insertion in insertions:
    #                     if insertion[0] < new_index:
    #                         new_index += 1
    #                 for insertion in insertions:
    #                     if insertion[0] > new_index:
    #                         insertion[0] += 1
    #                 insertions.append([new_index, to_insert])
    #             # if mask[i] and mask[i+1]:
    #             #     if start[i] == pair[0] and start[i+1] == pair[1]:
    #             #         start.insert(i+1, to_insert)
    #             #         mask.insert(i+1, False)
    #                 # print(start, i, pair)
    #             i += 1
    #     # print(start)
    #     # print(insertions)
    #     for insertion in sorted(insertions, key=lambda x:x[0]):
    #         start.insert(insertion[0], insertion[1])
    # # print(start)
    # counter = Counter(start)
    # print(max(counter.values()) - min(counter.values()))  

    start, rules = read()
    chain = defaultdict(lambda: 0)
    for i in range(len(start)-1):
        chain[start[i:i+2]] += 1

    rules_d = dict()
    for rule in rules:
        rules_d[rule[0]] = str(rule[0][0] + rule[1]), str(rule[1] + rule[0][1])
    # print(rules_d)
    # print(chain)


    for idk in range(80):
        new_chain = defaultdict(lambda: 0)
        for rule in rules_d:
            if chain[rule] > 0:
                num = chain[rule]
                # chain[rule] = 0
                new_chain[rules_d[rule][0]] += num
                new_chain[rules_d[rule][1]] += num
        chain = new_chain

    # print(sum(new_chain.values()))
    freqs = defaultdict(lambda: 0)
    freqs[start[0]] = -1
    freqs[start[-1]] = -1
    for el, freq in chain.items():
        freqs[el[0]] += freq
        freqs[el[1]] += freq
    freqs = {a: b//2 + (1 if a in [start[0], start[-1]] else 0) for a, b in freqs.items()}
    print(max(freqs.values()) - min(freqs.values()))


if __name__ == "__main__":
    start = time.perf_counter()
    # part1()
    part2()
    end = time.perf_counter()
    print(f"{end-start} seconds taken")