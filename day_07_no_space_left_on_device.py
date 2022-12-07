from collections import defaultdict


def solve(data):
    sizes = defaultdict(int)

    i = 1
    id = 0

    def r(current_dir):
        nonlocal i
        nonlocal id
        
        while True:
            i += 1
            if i >= len(data):
                return sizes[current_dir]
            line = data[i].split()
            if line[0] == "$":
                if line[1] == "cd":
                    if line[-1] == "..":
                        return sizes[current_dir]
                    else:
                        id += 1
                        sizes[current_dir] += r(id)
            elif line[0] != "dir":
                sizes[current_dir] += int(line[0])

    r("/")
    unused_space = 70000000 - sizes["/"]
    space_needed = 30000000 - unused_space
    return (
        sum(size for size in sizes.values() if size <= 100000),
        min(size for size in sizes.values() if size >= space_needed),
    )


if __name__ == "__main__":
    with open("day_07_input.txt", "r") as f:
        inp = f.readlines()
        part_1, part_2 = solve(inp)
        print("Part 1: " + str(part_1))
        print("Part 2: " + str(part_2))
