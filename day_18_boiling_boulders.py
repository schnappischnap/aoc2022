import itertools


def part_1(data):
    cubes = {tuple(int(i) for i in line.split(",")) for line in data}
    return sum(neighbour not in cubes for cube in cubes for neighbour in neighbours(*cube))


def part_2(data):
    cubes = {tuple(int(i) for i in line.split(",")) for line in data}

    def bfs(start):
        queue = [(start, 0)]
        discovered = {start}
        surface_area = 0
        while queue:
            (x, y, z), distance = queue.pop(0)
            cube_neighbours = sum(cube in cubes for cube in neighbours(x, y, z))
            if distance > 1 and cube_neighbours == 0:
                continue
            surface_area += cube_neighbours
            for neighbour in neighbours(x, y, z):
                if neighbour not in cubes and neighbour not in discovered:
                    discovered.add(neighbour)
                    queue.append((neighbour, 0 if cube_neighbours else distance + 1))
        return surface_area

    far_right_cube = max(cubes)
    start = (far_right_cube[0] + 1, far_right_cube[1], far_right_cube[2])
    return bfs(start)


def neighbours(x, y, z):
    return [(x + dx, y + dy, z + dz)
            for dx, dy, dz in itertools.product((-1, 0, 1), repeat=3)
            if (not dx) + (not dy) + (not dz) == 2]


if __name__ == "__main__":
    with open("day_18_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
