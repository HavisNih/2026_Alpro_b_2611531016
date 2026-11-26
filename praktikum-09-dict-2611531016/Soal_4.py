students = input("Masukkan semua nomor absen: ").split()
kumpul = set(input("Masukkan nomor absen yang mengumpulkan: ").split())

tidak_kumpul = set(students) - kumpul

print(f"Submitted: {len(kumpul)} students")
print(f"Not submitted: {len(tidak_kumpul)} students")
for student in students:
    if student not in kumpul:
        print(student)