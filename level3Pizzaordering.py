# Needs fixing
import os

size_prices = {'S': 8, 'M':10, 'L':12}
topping_prices = {'Pepperoni':3, 'Sausage':3, 'Mushrooms':3, 'Bacon':3, 'Onions':3, 'Extra Cheese':3, 'Peppers':3, 'Olives':3, 'Spinach':3, 'Basil':3, 'Tomato':3, 'Beef':3}

class Order():
    def __init__(self):
        self.order_items = []

    def add_item(self, item):
        for topping in item.toppings:
            if not is_topping_allowed(topping):
                raise Exception("invalid_topping " + topping)
        self.order_items.append(item)
    def remove_item(self, index):
        if index >= 0 and index <= len(self.order_items):
            del self.order_items[index]
            return True
        else:
            return False

    def compute_total(self):

        total = 0.0
        for item in self.order_items:
            item_price = size_prices[item.size]
            for topping in item.toppings:
                item_price += topping_prices[topping]
            total += item_price

        return total

class OrderItem():
    def __init__(self, product, toppings, size):
        self.product = product
        self.toppings = toppings
        self.size = size

    def parse_from_string(line):
        line = line.strip()
        product, toppings_csv, size = line.split(";")
        toppings = toppings_csv.split(",")
        return OrderItem(product, toppings, size)

def is_topping_allowed(topping):
    return topping in topping_prices

def display_header():
    print("Welcome to Lunch your order service!")


def display_order(order):
    if len(order.order_items) == 0:
        print("No order items yet")
    else:
        index = 1
        for item in order.order_items:
            print(
                f"Item {index}: Product '{item.product}' with toppings '{item.toppings}' in size '{item.size}'")
            index += 1

def get_users_choice():
    selection = input("(A)dd, (R)emove, (S)ave, (L)oad, (P)rint, (C)ompute total, (Q)uit: ")
    if len(selection.strip()) == 0:
        return "Q"
    return selection[0].upper()


def add_order_item(order):
    size = input("Please enter food size (S,M,L): ")[0].upper()
    print(f"Toppings:\n{','.join(topping_prices.keys())}")
    toppings = []
    while True:
        topping = input("Please enter your toppings or press enter to stop: ")
        if topping == "":
            break

        if not is_topping_allowed(topping):
            print(f"Topping {topping} is not allowed!")
            continue

        toppings.append(topping)

    order_item = OrderItem("Pizza", toppings, size)
    order.add_item(order_item)


def remove_order_item(order):

    index_to_remove = int(input("Please enter position of item to remove: ")) - 1
    if not order.remove_item(index_to_remove):
        print("Item does not exist in order.")

def save_order(order):
    file_name = input("Please enter file name: ")
    with open(file_name, 'w') as f:
        for item in order.order_items:
            # Pizza Salami M
            # Pizza Salami,Onions M
            f.write(f"{item.product};{','.join(item.toppings)};{item.size}\n")


def load_order():
    file_name = input("Please enter file name: ")

    order = Order()
    with open(file_name, 'r') as f:
        for line in f.readlines():
            # skip empty lines
            if line == '':
                continue
            order.add_item(OrderItem.parse_from_string(line))

    return order

def compute_order_price(order):
    total = order.compute_total()
    print(f"Total: {total}")

def display_goodbye():
    print("Thank you for using Lunch order!")

def main():
    display_header()
    
    order = Order()

    while True:
        choice = get_users_choice()
        os.system("clear")
        if choice == "A":
            add_order_item(order)

        elif choice == "R":
            remove_order_item(order)

        elif choice == "S":
            save_order(order)

        elif choice == "L":
            order = load_order()
        
        elif choice == "C":
            compute_order_price(order)
        
        elif choice == "P":
            display_order(order)

        if choice == "Q":
            break

    display_goodbye()


if __name__ == "__main__":
    main()