class Lagu:
    def __init__(self, penyanyi, judul, tahun):
        self.penyanyi = penyanyi
        self.judul = judul
        self.tahun = tahun

class Playlist():
    def __init__(self, daftar_lagu, lagu_yang_dimainkan_saat_ini):
        self.daftar_lagu = daftar_lagu
        self.__urutan_lagu_yang_dimainkan_saat_ini = lagu_yang_dimainkan_saat_ini
    
    def __pindah_lagu(self):
        pass
    
    def putar(self):
        print("Sedang memutar lagu " + self.daftar_lagu[self.__urutan_lagu_yang_dimainkan_saat_ini].judul)
    
    def putar_lagu_selanjutnya(self):
        print("Sedang memutar lagu " + self.daftar_lagu[self.__urutan_lagu_yang_dimainkan_saat_ini].judul)
    
    def putar_lagu_sebelumnya(self):
        print("Sedang memutar lagu " + self.daftar_lagu[self.__urutan_lagu_yang_dimainkan_saat_ini].judul)
    
    def putar_lagu_pertama(self):
        print("Sedang memutar lagu " + self.daftar_lagu[self.__urutan_lagu_yang_dimainkan_saat_ini].judul)
    
    def putar_lagu_terkahir(self):
        print("Sedang memutar lagu " + self.daftar_lagu[self.__urutan_lagu_yang_dimainkan_saat_ini].judul)
    
    def mencetak_lagu(self):
        print(self.daftar_lagu)

lagu1 = Lagu("Ungu", "Laguku", 2002)
lagu2 = Lagu("Dewa 19", "Kangen", 1992)
lagu3 = Lagu("Peterpan", "Ada Apa denganmu", 2004)
lagu4 = Lagu("Sheila on 7 ", "Dan", 1999)
lagu5 = Lagu("Kangen Band", "Pujaan Hati", 2009)

# print(lagu1.penyanyi)

lagu_lagu = [lagu1, lagu2, lagu3, lagu4, lagu5]

indexLagu = 0

musik = Playlist(lagu_lagu, indexLagu)

berhenti = False
while not berhenti:
    tombol = input("Tombol p untuk play/n untuk next/b untuk previous/f untuk first/l untuk last/c untuk cetak/s untuk berhenti? ")
    if tombol == "p":
        musik.putar()
    elif tombol == "n":
        indexLagu = indexLagu + 1
        musik.putar_lagu_selanjutnya()
    elif tombol == "b":
        indexLagu -= 1
        musik.putar_lagu_sebelumnya()
    elif tombol == "f":
        musik.putar_lagu_pertama()
    elif tombol == "l":
        indexLagu = len(lagu_lagu) - 1
        musik.putar_lagu_terkahir()
    elif tombol == "c":
        musik.mencetak_lagu()
    elif tombol == "s":
        print ("Berhenti")
        berhenti = True
    else:
        pass