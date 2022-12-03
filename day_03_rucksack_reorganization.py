import string


def part_1(data):
    priority_sum = 0
    for rucksack in data:
        compartments = [set(rucksack[:len(rucksack)//2]), set(rucksack[len(rucksack)//2:])]
        shared_item = set.intersection(*compartments)
        priority_sum += string.ascii_letters.index(shared_item.pop()) + 1
    return priority_sum


def part_2(data):
    priority_sum = 0
    for i in range(0, len(data), 3):
        rucksacks = [set(rucksack.strip()) for rucksack in data[i: i+3]]
        shared_item = set.intersection(*rucksacks)
        priority_sum += string.ascii_letters.index(shared_item.pop()) + 1
    return priority_sum


if __name__ == "__main__":
    with open("day_03_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
