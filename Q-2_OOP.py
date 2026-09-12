"""
QUESTION 2 - ORDER CLASS

Goal:

Create an Order class to represent an order with its
order ID, customer, and items.

The class should:

- Store the order ID and customer.
- Add items and their prices to the order.
- Calculate the total price of all items.
"""


# Order class with add_item() and total() methods.
class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    # Add an item and its price to the order.
    def add_item(self, item_name, price):
        self.items.append((item_name, price))

    # Calculate and return the order total.
    def total(self):
        total = 0

        for item_name, price in self.items:
            total += price

        return total


# Create an order.
order_1 = Order(101, "Ram")

order_1.add_item("banana", 20)
order_1.add_item("apple", 200)

print(order_1.customer)
print(order_1.total())