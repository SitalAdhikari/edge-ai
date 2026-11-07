import unittest

from benchmark_toolkit.statistics import calculate_statistics

class TestCalculateStatistics(unittest.TestCase):

    def setUp(self):
		"""managing the values"""
        self.values = [10, 20, 30, 40, 50]
        self.result = calculate_statistics(self.values)

    def test_count(self):
		"""Counting the total measurements"""
        self.assertEqual(self.result["count"], 5)

    def test_minimum(self):
		"""calculating the minimum value"""
        self.assertEqual(self.result["min"], 10.0)

    def test_maximum(self):
		"""calculating the maximum value"""
        self.assertEqual(self.result["max"], 50.0)

    def test_mean(self):
		"""calculating the mean"""
        self.assertEqual(self.result["mean"], 30.0)

    def test_median(self):
        self.assertEqual(self.result["median"], 30.0)

    def test_standard_deviation(self):
        self.assertAlmostEqual(self.result["std"], 14.1421356, places=5)

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            calculate_statistics([])

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            calculate_statistics([10, -5, 20])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate_statistics([10, "abc", 20])

    def test_nan_input(self):
        with self.assertRaises(ValueError):
            calculate_statistics([10, float("nan"), 20])

    def test_infinity_input(self):
        with self.assertRaises(ValueError):
            calculate_statistics([10, float("inf"), 20])


if __name__ == "__main__":
    unittest.main()
