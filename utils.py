def get_input(input_name):
    f = open(input_name + '_input.txt', 'r')
    puzzle_input = f.readlines()
    f.close()
    return puzzle_input
