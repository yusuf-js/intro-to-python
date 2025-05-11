#mobil

class mobil:
    nama_mobil = "default"
    _default_ban = 4

    def __init__(self,nama):
        self.nama_mobil = nama
        
    def getMerek(self):
        return f"merek mobil : {self.nama_mobil}\nJumlah ban : {self._default_ban} Ban"
    
    def setBan(self,jumlah_ban):
        self._defulat_ban = jumlah_ban

honda = mobil("puso")
honda.setBan(8)
print(f"{honda.getMerek()}")