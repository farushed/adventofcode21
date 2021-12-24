from time import perf_counter_ns
import re
import itertools

filename = "day22_input.txt"
# filename = "example.txt"

class Cuboid:
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax):
        self.xmin = xmin
        self.ymin = ymin
        self.zmin = zmin
        self.xmax = xmax
        self.ymax = ymax
        self.zmax = zmax

        self.off = []

    def __repr__(self):
        attrs = ", ".join(str(getattr(self, a+b)) for a, b in itertools.product("xyz", ("min", "max")))
        return f"<{self.__class__.__name__} object; {attrs}>"
    
    def get_volume(self):
        vol = (self.xmax - self.xmin) * (self.ymax - self.ymin) * (self.zmax - self.zmin)

        for c in self.off:
            vol -= c.get_volume()
        return vol
    
    def subtract(self, other):
        if (i:= intersection(self, other)):
            for c in self.off:
                c.subtract(other)
            self.off.append(i)


def line_intersection(x1, x2, x1_, x2_):
    assert x1 <= x2 and x1_ <= x2_, f"{x1=} {x2=} {x1_=} {x2_=}"
    
    if x2 < x1_ or x2_ < x1:
        return False
    
    return max(x1_, x1), min(x2_, x2)

def intersection(c1, c2):
    x = line_intersection(c1.xmin, c1.xmax, c2.xmin, c2.xmax)
    y = line_intersection(c1.ymin, c1.ymax, c2.ymin, c2.ymax)
    z = line_intersection(c1.zmin, c1.zmax, c2.zmin, c2.zmax)

    if all((x, y, z)):
        return Cuboid(*x, *y, *z)
    
    return False

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    
    steps = []
    for line in lines:
        on = line.split()[0] == "on"
        matches = [int(m) + i%2 for i, m in enumerate(re.findall(r"(-?\d+)", line))]
        steps.append(tuple([on, matches]))
    return steps

def part2():
    steps = read()
    positive = []
    for on, coords in steps:
        c = Cuboid(*coords)

        for p in positive:
            p.subtract(c)

        if on:
            positive.append(c)
        
    vol = sum(c.get_volume() for c in positive)
    print(vol)


if __name__ == "__main__":
    start = perf_counter_ns()

    # part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")