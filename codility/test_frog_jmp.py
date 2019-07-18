from unittest import TestCase, main

from codility.frog_jmp import solution


class TestFrogJmp(TestCase):
    def test_solution(self):
        self.assertEqual(solution(1, 1, 1), 0)
        self.assertEqual(solution(1000000000, 1000000000, 1000000000), 0)
        self.assertEqual(solution(1000000000, 1000000000, 1), 0)
        self.assertEqual(solution(1, 1, 1000000000), 0)
        self.assertEqual(solution(1, 2, 1000000000), 1)
        self.assertEqual(solution(1, 2, 1), 1)
        self.assertEqual(solution(1, 5, 4), 1)
        self.assertEqual(solution(1, 5, 3), 2)
        self.assertEqual(solution(1, 5, 2), 2)


if __name__ == '__main__':
    main()
