class Hewan:
    def __init__(self, nama, species, suara):
        self.nama = nama
        self.species = species
        self.suara = suara

    def bersuara(self):
        print(self.suara)


class Mammalia(Hewan):
    def __init__(self, nama, species, suara, kaki):
        super().__init__(nama, species, suara)
        self.kaki = kaki

    def berjalan(self):
        print(f"{self.nama} berjalan dengan {self.kaki} kaki.")


class kucing(Mammalia):
    def __init__(self, nama, ras, kaki):
        super().__init__(nama, "kucing", "persia", kaki)
        self.ras = ras

    def mengeong(self):
        print(f"{self.nama} bersuara mengeong.")


class Anjing(Mammalia):
    def __init__(self, nama, ras, kaki):
        super().__init__(nama, "anjing", "kintamani", kaki)
        self.ras = ras

    def mengejar(self):
        print(f"{self.nama} mengejar bola.")


kucingA = kucing("garong", "Kampung", 4)
anjingA = Anjing("guguk", "kintamani", 4)

kucingA.bersuara()
kucingA.berjalan()
kucingA.mengeong()

print("------------------------")

anjingA.bersuara()
anjingA.berjalan()
anjingA.mengejar()
