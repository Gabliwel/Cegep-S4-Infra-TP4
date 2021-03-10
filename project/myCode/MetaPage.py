from myCode import MyUtils
from myCode.CustomExceptions import *

class MetaPage:
	MAGICNUMBER_MEMORYLAYOUT = "4D4C4D4C"
	MEMORYLAYOUT_VSML = "56534D4C"

	def __init__(self, sizeOfPages, nbPhysicalPages, nbSwapPages, nbBitmapPages, nbPageTablePages, nbPLTPages):
		if isinstance(sizeOfPages, int) and isinstance(nbPhysicalPages, int) and isinstance(nbSwapPages, int) and isinstance(nbBitmapPages, int) and isinstance(nbPageTablePages, int) and isinstance(nbPLTPages, int):
			self.__magicNumber = MetaPage.MAGICNUMBER_MEMORYLAYOUT 
			self.__memoryLayoutType = MetaPage.MEMORYLAYOUT_VSML
			self.__sizeOfPages = sizeOfPages
			self.__nbPhysicalPages = nbPhysicalPages
			self.__nbSwapPages = nbSwapPages
			self.__nbBitmapPages = nbBitmapPages
			self.__nbPageTablePages = nbPageTablePages
			self.__nbPLTPages = nbPLTPages
		else:
			raise ValueError("Parameters given to the MetaPage constructor must all be integers.")

	def getNbBitmapPages(self):
		return self.__nbBitmapPages

	def getNbPageTablePages(self):
		return self.__nbPageTablePages

	def getNbPLTPages(self):
		return self.__nbPLTPages

	def getNbOctetsInPage(self):
		return getNbOctetsInPage(self.__sizeOfPages)

	def toMap(self):
		map = dict()
		map['magicNumber'] = self.__magicNumber
		map['memoryLayoutType'] = self.__memoryLayoutType
		map['pageSize'] = self.__sizeOfPages
		map['nbPhysicalPages'] = self.__nbPhysicalPages
		map['nbSwapPages'] = self.__nbSwapPages
		map['nbBitmapPages'] = self.__nbBitmapPages
		map['nbPTPages'] = self.__nbPageTablePages
		map['nbPLTPages'] = self.__nbPLTPages
		return map

def getNbOctetsInPage(sizeOfPages):
	return 1024 * sizeOfPages //8

def peekPageSizeOctets(hexDump):
	magicNumber = MyUtils.extractSequence(hexDump, 0, 4)
	if magicNumber != MetaPage.MAGICNUMBER_MEMORYLAYOUT:
		raise MemoryDumpFormatException("MetaPage-peek: The provided hexDump does not appear to be a memory layout (magic number does not match expected value of " + MetaPage.MAGICNUMBER_MEMORYLAYOUT  + "): " + hexDump[0:20] + "...")
	memoryLayoutType = MyUtils.extractSequence(hexDump, 4, 4)
	if memoryLayoutType != MetaPage.MEMORYLAYOUT_VSML:
		raise MemoryDumpFormatException("MetaPage-peek: The provided hexDump does not appear to be a supported memory layout (memory layout type is not the expected value of " + MetaPage.MEMORYLAYOUT_VSML  + "): " + hexDump[8:20] + "...")
	sizeOfPages = MyUtils.extractSequence(hexDump, 8, 2)
	sizeOfPagesOctets = getNbOctetsInPage(MyUtils.hexToInt(sizeOfPages))
	return sizeOfPagesOctets

def parseFromHexDump(hexDump):
	sizeOfPagesOctets = peekPageSizeOctets(hexDump)
	if len(hexDump) < 2*sizeOfPagesOctets:
		raise ValueError("MetaPage: The size of the provided hexDump is smaller (" + str(len(hexDump)/2) + " octets) than a single page (" + str(sizeOfPagesOctets)  + " octets).")
	if len(hexDump) > 2*sizeOfPagesOctets:
		raise ValueError("MetaPage: The size of the provided hexDump is larger (" + str(len(hexDump)/2) + " octets) than a single page (" + str(sizeOfPagesOctets)  + " octets).")
	sizeOfPages = MyUtils.extractSequence(hexDump, 8, 2)
	nbPhysicalPages = MyUtils.extractSequence(hexDump, 10, 2)
	nbSwapPages = MyUtils.extractSequence(hexDump, 12, 2)
	nbBitmapPages = MyUtils.extractSequence(hexDump, 14, 2)
	nbPageTablePages = MyUtils.extractSequence(hexDump, 16, 2)
	nbPLTPages = MyUtils.extractSequence(hexDump, 18, 2)

	return MetaPage(MyUtils.hexToInt(sizeOfPages), MyUtils.hexToInt(nbPhysicalPages), MyUtils.hexToInt(nbSwapPages), MyUtils.hexToInt(nbBitmapPages), MyUtils.hexToInt(nbPageTablePages), MyUtils.hexToInt(nbPLTPages))


