class pegawai:
    def __init__(self, nama, umur, gaji):
        self.nama = nama
        self.umur = umur
        self.gaji = gaji

    def display_info(self):
        print("Nama:", self.nama)
        print("Umur:", self.umur)
        print("Gaji:", self.gaji)


class Manager(pegawai):
    def __init__(self, name, umur, gaji, department):
        super().__init__(name, umur, gaji)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)


class SalesManager(Manager):
    def __init__(self, nama, umur, gaji, department, bonus):
        super().__init__(nama, umur, gaji, department)
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print("Bonus:", self.bonus)


class HRManager(Manager):
    def __init__(self, nama, umur, gaji, department, tunjangan):
        super().__init__(nama, umur, gaji, department)
        self.tunjangan = tunjangan

    def display_info(self):
        super().display_info()
        print("Tunjangan:", self.tunjangan)


pegawaiA = pegawai("bambang pamungkas", 20, 5000)
managerA = Manager("budi sudarsono", 30, 10000, "Sales")
smA = SalesManager("titus bonai", 35, 15000, "Sales", 5000)
hrA = HRManager("boaz salosa", 40, 20000, "HR", 10000)

pegawaiA.display_info()
print("------------------------")
managerA.display_info()
print("------------------------")
smA.display_info()
print("------------------------")
hrA.display_info()
