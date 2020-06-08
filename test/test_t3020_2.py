import unittest
import pytest
import t3020

class TestMonotonic(unittest.TestCase):

	@pytest.fixture(autouse=True)
	def _pass_fixtures(self,capsys):
		self.capsys = capsys
	def test_mono1(self):
		prev = [1,2,3,4,5,6,7,8,9]
		curr = [10,11,12,13,14,15,16,17,18]
		t3020.check_monotonic(prev,curr)
		captured = self.capsys.readouterr()
		self.assertEqual('',captured.out)

	if __name__ == '__main__':

	unittest.main()
