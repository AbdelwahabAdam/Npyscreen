class Customer (object):
    
   def __init__(self,name):
       self.orders = 0
       self.cart = {}
       self.name = name

   def add_toCart(self, item_name, quantity, price):
       self.orders += price*quantity
       self.cart.update({item_name: quantity})
       return self.cart

   def remove_fromCart(self, item_name, quantity, price):
       if item_name in self.cart:
           if quantity < self.cart[item_name] and quantity > 0:
               self.cart[item_name] -= quantity
               self.orders -= price*quantity
           return "Returned"

       else :
            return str(item_name)+" is not in your card"

   def cart_info (self):
        if self.cart == {} :
            return "Empty Cart"
        else :
            return self.cart

   def customer_info (self):
        return self.name

   def checkout (self, cash_paid):
       if cash_paid >= self.orders:
            if cash_paid - self.orders == 0:
                return 0
            else :
                return len(self.cart)  #cash_paid - self.orders
       return "sorry, Cash paid not enough"    

if __name__ == '__main__':

    hopa = Customer('hopa')
    print("******* Customer Info *******")
    print(hopa.customer_info())
    print(hopa.cart_info())
    print("*********** add order *******")
    print(hopa.orders)
    print(hopa.add_toCart('Vanilla',5,5))
    print("***********return************")
    print(hopa.remove_fromCart('Vanilla',5,5))
    print(hopa.cart_info())
    print("*********** Shop ************")
    print("******* Remove order ********")
