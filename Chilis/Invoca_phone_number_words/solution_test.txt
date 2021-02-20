import unittest

solution = __import__("solution")


class TestSolution(unittest.TestCase):

    def test_solution(self):
        correct = ["jcatd", "jcate", "jcatf", "kcatd", "kcate", "kcatf",
                   "lcatd", "lcate", "lcatf"]
        self.assertEqual(solution.findCombinations
                              ("52283", "cat"), correct)


if __name__ == "__main__":
    unittest.main()
