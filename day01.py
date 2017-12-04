from utils import get_input


def reverse_captcha(string):
    digits = list(map(lambda d: int(d), string))
    # offset = 1  # part 1: next digit in circular list
    offset = int(len(digits) / 2)  # part 2: digit halfway around circular list
    next_digits = iter(digits[offset:] + digits[:-offset])
    sum_digits = list(filter(lambda x: x == next(next_digits), digits))
    return sum(sum_digits)

if __name__ == "__main__":
    puzzle_input = get_input('day01')
    print(reverse_captcha(puzzle_input))
