# Buat file dengan nama lainnya_2611531016.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1016 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1016 = [int(angka.strip()) for angka in input_data_1016.split(",")]

nilai_dicari_1016 = int(input("Masukkan nilai yang ingin dicari: "))

# Operator in
hasil_1016 = nilai_dicari_1016 in data_1016
print("\nOperator Keanggotaan IN")
print(nilai_dicari_1016, "in", data_1016, "=", hasil_1016)

# Operator not in
hasil_1016 = nilai_dicari_1016 not in data_1016
print("\nOperator Keanggotaan NOT IN")
print(nilai_dicari_1016, "not in", data_1016, "=", hasil_1016)


print("===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

#objek1 menggunakan list dari input pengguna
objek1_1016 = data_1016

#objek2 merujuk pada objek yang sama dengan objek1
objek2_1016 = objek1_1016

# objek3 memiliki isi yang sama, tetaoi merupakan objek baru
objek3_1016 = data_1016.copy()

print("objek1 =", objek1_1016)
print("objek2 =", objek2_1016)
print("objek3 =", objek3_1016)

# Operator is
hasil_1016 = objek1_1016 is objek2_1016
print("\nOperator Identitas IS")
print("objek1 is objek2 =", hasil_1016)

# Operator is not
hasil_1016 = objek1_1016 is not objek3_1016
print("\nOperator Identitas IS NOT")
print("objek1 is not objek3 =", hasil_1016)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_1016 is objek3_1016)
print("objek1 == objek3 =", objek1_1016 == objek3_1016)