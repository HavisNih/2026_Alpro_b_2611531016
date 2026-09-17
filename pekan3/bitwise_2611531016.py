# Buat file dengan nama bitwise_2611531016.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()

print("===================================")
print("1. OPERATOR BITWISE")
print("===================================")

angka1_1016 = int(input("Masukkan angka bitwise-1: "))
angka2_1016 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_1016, "| biner =", bin(angka1_1016))
print("angka2 =", angka2_1016, "| biner =", bin(angka2_1016))

# Bitwise AND
hasil_1016 = angka1_1016 & angka2_1016
print("\nBitwise AND (&)")
print(angka1_1016, "&", angka2_1016, "=", hasil_1016)
print("Biner hasil =", bin(hasil_1016))
print("Biner hasil (8 bit) =", format(hasil_1016, '08b'))

# Bitwise OR
hasil_1016 = angka1_1016 | angka2_1016
print("\nBitwise OR (|)")
print(angka1_1016, "|", angka2_1016, "|", hasil_1016)
print("Biner hasil =", bin(hasil_1016))
print("Biner hasil (8 bit) =", format(hasil_1016, "08b"))

# Bitwise XOR
hasil_1016 = angka1_1016 ^ angka2_1016
print("\nBitwise XOR (^)")
print(angka1_1016, "^", angka2_1016, "=", hasil_1016)
print("Biner hasil =", bin(hasil_1016))
print("Biner hasil (8 bit) =", format(hasil_1016, '08b'))

# Bitwise NOT
hasil_1016 = ~angka1_1016
print("\nBitwise NOT (~)")
print("~", angka1_1016, "=", hasil_1016)
print("Biner hasil =", bin(hasil_1016))
print("Biner hasil (8 bit) =", format(hasil_1016, "08b"))

# Bitwise geser kiri
jumlah_geser_1016 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1016 = angka1_1016 << jumlah_geser_1016
print("\nBitwise geser kiri (<<)")
print(angka1_1016, "<<", jumlah_geser_1016, "=", hasil_1016)
print("Biner hasil =", bin(hasil_1016))
print("Biner hasil (8 bit) =", format(hasil_1016, "08b"))

# Bitwise geser kanan
hasil_1016 = angka1_1016 >> jumlah_geser_1016
print("\nBitwise geser kanan (>>)")
print(angka1_1016, ">>", jumlah_geser_1016, "=", hasil_1016)
print("Biner hasil =", bin(hasil_1016))
print("Biner hasil (8 bit) =", format(hasil_1016, "08b"))