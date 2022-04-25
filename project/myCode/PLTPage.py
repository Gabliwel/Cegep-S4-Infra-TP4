from myCode import PLTEntry
from myCode import PTPage
from myCode import PTEntry
from myCode import PageBroker

class PLTPage :

    def __init__(self, PLT_list):

        if isinstance(PLT_list, dict):
            self.__PLT_list = PLT_list
        else:
            raise ValueError(
                "Parameter given to the PLTPage constructor must be a dict.")
                    
    def toMap(self):
        map = dict()
        map['pltInfo'] = self.__PLT_list
        return map

def getListOfProcesses(hexDump):
    map = dict()

    listProcess = []
    pagesList = PTPage.getDictionary(hexDump, PageBroker.getPage(1)).getPagesList()
    for key, element in pagesList.items():
        listProcess = list(set(listProcess + element['ACL']))
    return listProcess

def getDictionary(hexDump):
    map = dict()
    pagesList = getListOfProcesses(hexDump)
    for i in pagesList:
        map[i] = PLTEntry.getProcessusPages(hexDump, i).toMap()
    return PLTPage(map)
    
