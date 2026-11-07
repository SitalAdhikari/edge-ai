import unittest
from statistics_utils import *

class TestStatistics( unittest.TestCase):
	def test_mean(self):
		self.assertEqual(calculate_mean([10, 20, 30]), 20)
	def test_median_odd(self):
		self.assertEqual(calculate_median([30, 10, 20]), 20)
	def test_median_even(self):
		self.assertEqual(calculate_median([10, 20, 30, 40]), 25)
	def test_minimum_and_maximum(self):
		self.assertEqual(calculate_min([8, 3, 5]), 3)
		self.assertEqual(calculate_max([8, 3, 5]), 8)
	
	def test_empty_input(self):
		with self.assertRaises(ValueError):
			calculate_mean([])
	
	def test_negative_value(self):
		with self.assertRaises(ValueError):
			calculate_mean([10, -2, 5])
			
	def test_non_numeric_value(self):
		with self.assertRaises(ValueError):
			calculate_mean([10, "hello", 20])
            
if __name__ == "__main__":
	unittest.main()            
