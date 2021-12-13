from collections import defaultdict

filename = "day12_input.txt"
# filename = "example.txt"


def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    lines = (line.strip().split("-") for line in lines)
    d = defaultdict(lambda: [])
    for a, b in lines:
        d[a].append(b)
        d[b].append(a)
    return dict(d)

def can_visit(path: str, new: str):
    if new.isupper():
        return True
    if new in path.split(","):
        return False
    return True

def can_visit_2(path: str, new: str):
    if new.isupper() or new not in path:
        return True
    if new == "start":
        return False
    lpath = path[1:]
    how_many = lpath.count(new)
    lpath = list(filter(lambda s: s.islower(), lpath))
    visited_twice = len(set(lpath)) != len(lpath)
    if how_many >= 2 or (how_many ==1 and visited_twice):
        return False
    if how_many == 1 and not visited_twice:
        return True
    return True

def part1():
    connections = read()
    
    paths = ["start"]
    closed_paths = []

    while paths:
        temp = []
        for path in paths:
            curr = path.split(",")[-1]
            for connection in connections[curr]:
                if can_visit(path, connection):
                    temp.append(f"{path},{connection}")
        paths = temp

        temp = []
        for path in paths:
            if path.endswith("end"):
                closed_paths.append(path)
            else:
                temp.append(path)
        paths = temp

    print(len(closed_paths))
    # print("\n".join(sorted(closed_paths)))

def part2():
    connections = read()

    paths = [["start"]]
    closed_paths = []

    while paths:
        temp = []
        for path in paths:
            curr = path[-1]
            for connection in connections[curr]:
                if can_visit_2(path, connection):
                    temp.append([*path, connection])
        paths = temp

        temp = []
        for path in paths:
            if path[-1] == "end":
                closed_paths.append(path)
            else:
                temp.append(path)
        paths = temp

    print(len(closed_paths))
    # print("\n".join(sorted(closed_paths)))

def part2_dfs():
    connections = read()
    print(dfs(connections, ["start"], "end"))

def dfs(g, visited, end):
    count = 0

    for c in g[visited[-1]]:
        if c == end:
            count += 1
            continue
        if can_visit_2(visited, c):
            new_visited = visited + [c]
            count += dfs(g, new_visited, end)
    return count


if __name__ == "__main__":
    # part1()
    # part2()
    part2_dfs()