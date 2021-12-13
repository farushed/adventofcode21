filename = "day13_input.txt"
# filename = "example.txt"


def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    coords = []
    folds = []
    for l in lines:
        l = l.strip()
        if l.startswith("fold"):
            folds.append(l.split(" ")[-1])
        elif len(l):
            coords.append([int(n) for n in l.split(",")])
    return coords, folds


def do_fold(coords, fold:str):
    vertical = 1 if fold[0] == "y" else 0
    axis = int(fold[2:])
    for coord in coords:
        if coord[vertical] > axis:
            coord[vertical] = 2*axis - coord[vertical]


def part1():
    coords, folds = read()

    do_fold(coords, folds[0])

    print(len(set([(x, y) for x, y in coords])))


def part2():
    coords, folds = read()

    for fold in folds:
        do_fold(coords, fold)

    xmax = max((a[0] for a in coords))
    ymax = max((a[1] for a in coords))
    for j in range(ymax+1):
        for i in range(xmax+1):
            print("#" if [i,j] in coords else " ", end="")
        print()


if __name__ == "__main__":
    part1()
    part2()