LAST_DIGIT = 6  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below

for i in range(7):
    expenses.append(int(input(f"Day {i + 1}: ")))

total = 0
for x in expenses:
    total += x

average = total / 7

highest = expenses[0]
highest_day = 1
for i in range(1, 7):
    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

days_above_limit = 0
for x in expenses:
    if x > daily_limit:
        days_above_limit += 1

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {days_above_limit}")