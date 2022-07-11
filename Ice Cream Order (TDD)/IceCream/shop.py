class IceCreamShop (object):

    def __init__(self,quantity):
        self.quantity = quantity

    def remove_ice(self,order):
        if isinstance(order, int):
            self.quantity -=order
            return self.quantity
        else :
            return 'Enter an Intger'

    def add_ice(self,newArrived):
        if isinstance(newArrived, int):
            self.quantity +=newArrived
            return self.quantity
        else :
            return 'Enter an Intger'
    


  
