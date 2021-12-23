from time import perf_counter_ns
from heapq import heappop, heappush

filename = "day23_input.txt"
# filename = "example.txt"

COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

class State:
    def __init__(self, strings):
        self.strings = strings

        self.complete = all(self.strings[i].strip().replace('#', '') == "ABCD" for i in range(2, len(self.strings)-1))

    def __lt__(self, other): # just for the heap
        return self.complete < other.complete
    
    def __eq__(self, other):
        return self.strings == other.strings
    
    def __hash__(self):
        return hash(tuple(self.strings))
    
    def __str__(self):
        return "\n".join(self.strings)

    def __repr__(self):
        return f"<{self.__class__.__name__} object; complete={self.complete}>"

    def all_moves(self):
        moves = []
        for j, row in enumerate(self.strings):
            for i, el in enumerate(row):
                if el in "ABCD":
                    moves.extend(self.moves_for(i, j))
        return moves

    def moves_for(self, x, y):
        moves = []

        cur_char = self.strings[y][x]
        dest_room = "ABCD".index(cur_char) * 2 + 3 # indices 3,5,7,9 in strings
        
        orig_x, orig_y = x, y

        if y > 1: # we are in a room
            if x == dest_room and (y == len(self.strings)-2 or all(self.strings[j][x] == cur_char for j in range(y, len(self.strings)-1))):
                return [] # in correct room and those deeper inside are the same
            if any(self.strings[j][x] != '.' for j in range(1, y)):
                return [] # we are blocked in

            # pretend we've moved out into just above the room aka (x, 1)
            for i in range(1, len(self.strings[1])-1):
                if i in (3,5,7,9):
                    continue # right above a room
                if all(self.strings[1][tmp] == '.' for tmp in range(min(i,x), max(i,x)+1)):
                    moves.append((x, y, i, 1)) # we know we can get out of room, and the hall is empty up to this point

        elif y == 1: # currently in the hall
            if all(tmp == x or self.strings[y][tmp] == '.' for tmp in range(min(dest_room,x), max(dest_room,x)+1)):
                # the path from our x to the destination x is clear
                room = "".join(self.strings[new_j][dest_room] for new_j in range(2, len(self.strings)-1))
                if any(c not in (cur_char, '.') for c in room):
                    return [] # room contains others!!
                d = room.find(cur_char) # find the deepest empty slot
                d += len(self.strings)-1 if d == -1 else 1
                moves.append((x, y, dest_room, d))
                
        return moves
    
    def moved_state(self, prev_cost, move):
        x, y, i, j = move
        strings = [list(s) for s in self.strings]

        char = strings[y][x]
        strings[j][i] = char
        strings[y][x] = '.'

        return prev_cost + COSTS[char] * (abs(x-i)+abs(y-j)), State([''.join(s) for s in strings])
        

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [l.strip("\n") for l in lines]

def dij(lines):
    start = State(lines)

    visited = set()
    costs = {}
    heap = [(0, start)]

    while heap:
        curr_cost, current = heappop(heap)
        visited.add(current)
        if current.complete:
            return curr_cost, current

        for move in current.all_moves():
            new_cost, new_state = current.moved_state(curr_cost, move)
            if new_state not in visited:
                if new_cost < costs.get(new_state, float("Inf")):
                    costs[new_state] = new_cost
                    heappush(heap, (new_cost, new_state))
    return curr_cost, current

def part1():
    lines = read()

    curr_cost, current = dij(lines)

    print(curr_cost)
    print(current)

def part2():
    lines = read()
    lines.insert(3, "  #D#C#B#A#")
    lines.insert(4, "  #D#B#A#C#")

    curr_cost, current = dij(lines)

    print(curr_cost)
    print(current)

if __name__ == "__main__":
    start = perf_counter_ns()

    # part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")