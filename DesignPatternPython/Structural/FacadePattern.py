from abc import ABC
class CcService:
    def getHistoryCalling(self,account):
        print("Call CC Service to get History calling of %s"%(account))

    def getComplaintHistory(self,account):
        print("Call CC Service to get complain history of %s"%(account))

class CmService:
    def getSubInfo(self,account):
        print("Call CM Service to get sub info of: %s" %(account))

    def getSubType(self,account):
        print("Call CM Service to get sub type of: %s"%(account))



class SubFacade:
    __ccService: None
    __cmService: None

    def __init__(self):
        self.__ccService = CcService()
        self.__cmService = CmService()

    def getAllInforOfSub(self, account):
        self.__cmService.getSubInfo(account)
        self.__cmService.getSubType(account)

    def getHistoryComplaintOfSub(self,account):
        self.__ccService.getComplaintHistory(account)
        self.__ccService.getHistoryCalling(account)

if __name__ == "__main__":
    __instance = SubFacade()
    __instance.getAllInforOfSub("h004_gftth_aaa")
    __instance.getHistoryComplaintOfSub("h004_gftth_aaa")