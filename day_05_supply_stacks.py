from collections import defaultdict


def part_1(data):
    drawing, instructions = data.split("\n\n")

    stacks = defaultdict(list)
    for line in reversed(drawing.split("\n")[:-1]):
        for stack, crate in enumerate(line[1::4], 1):
            if crate != " ":
                stacks[stack].append(crate)
    
    for instruction in instructions.split("\n"):
        count, start, end = (int(i) for i in instruction.split()[1::2])
        crates = stacks[start][-count:]
        stacks[start] = stacks[start][:-count]
        stacks[end].extend(reversed(crates))

    return "".join(stack[-1] for stack in stacks.values())


def part_2(data):
    drawing, instructions = data.split("\n\n")

    stacks = defaultdict(list)
    for line in reversed(drawing.split("\n")[:-1]):
        for stack, crate in enumerate(line[1::4], 1):
            if crate != " ":
                stacks[stack].append(crate)
    
    for instruction in instructions.split("\n"):
        count, start, end = (int(i) for i in instruction.split()[1::2])
        crates = stacks[start][-count:]
        stacks[start] = stacks[start][:-count]
        stacks[end].extend(crates)

    return "".join(stack[-1] for stack in stacks.values())


if __name__ == "__main__":
    with open("day_05_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
