def part_1(data):
    numbers = [int(i) for i in data]
    indices = list(range(len(numbers)))

    for i in indices[:]:
        j = indices.index(i)
        indices.pop(j)
        indices.insert((j + numbers[i]) % len(indices), i)
    
    zero = indices.index(numbers.index(0))
    return sum(numbers[indices[(zero + i) % len(numbers)]] for i in [1000, 2000, 3000])


def part_2(data):
    numbers = [int(i) * 811589153 for i in data]
    indices = list(range(len(numbers)))

    for i in indices * 10:
        j = indices.index(i)
        indices.pop(j)
        indices.insert((j + numbers[i]) % len(indices), i)
    
    zero = indices.index(numbers.index(0))
    return sum(numbers[indices[(zero + i) % len(numbers)]] for i in [1000, 2000, 3000])


if __name__ == "__main__":
    with open("day_20_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
