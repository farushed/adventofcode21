from time import perf_counter_ns

filename = "day17_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        line = f.readline()
    # return line.split(":")[1].split(", ")
    return [[int(c) for c in h.split("..")] for h in (line[line.index("x=")+2: line.index(", ")], line[line.index("y=")+2:])]

def part1():
    (xmin, xmax), (ymin, ymax) = read()
    # print(xmin, xmax, ymin, ymax)

    all_maxima = []
    # for yvel in range(0):
    orig_yvel = 0
    missed = 0
    while missed != 100:
        orig_yvel += 1
        ypos = 0
        # yvel = 1
        yvel = orig_yvel

        maxima = 0

        # for step in range(100):
        while True:
            ypos += yvel
            yvel -= 1
            if ypos > maxima:
                maxima = ypos

            if ypos >= ymin and ypos <= ymax:
                print(f"target reached with {ypos=} {yvel=} {orig_yvel=}")
                all_maxima.append((orig_yvel, maxima))
                break
            elif ypos < ymin:
                print(f"target missed with {ypos=} {yvel=} {orig_yvel=}")
                missed += 1
                break
            # print(ypos, yvel, ymin, ymax)

    print(sorted(all_maxima, key=lambda x: x[1], reverse=True))

def part2():
    (xmin, xmax), (ymin, ymax) = read()
    # print(xmin, xmax, ymin, ymax)

    y_that_reach = []
    # for yvel in range(0):
    orig_yvel = ymin
    missed = 0
    while missed != 100:
        ypos = 0
        yvel = orig_yvel

        while True:
            ypos += yvel
            yvel -= 1

            if ypos >= ymin and ypos <= ymax:
                # print(f"target reached with {ypos=} {yvel=} {orig_yvel=}")
                y_that_reach.append(orig_yvel)
                break
            elif ypos < ymin:
                # print(f"target missed with {ypos=} {yvel=} {orig_yvel=}")
                missed += 1
                break

        orig_yvel += 1

    # print(y_that_reach)
    initial_vels_that_reach = []

    for orig_yvel in y_that_reach:
        for orig_xvel in range(xmax+1):
            xpos, ypos = 0, 0
            xvel, yvel = orig_xvel, orig_yvel
            while True:
                ypos += yvel
                yvel -= 1
                xpos += xvel
                if xvel > 0: xvel -= 1

                if ypos >= ymin and ypos <= ymax and xpos >= xmin and xpos <= xmax:
                    # print(f"{orig_xvel=} {orig_yvel=}")
                    initial_vels_that_reach.append((orig_xvel, orig_yvel))
                    break
                elif xpos > xmax or ypos < ymin:
                    # print(f"target missed with {ypos=} {yvel=} {orig_yvel=}")
                    # missed += 1
                    break
    print(len(initial_vels_that_reach))

if __name__ == "__main__":
    start = perf_counter_ns()

    # part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")