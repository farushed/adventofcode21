filename = "day8_input.txt"
# filename = "example.txt"

def read():
    with open(filename, "r") as f:
        lines = f.readlines()
    return [[nums.split(" ") for nums in line.strip().split(" | ")] for line in lines]

def part1():
    l = read()
    total = 0
    for unique, output in l:
        for num in output:
            ln = len(num)
            if ln == 2 or ln == 4 or ln == 3 or ln == 7:
                total += 1
    print(total)

#  aaaa 
# b    c
# b    c
#  dddd 
# e    f
# e    f
#  gggg 

#  0000 
# 1    2
# 1    2
#  3333 
# 4    5
# 4    5
#  6666 

def part2():
    l = read()
    segments = {num: '' for num in range(7)}
    output_sum = 0
    numbers = dict()

    for unique, output in l:
        for n in sorted(unique, key=len):
            ln = len(n)
            if ln == 2:
                numbers[n] = 1  # must be a 1
                segments[2] = n
                segments[5] = n
            elif ln == 3:
                numbers[n] = 7  #must be a 7
                for c in segments[2]: n = n.replace(c, '')
                segments[0] = n
            elif ln == 4:
                numbers[n] = 4 # must be a 4
                for c in segments[2]: n = n.replace(c, '')
                segments[1] = n
                segments[3] = n
            elif ln == 7:
                numbers[n] = 8 # must be an 8
        
        for n in filter(lambda x: len(x) == 6, unique):
            for a in 'abcdefg':
                if a not in n:
                    missing = a

            if missing in segments[2]: # if top right, then must be a 6
                segments[2] = missing
                segments[5] = segments[5].replace(missing, '')
                numbers[n] = 6
            elif missing in segments[3]: # if middle then 0
                segments[3] = missing
                segments[1] = segments[1].replace(missing, '')
                numbers[n] = 0
            else: # must be 9
                segments[4] = missing
                numbers[n] = 9
        
        for a in 'abcdefg':
            if a not in segments.values():
                missing = a
                break
        for key, val in segments.items():
            if val == '':
                segments[key] = missing
                break
            
        for n in filter(lambda x: len(x) == 5, unique):
            missing = ''
            for a in 'abcdefg':
                if a not in n:
                    missing += a
            missing = sorted(missing)
            if missing == sorted([segments[1], segments[4]]): # 3
                numbers[n] = 3
            elif missing == sorted([segments[1], segments[5]]): # 2
                numbers[n] = 2
            else:
                numbers[n] = 5
        
        numbers = {''.join(sorted(k)): v for k,v in numbers.items()}
                            
        print(segments, numbers)
        out_num = ''
        for num in output:
            num = ''.join(sorted(num))
            out_num += str(numbers[num])
        output_sum += int(out_num)

    print(output_sum)



if __name__ == "__main__":
    # part1()
    part2()