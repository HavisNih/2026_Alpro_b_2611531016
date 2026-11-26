setoran = int(input("Masukkan jumlah data: "))
data = {}

for i in range(setoran):
    nama, total = input("Masukkan nama dan total setoran: ").split()
    total = int(total)
    data[nama] = data.get(nama, 0) + total

terbanyak = 0
top = ""
for nama, total in data.items():
    print(f"{nama}: {total}")
    if total > terbanyak:
        terbanyak = total
        top = nama

print(f"Total cash: {sum(data.values())}")
print(f"Top contributor: {top} ({terbanyak})")