import json


expenses = []
total = 0


while True:
    price = float(input("How much did you pay for this purchase: "))
    item = input("What did you purchase: ")
    category = input("What category is this purchase: ")
    purchase = {"price": price, "item": item, "category": category}
    expenses.append(purchase)
    again = input("Do you want to make another purchase(yes or no): ")
    corrected_input = again.strip().lower()
    
    if (corrected_input == "no"):
        break


with open("expenses.json", "w") as file:
    json.dump(expenses, file)


    print("Your expenses: ")
    for purchase in expenses:
        print(purchase["item"],f"${purchase["price"]}", purchase["category"])


for purchase in expenses:
    total += purchase["price"]
print(f"Your total expenses are: ${round(total, 2)}")

