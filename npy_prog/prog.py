# !/usr/bin/env python
### encoding: utf-8

import npyscreen
import pandas as pd

class Form1(npyscreen.Form):
    def create(self):
        self.message = self.add(npyscreen.TitleText,
                                name='Description',
                                value='Enter yor credentials.',
                                color='CURSOR',
                                editable=False)
        self.myName = self.add(npyscreen.TitleText,
                               name='Name', color='WARNING')
        self.myAge = self.add(npyscreen.TitleText,
                              name='Age', color='VERYGOOD')

    def afterEditing(self):
        self.parentApp.setNextForm("Form2")

###############################################################################


class Form2(npyscreen.FormWithMenus):

    # Must be changed to locals >> pass data between two Forms
    global df, years, industry_code, industry_name_ANZSIC, rme_size_grp, variable, value, unit
    df = pd.read_csv('sample.csv', delimiter=',')
    years = list(df['year'])
    industry_code = list(df['industry_code_ANZSIC'])
    industry_name_ANZSIC = list(df['industry_name_ANZSIC'])
    rme_size_grp = list(df['rme_size_grp'])
    variable = list(df['variable'])
    value = list(df['value'])
    unit = list(df['unit'])

    def buttonPress(self, widget):
        npyscreen.notify_confirm(
            "BUTTON PRESSED!", title="Woot!", wrap=True, wide=True, editw=1)

    def create(self):
        df = pd.read_csv('sample.csv', delimiter=',')
        # data
        years = list(df['year'])
        industry_code = list(df['industry_code_ANZSIC'])
        industry_name_ANZSIC = list(df['industry_name_ANZSIC'])
        rme_size_grp = list(df['rme_size_grp'])
        variable = list(df['variable'])
        value = list(df['value'])
        unit = list(df['unit'])
        # wedgitself.
##                y, x = self.useable_space()
        self.Multi = self.add(npyscreen.TitleMultiSelect, max_height=7, value=[1, ], name="Pick Several", values=[
                              'years', 'industry_code', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value', 'unit'], scroll_exit=True, color='LABELBOLD')
        self.button = self.add(npyscreen.Button, name="Search",
                               value_changed_callback=self.buttonPress, color='LABELBOLD')

        self.Grid = self.add(MyGrid)
        self.Grid.values = []
        self.Grid.values.append(
            ['years', 'industry_code', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value', 'unit'])

        for x in range(len(years)):
            row = []
            row.append(years[x])
            row.append(industry_code[x])
            row.append(industry_name_ANZSIC[x])
            row.append(rme_size_grp[x])
            row.append(variable[x])
            row.append(value[x])
            row.append(unit[x])
            self.Grid.values.append(row)

        # self.Grid.column_width = 5,
        # self.Grid.col_margin = 1,
        # self.Grid.row_height  = 10,

        # The menus are created here.
        self.m1 = self.add_menu(name="Main Menu", shortcut="M")
        self.m1.addItemsFromList([
            ("Reverse Sort", self.reverse, "R", None, (self,)),
            ("Exit Application", self.exit_application, "é"), ])

        self.m2 = self.add_menu(name="Another Menu", shortcut="e",)
        self.m2.addItemsFromList([
            ("Exit Application", self.exit_application, "é"),
            ("Exit Application", self.exit_application, "é"),
            ("Exit Application", self.exit_application, "é")])

#                npyscreen.notify_confirm(argument)

    def reverse(self, argument):

        npyscreen.notify_confirm("years has been changed")
        years.reverse()
        industry_code.reverse()
        industry_name_ANZSIC.reverse()
        rme_size_grp.reverse()
        variable.reverse()
        value.reverse()
        unit.reverse()
        self.Grid.values = []

        self.Grid.values.append(
            ['years', 'industry_code', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value', 'unit'])
        for x in range(len(years)):
            row = []
            row.append(years[x])
            row.append(industry_code[x])
            row.append(industry_name_ANZSIC[x])
            row.append(rme_size_grp[x])
            row.append(variable[x])
            row.append(value[x])
            row.append(unit[x])
            self.Grid.values.append(row)

    def exit_application(self):
        self.parentApp.setNextForm(None)
        self.editing = False
        self.parentApp.switchFormNow()

    def afterEditing(self):
        self.parentApp.setNextForm(None)


class MyGrid(npyscreen.GridColTitles):

    def custom_print_cell(self, actual_cell, cell_display_value):
        if cell_display_value in ['years', 'industry_code', 'industry_name_ANZSIC', 'rme_size_grp', 'variable', 'value', 'unit']:
            actual_cell.color = 'GOOD'
        else:
            actual_cell.color = 'CURSOR'


class HopaApp(npyscreen.NPSAppManaged):
    def onStart(self):
        npyscreen.setTheme(npyscreen.Themes.ColorfulTheme)
        self.registerForm("MAIN", Form1())
        self.registerForm("Form2", Form2())


if __name__ == "__main__":
    App = HopaApp()
    App.run()
