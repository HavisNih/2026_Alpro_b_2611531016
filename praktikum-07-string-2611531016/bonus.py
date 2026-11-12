# Name: Havis Lutfi
# NIM: 2611531016
# Question Bonus

kalimat = input("Masukkan kalimat: ")
clean = kalimat.lower().replace(" ", "")

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")