def part_1(data):
    return solve(data, 2022)


def part_2(data):
    return solve(data, 20000, True)


def solve(data, turn, part2=False):
    shapes = [
        [(2, 4), (3, 4), (4, 4), (5, 4)],
        [(2, 5), (3, 4), (3, 6), (3, 5), (4, 5)],
        [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)],
        [(2, 4), (2, 5), (2, 6), (2, 7)],
        [(2, 4), (3, 4), (2, 5), (3, 5)],
    ]
    settled = set((x, 0) for x in range(0, 7))
    patterns = dict()
    highest_rock = 0
    jet_i = 0

    for i in range(turn):
        rock = [(x, y + highest_rock) for x, y in shapes[i % 5]]
        while True:
            jet = data[jet_i]
            jet_i = (jet_i + 1) % len(data)
            if jet == ">" and rock[-1][0] < 6:
                potential_rock = [(x + 1, y) for x, y in rock]
            elif jet == "<" and rock[0][0] > 0:
                potential_rock = [(x - 1, y) for x, y in rock]
            if all(coord not in settled for coord in potential_rock):
                rock = potential_rock

            potential_rock = [(x, y - 1) for x, y in rock]
            if all(coord not in settled for coord in potential_rock):
                rock = potential_rock
            else:
                settled.update(rock)
                highest_rock = max(highest_rock, max(y for _, y in rock))
                if not part2:
                    break
                
                rock_height = rock[0][1]
                pattern = tuple(
                    (x, y) for x in range(7) for y in range(0, -20, -1) 
                    if (x, y + rock_height) in settled
                )
                if pattern in patterns:
                    start_i, start_height = patterns[pattern]
                    height_difference = highest_rock - start_height
                    i_difference = i - start_i
                    
                    for j in range(1000000000000, 0, -1):
                        if (j - start_i) % i_difference == 0:
                            break
                    
                    height_at_j = start_height + (height_difference * ((j - start_i)// i_difference))
                    remainder = start_i + (1000000000000 - j)
                    height_at_remainder =  solve(data, remainder)
                    return height_at_j + height_at_remainder - start_height
                else:
                    patterns[pattern] = (i, highest_rock)
                break
    
    return highest_rock


if __name__ == "__main__":
    with open("day_17_input.txt", "r") as f:
        inp = f.read()
        print("Part 1: " + str(part_1(inp.strip())))
        print("Part 2: " + str(part_2(inp)))
