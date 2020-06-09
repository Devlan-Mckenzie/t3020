import unittest

import t3020

class TestTotal(unittest.TestCase):

	def test_total1(self):
		curr = [1,2,3,4,5,6,7,8,9]
		t1 = t3020.calc_total(curr)
		self.assertEqual(t1,44)

	def test_total2(self):
		curr = [10,11,12,13,14,15,16,17,18]
		t2 = t3020.calc_total(curr)
		self.assertEqual(t2,116)

	if __name__ == '__main__':

	unittest.main()
