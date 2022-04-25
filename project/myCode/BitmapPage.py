from myCode import MyUtils
from myCode import MetaPage


class BitMap:

    def __init__(self, bitmapPages):
        if isinstance(bitmapPages, list):
            self.__bitmapPages = bitmapPages
        else:
            raise ValueError(
                "Parameter given to the BitmapPage constructor must be a list.")
        
    def getPagesList(self):
        return self.__bitmapPages

    def toMap(self):
        map = dict()
        map['bitmapInfo'] = self.__bitmapPages
        return map


def getListOfPages(hexDump):
    bitmapSequence = MyUtils.extractSequence(hexDump, 0, 4)
    binaryBitmap = str(bin(int(hexDump, 16))[2:])

    bitmapPagesList = []

    for i, number in enumerate(binaryBitmap):
        if(number == '1'):
            bitmapPagesList.append(i)
    return BitMap(bitmapPagesList)
