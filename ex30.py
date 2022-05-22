people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("There are too many trucks.")
elif trucks < cars:
    print("May be we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# Extra stuff below. (Optional)
money_in_account = 100
# Items available in the grocery store
inventory = {
    "water": 5,
    "milk": 25,
    "eggs": 29,
    "bread": 15,
    "tea": 18,
    "coffee": 25
}
# Customer's shoppingcart set to [] to empty it.
shopping_cart = []
# Check the whole inventory for what the customer can buy in money that she has in her account.
for key in inventory:
    if money_in_account > 0:
        money_in_account -= inventory[key]
        shopping_cart.append({key: inventory[key]})

# Calculate the total to pay at checkout.
# Iterate over the shopping_Cart which is a list; Get one type of items and get their prices as a list.
# sum the list made in the step above. Now you have a list in which each item is a subtotal for one type of items.
# Sum the list made in the step above and assign it to the variable to_pay
#
to_pay = sum(sum(list(item.values())) for item in shopping_cart)
print(f"Please pay {to_pay} USD for the items: {shopping_cart}")

print("@@@@@@@@@@@ Again @@@@@@@@@@")  # Correct if statement version but customer has some money left.
shopping_cart = []
money_in_account = 100

for key in inventory:
    if 0 < money_in_account >= inventory[key]:
        money_in_account -= inventory[key]
        shopping_cart.append({key: inventory[key]})

to_pay = sum(sum(list(item.values())) for item in shopping_cart)
print(f"Please pay {to_pay} USD for the items: {shopping_cart}")

print("€€€€€€€€€€€€€ Once Again €€€€€€€€€€€€€")  # Correct if statement version but customer has some money left.
shopping_cart = []
money_in_account = 100


def add_items_to_cart(money):
    for k in inventory:
        if 0 < money >= inventory[k]:
            money -= inventory[k]
            shopping_cart.append({k: inventory[k]})


if money_in_account > 0:
    # while money_in_account >= 0:
    add_items_to_cart(money_in_account)

to_pay = sum(sum(list(item.values())) for item in shopping_cart)
print(f"Please pay {to_pay} USD for the items: {shopping_cart}")

print("££££££££££££££££££ The final version £££££££££££££££££££££")
shopping_cart = []
money_in_account = 100
least_price = inventory[min(inventory, key=inventory.get)]


def add_items_to_cart(money_available):
    for k in inventory:
        if 0 < money_available >= inventory[k]:
            money_available -= inventory[k]
            shopping_cart.append({k: inventory[k]})
    return money_available


while money_in_account > 0 and money_in_account >= least_price:
    money_in_account = add_items_to_cart(money_in_account)


to_pay = sum(sum(list(item.values())) for item in shopping_cart)
print(f"Please pay {to_pay} USD for the items: {shopping_cart}")
print(f"Price of the cheapest item: {least_price}\nMoney left in account: {money_in_account}")
