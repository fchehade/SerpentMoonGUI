import unittest
from datetime import datetime, timedelta

from SerpentMoonGUI.Calculator.calculator import calculate_needed_points

event_ending = datetime(2022, 9, 26, 16, 0, 0)
event_start = event_ending - timedelta(days=60)


class TestCalculator(unittest.TestCase):
    def test_day_calculations(self):
        self.assertEqual(event_start, datetime(2022, 7, 28, 16, 0, 0))
        self.assertEqual(event_ending - timedelta(days=10), datetime(2022, 9, 16, 16, 0, 0))

    def test_xp_needed(self):
        self.assertEqual(calculate_needed_points(1, 0, date_to_compare=event_start), 411.67)
        self.assertEqual(calculate_needed_points(9, 1000, date_to_compare=datetime(2022, 8, 7, 22, 0, 0)), 361.22)
        self.assertEqual(calculate_needed_points(19, 2200, date_to_compare=datetime(2022, 9, 25, 15, 0, 0)), 0.0)


if __name__ == '__main__':
    unittest.main()
