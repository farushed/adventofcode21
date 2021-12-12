import itertools, functools

filename = "day4_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()

    numbers = [int(num) for num in lines[0].split(",")]
    boards = []
    for ele, sub in itertools.groupby((l.strip() for l in lines[1:]), key=bool):
        if ele:
            board = []
            for row in list(sub):
                board.append([[int(i), False] for i in row.split()])
            boards.append(board)

    return numbers, boards

def check(board):
    for row in board:
        if functools.reduce(lambda a, b: a and b, [i[1] for i in row]):
            return True
    for i in range(len(board[0])):
        if functools.reduce(lambda a, b: a and b, (row[i][1] for row in board)):
            return True
    return False

def print_board(board):
    print("\n".join(("\t".join([str(e[0])for e in r]) for r in board)))
    print("\n")
    print("\n".join(("\t".join([str(e[0]) if e[1] else "  " for e in r]) for r in board)))

def part1():
    numbers, boards = read()
    # print(numbers)
    # print(boards)
    for num in numbers:
        for board in boards:
            for row in board:
                for elem in row:
                    if elem[0] == num:
                        elem[1] = True
            if check(board):
                print_board(board)
                sum_unmarked = sum([e[0] if not e[1] else 0 for r in board for e in r])
                print(f"sum unmarked = {sum_unmarked}")
                print(f"current num = {num}")
                print(f"product = {sum_unmarked * num}")
                return

def part2():
    numbers, boards = read()
    # print(numbers)
    # print(boards)
    winning_boards = []
    winning_nums = []
    for num in numbers:
        for board in boards:
            if board in winning_boards:
                continue
            for row in board:
                for elem in row:
                    if elem[0] == num:
                        elem[1] = True
            if check(board):
                winning_boards.append(board)
                winning_nums.append(num)

    board = winning_boards[-1]
    num = winning_nums[-1]
    sum_unmarked = sum([e[0] if not e[1] else 0 for r in board for e in r])
    print(f"sum unmarked = {sum_unmarked}")
    print(f"current num = {num}")
    print(f"product = {sum_unmarked * num}")
    return

if __name__ == "__main__":
    # part1()
    part2()