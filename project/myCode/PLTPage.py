from myCode import PLTEntry
from myCode import PTPage
from myCode import PTEntry
from myCode import PageBroker

class PLTPage :

    def __init__(self, ACL_list):
        self.__ACL_list = ACL_list
                    
    def toMap(self):
        map = dict()
        map['pltInfo'] = self.__ACL_list
        return map

def getListOfProcesses(hexDump):
    map = dict()

    listProcess = []
    pagesList = PTPage.getDictionary(hexDump, PageBroker.getPage(1)).getList()
    for key, element in pagesList.items():
        listProcess = list(set(listProcess + element['ACL']))
    return listProcess

def getDictionary(hexDump):
    map = dict()
    pagesList = getListOfProcesses(hexDump)
    for i in pagesList:
        map[i] = PLTEntry.getProcessusPages(hexDump, i).toMap()
    return PLTPage(map)
    
