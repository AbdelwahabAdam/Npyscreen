class Customer (object):

    def __init__(self, name):
        self.orders = 0
        self.cart = {}
        self.name = name

    def add_toCart(self, item_name, quantity, price):
        if isinstance(item_name, str) and isinstance(quantity, int) and isinstance(price, int):
            self.orders += price*quantity
            self.cart.update({item_name: quantity})
            return self.cart
        else:
            return 'Enter an Intger'

    def remove_fromCart(self, item_name, quantity, price):
        if isinstance(item_name, str) and isinstance(quantity, int) and isinstance(price, int):
            if item_name in self.cart:
                if quantity < self.cart[item_name] and quantity > 0:
                    self.cart[item_name] -= quantity
                    self.orders -= price*quantity
                elif quantity == self.cart[item_name]:
                    self.orders = self.orders - price*quantity
                    del self.cart[item_name]
                return self.orders
            else:
                return str(item_name)+" is not in your card"
        else:
            return 'Enter an Intger'

    def cart_info(self):
        if self.cart == {}:
            return {}
        else:
            return self.cart

    def customer_info(self):
        return self.name 

    def checkout(self, cash_paid):
        if cash_paid >= self.orders:
            if cash_paid - self.orders == 0:
                self.cart = {}
                return 0
            else:
                self.cart = {}
                return cash_paid - self.orders
        return "sorry, Cash paid not enough"
