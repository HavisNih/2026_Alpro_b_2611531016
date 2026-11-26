schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

terbanyak = ""
maks = 0
for day in schedule:
    if len(schedule[day]) > maks:
        maks = len(schedule[day])
        terbanyak = day
print("Busiest day:", terbanyak, "(" + str(maks) + " courses)")

course = input("Masukkan nama mata kuliah:").title()
count = 0
for day in schedule:
    if course in schedule[day]:
        count += 1
print(course + ": " + str(count) + " days")