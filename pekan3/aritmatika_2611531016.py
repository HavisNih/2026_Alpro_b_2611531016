# Buat file dengan nama aritmatika_2611531016.py
# Buatlah program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Nilai yang dimasukan akan dikonversi menjadi tipe data integer

angka1_1016 = int(input("Masukkan angka-1: "))
angka2_1016 = int(input("Masukkan angka-2: "))

# Penjumlahan
hasil_1016 = angka1_1016 + angka2_1016
print("\nOperator Penjumlahan")
print("Hasil =", hasil_1016)

# Pengurangan
hasil_1016 = angka1_1016 - angka2_1016
print("\nOperator Pengurangan")
print("Hasil =", hasil_1016)

# Perkalian
hasil_1016 = angka1_1016 * angka2_1016
print("\nOperator Perkalian")
print("Hasil =", hasil_1016)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1016 != 0:
    hasil_1016 = angka1_1016 / angka2_1016
    print("\nOperator Pembagian")
    print("Hasil =", hasil_1016)

    hasil_1016 = angka1_1016 // angka2_1016
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_1016)

    hasil_1016 = angka1_1016 % angka2_1016
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_1016)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_1016 = angka1_1016 ** angka2_1016
print("\nOperator Pangkat")
print("Hasil =", hasil_1016)
