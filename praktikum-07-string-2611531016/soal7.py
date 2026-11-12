# Name: Havis Lutfi
# NIM: 2611531016
# Question 7

full_name = input("Masukkan Nama: ")
nim = input("Masukkan NIM: ")
intake = "20" + nim[:2]

clean = full_name.strip().lower()
space = clean.find(" ")

if space == -1:
    nama_depan = clean
else:
    nama_depan = clean[:space]
    
username = nama_depan + nim[-3:]

print("=" * 30)
print(f"{'STUDENT CARD':^30}")
print("=" * 30)
print(f"{'Name':<10}: {clean.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {intake}")
print("=" * 30)