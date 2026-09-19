# Tugas 3 Havis Lutfi
# Nim : 2611531016
# Sistem Simulasi Transaksi dan Validasi Akses Toko
# ga bikin komen takut pusing, bikin komen takut dikira ai aduhhhh
# Maaf berantakan bg puyeng mikir konsepnyah

print("\n=== SISTEM TRANSAKSI TOKO HAVISCIHUY ===\n")

nama_1016 = input("Masukkan nama Pelanggan                      : ")
member_1016 = input("Masukkan Status Pelanggan (member/nonmember) : ")
totalbelanja_1016 = int(input("Masukkan total belanja (Rp)                  : "))
jumlahbarang_1016 = int(input("Masukkan Jumlah Barang                       : "))
berat_1016= int(input("Masukkan Total Berat Barang (Kg)             : ")) 
poin_1016 = int(input("Masukkan jumlah poin (jika member) atau 0    : "))
promo_1016 = input("Masukkan Kode Promo                          : ").upper()

print("\n=== DATA TRANSAKSI ===\n")
print("Nama Pelanggan   : ", nama_1016)
print("Status Pelanggan : ", member_1016)
print("Total Belanja    : Rp", totalbelanja_1016)
print("Jumlah Barang    : ", jumlahbarang_1016)
print("Berat Total      : ", berat_1016, "Kg")
print("Kode Promo       : ", promo_1016)

kode_promo_1016 = ["HEMAT10", "HEMAT20", "GRATISONGKIR", "HAVISGANTENG" ]
# OPERATOR PERBANDINGAN
syarat_totalbelanja_1016 = totalbelanja_1016 >= 200000
syarat_jumlahbarang_1016 = jumlahbarang_1016 >= 3
statusmember_1016 = member_1016.lower() == "member"
# OPERATOR KEANGGOTAAN
promotersedia_1016 = promo_1016 in kode_promo_1016
dapatdiskon_1016 = statusmember_1016
# OPERATOR LOGIKA
dapatpromo_1016 = promotersedia_1016 and (syarat_jumlahbarang_1016 or syarat_totalbelanja_1016)

print("\n=== Hasil Validasi ===\n")
print("Belanja >= Rp200000 : ", syarat_totalbelanja_1016)
print("Jumlah Barang >= 3  : ", syarat_jumlahbarang_1016)
print("Status Member       : ", statusmember_1016)
print("Kode Promo Tersedia : ", promotersedia_1016)
print("Mendapatkan Dsikon  : ", dapatdiskon_1016)
print("Mendapatkan Promo   : ", dapatpromo_1016)

#variabel awal
diskonpromo_1016 = 0
diskonmember_1016 = 0
diskonpoin_1016 = 0
ongkir_1016 = 0
diskonongkir_1016 = 0

#harga ongkir
if berat_1016 >= 3 :       # ongkir hanya ada saat berat lebih dari atau sama dengan 3kg
    ongkir_1016 = berat_1016 * 5000 # OPERATOR ARITMATIKA

# diskon promo (takut kurang nilai kalau pake nested if)
# OPERATOR PENUGASAN DAN LOGIKA
if dapatpromo_1016 and promo_1016 == "HEMAT10":
    diskonpromo_1016 += 10000
if dapatpromo_1016 and promo_1016 == "HEMAT20":
    diskonpromo_1016 += 20000
if dapatpromo_1016 and promo_1016 == "HAVISGANTENG":
    diskonpromo_1016 += 50000
if dapatpromo_1016 and promo_1016 == "GRATISONGKIR":
    diskonongkir_1016 = ongkir_1016

# diskon poin
if poin_1016 >= 100 :
    diskonpoin_1016 = poin_1016 * 100

#diskon member
if statusmember_1016:
    diskonmember_1016 += 10000

#rumus
# OPERATOR ARITMATIKA
totaldiskon_1016 = diskonpromo_1016 + diskonmember_1016 + diskonpoin_1016
ongkirpromo_1016 = ongkir_1016 - diskonongkir_1016
totalbayar_1016 = totalbelanja_1016 - (totaldiskon_1016 + diskonongkir_1016)
ratabarang_1016 = totalbelanja_1016 / jumlahbarang_1016
dapatpoin_1016 = totalbelanja_1016 // 2000
poin_1016 += dapatpoin_1016

