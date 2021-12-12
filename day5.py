import itertools, functools

filename = "day5_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [[tuple(map(int, h.split(","))) for h in line.split(" -> ")] for line in lines]

def print_board(board):
    print("\n".join(("\t".join([str(e)for e in r]) for r in board)))

def part1():
    coord_pairs = read()
    max_x = max(*(pair[0][0] for pair in coord_pairs), *(pair[1][0] for pair in coord_pairs))
    max_y = max(*(pair[0][1] for pair in coord_pairs), *(pair[1][1] for pair in coord_pairs))
    print(max_x, max_y)

    board = [[0]*(max_x+1) for i in range(max_y+1)]

    for pair in coord_pairs:
        start = pair[0]
        end = pair[1]
        (s_x, s_y), (e_x, e_y) = start, end
        if (s_x != e_x) and (s_y != e_y):
            continue # if not horizontal or vertical

        # hack to make the range always low -> high
        if s_x > e_x:
            s_x, e_x = e_x, s_x
        if s_y > e_y:
            s_y, e_y = e_y, s_y
        for curr_x in range(s_x, e_x+1):
            for curr_y in range(s_y, e_y+1):
                board[curr_y][curr_x] += 1
    
    all_vals = [i for sublist in board for i in sublist]
    # print_board(board)
    print(len(list(filter(lambda i: i >= 2, all_vals))))
    

def part2():
    coord_pairs = read()
    max_x = max(*(pair[0][0] for pair in coord_pairs), *(pair[1][0] for pair in coord_pairs))
    max_y = max(*(pair[0][1] for pair in coord_pairs), *(pair[1][1] for pair in coord_pairs))
    print(max_x, max_y)

    board = [[0]*(max_x+1) for i in range(max_y+1)]

    for pair in coord_pairs:
        (s_x, s_y), (e_x, e_y) = pair[0], pair[1]
        rev = False
        if s_x > e_x:
            s_x, e_x = e_x, s_x
            rev = not rev
        if s_y > e_y:
            s_y, e_y = e_y, s_y
            rev = not rev
        
        
        if (s_x != e_x) and (s_y != e_y):
            # diagonal
            x_range = range(s_x, e_x+1)
            y_range = range(s_y, e_y+1)
            if rev: # if odd number of swaps earlier, reverse one of the ranges
                y_range = reversed(y_range)
            for curr_x, curr_y in zip(x_range, y_range):
                board[curr_y][curr_x] += 1
        else:
            # same as part1
            for curr_x in range(s_x, e_x+1):
                for curr_y in range(s_y, e_y+1):
                    board[curr_y][curr_x] += 1
    
    all_vals = [i for sublist in board for i in sublist]
    # print_board(board)
    print(len(list(filter(lambda i: i >= 2, all_vals))))

if __name__ == "__main__":
    # part1()
    part2()