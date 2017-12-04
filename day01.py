from utils import get_input


def reverse_captcha(string):
    digits = list(map(lambda d: int(d), string))
    next_digits = iter(digits[1:] + digits[:-1])
    sum_digits = list(filter(lambda x: x == next(next_digits), digits))
    return sum(sum_digits)

if __name__ == "__main__":
    puzzle_input = get_input('day01')
    print(reverse_captcha(puzzle_input))