print("\n=== HASIL PERHITUNGAN===\n")
print("Harga Total                : Rp", totalbelanja_1016)
print("Diskon Promo               : Rp", diskonpromo_1016)
print("Diskon Member              : Rp", diskonmember_1016)
print("Diskon Poin                : Rp", diskonpoin_1016)
print("Total Diskon               : Rp", totaldiskon_1016)
print("Harga Ongkir               : Rp", ongkir_1016)
print("Harga ongkir setelah promo : Rp", ongkirpromo_1016)
print("-------------------------------------------------")
print("Total Pembayaran           : Rp", totalbayar_1016)
print("\nRata-rata Harga Barang   : Rp", ratabarang_1016)
print("Perolehan Poin             : ", dapatpoin_1016)
print("Total Poin                 : ", poin_1016)

# OPERATOR IDENTITAS
objek1_status_1016 = member_1016.lower()
objek2_status_1016 = objek1_status_1016
objek3_status_1016 = str(member_1016.lower())

is_identik_1016 = objek1_status_1016 is objek2_status_1016
is_not_identik_1016 = objek1_status_1016 is not objek3_status_1016

print("\n=== OPERATOR IDENTITAS ===")
print("objek1 is objek2     : ", is_identik_1016)
print("objek1 is not objek3 : ", is_not_identik_1016)

# OPERATOR BITWISE
if statusmember_1016:
    bitmember_1016 = 1
else:
    bitmember_1016 = 0

if syarat_totalbelanja_1016:
    bitbelanja_1016 = 2
else:
    bitbelanja_1016 = 0

if syarat_jumlahbarang_1016:
    bitbarang_1016 = 4
else:
    bitbarang_1016 = 0

if promotersedia_1016:
    bitpromo_1016 = 8
else:
    bitpromo_1016 = 0

# Operator Bitwise OR (|)
hak_akses_1016 = bitmember_1016 | bitbelanja_1016 | bitbarang_1016 | bitpromo_1016

# Operator Bitwise AND (&)
cek_member_1016 = hak_akses_1016 & 1
cek_promo_1016 = hak_akses_1016 & 8

# Operator Bitwise XOR (^)
kode_referensi_1016 = 11
beda_status_1016 = hak_akses_1016 ^ kode_referensi_1016

# Operator Bitwise Shift Left (<<)
shift_left_1016 = hak_akses_1016 << 1

print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       : ", format(hak_akses_1016, '04b'))
print("Member Access        : ", bool(cek_member_1016))
print("Promo Access         : ", bool(cek_promo_1016))
print("Free Shipping Access : ", promo_1016 == "GRATISONGKIR")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print("Kode Biner   : ", format(hak_akses_1016, '04b'))
print("Kode Desimal : ", hak_akses_1016)

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(format(hak_akses_1016, '04b'), "& 0001")
print("Hasil Biner   : ", format(cek_member_1016, '04b'))
print("Hasil Desimal : ", cek_member_1016)

print("\nCek Promo")
print(format(hak_akses_1016, '04b'), "& 1000")
print("Hasil Biner   : ", format(cek_promo_1016, '04b'))
print("Hasil Desimal : ", cek_promo_1016)

print("\n=== Perbandingan Status ===")
print("Kode Transaksi : ", format(hak_akses_1016, '04b'))
print("Kode Referensi : ", format(kode_referensi_1016, '04b'))
print(format(hak_akses_1016, '04b'), "^", format(kode_referensi_1016, '04b'))
print("Hasil Biner   : ", format(beda_status_1016, '04b'))
print("Hasil Desimal : ", beda_status_1016)

print("\n=== Shift ===")
print(format(hak_akses_1016, '04b'), "<< 1")
print("Hasil Biner   : ", format(shift_left_1016, '05b'))
print("Hasil Desimal : ", shift_left_1016)

print("\n=== SELESAI ===")