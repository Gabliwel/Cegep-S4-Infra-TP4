from myCode import MetaPage
from myCode import MyUtils


DUMP_FILE = "/mnt/data/files/dump.vsml"

class PTEntry :

    def __init__(self, ACL_list, isSwappedOut, pageId, pageLocation):
        if isinstance(isSwappedOut, bool) and isinstance(pageId, int) and isinstance(pageLocation, int) and isinstance(ACL_list, list):
            self.__isSwappedOut = isSwappedOut
            self.__pageId = pageId
            self.__pageLocation = pageLocation
            self.__ACL_list = ACL_list

        else:
            raise ValueError("Parameters given to the MetaPage constructor must all be integers.")
                    
    def toMap(self):
        map = dict()
        map['ACL'] = self.__ACL_list
        map['isSwappedOut'] = self.__isSwappedOut
        map['pageId'] = self.__pageId
        map['page location'] = self.__pageLocation
        return map

    
    def getACLList(self):
	    return self.__ACL_list

def getPTEntrySizeWithPageNumber(hexDump, pageNumber):
    size = MetaPage.peekPageSizeOctets(hexDump)
    size = (MetaPage.parseFromHexDump(hexDump).getNbBitmapPages() + 1 ) * size
    size = size + (64*pageNumber)
    return size

	#def test_getPTEntryDataWithSize(self, mock_utils): AUCUNE UTILITÉE À TESTER CETTE FONCTION
def getPTEntryDataWithSize(hexDump, pageNumber):
    size = getPTEntrySizeWithPageNumber(hexDump, pageNumber)
    data = MyUtils.readBlockFromFileInHex(DUMP_FILE, size, 32) # 32 pour la longueur de l'entrée
    return data

def parseFromHexDump(hexDump, pageNumber):
    data = getPTEntryDataWithSize(hexDump, pageNumber)
    ACL_list = [0]
    i = 2 # Afin de passer les deux premiers octets
    while (MyUtils.extractSequence(data, i, 1)) != '00' :
            processus = MyUtils.hexToInt(MyUtils.extractSequence(data, i, 1))
            ACL_list.append(int(processus))
            i += 1
    isSwappedOut = (MyUtils.extractSequence(data, 0, 1) == 00)
    pageId = pageNumber
    pageLocation = MyUtils.hexToInt(MyUtils.extractSequence(data, 1, 1))
    return PTEntry(ACL_list, isSwappedOut, pageId, pageLocation)