# Buat file dengan nama logika_2611531016.py
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Program operator logika dalam python

# Memasukkan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1016 = input("Input nilai boolean-1 (True/False): ").strip().lower() == "true"
a2_1016 = input("Input nilai boolean-2 (True/False): ").strip().lower() == "true"

print("\nA1 =", a1_1016)
print("\nA2 =", a2_1016)

# Konjungsi bernilai True jika keduanya True
hasil_1016 = a1_1016 and a2_1016
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil_1016)

# Disjungsi bernilai True jika salah satunya True
hasil_1016 = a1_1016 or a2_1016
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil_1016)

# Negasi A1: Membalik nilai A1
hasil_1016 = not a1_1016
print("\nNegasi A1 (NOT)")
print("not A1 =", hasil_1016)

# Negasi A2: Membalik nilai A2
hasil_1016 = not a2_1016
print("\nNegasi A2 (NOT)")
print("not A2 =", hasil_1016)

#XOR bernilai True jika kedua nilai berbeda
hasil_1016 = a1_1016 != a2_1016
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 =", hasil_1016)