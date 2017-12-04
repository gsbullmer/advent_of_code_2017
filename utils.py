def get_input(input_name):
    f = open(input_name + '_input.txt', 'r')
    puzzle_input = f.readline()
    f.close()
    return puzzle_input
