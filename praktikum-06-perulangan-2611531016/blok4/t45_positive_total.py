Total = 0

while True:
    angka = int(input("Enter a number: "))
    if angka == 0:
        continue
    elif angka > 0:
        Total += angka
        print("Positive number: ", angka)
    elif angka < 0:
        break
print("Total :", Total)
