# Buat file dengan nama assignment_2611531016.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Nilai yang dimasukan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam python

angka1_1016 = int(input("Masukkan angka-1: "))
angka2_1016 = int(input("Masukkan angka-2: "))

print("\nNilai awal angka1 =", angka1_1016)
print("Nilai angka2 =", angka2_1016)

# Assignment biasa
hasil_1016 = angka1_1016
print("\nAssignment Biasa(=)")
print("Hasil =", hasil_1016)

# Assignment penambahan
hasil_1016 = angka1_1016
hasil_1016 += angka2_1016
print("\nAssignment Penambahan(+=)")
print("Hasil =", hasil_1016)

# Assignment pengurangan
hasil_1016 = angka1_1016
hasil_1016 -= angka2_1016
print("\nAssignment Pengurangan(-=)")
print("Hasil =", hasil_1016)

# Assignment perkalian
hasil_1016 = angka1_1016
hasil_1016 *= angka2_1016
print("\nAssignment Perkalian(*=)")
print("Hasil =", hasil_1016)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_1016 != 0:
    hasil_1016 = angka1_1016
    hasil_1016 /= angka2_1016
    print("\nAssignment Pembagian(/=)")
    print("Hasil =", hasil_1016)
    # Operator tambahan
    hasil_1016 = angka1_1016
    hasil_1016 //= angka2_1016
    print("\nAssignment Pembagian Bulat(//=)")
    print("Hasil =", hasil_1016)
    hasil_1016 = angka1_1016
    hasil_1016 %= angka2_1016
    print("\nAssignment Sisa Bagi(%=)")
    print("Hasil =", hasil_1016)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_1016 = angka1_1016
hasil_1016 **= angka2_1016
print("\nAssignment Perpangkatan (**=)")
print("Hasil =", hasil_1016)