from time import perf_counter_ns

filename = "day24_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return tuple(tuple(l.strip().split()) for l in lines)

def extract_vars(instructions):
    vars = []
    v = []
    for inst in instructions:
        if inst[0] == "inp":
            i = 0
        if i == 4:
            v.append(int(inst[2]))
        elif i == 5:
            v.append(int(inst[2]))
        elif i == 15:
            v.append(int(inst[2]))
            vars.append(tuple(v))
            v = []
        i += 1
    return vars

def search(vars, z, num_so_far="", find_highest=True):
    if not vars: # at the end
        return num_so_far if z == 0 else False

    a, b, c = vars[0]

    if a == 26: # dividing by 26 is better than multiplying by 26 ... set new num to ensure this
        assert b < 0
        # need x = 0 -> (z%26 + b) == new_num
        num = z % 26 + b
        if num >= 1 and num <= 9:
            return search(vars[1:], z//26, num_so_far + str(num), find_highest)
    else:
        # no necessary preference, just try them all
        nums_to_check = range(1, 10)
        if find_highest:
            nums_to_check = reversed(nums_to_check)
        for num in nums_to_check:
            assert (z % 26 + b) != num # it can't ... b > 10 always
            new_z = z * 26 + num + c
            ret = search(vars[1:], new_z, num_so_far + str(num), find_highest)
            if ret:
                return ret

    return False

def part1():
    instructions = read()
    vars = extract_vars(instructions)
    print(search(vars, 0))

def part2():
    instructions = read()
    vars = extract_vars(instructions)
    print(search(vars, 0, find_highest=False))


if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    # part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")