from utils import get_input


def traverse_maze(maze):
    i = 0
    steps = 0

    while 0 <= i < len(maze):
        # print(i, steps)  # `print()` is slow
        new_i = i + maze[i]
        if maze[i] >= 3:    # part 2
            maze[i] -= 1
        else:               # part 1
            maze[i] += 1
        i = new_i
        steps += 1

    return steps


if __name__ == "__main__":
    puzzle_input = get_input('day05')
    puzzle_input = [int("".join(x.split())) for x in puzzle_input]
    print(traverse_maze(puzzle_input))
    # print(traverse_maze([0, 3, 0, 1, -3]))
