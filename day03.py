import unittest
from math import sqrt, ceil, floor


def spiral_memory(data):
    if data == 1:
        return 0

    side = side_length(data)
    axis = (side - 1) / 2
    sides = map(lambda i: side ** 2 - ((side - 1) * i) - floor(side / 2),
                range(0, 4))
    offset = min([abs(side - data) for side in sides])

    return axis + offset


def side_length(num):
    base = ceil(sqrt(num))
    side = base if base % 2 != 0 else base + 1
    return side


class tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(spiral_memory(1), 0)

    def test_2(self):
        self.assertEqual(spiral_memory(11), 2)

    def test_3(self):
        self.assertEqual(spiral_memory(23), 2)

    def test_4(self):
        self.assertEqual(spiral_memory(1024), 31)


if __name__ == "__main__":
    print(spiral_memory(289326))
    # unittest.main()
