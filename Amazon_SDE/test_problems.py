import unittest
import problem1
import problem2

class TestProblems(unittest.TestCase):

    def test_problem1(self):
        self.assertEqual(problem1.solve(3, [8, 5, 6, 25, 6, 16]), 41)

    def test_problem2(self):
        self.assertEqual(problem2.solve(3,'abc'),[6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(problem2.solve(4,'aabc'),[10, 5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()