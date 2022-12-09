def part_1(data):
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    visited = set([(0, 0)])

    for line in data:
        direction, amount = line.split()
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0
        for _ in range(int(amount)):
            head_x += dx
            head_y += dy
            if abs(head_y - tail_y) == 2:
                tail_y = (head_y + tail_y) // 2
                if head_x != tail_x:
                    tail_x = head_x
            elif abs(head_x - tail_x) == 2:
                tail_x = (head_x + tail_x) // 2
                if head_y != tail_y:
                    tail_y = head_y
            visited.add((tail_x, tail_y))

    return len(visited)


def part_2(data):
    knots = [(0, 0)] * 10
    visited = set([(0, 0)])

    for line in data:
        direction, amount = line.split()
        dx = 1 if direction == "R" else -1 if direction == "L" else 0
        dy = 1 if direction == "U" else -1 if direction == "D" else 0
        for _ in range(int(amount)):
            knots[0] = (knots[0][0] + dx, knots[0][1] + dy)
            for i, knot in enumerate(knots[1:], 1):
                tail_x, tail_y = knot
                head_x, head_y = knots[i - 1]
                x_distance = abs(head_x - tail_x)
                y_distance = abs(head_y - tail_y)
                if x_distance == 2:
                    tail_x = (head_x + tail_x) // 2
                    if y_distance == 1:
                        tail_y = head_y
                if y_distance == 2:
                    tail_y = (head_y + tail_y) // 2
                    if x_distance == 1:
                        tail_x = head_x
                knots[i] = (tail_x, tail_y)
            visited.add(knots[-1])

    return len(visited)


if __name__ == "__main__":
    with open("day_09_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
