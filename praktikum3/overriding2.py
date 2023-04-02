from abc import ABC, abstractmethod

class kendaraan(ABC):
    @abstractmethod
    def start(self):
        pass

class mobil(kendaraan):
    def start(self):
        print("mobil dinyalakan dengan cara di starter")

class motor(kendaraan):
    def start(self):
        print("motor dinyalakan dengan cara disela")

class traktor(kendaraan):
    def start(self):
        print("traktor dinyalakan dengan cara di starter")



M = mobil()
Mo = motor()
T = traktor()

M.start()    
Mo.start()    
T.start()    
