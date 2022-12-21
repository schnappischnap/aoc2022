import operator as op


def part_1(data):
    operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.floordiv}
    monkeys = {}
    for line in data:
        monkey = line[:4]
        expression = line.strip().split(" ")[1:]
        monkeys[monkey] = expression
    
    def get_value(monkey):
        value = monkeys[monkey]
        try:
            return int(value[0])
        except ValueError:
            monkey1, operator, monkey2 = value
            return operators[operator](get_value(monkey1), get_value(monkey2))

    return get_value("root")


def part_2(data):
    operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
    monkeys = {}
    for line in data:
        monkey = line[:4]
        expression = line.strip().split(" ")[1:]
        monkeys[monkey] = expression
    
    def get_value(monkey, humn_value):
        if monkey == "humn":
            return humn_value
        value = monkeys[monkey]
        try:
            return int(value[0])
        except ValueError:
            monkey1, operator, monkey2 = value
            return operators[operator](get_value(monkey1, humn_value), get_value(monkey2, humn_value))

    lhs = monkeys["root"][0]
    rhs = monkeys["root"][2]

    target = get_value(lhs, 0)
    humn_side = rhs
    if (t := get_value(rhs, 0)) == get_value(rhs, 1):
        target = t
        humn_side = lhs

    low = 0
    high = int(1e20)
    while low <= high:
        mid = (low + high) // 2
        result = get_value(humn_side, mid)
        if result > target:
            low = mid + 1
        elif result < target:
            high = mid - 1
        else:
            return mid


if __name__ == "__main__":
    with open("day_21_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
