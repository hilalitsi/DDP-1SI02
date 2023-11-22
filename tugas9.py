def cek (nama,alamat,gender,umur,hobi):
    print("nama saya adalah :", nama)
    print("alamat saya di :", alamat)
    print("gender saya adalah :", gender)
    print("umur saya adalah :", umur)
    print("hobi saya adalah :", hobi)
#Panggil
cek("Hilal Hamdani Nabil", "Cibinong Bogor", "Laki Laki", 18, "Berenang")

print("=============================")

def ceknilai(nilai):
    if nilai < 60:
        print("Gagal")
    elif 61 <= nilai <= 70:
        print("Baik")
    elif 71 <= nilai <= 80:
        print("Sangat Baik")
    elif 81 <= nilai <= 100:
        print("Istimewa")
    
    else:
        print("Tidak Lulus")
ceknilai(81)

print("=============================")

def ganjil(angka):
    for p in range(1, angka + 1, 2):
        print(p)
ganjil(100)