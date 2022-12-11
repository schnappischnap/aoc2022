import math
import operator as op


def part_1(data):
    items = []
    tests = []
    targets = []
    operations = []
    
    for i in range(1, len(data), 7):
        items.append(list(int(v) for v in data[i].split(":")[1].split(", ")))
        tests.append(int(data[i+2].split()[-1]))
        targets.append(tuple(int(monkey.split()[-1]) for monkey in data[i+3:i+5]))

        operator, operand = data[i+1].split()[-2:]
        if operand == "old":
            operations.append((op.pow, 2))
        else:
            operations.append((op.add if operator == "+" else op.mul, int(operand)))

    inspections = [0] * len(items)
    for _ in range(20):
        for monkey in range(len(items)):
            inspections[monkey] += len(items[monkey])
            while items[monkey]:
                operator, operand = operations[monkey]
                item = operator(items[monkey].pop(0), operand) // 3
                target = targets[monkey][item % tests[monkey] != 0]
                items[target].append(item)

    return op.mul(*sorted(inspections)[-2:])


def part_2(data):
    items = []
    tests = []
    targets = []
    operations = []
    
    for i in range(1, len(data), 7):
        items.append(list(int(v) for v in data[i].split(":")[1].split(", ")))
        tests.append(int(data[i+2].split()[-1]))
        targets.append(tuple(int(monkey.split()[-1]) for monkey in data[i+3:i+5]))

        operator, operand = data[i+1].split()[-2:]
        if operand == "old":
            operations.append((op.pow, 2))
        else:
            operations.append((op.add if operator == "+" else op.mul, int(operand)))

    divisor = math.prod(tests)
    inspections = [0] * len(items)
    for _ in range(10000):
        for monkey in range(len(items)):
            inspections[monkey] += len(items[monkey])
            while items[monkey]:
                operator, operand = operations[monkey]
                item = operator(items[monkey].pop(0), operand) % divisor
                target = targets[monkey][item % tests[monkey] != 0]
                items[target].append(item)

    return op.mul(*sorted(inspections)[-2:])


if __name__ == "__main__":
    with open("day_11_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
