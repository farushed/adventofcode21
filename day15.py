filename = "day15_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [[int(c) for c in line.strip()] for line in lines]

# def dfs(grid, pos, visited):
#     visited.append(pos)
#     # print(f"at {pos}")
#     x, y = pos
#     if x == len(grid[y])-1 and y == len(grid)-1:
#         # return grid[y][x]
#         tmp = [sum(grid[vy][vx] for vx, vy in visited)]
#         visited.pop()
#         return tmp

#     paths = []    
#     for nx, ny in [(x+1, y), (x, y+1)]:#, (x-1, y), (x, y-1)]:
#         if (nx, ny) in visited:
#             continue
#         if ny < 0 or ny > (len(grid)-1) or nx < 0 or nx > (len(grid[ny])-1):
#             continue
#         l = dfs(grid, (nx, ny), visited)
#         paths.extend(l)

#     visited.pop()
#     # return grid[y][x] + (min(paths) if paths else 0)
#     return paths
    
def idk(grid, distances, visited, pos):
    if pos in visited:
        return []
    else:
        visited.append(pos)
    x, y = pos
    

    neighbours = []
    for nx, ny in [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]:
        if nx >= 0 and ny >= 0 and ny < len(distances) and nx < len(distances[ny]):
            if (nx, ny) in visited:
                continue
            dist = grid[ny][nx] + distances[y][x]
            print("------")
            print(f"at {x},{y} (val{grid[y][x]}) the dist to node at {nx},{ny} (val{grid[ny][nx]}) is {dist} with {distances[ny][nx]} already there")
            # print(f"{distances[ny][nx]}")
            if dist < distances[ny][nx] or distances[ny][nx] == -1:
                distances[ny][nx] = dist
                # print(f"set {nx},{ny} in distances to {dist}")
            neighbours.append((nx, ny))


    return neighbours
    # lx, ly = x-1, y
    # ux, uy = x, y-1
    # if lx >= 0:
    #     if grid_sums[ly][lx] == 0:
    #         grid[ly][lx] += grid[y][x]
    #         grid_sums[ly][lx] = grid[y][x]
    #     elif grid_sums[ly][lx] > grid[y][x]:
    #         diff = grid_sums[ly][lx] - grid[y][x]
    #         grid[ly][lx] -= diff
    #         grid_sums[ly][lx] = grid[y][x]
    #     # idk(grid, grid_sums, (lx, ly))
    #     neighbours.append((lx, ly))
    # if uy >= 0:
    #     if grid_sums[uy][ux] == 0:
    #         grid[uy][ux] += grid[y][x]
    #         grid_sums[uy][ux] = grid[y][x]
    #     elif grid_sums[uy][ux] > grid[y][x]:
    #         diff = grid_sums[uy][ux] - grid[y][x]
    #         grid[uy][ux] -= diff
    #         grid_sums[uy][ux] = grid[y][x]
    #     # idk(grid, grid_sums, (ux, uy))
    #     neighbours.append((ux, uy))

def print_grid(grid):
    for row in grid:
        for el in row:
            print(f"{el:4}", end="")
        print()

from queue import PriorityQueue
from time import perf_counter_ns

def dij(grid, start_pos, end_pos, debug=False):
    # if pos in visited:
    #     return []
    # else:
    #     visited.append(pos)
    # x, y = pos
    

    # neighbours = []

    # at smallest dist node already
    visited = set()

    distances = [[-1 for j in i]for i in grid]

    pq = PriorityQueue()
    pq.put((0, start_pos))
    while pq.qsize() != 0:
        (dist, (cx, cy)) = pq.get()
        if (cx, cy) == end_pos:
            print(f"final distance {dist}")
            break
        if debug:
            print("-----------")
            print(dist, cx, cy)
        #     yield print_grid(distances)
        visited.add((cx, cy))
        for nx, ny in [(cx-1, cy), (cx, cy-1), (cx+1, cy), (cx, cy+1)]:
            if nx >= 0 and ny >= 0 and ny < len(distances) and nx < len(distances[ny]):
                if (nx, ny) not in visited:
                    ndist = dist + grid[ny][nx]
                    if debug: print(f"at {nx},{ny}(val{grid[ny][nx]}), {dist=}, {ndist=}, {distances[ny][nx]=}")
                    if ndist < distances[ny][nx] or distances[ny][nx] == -1: 
                        distances[ny][nx] = ndist
                        pq.put((ndist, (nx, ny)))
                        if debug: print(f"putting {nx},{ny}(val{grid[ny][nx]}) in pq, {ndist=}")
    return

