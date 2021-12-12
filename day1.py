filename = "day1_input.txt"
# filename = "example.txt"

def part1():
    with open(filename, "r") as f:
        readings = [int(l) for l in f.readlines()]
    amount = 0
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            amount += 1
    print(amount)

def part2():
    with open(filename, "r") as f:
        readings = [int(l) for l in f.readlines()]
    amount = 0
    for i in range(0, len(readings) - 3):
        # print(f"{readings[i+1:i+4]} {readings[i:i+3]}")
        # print(f"{sum(readings[i+1:i+4])} {sum(readings[i:i+3])}")
        if sum(readings[i+1:i+4]) > sum(readings[i:i+3]):
            amount += 1
    print(amount)

if __name__ == "__main__":
    # part1()
    part2()