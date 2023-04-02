class kendaraan:
    def move(self):
        print("kendaraan berjalan")

class mobil(kendaraan):
    def move(self):
        print("mobil berjalan")

class motor(kendaraan):
    def move(self):
        print("motor berjalan")

K = kendaraan()
M = mobil()
Mo = motor()

K.move()    
M.move()    
Mo.move()    