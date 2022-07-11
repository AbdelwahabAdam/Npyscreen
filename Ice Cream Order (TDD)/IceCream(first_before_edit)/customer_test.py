import unittest
from  customer import *

class ShoppingCartTestCases(unittest.TestCase):

    def setUp(self):
        self.customer = Customer('hopa')

    def test_init(self):
        #### check all init conditions
        self.assertEqual(self.customer.cart, {}, msg='Initial value of cart, not correct')
        self.assertEqual(self.customer.orders, 0, msg='Initial value of orders, not correct')
        self.assertEqual(self.customer.name, 'hopa', msg='Initial value of name, not correct')

    def test_diffrent_In(self) :
        ##### String and Float input for add_toCart
        self.assertEqual(self.customer.add_toCart('Vanilla', '4', 3), 'Enter an Intger', msg='String is not handeld quantity')
        self.assertEqual(self.customer.add_toCart('Vanilla', 4, '3'), 'Enter an Intger', msg='String is not handeld price')      
        self.assertEqual(self.customer.add_toCart('Vanilla', 4.5, 3), 'Enter an Intger', msg='float is not handeld quantity')
        self.assertEqual(self.customer.add_toCart('Vanilla', 4, 3.2), 'Enter an Intger', msg='float is not handeld price')   
        ##### String and Float input for remove_fromCart
        self.customer.add_toCart('Vanilla', 4, 3)
        self.assertEqual(self.customer.remove_fromCart('Vanilla', '4', 3), 'Enter an Intger', msg='String is not handeld quantity')
        self.assertEqual(self.customer.remove_fromCart('Vanilla', 4, '3'), 'Enter an Intger', msg='String is not handeld price')      
        self.assertEqual(self.customer.remove_fromCart('Vanilla', 4.5, 3), 'Enter an Intger', msg='float is not handeld quantity')
        self.assertEqual(self.customer.remove_fromCart('Vanilla', 4, 3.2), 'Enter an Intger', msg='float is not handeld price')      


    def test_add_toCart(self):
        ##### 1 >>>> add_toCart >>>> add  1 then check     
        self.customer.add_toCart('Vanilla', 4, 3)
        self.assertEqual(self.customer.orders, 12, msg='Customer orders is not correct after add icecream')
        self.assertEqual(self.customer.cart['Vanilla'], 4, msg='Customer cart is not correct after adding icecream')
        ##### 2 >>>> add_toCart >>>> add  2 then check     
        self.customer.add_toCart('choco', 2,5)
        self.assertEqual(self.customer.orders, 22, msg='Customer orders is not correct after add two icecream')
        self.assertEqual(self.customer.cart['Vanilla'], 4, msg='Customer cart is not correct after adding two icecream')        
        self.assertEqual(self.customer.cart['choco'], 2, msg='Customer cart is not correct after adding two icecream')     


    def test_remove_fromCart(self):
        ##### 1 >>>> remove_fromCart >>>> add  1 then remove it completely   
        self.customer.orders = 0
        self.customer.cart = {}
        self.customer.add_toCart('Vanilla', 5, 2)
        self.customer.remove_fromCart('Vanilla', 5, 2)
        self.assertEqual(self.customer.orders, 10, msg='Customer orders is not correct after remove icecream2')
        self.assertEqual(self.customer.cart, {}, msg='Customer cart is not empty after remove icecream2') #### error
        ##### 2 >>>> remove_fromCart >>>> add  2 then remove part of them     
        self.customer.add_toCart('Vanilla', 5, 2)
        self.customer.add_toCart('choco', 4, 3)
        self.customer.remove_fromCart('Vanilla', 3, 2)
        self.customer.remove_fromCart('choco', 2, 3)
        self.assertEqual(self.customer.orders, 10, msg='Customer orders is not correct after diff. add and remove icecream')
        self.assertEqual(self.customer.cart, {'Vanilla': 2, 'choco': 2}, msg='Customer cart is not empty after remove icecream2')
        ##### 3 >>>> remove_fromCart >>>>  remove with out adding
        self.customer.orders = 0
        self.customer.cart = {}
        self.customer.remove_fromCart('Vanilla', 3, 2)

    def test_cart_info (self):
        ##### 1 >>>> cart_info >>>>  check  without adding         
        self.assertEqual(self.customer.cart_info(), {}, msg='Cart info is not correct after adding two icecream')
        ##### 2 >>>> cart_info >>>> add  2 then check           
        self.customer.add_toCart('Vanilla', 5, 2)
        self.customer.add_toCart('choco', 3, 4)
        self.assertEqual(self.customer.cart_info(), {'Vanilla': 5, 'choco': 3}, msg='Cart info is not correct after adding two icecream')

    def test_customer_info (self):
        ##### 1 >>>> customer_info >>>>  Only Name here       
        self.assertEqual(self.customer.name,'hopa', msg='cutomer Info is not correct')

    def test_checkout (self):
        ##### 1 >>>> checkout >>>>  add 1 then checkout with extra moeny   
        self.customer.add_toCart('Vanilla', 5, 2)
        self.customer.checkout(20)
        self.assertEqual(self.customer.checkout(20),10, msg='check out reminder is not correct') ## error
        ##### 2 >>>> checkout >>>>  add 1 then checkout with low moeny   
        self.customer.orders = 0
        self.customer.cart = {}       
        self.customer.add_toCart('Vanilla', 5, 2)
        self.customer.checkout(5)
        self.assertEqual(self.customer.checkout(5),"sorry, Cash paid not enough", msg='negative reminder is not correcet')
        self.assertEqual(self.customer.cart_info(),{}, msg='cart is not empty after  check out') ## error
        ##### 3 >>>> checkout >>>>  add 1 then checkout with exact amount of moeny   
        self.customer.orders = 0
        self.customer.cart = {}           
        self.customer.add_toCart('Vanilla', 5, 2)
        self.customer.checkout(10)
        self.assertEqual(self.customer.checkout(10),0, msg='check out reminder is not correct') ## error


if __name__ == '__main__':
    unittest.main()