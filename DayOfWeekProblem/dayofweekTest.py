import unittest
import dayOfWeek 

class TestdayOfWeek(unittest.TestCase):
    def testValidInput(self):
        self.assertEqual(dayOfWeek.solution("Mon", 3), "Thu")
        self.assertEqual(dayOfWeek.solution("Tue", 10), "Fri")
        self.assertEqual(dayOfWeek.solution("Sun", 7), "Sun")

    def test_invalidk(self):
        self.assertEqual(dayOfWeek.solution("Wed", -1), "k must be between 0 and 500")
        self.assertEqual(dayOfWeek.solution("Thu", 501), "k must be between 0 and 500")

    def test_invalid_day(self):
        self.assertEqual(dayOfWeek.solution("Monday", 2), "Monday is not on the list")
        self.assertEqual(dayOfWeek.solution("XYZ", 5), "XYZ is not on the list")
