def part_1(data):
    def to_snafu(decimal):
        conversion = ["=", "-", "0", "1", "2"]
        snafu = []
        while decimal > 0:
            decimal, remainder = divmod(decimal + 2, 5)
            snafu.append(conversion[remainder])
        return "".join(reversed(snafu))

    def to_decimal(snafu):
        conversion = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
        decimal = 0
        for i, c in enumerate(reversed(snafu)):
            decimal += conversion[c] * (5 ** i)
        return decimal

    return to_snafu(sum(to_decimal(line.strip()) for line in data))


if __name__ == "__main__":
    with open("day_25_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
