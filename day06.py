from utils import get_input


def memory_reallocation(data):
    states = []
    steps = 0

    while str(data) not in states:
        states.append(str(data))
        idx = data.index(max(data))
        counter = data[idx]
        data[idx] = 0
        data = distribute_memory(data, counter, idx + 1)
        steps += 1

    cycle_size = len(states) - states.index(str(data))
    return (steps, cycle_size)


def distribute_memory(data, counter, idx):
    if counter <= 0:
        return data

    idx = idx if idx < len(data) else 0
    data[idx] += 1
    return distribute_memory(data, counter - 1, idx + 1)


if __name__ == "__main__":
    puzzle_input = get_input('day06')[0]
    puzzle_input = [int(x) for x in puzzle_input.split()]
    print(memory_reallocation([0, 2, 7, 0]))
    print(memory_reallocation(puzzle_input))
