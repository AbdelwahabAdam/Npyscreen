#!/usr/bin/env python
# encoding: utf-8

import npyscreen
from datetime import date

class HopaForm(npyscreen.Form):
    def create(self):
        self.myName        = self.add(npyscreen.TitleText, name='Name')
        self.myAge  = self.add(npyscreen.TitleText, name='Age')
        self.myBirthDate        = self.add(npyscreen.TitleDateCombo, name='Date of Birth')

def myFunction(*args):
    F = HopaForm(name = "how many day have you lived")
    F.edit()
    if F.myBirthDate.value == '' or F.myName.value == '' or F.myAge.value == '' :
        return "***** please Fill all the field *****"

    else :
        dumy_birth = str(F.myBirthDate.value).split('-')
        
            
        birth = date(int(dumy_birth[0]),int(dumy_birth[1]),int(dumy_birth[2]))
        today = date.today()
        Lived_days = today - birth


        return F.myName.value + ",You are " + F.myAge.value+ " Years old and you lived " + str(Lived_days.days) + " days"

if __name__ == '__main__':
    print (npyscreen.wrapper_basic(myFunction))
