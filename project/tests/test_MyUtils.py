import unittest

from myCode.MyUtils import *

class MyUtilsTests(unittest.TestCase):

	def test_hexToInt(self):
		self.assertEqual(16, hexToInt('10'))
		self.assertEqual(15, hexToInt('F'))
		self.assertEqual(17, hexToInt('11'))
		self.assertEqual(32, hexToInt('20'))

	def test_extractSequence1(self):
		self.assertRaises(ValueError, extractSequence, "AABBCCDDEEFF", -3, 3)

	def test_extractSequence2(self):
		self.assertRaises(ValueError, extractSequence, "AABBCCDDEEFF", 0, 7)

	def test_extractSequence3(self):
		self.assertRaises(ValueError, extractSequence, "AABBCCDDEEFF", 4, 3)

	def test_extractSequence4(self):
		dataBlock = "AABBCCDDEEFF"
		expected = "AABBCCDDEEFF"
		actual =extractSequence(dataBlock, 0, 6)
		self.assertEqual(expected, actual)

	def test_extractSequence5(self):
		dataBlock = "AABBCCDDEEFF"
		expected = "BBCC"
		actual =extractSequence(dataBlock, 1, 2)
		self.assertEqual(expected, actual)

	def test_extractSequence6(self):
		dataBlock = "AABBCCDDEEFF"
		expected = ""
		actual =extractSequence(dataBlock, 3, 0)
		self.assertEqual(expected, actual)

	def test_extractSequence7(self):
		dataBlock = "AABBCCDDEEFF"
		expected = "EEFF"
		actual =extractSequence(dataBlock, 4, 2)
		self.assertEqual(expected, actual)

	def test_extractSequence8(self):
		dataBlock = "AABBCCDDEEFF"
		expected = "AABBCC"
		actual =extractSequence(dataBlock, 0, 3)
		self.assertEqual(expected, actual)

	def test_readBlockFromFileInHex(self):
		actual = readBlockFromFileInHex("./project/files/MemoryLayout1.vsml", 0, 20)
		expected = "4D4C4D4C56534D4C001000400000000100020001" #len = 40
		self.assertEqual(expected, actual)


if __name__ == "__main__":
	unittest.main()

