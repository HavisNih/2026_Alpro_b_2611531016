#Tugas 4 Havis Lutfi
#Nim 2611531016
# Inputan pengguna
print("===SISTEM LOKET ALPRO ADVENTURE PARK===")
nama_1016 = input("Masukkan Nama Pengunjung : ")
umur_1016 = int(input("Masukkan umur anda       : "))
sim_1016 = input("apakah Anda Sudah Punya SIM C (y/t) : ").strip().lower()[0]

#Daftar paket
print("\nPilihan Paket Wahana (1-5):")
print("1. Safari Rimba           (Rp 50,000)")
print("2. Arung Jeram            (Rp 75,000)")
print("3. Motor ATV Ekstrim      (Rp 120,000)")
print("4. Roller Coaster Kilat   (Rp 100,000)")
print("5. All-Access VIP         (Rp 220,000)\n")

#inputan pengguna
nomor_paket_1016 = int(input("Masukkan nomor paket (1-5)     : "))
jumlah_tiket_1016 = int(input("Masukkan jumlah tiket          : "))
status_member_1016 = input("Apakah Anda member? (y/t)      : ").strip().lower()[0]
promo_valid_1016 = input("Apakah kode promo valid? (y/t) : ").strip().lower()[0]

#if tunggal
if jumlah_tiket_1016 <= 0:
    print("Jumlah tiket gak valid nichh!")
    exit()

#Match case
#ribet kali kalau ga boleh pake nested if mahhh-_-
match nomor_paket_1016:
    case 1:
        print("\n---KELAYAKAN WAHANA---")
        if umur_1016 >= 10:
            print("Status Akses : Anda sudah cukup umur untuk masuk wahana Safari Rimba")
        else:
            print("Status Akses : Anda belum cukup umur, harus didampingi oleh orang dewasa")
        harga_1016 = 50000
        pilihan_paket_1016 = "Safari Rimba"

    case 2:
        print("\n---KELAYAKAN WAHANA---")
        if umur_1016 >= 10:
            print("Status Akses : Anda sudah cukup umur untuk masuk wahana Arung Jeram")
        else:
            print("Status Akses : Anda belum cukup umur,tidak bisa masuk wahana Arung Jeram!")
        pilihan_paket_1016 = "Arung Jeram"
        harga_1016 = 75000


    case 3:
        #if elif else
        print("\n---KELAYAKAN PENGENDARA WAHANA---")
        if umur_1016 >= 17 and sim_1016 == 'y':
            print("Status Akses : Anda Sudah dewasa dan boleh mengendarai ATV sendiri")
        elif umur_1016 >= 17 and sim_1016 != 'y':
            print("Status Akses : Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_1016 < 17 and sim_1016 == 'y':
            print("Status Akses : Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Status Akses : Anda belum cukup umur dan tidak boleh bawa motor ATV")
        pilihan_paket_1016 = "Motor ATV Ekstrim"
        harga_1016 = 120000

    case 4:
        print("\n---KELAYAKAN WAHANA---")
        if umur_1016 >= 10:
            print("Status Akses : Anda sudah cukup umur untuk masuk wahana Roaller Coaster Kilat")
        else:
            print("Status Akses : Anda belum cukup umur,tidak bisa masuk wahana Roller Coaster Kilat!")
        pilihan_paket_1016 = "Roller Coaster Kilat"
        harga_1016 = 100000

    case 5:
        #Wahana ATV
        #If elif else
        print("\n---KELAYAKAN PENGENDARA WAHANA---")
        if umur_1016 >= 17 and sim_1016 == 'y':
            print("Status Akses : Anda Sudah dewasa dan boleh mengendarai ATV sendiri")
        elif umur_1016 >= 17 and sim_1016 != 'y':
            print("Status Akses : Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur).")
        elif umur_1016 < 17 and sim_1016 == 'y':
            print("Status Akses : Identitas tidak valid: Belum cukup umur memiliki SIM.")
        else:
            print("Status Akses : Anda belum cukup umur dan tidak boleh bawa motor ATV")
        #Wahana lain
        print("\n---KELAYAKAN WAHANA---")
        if umur_1016 >= 10:
            print("Status Akses : Anda sudah cukup umur untuk masuk wahana Safari Rimba, Arung Jeram, Roller Coaster Kilat")
        else:
            print("Status Akses : Anda belum cukup umur,tidak bisa masuk wahana Safari Rimba, Arung Jeram, Roller Coaster Kilat!")
        pilihan_paket_1016 = "All-Access VIP"
        harga_1016 = 220000

    case _:
        print("Paket wahana tidak valid!")
        exit()



#inisialisasi
# Multi if
subtotal_1016 = jumlah_tiket_1016 * harga_1016
total_diskon_persen_1016 = 0
if subtotal_1016 >= 200000:
    total_diskon_persen_1016 += 10
if status_member_1016 in ['y', 'ya']:
    total_diskon_persen_1016 += 5
if promo_valid_1016 in ['y', 'ya']:
    total_diskon_persen_1016 += 15
if jumlah_tiket_1016 >= 5:
    total_diskon_persen_1016 += 5

total_diskon_1016 = subtotal_1016 * (total_diskon_persen_1016/100)
total_bayar_1016 = subtotal_1016 - total_diskon_1016

#Rincian
print("\n---Rincian Pembayaran---")
print(f"Nama Pengunjung   : {nama_1016}")
print(f"Pilihan Paket     : {pilihan_paket_1016}")
print(f"Subtotal Belanja  : Rp {subtotal_1016:,.0f}")
print(f"Total Diskon      : {total_diskon_persen_1016}% (Rp {total_diskon_1016:,.0f}) ")
print(f"Total Bayar       : Rp {total_bayar_1016:,.0f}")
if total_bayar_1016 > 300000:
    print("Selamat! Anda berhak mendapatkan Souvenir Gratis.")
    print("Terima kasih telah berkunjung.")
else:
    print("Terima kasih telah berkunjung.")
print("Program Selesai")