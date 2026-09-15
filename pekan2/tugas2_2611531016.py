from typing import Final, final

sinyal_1016 = 100+3j
batasnilai_1016 : Final = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1016 = input("Masukkan Nama Mahasiswa : ")
kelamin_1016 = input("Masukkan Jenis Kelamin (L/P) : ")
umur_1016 = int(input("Masukkan Umur Mahasiswa : "))
skor_1016 = float(input("Masukkan Skor Tes Awal : "))
alamat_1016 = """
Jl. Kampus Unand,
Kecamatan Pauh,
Kota Padang"""

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ", nama_1016, "| TIPE: ", type(nama_1016) )
print("Jenis Kelamin : ", kelamin_1016, "| TIPE: ", type(kelamin_1016) )
print("Alamat Domisili:", alamat_1016, "| TIPE: ", type(alamat_1016) )
print("Umur : ", umur_1016, "tahun | TIPE: ", type(umur_1016) )
print("Skor Tes Awal : ", skor_1016, "| TIPE: ", type(skor_1016) )
print("ID Token Sinyal :", sinyal_1016, "| TIPE: ", type(sinyal_1016) )

Lulus_1016 = skor_1016 >= batasnilai_1016

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai :", batasnilai_1016)
print("Apakah Dinyatakan Lulus? :", Lulus_1016, "| TIPE: ", type(Lulus_1016) )



