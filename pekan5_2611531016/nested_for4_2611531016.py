# Buat file dengan nama nested_for4_2611531016.py
# Buat program untuk perulangan for dalam Python
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()

tinggi_1016 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_1016 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_1016 = tinggi_1016
    c_1016 = a_1016
    lebar_1016 = (2 * tinggi_1016) - 2

    for i_1016 in range(1, tinggi_1016 + 1):
        b_1016 = c_1016 + 1

        for j_1016 in range(1, lebar_1016 + 1):

            # Baris atas dan bawah
            if i_1016 == 1 or i_1016 == tinggi_1016:
                if j_1016 == 1 or j_1016 == lebar_1016:
                    print("#", end="")
                else:
                    print("=", end="")

                    # Baris isi
            else:
                if j_1016 == 1 or j_1016 == lebar_1016:
                    print("|", end="")
                else:
                    if j_1016 == c_1016:
                        print("<", end="")
                    elif j_1016 == b_1016:
                        print(">", end="")
                    elif j_1016 == (lebar_1016 - c_1016):
                        print("<", end="")
                    elif j_1016 == (lebar_1016 - c_1016 + 1):
                        print(">", end="")
                    elif j_1016 > b_1016 and j_1016 < (lebar_1016 - c_1016):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # Logika asli Java
        a_1016 -= 2

        if a_1016 <= 0:
            c_1016 = (-a_1016) + 2
        else:
            c_1016 = a_1016