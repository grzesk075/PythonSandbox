from unittest import TestCase, main

from codility.binary_gap import solution


class TestBinaryGap(TestCase):
    def test_solution(self):
        self.assertEqual(solution(0), 0)
        self.assertEqual(solution(1), 0)
        self.assertEqual(solution(2), 0)
        self.assertEqual(solution(3), 0)
        self.assertEqual(solution(4), 0)
        self.assertEqual(solution(5), 1)
        self.assertEqual(solution(6), 0)
        self.assertEqual(solution(7), 0)
        self.assertEqual(solution(8), 0)
        self.assertEqual(solution(9), 2)
        self.assertEqual(solution(1041), 5)
        self.assertEqual(solution((1 << 31) - 1), 0)


if __name__ == '__main__':
    main()
