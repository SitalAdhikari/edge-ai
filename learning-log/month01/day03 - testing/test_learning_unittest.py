import unittest
from learning_unittest import *

class Testfn(unittest.TestCase):
	def test_add_positive(self):
		self.assertEqual(add(2,3),5)
		# self.assertEqual(cal_real_value, expected_value)
	
	def test_add_negative(self):
		self.assertEqual(add(-2,-3),-5)


if __name__ == "__main__":
	unittest.main()
