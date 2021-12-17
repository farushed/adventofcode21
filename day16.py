from time import perf_counter_ns
import functools

filename = "day16_input.txt"
# filename = "example.txt"


basetwo = functools.partial(int, base=2)
hex = {'0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}
tabchar = '\t'

def read():
    with open(filename, "r") as f:
        line = f.readline()
    return line.strip()

def parse_packet(packet, debug=False, indents=0):
    if packet == 0 or basetwo(packet) == 0:
        return [], [], [], len(str(packet)), 0
    version, packet = basetwo(packet[0:3]), packet[3:]
    type_id, packet = basetwo(packet[0:3]), packet[3:]
    curr_len = 3+3
    if type_id == 4:
        num = ""
        while True:
            last, bits, packet = (packet[0] == "0"), packet[1:5], packet[5:]
            num += bits
            curr_len += 5
            if last: break
        num = basetwo(num)
        if debug: print(f"{tabchar*indents}literal {num}")
        return [version], [type_id], [num], curr_len, packet
    elif type_id == 0: name="+";    func = lambda x, y: x + y
    elif type_id == 1: name="*";    func = lambda x, y: x * y
    elif type_id == 2: name="min";  func = min
    elif type_id == 3: name="max";  func = max
    elif type_id == 5: name=">";    func = lambda x, y: int(x > y)
    elif type_id == 6: name="<";    func = lambda x, y: int(x < y)
    elif type_id == 7: name="==";   func = lambda x, y: int(x == y)

    length_type, packet = packet[0], packet[1:]
    curr_len += 1
    if length_type == "1":
        num_subpackets, subpackets = basetwo(packet[0:11]), packet[11:]
        curr_len += 11
        if debug: print(f"{tabchar*indents}operator {name} over {num_subpackets} subpackets {{")

    elif length_type == "0":
        length_subpackets, subpackets = basetwo(packet[0:15]), packet[15:]
        curr_len += 15
        if debug: print(f"{tabchar*indents}operator {name} over {length_subpackets} bits {{")

    versions, type_ids, all_contents = [version], [type_id], []
    while (num_subpackets if length_type == "1" else length_subpackets > 0):
        version, type_id, contents, length_subpacket, subpackets = parse_packet(subpackets, debug, indents+1)
        versions.extend(version)
        type_ids.extend(type_id)
        all_contents.extend(contents)
        curr_len += length_subpacket

        if length_type == "1":
            num_subpackets -= 1
            if debug: print(f"{tabchar*(indents+1)}{num_subpackets} more subpackets after subpacket of length {length_subpacket}")
        elif length_type == "0":
            length_subpackets -= length_subpacket
            if debug: print(f"{tabchar*(indents+1)}{length_subpackets} more bits after subpacket of length {length_subpacket}")

    result = functools.reduce(func, all_contents)
    if debug: print(f"{tabchar*indents}}} = {result}")
    return versions, type_ids, [result], curr_len, subpackets


def part1():
    transmission = read()
    packet = "".join(hex[c] for c in transmission)

    versions, *_ = parse_packet(packet)

    print(sum(versions))


def part2():
    transmission = read()
    binary = "".join(hex[c] for c in transmission)

    packet = binary
    _, _, all_contents, _, _ = parse_packet(packet)

    print(all_contents[0])

if __name__ == "__main__":
    start = perf_counter_ns()

    part1()
    part2()

    stop = perf_counter_ns()
    interval = stop - start
    print(f"\nTime taken: {interval} ns = {interval/(10**6):.2f} ms = {interval/(10**9):.2f} s")