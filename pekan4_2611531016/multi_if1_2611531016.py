#Buat file dengan nama if3_2611531016.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()

umur_1016 = int(input("Input umur anda: "))
sim_1016 = input("Apakah Anda Sudah Punya Sim C (y/t) : ")[0]

if umur_1016 >= 17 and sim_1016 == 'y':
    print("Anda Sudah dewasa dan boleh bawa motor")

if umur_1016 >= 17 and sim_1016 != 'y':
    print("Anda Sudah dewasa tetapi tidak boleh bawa motor")

if umur_1016 <= 17 and sim_1016 == 'y':
    print("Anda Belum Cukup Umur punya SIM")

if umur_1016 != 17 and sim_1016 != 'y':
    print("Anda Belum Cukup Umur bawa motor")