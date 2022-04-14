from myCode import PTEntry
from myCode import BitmapPage

class PTPage :

    def __init__(self, PT_list):
            self.__PT_list = PT_list
                    
    def toMap(self):
        map = dict()
        map['ptinfo'] = self.__PT_list
        return map
    
    def getList(self):
        return self.__PT_list

def getDictionary(hexDump, pageList):
    map = dict()
    pagesList = BitmapPage.getListOfPages(pageList)
    for i in pagesList:
        map[i] = PTEntry.parseFromHexDump(hexDump, i).toMap()
    return PTPage(map)
