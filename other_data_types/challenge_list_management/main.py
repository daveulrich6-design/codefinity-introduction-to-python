meat = ["Ham", 3.99, 50, "Sliced"] # Item name, price, quantity, type
cheese = ["Cheddar", 5.49, 100, "Sharp"]   # Item name, price, quantity, type
condiment = ["Mustard", 1.99, 75, "Spicy"] # Item name, price, quantity, type

# Create the main grocery list that contains these items
deli_dept = [meat, cheese, condiment]
print("Initial Deli List: ", deli_dept)

if "Ham" in meat and meat[2] < 100:
    meat = ["Ham", 3.99, 100, "Sliced"] 

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)
deli_dept.remove(condiment)
deli_dept.sort()

print("Updated Deli List: " , deli_dept)