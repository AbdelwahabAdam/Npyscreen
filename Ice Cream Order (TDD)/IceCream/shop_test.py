import unittest
from shop import *


class shopTestCases(unittest.TestCase):

    def setUp(self):
        self.shop = IceCreamShop(100)

    def test_init(self):
        # check all init conditions
        self.assertEqual(self.shop.quantity,100,msg='Initial value of shop quantitiy, not correct')
  

    def test_diffrent_In(self):
        # String input for remove_ice, add_ice
        self.assertEqual(self.shop.remove_ice('545'),'Enter an Intger',msg='Initial value of shop quantitiy, not correct')
        self.assertEqual(self.shop.add_ice('asd'),'Enter an Intger',msg='Initial value of shop quantitiy, not correct')
        # float input for remove_ice, add_ice
        self.assertEqual(self.shop.remove_ice(12.5),'Enter an Intger',msg='Initial value of shop quantitiy, not correct')
        self.assertEqual(self.shop.add_ice(0.5),'Enter an Intger',msg='Initial value of shop quantitiy, not correct')
  
 
    def test_remove_ice(self):
        # 1 >>>> remove_ice >>>> remove then check
        self.shop.remove_ice(5)
        self.assertEqual(self.shop.quantity,95,msg='shop quantity is not correct after removing ice')
        # 2 >>>> remove_ice >>>> add then remove then check
        self.shop.quantity = 100
        self.shop.add_ice(20)
        self.shop.remove_ice(10)
        self.assertEqual(self.shop.quantity,110,msg='shop quantity is not correct after removing ice')
        

    def test_add_ice(self):
        # 1 >>>> add_ice >>>> add then  check
        self.shop.add_ice(10)
        self.assertEqual(self.shop.quantity,110,msg='shop quantity is not correct after adding ice')



    


  
