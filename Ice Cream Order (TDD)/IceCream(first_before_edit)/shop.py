class IceCreamShop (object):

    def __init__(self,quantity):
        self.quantity = quantity

    def remove_ice(self,order):
        self.quantity -=order
        return 'removed'

    def add_ice(self,newArrived):
        self.quantity -=newArrived
        return 'added'

    


  
