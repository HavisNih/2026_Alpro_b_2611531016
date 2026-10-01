# Buat file dengan nama nested_for1_2611531016.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()

batas_1016 = int(input("Masukkan nilai batas: "))
for line_1016 in range(1, batas_1016 + 1):
    for j_1016 in range(1, (-1 * line_1016 + batas_1016) + 1):
        print(".", end="")
    print(line_1016)