def part1():
    grid = read()

    start_pos = (0, 0)

    # l = dfs(grid, start_pos, [])
    # print(min(l))

    
    dij(grid, (0, 0), (len(grid[-1])-1, len(grid)-1), debug=False)

    # d = dij(grid, (0, 0), (len(grid[-1])-1, len(grid)-1), visualise=True)
    # while True:
    #     next(d)
    #     input(">")
    return

    # pos = [len(grid[-1])-1, len(grid)-1]
    pos = (0, 0)
    distances = [[-1 for j in i] for i in grid]
    # distances[-1][-1] = grid[-1][-1]
    distances[0][0] = 0

    visited = []
    neighbours = idk(grid, distances, visited, pos)
    while distances[-1][-1] == -1 or neighbours:
        neighbours = sorted(neighbours, key=lambda n: distances[n[1]][n[0]])
        # print(neighbours)
        # print([distances[n[1]][n[0]] for n in neighbours])
        new_neighbours = []
        for n in neighbours:
            new_neighbours.extend(idk(grid, distances, visited, n))
        neighbours = new_neighbours

    print(distances[-1][-1])
    # print_grid(distances)
    # print(grid)
    # print(distances)

def part2():
    grid = read()

    start_pos = (0,0)
    grid_x, grid_y = len(grid[0]), len(grid)
    new_grid = [[0 for i in range(grid_x*5)] for j in range(grid_y*5)]
    for j in range(len(new_grid)):
        for i in range(len(new_grid[j])):
            tile_i, tile_j = i//grid_x, j//grid_y
            orig_i, orig_j = i - grid_x*tile_i, j - grid_y*tile_j
            increase = tile_i + tile_j
            # print(i, j, tile_i, tile_j, orig_i, orig_j, increase)
            new_grid[j][i] = (grid[orig_j][orig_i] + increase -1) % 9 +1
    grid = new_grid
    end_pos = (len(new_grid[0])-1, len(new_grid)-1)
    
    # print("grid finished")

    debug = False

    # visited = []
    visited = set()
    distances = [[-1 for j in i]for i in grid]

    # steps = 0
    pq = PriorityQueue()
    pq.put((0, start_pos))
    while pq.qsize() != 0:
        (dist, (cx, cy)) = pq.get()
        if (cx, cy) == end_pos:
            print(f"final distance {dist}")
            break
        # steps += 1
        if debug:
            print("-----------")
            print(dist, cx, cy)
        #     yield print_grid(distances)
        # visited.append((cx, cy))
        visited.add((cx, cy))
        for nx, ny in [(cx+1, cy), (cx, cy+1), (cx-1, cy), (cx, cy-1)]:
            if nx >= 0 and ny >= 0 and ny < len(distances) and nx < len(distances[ny]):
                if (nx, ny) not in visited:
                    ndist = dist + grid[ny][nx]
                    if debug: print(f"at {nx},{ny}(val{grid[ny][nx]}), {dist=}, {ndist=}, {distances[ny][nx]=}")
                    if ndist < distances[ny][nx] or distances[ny][nx] == -1: 
                        distances[ny][nx] = ndist
                        pq.put((ndist, (nx, ny)))
                        if debug: print(f"putting {nx},{ny}(val{grid[ny][nx]}) in pq, {ndist=}")
    # print(steps)

if __name__ == "__main__":
    start = perf_counter_ns()

    # part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"Time taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")