# Name: Havis Lutfi
# NIM: 2611531016
# Question 5

#A
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"

username = input("Username: ")

if len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: letters and digits only")
elif not username[0].isalpha() :
    print("Invalid: must start with a letter")
else:
    print("Valid")

#B
NIM = input("Masukkan NIM : ")

if len(NIM) == 10 and NIM.isdigit():
    print(f"Valid, intake year 20{NIM[:2]}")
else:
    print("Invalid NIM")