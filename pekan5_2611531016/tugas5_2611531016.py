# Ini saya ga nyalin ai ya bang -_-, bikin sendiri, tapi nanya ai sih biar logikanya dapet, tapi ga nyalin langsung


print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

N_1016 = int(input("Masukkan ukuran skala jam pasir (N): "))

# Bingkai atas
print("#", end="")
for bingkai_1016 in range((4 * N_1016) + 5):
    print("=", end="")
print("#")

# Fase 1
for baris_1016 in range(1, N_1016 + 1):
    banyak_1016 = N_1016 - baris_1016 + 1   #Bingung namain apa soalnya kepake buat spasi dan angka mundur sekaligus
    # Bingkai kiri
    print("|", end="")
    print(" ", end="")
    # Spasi kiri
    for spasi_1016 in range(2 * (N_1016 - banyak_1016)):
        print(" ", end="")
    # Angka mundur
    for angka_1016 in range(1, banyak_1016 + 1):
        print(banyak_1016 - angka_1016 + 1, end="")
        print(" ", end="")
    # Tengah
    print("<*>", end="")
    # Angka maju
    for angka_1016 in range(1, banyak_1016 + 1):
        print(" ", end="")
        print(angka_1016, end="")
    # Spasi kanan
    for spasi_1016 in range(2 * (N_1016 - banyak_1016)):
        print(" ", end="")
    # Bingkai kanan
    print(" ", end="")
    print("|")

# Fase 2
print("|", end="")
for spasi_1016 in range(2 * N_1016 + 1):
    print(" ", end="")
print("<*>", end="")
for spasi_1016 in range(2 * N_1016 + 1):
    print(" ", end="")
print("|")

# Fase 3
for baris_1016 in range(1, N_1016 + 1):
    # Bingkai kiri
    print("|", end="")
    print(" ", end="")
    # Spasi kiri
    for spasi_1016 in range(2 * (N_1016 - baris_1016)):
        print(" ", end="")
    # Angka mundur
    for angka_1016 in range(1, baris_1016 + 1):
        print(baris_1016 - angka_1016 + 1, end="")
        print(" ", end="")
    # Tengah
    print("<*>", end="")
    # Angka maju
    for angka_1016 in range(1, baris_1016 + 1):
        print(" ", end="")
        print(angka_1016, end="")
    # Spasi kanan
    for spasi_1016 in range(2 * (N_1016 - baris_1016)):
        print(" ", end="")
    # Bingkai kanan
    print(" ", end="")
    print("|")