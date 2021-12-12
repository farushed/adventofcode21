from collections import defaultdict


filename = "day3_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return len(lines[0]), [int(l, 2) for l in lines]

def part1():
    bits, nums = read()

    freqs  = defaultdict(lambda: 0)
    for num in nums:
        i = 0
        while num > 0:
            freqs[i] += num & 0b1
            num = num >> 1
            i += 1
    print(freqs.items())
    gamma = 0
    epsilon = 0
    for bit, freq in freqs.items():
        if freq >= len(nums)/2:
            gamma += 0b1 << bit
        else:
            epsilon += 0b1 << bit
    # print(bin(gamma), bin(epsilon))
    print(gamma*epsilon)

def part2():
    with open(filename, "r") as f:
        lines = f.readlines()
    # oxygen
    freqs = defaultdict(lambda: 0)
    i = 0
    while len(lines) > 1:
        for l in lines:
            if l[i] == "1":
                freqs[i] += 1
        val = "1" if freqs[i] >= len(lines)/2 else "0"
        lines = list(filter(lambda l: l[i] == val, lines))
        i += 1
    print(lines)
    oxy = int(lines[0], 2)


    with open(filename, "r") as f:
        lines = f.readlines()
    # co2
    freqs = defaultdict(lambda: 0)
    i = 0
    while len(lines) > 1:
        for l in lines:
            if l[i] == "0":
                freqs[i] += 1
        val = "0" if freqs[i] <= len(lines)/2 else "1"
        lines = list(filter(lambda l: l[i] == val, lines))
        i += 1
    print(lines)
    co2 = int(lines[0], 2)

    print(oxy, co2, oxy*co2)
    


if __name__ == "__main__":
    # part1()
    part2()