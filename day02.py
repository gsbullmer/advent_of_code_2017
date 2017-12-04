from utils import get_input


def corruption_checksum(data):
    # sum_digits = list(map(lambda row: max(row) - min(row), data))  # part 1
    sum_digits = list(map(lambda row: divisor(row), data))  # part 2
    return sum(sum_digits)


def divisor(row):
    row.sort()
    row.reverse()
    for idx1 in range(len(row)):
        for idx2 in range(idx1 + 1, len(row)):
            if row[idx1] % row[idx2] is 0:
                return int(row[idx1] / row[idx2])
    return


if __name__ == "__main__":
    puzzle_input = get_input('day02')
    puzzle_input = list(map(
        lambda row: list(map(
            lambda x: int(x), row.split('\t'))
        ),
        puzzle_input))
    print(corruption_checksum(puzzle_input))
