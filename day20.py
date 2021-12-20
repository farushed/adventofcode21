from time import perf_counter_ns
import itertools

filename = "day20_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    algorithm = lines[0]
    assert lines[1] == '\n'

    image_points = set()
    j = 0
    for line in lines[2:]:
        i = 0
        for ch in line.strip():
            if ch == '#':
                image_points.add((i, j))
            i += 1
        j += 1
    return algorithm, image_points

def print_image(points: set):
    xmin, *_, xmax = sorted((p[0] for p in points))
    ymin, *_, ymax = sorted((p[1] for p in points))
    for j in range(ymin-2, ymax+3):
        for i in range(xmin-2, xmax+3):
            if (i, j) in points:
                print('#', end='')
            else:
                print('.', end='')
        print()

def part1(steps=2):
    algorithm, image = read()

    # print_image(image)

    at_infty = False

    # xmin, *_, xmax = sorted((p[0] for p in image))
    # ymin, *_, ymax = sorted((p[1] for p in image))
    xmin = min(p[0] for p in image)
    xmax = max(p[0] for p in image)
    ymin = min(p[1] for p in image)
    ymax = max(p[1] for p in image)
    for i in range(steps):
        new_image = set()
        for i, j in itertools.product(range(xmin-2, xmax+3), range(ymin-2, ymax+3)):
            num = 0
            for n, (y, x) in enumerate(itertools.product(range(j+1, j-2, -1), range(i+1, i-2, -1))):
                if x >= xmax+1 or x <= xmin-1 or y >= ymax+1 or y <= ymin-1:
                    if at_infty: num += 2**n
                else:
                    if (x, y) in image: num += 2**n
            if algorithm[num] == '#':
                new_image.add((i,j))
        at_infty = algorithm[-1 if at_infty else 0] == '#'
        image = new_image
        # could find min and max every step but this is probably faster
        xmin -= 1
        xmax += 1
        ymin -= 1
        ymax += 1
        # print_image(image)
    print(len(image))

def part2():
    part1(steps=50)

if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")