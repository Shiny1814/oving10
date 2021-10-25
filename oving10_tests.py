import unittest
from oving10 import Question
# test check_ans, correct_ans_text

class Tests(unittest.TestCase):
    def test_check_ans(self):
        q1 = Question("q?", ["a1", "a2", "a3"], 1)
        self.assertTrue(q1.check_ans(1))
        self.assertFalse(q1.check_ans(3))
    def test_correct_ans_text(self):
        q1 = Question("q?", ["a1", "a2", "a3"], 1)
        self.assertEqual(q1.correct_ans_text(), "Korrekt svar: a1")

if __name__ == "__main__":
    unittest.main()
