number = 10
string = "abc"

try:
    result = number + string
    print(result)
except TypeError:
    print("Terjadi kesalahan tipe data! Mohon pastikan tipe data variabel sudah benar.")
