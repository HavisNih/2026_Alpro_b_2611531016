# Name: Havis Lutfi
# NIM: 2611531016
# Question 3

#A
text = "Informatika"
print(text[10])
print(text.upper())
print(text[0:20])

#B
text = "Havis Lutfi"

count = 0
for char in text.lower():
    if char in "aiueo":
        count += 1
print("Vowels:", count)
