setoran = int(input("Masukkan jumlah data: "))
data = {}

for i in range(setoran):
    nama, cash = input("Masukkan nama dan total setoran: ").split()
    cash = int(cash)
    data[nama] = data.get(nama, 0) + cash

terbanyak = 0
top = ""
for nama, cash in data.items():
    print(f"{nama}: {cash}")
    if cash > terbanyak:
        terbanyak = cash
        top = nama

print(f"Total cash: {sum(data.values())}")
print(f"Top contributor: {top} ({terbanyak})")