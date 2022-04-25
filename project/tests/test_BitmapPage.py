import unittest

from myCode import BitmapPage
from myCode import MyUtils
from myCode.CustomExceptions import *


class BitmapPageTests(unittest.TestCase):

    defaultMap = dict()

    @classmethod
    def setUpClass(self):
        self.defaultMap['bitmapInfo'] = [2]

    def test_contructor(self):
        bitMapPage = BitmapPage.BitMap([2])
        self.assertEqual(self.defaultMap, bitMapPage.toMap())
        self.assertEqual([2], bitMapPage.getPagesList())

    def test_contructor2(self):
        self.assertRaises(ValueError, BitmapPage.BitMap, 64)

    def test_toMap(self):
        bitMapPage = BitmapPage.BitMap([2])
        map = bitMapPage.toMap()

        self.assertEqual(self.defaultMap, map)

    def test_parseFromHex6(self):
        hex = "FFE0000800200000000008000C000000"
        expectedResult = dict()
        expectedResult['bitmapInfo'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 28, 42, 84, 100, 101]
        bitmapPage = BitmapPage.getListOfPages(hex)
        self.assertEqual(expectedResult, bitmapPage.toMap())


    if __name__ == "__main__":
        unittest.main()
