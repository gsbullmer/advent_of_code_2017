from utils import get_input


def high_entropy_passphrases(data):
    return len(list(filter(remove_dups, data)))


def remove_dups(data):
    l = data.split()  # part 1
    l = list(map(sort_word, l))  # add for part 2
    original_len = len(l)
    set_len = len(set(l))
    print(original_len, set_len)
    return original_len == set_len


def sort_word(string):
    s = [char for char in string]
    s.sort()
    return "".join(s)


if __name__ == "__main__":
    puzzle_input = get_input('day04')
    print(high_entropy_passphrases(puzzle_input))
