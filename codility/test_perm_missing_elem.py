from unittest import TestCase, main

from codility.perm_missing_elem import solution


class TestOddOccurrencesInArray(TestCase):
    def test_solution(self):
        self.assertEqual(solution([1]), 2)
        self.assertEqual(solution([2]), 1)
        self.assertEqual(solution([1, 3]), 2)
        self.assertEqual(solution([3, 1]), 2)
        self.assertEqual(solution([2, 3]), 1)
        self.assertEqual(solution([2, 1]), 3)
        self.assertEqual(solution([2, 3, 5, 1]), 4)

        N = 100000
        A = list(range(1, N + 2))
        missing = 23974
        del (A[missing - 1])
        self.assertEqual(solution(A), missing)


if __name__ == '__main__':
    main()
