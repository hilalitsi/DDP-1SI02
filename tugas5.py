
kendaraan = ["mobil", "hypercar", "6496", "merah", "4 roda"]
print (kendaraan)
#variabel kendaraan
kendaraan.append ("1.000.000.000")
kendaraan.append ("sport")
kendaraan.insert (2,"ferrari")
print ("kendaraan ini saya pakain untuk liburan")
print (kendaraan)

menghitung = input("PILIH OPERASI: \n 1. hitung luas persegi \n 2. hitung luas lingkaran \n 3. hitung luas segitiga \n pilihan :")
match menghitung:
    case "1":
        sisi = int(input("masukan panjang sisi"))
        luas = sisi*sisi
        print (luas)
    case "2":
        jari_jari = int (input("masukan nilai jari-jari: "))
        luas = 3.14* jari_jari * jari_jari
        print (luas)
    case "3":
        alas = int (input("masukan nilai alas: "))
        tinggi = int (input("masukan nilai tinggi: "))
        luas = 0.5 * alas * tinggi
        print (luas)
    case _:
        print("salah pilih")