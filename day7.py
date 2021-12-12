filename = "day7_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        line = f.readline()
    return list(map(int, line.strip().split(",")))

def each_distance(list_of_positions, position):
    return [abs(position - pos) for pos in list_of_positions]

def weighted_distance(p1, p2):
    n = abs(p1-p2)
    return int(n*(n+1)/2)

def part1():
    positions = read()
    
    fuel = dict()
    for p in range(min(positions), max(positions)+1):
        fuel[p] = sum(each_distance(positions, p))
    print(sorted(fuel.items(), key=lambda x: x[1])[0])

def part2():
    positions = read()
    
    # could most likely just check between avg-std, avg+std, or even less
    # but brute force doesn't take too long
    fuel = dict()
    for p in range(min(positions), max(positions)+1):
        # fuel[p] = sum(each_weighted_distance(positions, p))
        fuel[p] = sum([weighted_distance(p, pos) for pos in positions])
    print(sorted(fuel.items(), key=lambda x: x[1])[0])

if __name__ == "__main__":
    # part1()
    # part2()
    
    # a oneliner for part 2 because why not
    with open("day7_input.txt", "r") as f: print(min((lambda ps: [sum(map(lambda x: int(abs(x-p)*(abs(x-p)+1)/2), ps)) for p in range(min(ps), max(ps)+1)])(list(map(int, f.readline().split(","))))))
    