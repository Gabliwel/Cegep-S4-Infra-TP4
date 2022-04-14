from myCode import MyUtils


class BitMap :

    def __init__(self, nbBitmapPages):
            self.__nbBitmapPages = nbBitmapPages
                
    def toMap(self):
        map = dict()
        map['bitmapInfo'] = self.__nbBitmapPages
        return map

def getListOfPages(hexDump):
    bitmapSequence = MyUtils.extractSequence(hexDump, 0, 4)
    binaryBitmap = str(bin(int(hexDump, 16)) [2:])

    bitmapPagesList = []

    for i, number in enumerate(binaryBitmap):
        if(number == '1') :
            bitmapPagesList.append(i)
    return bitmapPagesList

def parseFromHexDump(hexDump):
    nbBitmapPages = getListOfPages(hexDump)
    return BitMap(nbBitmapPages)
