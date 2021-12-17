from heapq import heappush, heappop
from time import perf_counter_ns

filename = "day15_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [[int(c) for c in line.strip()] for line in lines]

def print_grid(grid):
    for row in grid:
        for el in row:
            print(f"{el:4}", end="")
        print()


def dij(grid, start_pos, end_pos, debug=False):
    visited = set()

    distances = [[-1 for j in i]for i in grid]

    heap = []
    heappush(heap, (0, *start_pos))
    while len(heap):
        dist, cx, cy = heappop(heap)

        if (cx, cy) == end_pos:
            return dist
        if debug:
            print("-----------")
            print(dist, cx, cy)
        visited.add((cx, cy))
        for nx, ny in [(cx-1, cy), (cx, cy-1), (cx+1, cy), (cx, cy+1)]:
            if nx >= 0 and ny >= 0 and ny < len(distances) and nx < len(distances[ny]):
                if (nx, ny) not in visited:
                    ndist = dist + grid[ny][nx]
                    if debug: print(f"at {nx},{ny}(val{grid[ny][nx]}), {dist=}, {ndist=}, {distances[ny][nx]=}")
                    if ndist < distances[ny][nx] or distances[ny][nx] == -1: 
                        distances[ny][nx] = ndist
                        heappush(heap, (ndist, nx, ny))
                        if debug: print(f"putting {nx},{ny}(val{grid[ny][nx]}) in pq, {ndist=}")

def part1():
    grid = read()

    start_pos = (0, 0)
    end_pos = (len(grid[-1])-1, len(grid)-1)
    
    distance = dij(grid, start_pos, end_pos)
    print(distance)

def part2():
    grid = read()

    start_pos = (0,0)
    grid_x, grid_y = len(grid[0]), len(grid)
    new_grid = [[0 for i in range(grid_x*5)] for j in range(grid_y*5)]
    for j in range(len(new_grid)):
        for i in range(len(new_grid[j])):
            tile_i, orig_i = divmod(i, grid_x)
            tile_j, orig_j = divmod(j, grid_y)
            increase = tile_i + tile_j

            new_grid[j][i] = (grid[orig_j][orig_i] + increase -1) % 9 +1
    grid = new_grid
    end_pos = (len(new_grid[0])-1, len(new_grid)-1)
    
    distance = dij(grid, start_pos, end_pos)
    print(distance)

if __name__ == "__main__":
    start = perf_counter_ns()

    # part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")