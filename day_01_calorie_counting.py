def part_1(data):
    calorie_sums = [sum(int(line) for line in elf.split()) for elf in data.split("\n\n")]
    return max(calorie_sums)


def part_2(data):
    calorie_sums = [sum(int(line) for line in elf.split()) for elf in data.split("\n\n")]
    return sum(sorted(calorie_sums)[-3:])


if __name__ == "__main__":
    with open("day_01_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
