import unittest

from myCode import MetaPage
from myCode import MyUtils
from myCode.CustomExceptions import *

class MetaPageTests(unittest.TestCase):

	defaultMap = dict()

	@classmethod
	def setUpClass(self):
		self.defaultMap['magicNumber'] = "4D4C4D4C"
		self.defaultMap['memoryLayoutType'] = "56534D4C"
		self.defaultMap['pageSize'] = 16
		self.defaultMap['nbPhysicalPages'] = 64
		self.defaultMap['nbSwapPages'] = 0
		self.defaultMap['nbBitmapPages'] = 1
		self.defaultMap['nbPTPages'] = 3
		self.defaultMap['nbPLTPages'] = 1

	def test_contructor(self):
		metaPage = MetaPage.MetaPage(16, 64, 0, 1, 3, 1)

		self.assertEqual(self.defaultMap, metaPage.toMap())

		self.assertEqual(1, metaPage.getNbBitmapPages())
		self.assertEqual(3, metaPage.getNbPageTablePages())
		self.assertEqual(1, metaPage.getNbPLTPages())

		self.assertEqual(2048, metaPage.getNbOctetsInPage())

	def test_contructor2(self):
		self.assertRaises(ValueError, MetaPage.MetaPage, "16", 64, 0, 1, 3, 1)
		self.assertRaises(ValueError, MetaPage.MetaPage, 16, 'c', 0, 1, 3, 1)
		self.assertRaises(ValueError, MetaPage.MetaPage, 16, 64, "0", 1, 3, 1)
		self.assertRaises(ValueError, MetaPage.MetaPage, 16, 64, 0, 1.44, 3, 1)
		self.assertRaises(ValueError, MetaPage.MetaPage, 16, 64, 0, 1, "3", 1)
		self.assertRaises(ValueError, MetaPage.MetaPage, 16, 64, 0, 1, 3, "1")

	def test_toMap(self):
		metaPage = MetaPage.MetaPage(16, 64, 0, 1, 3, 1)
		map = metaPage.toMap()

		self.assertEqual(self.defaultMap, map)

	def test_parseFromHex1(self):
		hex = "3D4C4D4C56534D4C000800400000000100030001"
		with self.assertRaises(MemoryDumpFormatException) as context:
			MetaPage.parseFromHexDump(hex)

	def test_parseFromHex2(self):
		hex = "4D4C4D4C57534D4C000800400000000100030001"
		with self.assertRaises(MemoryDumpFormatException) as context:
			MetaPage.parseFromHexDump(hex)

	def test_parseFromHex3(self):
		hex = "4D4C4D4C56534D4C000800400000000100030001"
		with self.assertRaises(ValueError) as context:
			MetaPage.parseFromHexDump(hex)


	def test_parseFromHex4(self):
		hex = "4D4C4D4C56534D4C001000400000000100030001"
		sizeOfPages = 16	
		totalSize =  MetaPage.getNbOctetsInPage(sizeOfPages) *2
		while len(hex) < totalSize:
			hex = hex + "00"
		metaPage = MetaPage.parseFromHexDump(hex)
		self.assertEqual(self.defaultMap, metaPage.toMap())


	def test_parseFromHex5(self):
		hex = "4D4C4D4C56534D4C001000400000000100030001"
		sizeOfPages = 16	
		totalSize =  MetaPage.getNbOctetsInPage(sizeOfPages) *2
		while len(hex) < totalSize:
			hex = hex + "00"
		hex = hex + "00"
		self.assertRaises(ValueError, MetaPage.parseFromHexDump, hex)

	def test_parseFromHex6(self):
		hex = "4D4C4D4C56534D4C001000400000000100030001"
		sizeOfPages = 16	
		totalSize =  MetaPage.getNbOctetsInPage(sizeOfPages) *2
		while len(hex) < totalSize:
			hex = hex + "00"
		metaPage = MetaPage.parseFromHexDump(hex)
		self.assertEqual(self.defaultMap, metaPage.toMap())

	def test_parseFromHex7(self):
		hex = "4D4C4D4C56534D4C001000400000000100030001"
		sizeOfPages = 16
		totalSize =  MetaPage.getNbOctetsInPage(sizeOfPages) *2
		while len(hex) < totalSize:
			hex = hex + "00"
		hex = hex + hex + hex + hex
		hex = hex[0:len(hex)-2]
		self.assertRaises(ValueError, MetaPage.parseFromHexDump, hex)


if __name__ == "__main__":
	unittest.main()

