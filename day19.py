from time import perf_counter_ns
import re
import itertools
import numpy as np

filename = "day19_input.txt"
# filename = "example.txt"

def xrot3(angle):
    angle = np.radians(angle)
    c, s = np.cos(angle), np.sin(angle)
    return np.array(((1, 0, 0), (0, c, -s), (0, s, c)))

def yrot3(angle):
    angle = np.radians(angle)
    c, s = np.cos(angle), np.sin(angle)
    return np.array(((c, 0, s), (0, 1, 0), (-s, 0, c)))

def zrot3(angle):
    angle = np.radians(angle)
    c, s = np.cos(angle), np.sin(angle)
    return np.array(((c, -s, 0), (s, c, 0), (0, 0, 1)))

class Scanner:
    def __init__(self, id: int, beacons: list[tuple[int]]):
        self.id = id
        self.beaconsset = set(beacons)
        self.beacons = np.array(beacons)
        self.absolute_pos = np.zeros(3, int) if id == 0 else None
        self.absolute_rot = np.zeros(3, int) if id == 0 else None
        self.rot_mat = np.eye(3, dtype=int) if id == 0 else None
        self.located = True if id == 0 else False
    
    def __repr__(self):
        return f"<{self.__class__.__name__} object; id={self.id} len(beacons)={len(self.beacons)} " \
            + f"located={self.located} position={self.absolute_pos} rotation={self.absolute_rot}>"
    
    def update_pos_rot(self, pos, rot, rot_mat):
        self.absolute_pos = pos
        self.absolute_rot = rot
        self.rot_mat = rot_mat
        self.located = True

    def intersect(self, other):
        # so far works on ones we know
        if not self.located:
            return False
        if other.located:
            return True

        # hack because i just can't
        # product will return loads of repeats, but i only want unique rotation matrices
        # could do something clever - or just store string representations in a set
        rots = set()
        for ax, ay, az in itertools.product([0, 90, 180, 270], repeat=3):
            xrot = xrot3(ax).astype(int)
            yrot = yrot3(ay).astype(int)
            zrot = zrot3(az).astype(int)
            rot = zrot @ yrot @ xrot

            if (s := np.array2string(rot)) in rots: continue
            rots.add(s)

            # print(f"{ax=} {ay=} {az=}")

            # create a higher dimension matrix which contains [el_1-other_1, el_1-other_2, ... el_1-other_n]
            # then [el_2-other_1, el_2-other_2, ... el_2-other_n] and so on
            their_pos = self.absolute_beacons()[:, None] - (rot @ other.beacons.T).T
            # flatten into just pairs (coords)
            their_pos = their_pos.reshape(-1, their_pos.shape[-1])
            # the true scanner position will be the most reoccuring coordinate (if >= 12)
            unique, counts = np.unique(their_pos, axis=0, return_counts=True)
            most_common = np.argmax(counts)
            if counts[most_common] >= 12:
                print(f"found scanner {other.id:02}: pos={unique[most_common]} rot={[ax,ay,az]} using scanner {self.id}")
                other.update_pos_rot(unique[most_common], [ax, ay, az], rot)
                return True

        return False

    def absolute_beacons(self):
        return (self.rot_mat @ self.beacons.T).T + self.absolute_pos 


def read() -> list[Scanner]:
    with open(filename, "r") as f:
        lines = f.readlines()

    scanners = []
    beacons = []
    scanner_line = True
    lines.append('\n') # just so the last scanner is also created
    for line in lines:
        if scanner_line:
            num = int(re.search(r"([0-9]+)", line).group(1))
            scanner_line = False
        elif line == '\n':
            scanners.append(Scanner(num, beacons))
            beacons = []
            scanner_line = True
        else:
            beacons.append(tuple(int(n) for n in line.strip().split(",")))
    return scanners


def part1():
    scanners = read()

    located = [scanners[0]]
    try_using = [scanners[0]]
    not_located = scanners[1:]

    while not_located:
        for s in try_using:
            for nls in not_located:
                if s.intersect(nls):
                    located.append(nls)
                    try_using.append(nls)
                    not_located.remove(nls)

    # print(scanners)

    all_beacons = set()
    for scanner in scanners:
        all_beacons |= set(tuple(b) for b in scanner.absolute_beacons())
    
    print(len(all_beacons))


def part2():
    scanners = read()

    located = [scanners[0]]
    try_using = [scanners[0]]
    not_located = scanners[1:]

    while not_located:
        for s in try_using:
            for nls in not_located:
                if s.intersect(nls):
                    located.append(nls)
                    try_using.append(nls)
                    not_located.remove(nls)

    max = 0
    for s1, s2 in itertools.combinations(scanners, 2):
        manhattan = np.sum(np.abs(s1.absolute_pos - s2.absolute_pos))
        print(f"dist between {s1.id:2} and {s2.id:2} is {manhattan}")
        if manhattan > max:
            max = manhattan
    print(max)

if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    # part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")