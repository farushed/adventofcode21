filename = "day10_input.txt"
# filename = "example.txt"

open_brackets = {'(': 3, '[': 57, '{': 1197, '<': 25137}
close_brackets = {')': 3, ']': 57, '}': 1197, '>': 25137}


open_to_close = {'(': 1, '[': 2, '{': 3, '<': 4}

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def part1():
    lines = read()

    opened = []

    illegal_chars = []
    for line in lines:
        for ch in line:
            if ch in open_brackets:
                opened.append(ch)
            elif ch in close_brackets:
                last_opened = opened.pop()
                if open_brackets[last_opened] != close_brackets[ch]:
                    illegal_chars.append((ch, last_opened))
                    break
    print(sum((close_brackets[ch[0]] for ch in illegal_chars)))

    
def part2():
    lines = read()

    scores = []
    for line in lines:
        opened = []
        for ch in line:
            if ch in open_brackets:
                opened.append(ch)
            elif ch in close_brackets:
                last_opened = opened.pop()
                if open_brackets[last_opened] != close_brackets[ch]:
                    break
        else:
            opened.reverse()
            score = 0
            for ch in opened:
                score *= 5
                score += open_to_close[ch]
            scores.append(score)

    print(sorted(scores)[int(len(scores)/2)])


if __name__ == "__main__":
    # part1()
    part2()