import functools
import re


def part_1(data):
    return sum(
        i + 1
        for i in range(len(data) // 3 + 1)
        if compare(*(re.findall(r"\d+|\[|\]", packet[1:-2]) for packet in data[i*3 : i*3+2])) == 1
    )


def part_2(data):
    divider1 = list("[2]")
    divider2 = list("[6]")
    packets = [re.findall(r"\d+|\[|\]", packet[1:-2]) for packet in data if packet != "\n"]
    packets.extend([divider1, divider2])
    packets.sort(key=functools.cmp_to_key(compare), reverse=True)
    return (packets.index(divider1) + 1) * (packets.index(divider2) + 1)


def compare(packet1, packet2):
    i, j = 0, 0
    while i < len(packet1) and j < len(packet2):
        left, right = packet1[i], packet2[j]
        if left == "]":
            i += 1
            continue
        if right == "]":
            j += 1
            continue
        if left == "[" or right == "[":
            new_packet1 = get_inner_packet(packet1[i + 1 :]) if left == "[" else [left]
            new_packet2 = get_inner_packet(packet2[j + 1 :]) if right == "[" else [right]
            comparison = compare(new_packet1, new_packet2)
            if comparison != 0:
                return comparison
            else:
                i = packet1.index("]", i) + 1 if left == "[" else i + 1
                j = packet2.index("]", j) + 1 if right == "[" else j + 1
                continue
        left, right = int(left), int(right)
        if left < right:
            return 1
        if right < left:
            return -1
        i += 1
        j += 1

    if len(packet1) < len(packet2):
        return 1
    if len(packet2) < len(packet1):
        return -1
    return 0


def get_inner_packet(packet):
    depth = 0
    new_packet = []
    for c in packet:
        if c == "[":
            depth += 1
        elif c == "]":
            if depth == 0:
                return new_packet
            depth -= 1
        new_packet.append(c)
    return new_packet


if __name__ == "__main__":
    with open("day_13_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
