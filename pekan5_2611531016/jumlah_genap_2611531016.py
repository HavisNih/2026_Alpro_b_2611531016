#Buat file dengan nama jumlah_genap_2611531016.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()

ulang_1016 = int(input("Masukkan jumlah perulangan = "))

jumlah_1016 = 0
for i_1016 in range(1, ulang_1016 + 1):
    if i_1016 % 2 == 0:
        print(i_1016, end=" ")
        jumlah_1016 = jumlah_1016 + i_1016

        if i_1016 < ulang_1016:
            print("+", end=" ")
        else:
            print("=", jumlah_1016,end=" ") 
print()
print("Jumlah= " ,jumlah_1016)