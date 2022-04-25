from myCode import PTEntry
from myCode import BitmapPage

class PTPage :

    def __init__(self, PT_list):
        if isinstance(PT_list, dict):
            self.__PT_list = PT_list
        else:
            raise ValueError(
                "Parameter given to the PTPage constructor must be a dict.")
        
    def getPagesList(self):
        return self.__PT_list
                    
    def toMap(self):
        map = dict()
        map['ptinfo'] = self.__PT_list
        return map

def getDictionary(hexDump, pageList):
    map = dict()
    pagesList = BitmapPage.getListOfPages(pageList)
    for i in pagesList.getPagesList():
        map[i] = PTEntry.parseFromHexDump(hexDump, i).toMap()
    return PTPage(map)
