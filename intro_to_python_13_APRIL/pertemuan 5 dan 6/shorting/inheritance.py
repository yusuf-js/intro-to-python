class ibu:
    panggilan = "ini punya ibu"

    def memanggil(self):
        print("iya, ada apa?")

    def setsifat(self,sifat):
        self.__sifat = sifat

    def getsifat(self):
        print(f"sifat ibu {self.__sifat}")

class anak(ibu):
    def suruh(self):
        print("nanti dulu lah")


toni = anak()
toni.panggilan = "toni"
print(f"siapa nama anak ini : {toni.panggilan}")
toni.memanggil()
toni.suruh()
toni.setsifat("baik")
toni.getsifat()