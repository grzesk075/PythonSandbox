from unittest import TestCase, main

from codility.cyclic_rotation import solution


class TestCyclicRotation(TestCase):
    def test_solution(self):
        self.assertEqual(solution([3], 123), [3])
        self.assertEqual(solution([3, 5], 1), [5, 3])
        self.assertEqual(solution([3, 5], 2), [3, 5])
        self.assertEqual(solution([3, 5], 3), [5, 3])
        self.assertEqual(solution([3, 5], 5), [5, 3])
        self.assertEqual(solution([3, 5], 7), [5, 3])
        self.assertEqual(solution([3, 5], 4), [3, 5])
        self.assertEqual(solution([7, 3, 5], 1), [5, 7, 3])
        self.assertEqual(solution([7, 3, 5], 4), [5, 7, 3])
        self.assertEqual(solution([7, 3, 5], 7), [5, 7, 3])
        self.assertEqual(solution([7, 3, 5], 2), [3, 5, 7])
        self.assertEqual(solution([7, 3, 5], 5), [3, 5, 7])
        self.assertEqual(solution([7, 3, 5], 8), [3, 5, 7])
        self.assertEqual(solution([7, 3, 5], 3), [7, 3, 5])
        self.assertEqual(solution([7, 3, 5], 6), [7, 3, 5])
        self.assertEqual(solution([7, 3, 5], 9), [7, 3, 5])
        self.assertEqual(solution([-1, -2, -3, -4, -5, -6], 10), [-3, -4, -5, -6, -1, -2])


if __name__ == '__main__':
    main()
