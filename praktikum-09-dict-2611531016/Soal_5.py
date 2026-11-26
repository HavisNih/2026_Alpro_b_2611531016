setoran = int(input("Masukkan jumlah setoran: "))
data = {}
for i in range(setoran):
    nama, total = input("Masukkan nama dan total setoran: ").split()
    data[nama] = int(total)

name = ""
total = 0
for nama, total_setoran in data.items():
    print(f"{nama}: {total_setoran}")
    if nama in data:
        data[nama] += total_setoran
    if total_setoran > total:
        name = nama
        total = total_setoran

total_cash = sum(data.values())
print("Total cash:", total_cash)
print("Top contributor: ", name, total)
