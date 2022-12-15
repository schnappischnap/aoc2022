import re


def part_1(data):
    search_row = 2000000
    positions = set()
    beacons = set()

    for line in data:
        sensor_x, sensor_y, beacon_x, beacon_y = (int(i) for i in re.findall("(-?\d+)", line))
        if beacon_y == search_row:
            beacons.add(beacon_x)
        beacon_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        search_row_distance = abs(search_row - sensor_y)
        sensor_length = beacon_distance - search_row_distance
        positions.update(range(sensor_x - sensor_length, sensor_x + sensor_length + 1))

    return len(positions.difference(beacons))


def part_2(data):
    limit = 4000000
    rows_ranges = [[] for _ in range(limit)]

    for line in data:
        sensor_x, sensor_y, beacon_x, beacon_y = (int(i) for i in re.findall("(-?\d+)", line))
        beacon_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        min_row = max(0, sensor_y - beacon_distance)
        max_row = min(limit, sensor_y + beacon_distance + 1)
        for row in range(min_row, max_row):
            sensor_length = beacon_distance - abs(row - sensor_y)
            min_x = max(0, sensor_x - sensor_length)
            max_x = min(limit, sensor_x + sensor_length + 1)
            if not rows_ranges[row]:
                rows_ranges[row] = [(min_x, max_x)]
            else:
                new_row_ranges = []
                for begin, end in rows_ranges[row]:
                    if begin <= max_x and end >= min_x:
                        min_x, max_x = (min(begin, min_x), max(end, max_x))
                    else:
                        new_row_ranges.append((begin, end))
                new_row_ranges.append((min_x, max_x))
                rows_ranges[row] = new_row_ranges
    
    for y, row_ranges in enumerate(rows_ranges):
        if len(row_ranges) > 1:
            return min(row_range[1] for row_range in row_ranges) * 4000000 + y


if __name__ == "__main__":
    with open("day_15_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
