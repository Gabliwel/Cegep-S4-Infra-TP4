from myCode import MetaPage
from myCode import MyUtils


DUMP_FILE = "/mnt/data/files/dump.vsml"

def getPage(pageNumber):
	fileName = DUMP_FILE

	#First, we load the first part of the MetaPage to get the pageSize
	pageSizeOctets = 128 #a first guess, should be enough to get at least up to the pageSize part of the Metapage
	dump = MyUtils.readBlockFromFileInHex(fileName, 0, pageSizeOctets)
	pageSizeOctets = MetaPage.peekPageSizeOctets(dump)

	#now we know the true pageSize of the memory dump, we can now get the page we want.
	offset = pageSizeOctets*pageNumber

	dump = MyUtils.readBlockFromFileInHex(fileName, offset, pageSizeOctets)
	return dump
