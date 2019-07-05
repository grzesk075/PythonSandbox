from unittest import TestCase, main

from codility.odd_occurrences_in_array import solution


class TestOddOccurrencesInArray(TestCase):
    def test_solution(self):
        self.assertEqual(solution([1, 7, 1, 7, 8, 8, 9, 2, 3, 2, 3]), 9)
        self.assertEqual(solution([1, 5, 1000000000, 1, 1000000000, 1, 1000000000, 5, 9, 1, 1000000000, 3, 6, 6, 3]), 9)
        self.assertEqual(solution([5]), 5)
        self.assertEqual(solution([1, 1000000000, 1000000000]), 1)
        self.assertEqual(solution([1, 1, 1000000000]), 1000000000)
        self.assertEqual(solution([1, 1, 1, 1, 1000000000]), 1000000000)
        self.assertEqual(solution([12] * 100000 + [1] * 100000 + [7] + [1000000000] * 700000 + [345] * (100000 - 2)), 7)


if __name__ == '__main__':
    main()
