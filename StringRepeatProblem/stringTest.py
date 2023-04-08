import unittest
import stringRepeat 

class TestStringRepeat(unittest.TestCase):
    def test_oddValue(self):
        result = stringRepeat.solution(5)
        self.assertEqual(result, "+-+-+")

    def test_evenValue(self):
        result = stringRepeat.solution(6)
        self.assertEqual(result, "+-+-+-")

    def test_moreThan100(self):
        result = stringRepeat.solution(101)
        self.assertEqual(result, "N should be between 1-100")

    def test_lessThan1(self):
        result = stringRepeat.solution(0)
        self.assertEqual(result, "N should be between 1-100")

    def test_minusValue(self):
        result = stringRepeat.solution(-5)
        self.assertEqual(result, "N should be between 1-100")
        
    def test_equalOne(self):
        result = stringRepeat.solution(1)
        self.assertEqual(result, "+")
