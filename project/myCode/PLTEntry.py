from myCode import MetaPage
from myCode import MyUtils
import logging

DUMP_FILE = "/mnt/data/files/dump.vsml"

class PLTEntry :

    def __init__(self, ACL_list):
        if isinstance(ACL_list, list):
            self.__ACL_list = ACL_list
        else:
            raise ValueError(
                "Parameter given to the BitmapPage constructor must be a list.")
        
                    
    def toMap(self):
        map = self.__ACL_list
        return map

def getPLTEntrySizeWithPageNumber(hexDump, processusNumber):
    nbOfPagesToSkip = MetaPage.parseFromHexDump(hexDump).getNbBitmapPages() + MetaPage.parseFromHexDump(hexDump).getNbPageTablePages() + 1
    size = MetaPage.peekPageSizeOctets(hexDump)
    size = nbOfPagesToSkip * size
    size = size + (32*processusNumber) # 32 octets taille d'une page plt
    return size

def removePLTEntryDataExtraZeros(hexDump, processusNumber):
    size = getPLTEntrySizeWithPageNumber(hexDump, processusNumber)
    data = MyUtils.readBlockFromFileInHex(DUMP_FILE, size, 32) # 32 pour la longueur de l'entrée
    data = data.rstrip("0") 
    if(len(data) % 2 != 0): # Enlever les zéros de trop et en rajouter un si le nombre est impair
        data += "0"
    return data

def getProcessusPages(hexDump, processusNumber):
    i = 1
    pages = []
    data = removePLTEntryDataExtraZeros(hexDump, processusNumber)
    while i < len(data) / 2 :
            processusPage = MyUtils.hexToInt(MyUtils.extractSequence(data, i, 1))
            pages.append(processusPage)
            i += 1
    return PLTEntry(pages)