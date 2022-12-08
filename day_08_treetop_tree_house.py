import numpy as np


def part_1(data):
    trees = np.array([[i for i in line.strip()] for line in data], dtype=int)
    width, height = trees.shape
    visible = 0

    for x in range(0, width):
        for y in range(0, height):
            tree = trees[x, y]
            views = [trees[x, :y], trees[x, y+1:], trees[:x, y], trees[x+1:, y]]
            visible += any(np.all(view < tree) for view in views)
            
    return visible


def part_2(data):
    trees = np.array([[i for i in line.strip()] for line in data], dtype=int)
    width, height = trees.shape
    max_score = 0

    for x in range(0, width):
        for y in range(0, height):
            tree = trees[x, y]
            views = [trees[x, :y][::-1], trees[x, y+1:], trees[:x, y][::-1], trees[x+1:, y]]
            score = np.prod([np.append(np.nonzero(view >= tree)[0] + 1, [len(view)])[0] for view in views])
            if score > max_score:
                max_score = score
    
    return max_score            


if __name__ == "__main__":
    with open("day_08_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
