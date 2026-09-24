#Buat file dengan nama multi_if2_2611531016.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dari user
total_belanja_1016 = float(input("Masukkan total belanja (Rp)"))

# Input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_1016 = input("Apakah Anda member? (y/t): ").strip().lower()
is_member_1016 = input_member_1016 in ["y", "ya"]

# Input status kode promo (mengecek user mengetik 'y' atau 'ya)
input_promo_1016 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1016 = input_promo_1016 in ["y", "ya"]

total_diskon_persen_1016 = 0

# Multi-IF terpisah: Setiap kondisi diperika secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus
 
if total_belanja_1016 > 1000000:
    total_diskon_persen_1016 += 10  # Diskon belanja besar
  
if is_member_1016:
    total_diskon_persen_1016 += 5   # Diskon member

if kode_promo_valid_1016:
    total_diskon_persen_1016 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1016 = total_belanja_1016 * (total_diskon_persen_1016 / 100)
total_bayar_1016 = total_belanja_1016 - nominal_diskon_1016
 
# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_1016}% (Rp {nominal_diskon_1016:,.0f})")
print(f"Total Bayar   : Rp {total_bayar_1016:,.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_1016}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid