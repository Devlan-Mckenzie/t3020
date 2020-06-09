import unittest
import t3020

class TestRow(unittest.TestCase):

	def test_row1(self):
		n = 1
		prev = [44,2,3,4,5,6,7,8,9]
		curr_str = [116,11,12,13,14,15,16,17,18]
		r1 = t3020.check_row(n,prev,curr_str)
		self.assertEqual(r1,1)

	def test_row2(self):
		n = 2
		prev = [44,2,3,4,5,6,7,8,9]
		curr_str = [100,11,12,13,14,15,16,17,18]
		r2 = t3020.check_row(n,prev,curr_str)
		self.assertEqual(r2,0)

	if __name__ == '__main__':

	unittest.main()
