# Name: Havis Lutfi
# NIM: 2611531016
# Question 4

phone = "082611531016"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)
