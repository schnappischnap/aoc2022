def part_1(data):
    cycle = 1
    X = 1
    signal_strength_sum = 0

    for line in data:
        if (cycle - 20) % 40 == 0:
            signal_strength_sum += cycle * X
        if line.startswith("noop"):
            cycle += 1
        else:
            if (cycle - 20) % 40 == 39:
                signal_strength_sum += (cycle + 1) * X
            cycle += 2
            X += int(line.split()[-1])

    return signal_strength_sum


def part_2(data):
    pixels = []
    cycle = 0
    X = 1

    for line in data:
        pixels.append("#" if abs((cycle % 40) - X) < 2 else ".")
        if line.startswith("noop"):
            cycle += 1
        else:
            pixels.append("#" if abs((cycle + 1) % 40 - X) < 2 else ".")
            cycle += 2
            X += int(line.split()[-1])

    return "\n" + "\n".join("".join(pixels[i: i+40]) for i in range(0, len(pixels), 40))


if __name__ == "__main__":
    with open("day_10_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
