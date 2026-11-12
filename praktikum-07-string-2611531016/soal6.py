# Name: Havis Lutfi
# NIM: 2611531016
# Question 6

first_name = " muhammad"
last_name = "rafi "
full_name = first_name.strip() + " " + last_name.strip()
print(full_name)
print(full_name.title())

full_name = input("Masukkan Nama : ")
nim = input("Masukkan NIM : ")

clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    nama_depan = clean
else:
    nama_depan = clean[:space]

username = nama_depan + nim[-3:]
print(username)