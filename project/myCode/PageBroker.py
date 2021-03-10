from myCode import MetaPage
from myCode import MyUtils


#TODO remove for students
from os import path
def isInProd():
	if path.exists("/mnt/code/prod.txt"): #TODO maybe use an env variable instead
		return True
	return False

def getDumpFileName():
	if isInProd():
		#For prod
		date = datetime.now() - timedelta(hours=5)
		date = date.strftime('%d')

		fileName = "./project/files/MemoryLayout1.vsml"
		if int(date) % 2 == 0:
			fileName = "./project/files/MemoryLayout1b.vsml"
		return fileName
	else:
	#for test
		return DUMP_FILE
#################


DUMP_FILE = "/mnt/data/files/dump.vsml"

def getPage(pageNumber):
#TODO switch the following lines for students
	fileName = getDumpFileName()
	#fileName = DUMP_FILE

	#First, we load the first part of the MetaPage to get the pageSize
	pageSizeOctets = 128 #a first guess, should be enough to get at least up to the pageSize part of the Metapage
	dump = MyUtils.readBlockFromFileInHex(fileName, 0, pageSizeOctets)
	pageSizeOctets = MetaPage.peekPageSizeOctets(dump)

	#now we know the true pageSize of the memory dump, we can now get the page we want.
	offset = pageSizeOctets*pageNumber

	dump = MyUtils.readBlockFromFileInHex(fileName, offset, pageSizeOctets)
	return dump
