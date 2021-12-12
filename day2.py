filename = "day2_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [(l.split()[0], int(l.split()[1])) for l in lines]

def part1():
    steps = read()

    pos, depth = 0, 0
    for dir, val in steps:
        if dir == "forward":
            pos += val
        elif dir == "down":
            depth += val
        elif dir == "up":
            depth -= val
    print(f"pos*depth = {pos*depth}")

def part2():
    steps = read()

    pos, depth, aim = 0, 0, 0
    for dir, val in steps:
        if dir == "forward":
            pos += val
            depth += val*aim
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
    print(f"pos = {pos}\ndepth = {depth}\npos*depth = {pos*depth}")

if __name__ == "__main__":
    # part1()
    part2()