class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self._last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        amount = price * quantity
        self._last_transaction = amount
        self.total += amount

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self.total = int(self.total * (100 - self.discount) / 100)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        self.total -= self._last_transaction
        self._last_transaction = 0
