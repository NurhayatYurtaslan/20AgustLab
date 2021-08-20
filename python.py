class savasci:
    def __init__(self,atak = 20 ,defans = 10, isim = "Default Savaşçı"):
        self.atak = atak
        self.defans = defans 
        self.can = 100
        self.isim = isim
    def setAtak(self,atak):
        self.atak = atak
    def setDefans(self, defans):
        self.defans = defans
    def getAtak(self):
        return self.atak
    def getDefans(self):
        return self.defans

    def setCan(self,can):
        self.can = can
    def getCan(self):
        return self.can