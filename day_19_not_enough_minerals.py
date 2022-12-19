from collections import deque
import re

def part_1(data):
    def dfs(c_ore, c_clay, c_obsidian, c_geodes):
        max_ore = max(c_ore, c_clay, c_obsidian[0], c_geodes[0])

        most_geodes = 0
        queue = deque([(0, 0, 0, 0, 1, 0, 0, 0, 24)])
        visited = set()
        
        while queue:
            state = queue.pop()

            ore, clay, obsidian, geodes, r_ore, r_clay, r_obsidian, r_geodes, time = state
            ore = min(ore, max_ore*time)
            r_ore = min(r_ore, max_ore)
            clay = min(clay, c_obsidian[1]*time)
            r_clay = min(r_clay, c_obsidian[1])
            obsidian = min(obsidian, c_geodes[1]*time)
            r_obsidian = min(r_obsidian, c_geodes[1])
            state = ore, clay, obsidian, geodes, r_ore, r_clay, r_obsidian, r_geodes, time

            if state in visited:
                continue
            visited.add(state)

            n_ore = ore + r_ore
            n_clay = clay + r_clay
            n_obsidian = obsidian + r_obsidian
            n_geodes = geodes + r_geodes
            time -= 1

            if time == 0:
                most_geodes = max(n_geodes, most_geodes)
                continue
        
            if ore >= c_geodes[0] and obsidian >= c_geodes[1]:
                queue.append((n_ore - c_geodes[0], n_clay, n_obsidian - c_geodes[1], n_geodes, r_ore, r_clay, r_obsidian, r_geodes+1, time))
                continue
            if ore >= c_obsidian[0] and clay >= c_obsidian[1]:
                queue.append((n_ore - c_obsidian[0], n_clay - c_obsidian[1], n_obsidian, n_geodes, r_ore, r_clay, r_obsidian+1, r_geodes, time))
            if ore >= c_clay:
                queue.append((n_ore-c_clay, n_clay, n_obsidian, n_geodes, r_ore, r_clay+1, r_obsidian, r_geodes, time))
            if ore >= c_ore:
                queue.append((n_ore-c_ore, n_clay, n_obsidian, n_geodes, r_ore+1, r_clay, r_obsidian, r_geodes, time))
            
            queue.append((n_ore, n_clay, n_obsidian, n_geodes, r_ore, r_clay, r_obsidian, r_geodes, time))
            
        return most_geodes

    quality_sum = 0
    for i, line in enumerate(data, 1):
        blueprints = tuple(int(j) for j in re.findall(r"(\d+)", line)[1:])
        m = dfs(blueprints[0], blueprints[1], (blueprints[2], blueprints[3]), (blueprints[4], blueprints[5]))
        quality = m * i
        quality_sum += quality
        
    return quality_sum


def part_2(data):
    def dfs(c_ore, c_clay, c_obsidian, c_geodes):
        max_ore = max(c_ore, c_clay, c_obsidian[0], c_geodes[0])

        most_geodes = 0
        queue = deque([(0, 0, 0, 0, 1, 0, 0, 0, 32)])
        visited = set()
        
        while queue:
            state = queue.pop()

            ore, clay, obsidian, geodes, r_ore, r_clay, r_obsidian, r_geodes, time = state
            ore = min(ore, max_ore*time)
            r_ore = min(r_ore, max_ore)
            clay = min(clay, c_obsidian[1]*time)
            r_clay = min(r_clay, c_obsidian[1])
            obsidian = min(obsidian, c_geodes[1]*time)
            r_obsidian = min(r_obsidian, c_geodes[1])
            state = ore, clay, obsidian, geodes, r_ore, r_clay, r_obsidian, r_geodes, time

            if state in visited:
                continue
            visited.add(state)

            ore, clay, obsidian, geodes, r_ore, r_clay, r_obsidian, r_geodes, time = state
            r_ore = min(r_ore, max_ore)

            n_ore = ore + r_ore
            n_clay = clay + r_clay
            n_obsidian = obsidian + r_obsidian
            n_geodes = geodes + r_geodes
            time -= 1

            if time == 0:
                most_geodes = max(n_geodes, most_geodes)
                continue

            if ore >= c_geodes[0] and obsidian >= c_geodes[1]:
                queue.append((n_ore - c_geodes[0], n_clay, n_obsidian - c_geodes[1], n_geodes, r_ore, r_clay, r_obsidian, r_geodes+1, time))
                continue
            if ore >= c_obsidian[0] and clay >= c_obsidian[1]:
                queue.append((n_ore - c_obsidian[0], n_clay - c_obsidian[1], n_obsidian, n_geodes, r_ore, r_clay, r_obsidian+1, r_geodes, time))
            if ore >= c_clay:
                queue.append((n_ore-c_clay, n_clay, n_obsidian, n_geodes, r_ore, r_clay+1, r_obsidian, r_geodes, time))
            if ore >= c_ore:
                queue.append((n_ore-c_ore, n_clay, n_obsidian, n_geodes, r_ore+1, r_clay, r_obsidian, r_geodes, time))
            
            queue.append((n_ore, n_clay, n_obsidian, n_geodes, r_ore, r_clay, r_obsidian, r_geodes, time))
            
        return most_geodes

    geode_sum = 1
    for line in data[:3]:
        blueprints = tuple(int(j) for j in re.findall(r"(\d+)", line)[1:])
        m = dfs(blueprints[0], blueprints[1], (blueprints[2], blueprints[3]), (blueprints[4], blueprints[5]))
        geode_sum *= m
        
    return geode_sum


if __name__ == "__main__":
    with open("day_19_input.txt", "r") as f:
        inp = f.readlines()
        #print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
