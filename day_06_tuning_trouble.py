import re


def part_1(data):
    pattern = "(.)(?!" + "(.)(?!".join("|".join(f"\\{i+1}" for i in range(j)) + ")" for j in range(1, 4))
    return re.search(pattern, data).end()+1


def part_2(data):
    pattern = "(.)(?!" + "(.)(?!".join("|".join(f"\\{i+1}" for i in range(j)) + ")" for j in range(1, 14))
    return re.search(pattern, data).end()+1


if __name__ == "__main__":
    with open("day_06_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
