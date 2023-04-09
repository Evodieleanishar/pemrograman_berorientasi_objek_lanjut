class Bahan:
    def __init__(self, nama, kuantitas):
        self.nama = nama
        self.kuantitas = kuantitas
    
    def __str__(self):
        return f"{self.kuantitas} {self.nama}"
    
class ProdukMakanan:
    def __init__(self, nama, daftar_bahan):
        self.nama = nama
        self.daftar_bahan = daftar_bahan
    
    def tambah_bahan(self, bahan):
        self.daftar_bahan.append(bahan)
        
    def __str__(self):
        return f"{self.nama} terbuat dari: {', '.join(str(bahan) for bahan in self.daftar_bahan)}"
        
        
bahan1 = Bahan("Daging sapi", "500 gram")
bahan2 = Bahan("Nasi", "1 kilogram")
bahan3 = Bahan("Bawang merah", "100 gram")

nasi_goreng = ProdukMakanan("Nasi goreng", [bahan2, bahan3])
rendang = ProdukMakanan("Rendang", [bahan1, bahan3])

print(nasi_goreng)
print(rendang)
