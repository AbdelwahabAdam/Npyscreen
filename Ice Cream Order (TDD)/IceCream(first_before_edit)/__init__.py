from customer import * 
from shop import *

if __name__ == '__main__':

    blabn = IceCreamShop(100)
    hopa = Customer('hopa')
    print("******* Customer Info *******")
    print(hopa.customer_info())
    print(hopa.cart_info())
    print("*********** add order *******")
    print(hopa.orders)
    print(hopa.add_toCart('Vanilla',5,5))
    print("*********** check out *******")
    print(hopa.checkout(20))
    print("***********return************")
    print(hopa.remove_fromCart('Choco',2,5))
    print(hopa.cart_info())
    print("***********return************")
    print(hopa.remove_fromCart('Vanilla',2,5))
    print(hopa.cart_info())
    print("*********** check out *******")
    print(hopa.checkout(20))
    print("*****************************")
    print("*********** Shop ************")
    print("******* Remove order ********")
    print(blabn.quantity)
    blabn.remove_ice(hopa.checkout(20))
    print(blabn.quantity)