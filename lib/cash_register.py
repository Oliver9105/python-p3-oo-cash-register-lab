#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes a CashRegister instance.
        :param discount: Optional discount percentage to apply.
        """
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        """
        Adds an item to the register.
        :param title: Name of the item.
        :param price: Price of the item.
        :param quantity: Quantity of the item being added.
        """
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        """
        Applies the discount to the total if available.
        Prints the updated total or a message if no discount is available.
        """
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Voids the last transaction by subtracting its amount from the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0
