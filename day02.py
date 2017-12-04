from utils import get_input


def corruption_checksum(data):
    sum_digits = list(map(lambda x: max(x) - min(x), data))  # part 1
    return sum(sum_digits)

if __name__ == "__main__":
    puzzle_input = get_input('day02')
    puzzle_input = list(map(
        lambda row: list(map(
            lambda x: int(x), row.split('\t'))
        ),
        puzzle_input))
    print(corruption_checksum(puzzle_input))
