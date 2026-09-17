# Order model.


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.items = []

    # Add an item to the order.
    def add_item(self, item_name, price):
        self.items.append((item_name, price))

    # Calculate the order total.
    def total(self):
        total = 0

        for item_name, price in self.items:
            total += price

        return total