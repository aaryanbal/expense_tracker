expenses = []

price = float(input("How much did you pay for this purchase: "))
item = input("What did you purchase: ")
category = input("What category is this purchase: ")


purchase = {"price": price, "item": item, "category": category}
expenses.append(purchase)
print(expenses)

while True:
    price = float(input("How much did you pay for this purchase: "))
    item = input("What did you purchase: ")
    category = input("What category is this purchase: ")
    purchase = {"price": price, "item": item, "category": category}
    expenses.append(purchase)
    again = input("Do you want to make another purchase(yes or no): ")
    
    if (again == "no"):
        break
for purchase in expenses:
    print(purchase)




    
    