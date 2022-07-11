#!/usr/bin/env python
import npyscreen
class HopaApp(npyscreen.NPSApp):
	def main(self):
		# These lines create the form and populate it with widgets.
		# A fairly complex screen in only 8 or so lines of code - a line for each control.
		npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
		F = npyscreen.ActionFormWithMenus(name = "hopa example 2")
		
		
		## npyscreen has many (Widget) >>> TitleText >> normall string to be writen. 
		t = F.add(npyscreen.TitleText, name = "Text:" )
		
		## npyscreen has many (Widget) >>> TitleFilename >> file name >> auto complete 'tab'.		
		fn = F.add(npyscreen.TitleFilename, name = "Filename:")

		## npyscreen has many (Widget) >>> TitleDateCombo >> Date with many keys. 
		## d : day forward   , D : day backward
		## w : week forward  , W : week backward
		## m : month forward , M : month backward
		## y : year forward  , Y : year backward
		## t : time Now
		## c : cancel 	     , q : quit
		dt = F.add(npyscreen.TitleDateCombo, name = "Date:")

		## npyscreen has many (Widget) >>> TitleSlider >> a slider with a max value.
		s = F.add(npyscreen.TitleSlider, out_of=12, name = "Slider")
		
		## npyscreen has many (Widget) >>> MultiLineEdit >> a multi line text that can be edit.
		## max_height 	>> max visible lines (can be scrolled)
		## rely 	>> position relative to the origin.		
		ml= F.add(npyscreen.MultiLineEdit, value = """try typing here! Mutiline text, press ^R to reformat.\n""", 
			max_height=5, rely=9)

		## npyscreen has many (Widget) >>> TitleSelectOne >> radio buttons to select only one
		## max_height 	>> max visible lines (can be scrolled)
		## value 	>>	starting selected value can be none	>> start from index 0
		## name 	>>	the name of the widget	
		## values 	>>	the list to select from	
		## scroll_exit >> 	exit if scrolled >>>> if false > cant exit with scrolling 	
		ms= F.add(npyscreen.TitleSelectOne, max_height=4, value = [1,], name="Pick One", 
				values = ["Option1","Option2","Option3"], scroll_exit=True)

		## npyscreen has many (Widget) >>> TitleMultiSelect >> radio buttons to select only one
		## max_height 	>> max visible lines (can be scrolled)
		## value 	>>	starting selected value can be none	 >> start from index 0
		## name 	>>	the name of the widget	
		## values 	>>	the list to select from	
		## scroll_exit >> 	exit if scrolled >>>> if false > cant exit with scrolling 		
		ms2= F.add(npyscreen.TitleMultiSelect, max_height=4, value = [1,2], name="Pick Several", 
				values = ["Option1","Option2","Option3"], scroll_exit=True)
		
		# This lets the user play with the Form.
		F.edit()


if __name__ == "__main__":
	App = HopaApp()
	App.run()


