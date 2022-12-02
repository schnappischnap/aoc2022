def part_1(data):
    score = 0
    for line in data:
        opponent_shape = ord(line[0]) - 64  # A=1, B=2, C=3
        player_shape = ord(line[2]) - 87  # X=1, Y=2, Z=3
        outcome = ((1 + player_shape - opponent_shape) % 3) * 3
        score += player_shape + outcome
    return score


def part_2(data):
    score = 0
    for line in data:
        opponent_shape = ord(line[0]) - 65  # A=0, B=1, C=2
        outcome = ord(line[2]) - 88  # X=0, Y=1, Z=2
        player_shape = (opponent_shape + outcome - 1) % 3 + 1
        score +=  player_shape + outcome * 3
    return score


if __name__ == "__main__":
    with open("day_02_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
