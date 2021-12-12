from collections import Counter, defaultdict

filename = "day6_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        line = f.readline()
    return list(map(int, line.strip().split(",")))

def age_fishes(fishes):
    for i in range(len(fishes)):
        fish = fishes[i]
        if fish <= 0:
            fishes[i] = 6
            fishes.append(8)
        else:
            fishes[i] = fish - 1

def part1():
    fishes = read()
    print(fishes)
    for i in range(80):
        age_fishes(fishes)
    print(len(fishes))
    
def part2():
    fishes = read()
    fishes = dict(Counter(fishes))
    print(fishes)
    for i in range(256):
        temp = defaultdict(lambda: 0)
        for age in fishes:
            if age == 0:
                temp[8] += fishes[age]
                temp[6] += fishes[age]
            else:
                temp[age-1] += fishes[age]
        fishes = temp
    print(sum(temp.values()))
    print(temp)

if __name__ == "__main__":
    # part1()
    part2()