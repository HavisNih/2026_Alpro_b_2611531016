menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below 

for day in range(number_of_days):
    row = []
    for menu in menus:
        value = int(input(f"Day {day + 1}, {menu}: "))
        row.append(value)
    sales.append(row)

print("Total per day:")
for day in range(number_of_days):
    total_day = 0
    for value in sales[day]:
        total_day += value
    print(f"Day {day + 1}: {total_day}")

menu_totals = []
for i in range(len(menus)):
    total_menu = 0
    for day in range(number_of_days):
        total_menu += sales[day][i]
    menu_totals.append((menus[i], total_menu))

print("Total per menu: ",menu_totals)

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]

for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total

print(f"Best seller: {best_name} ({best_total})")