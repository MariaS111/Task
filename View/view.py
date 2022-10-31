from kivy.config import Config
from kivy.uix.dropdown import DropDown
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
import os
import re
import xml.dom.minidom as minidom
from kivy.core.window import Window
from Control.controller import DataBaseController
from Model.model import Sportsman


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '1024')
Config.set('graphics', 'height', '720')


RED = [2.55, 1.53, 1.53, 1]
GREEN = [1.53, 2.55, 1.53, 1]
BLUE = [1.53, 1.53, 2.55, 1]
LUV = [2.29, 2.04, 2.55, 1]
GRAY = [2.24, 2.24, 2.24, 2.24]
P = [2.65, 2.55, 2.75, 1]

Builder.load_string("""
<CustomDropDown1>
    Button:
        text:"Main"
        size_hint_y: None
        height: 40
        on_release: root.select("Main")
        background_color: [2.29, 2.04, 2.55, 1]
    Button:
        text:"Spare"
        size_hint_y: None
        height: 40
        on_release: root.select("Spare")
        background_color: [2.29, 2.04, 2.55, 1] 
    Button:
        text:"Unknown"
        size_hint_y: None
        height: 40
        on_release: root.select("Unknown")
        background_color: [2.29, 2.04, 2.55, 1]      

<CustomDropDown2>
    Button:
        text:"Football"
        size_hint_y: None
        height: 40
        on_release: root.select("Football")
        background_color: [2.29, 2.04, 2.55, 1]
    Button:
        text:"Hockey"
        size_hint_y: None
        height: 40
        on_release: root.select("Hockey")
        background_color: [2.29, 2.04, 2.55, 1] 
    Button:
        text:"Swimming"
        size_hint_y: None
        height: 40
        on_release: root.select("Swimming")
        background_color: [2.29, 2.04, 2.55, 1]    
    Button:
        text:"Backetball"
        size_hint_y: None
        height: 40
        on_release: root.select("Backetball")
        background_color: [2.29, 2.04, 2.55, 1]       
    Button:
        text:"Aerobics"
        size_hint_y: None
        height: 40
        on_release: root.select("Aerobics")
        background_color: [2.29, 2.04, 2.55, 1]        

<CustomDropDown3>
    Button:
        text:"1 youth "
        size_hint_y: None
        height: 20
        on_release: root.select("1 youth")
        background_color: [2.29, 2.04, 2.55, 1]
    Button:
        text:"2"
        size_hint_y: None
        height: 20
        on_release: root.select("2")
        background_color: [2.29, 2.04, 2.55, 1] 
    Button:
        text:"3"
        size_hint_y: None
        height: 30
        on_release: root.select("3")
        background_color: [2.29, 2.04, 2.55, 1]   
    Button:
        text:"CMS"
        size_hint_y: None
        height: 30
        on_release: root.select("CMS")
        background_color: [2.29, 2.04, 2.55, 1] 
    Button:
        text:"MS"
        size_hint_y: None
        height: 30
        on_release: root.select("MS")
        background_color: [2.29, 2.04, 2.55, 1]      
"""
                    )

db_controller = None


class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        self._controller = db_controller

        Window.clearcolor = (2.55, 2.29, 2.04, 1)
        bx = BoxLayout(orientation='vertical')
        menu = Label(text="What would you like to do?", font_size=50, size_hint=(1, .3), color=P)
        gl = GridLayout(rows=2, spacing=50, padding=30)
        add = Button(text="Add sportsman", font_size=30,
                     on_press=lambda x: set_screen("add"), background_color=LUV)
        remove = Button(text="Delete sportsman", font_size=30,
                        on_press=lambda x: set_screen("remove"), background_color=LUV)
        show = Button(text="Search and show sportsman", font_size=30,
                      on_press=lambda x: set_screen("show"), background_color=LUV)

        exit = Button(text="Exit program", font_size=30,
                      on_press=lambda x: self.exit_program(), background_color=LUV)
        bx.add_widget(menu)
        bx.add_widget(gl)
        gl.add_widget(add)
        gl.add_widget(remove)
        gl.add_widget(show)
        gl.add_widget(exit)
        self.add_widget(bx)

    def exit_program(self):
        self._controller.write_data_into_file()
        raise SystemExit


class CustomDropDown1(DropDown):
    pass


class CustomDropDown2(DropDown):
    pass


class CustomDropDown3(DropDown):
    pass


class AddScreen(Screen):

    def __init__(self, **kw):
        super(AddScreen, self).__init__(**kw)
        self._controller = db_controller

        Window.clearcolor = (2.55, 2.29, 2.04, 1)
        new_field = GridLayout(rows=3, padding=10, spacing=10)

        fio_sportsman_text = Button(text="Sportsman", background_color=LUV)
        fio_sportsman_input = GridLayout(cols=3)
        name_sportsman_text = Button(text="Name", background_color=LUV)
        surname_sportsman_text = Button(text="Last name", background_color=LUV)
        patronymic_sportsman_text = Button(text="Patronymic", background_color=LUV)

        self.name_sportsman_input = TextInput()
        self.surname_sportsman_input = TextInput()
        self.patronymic_sportsman_input = TextInput()

        fio_sportsman_input.add_widget(surname_sportsman_text)
        fio_sportsman_input.add_widget(name_sportsman_text)
        fio_sportsman_input.add_widget(patronymic_sportsman_text)

        fio_sportsman_input.add_widget(self.surname_sportsman_input)
        fio_sportsman_input.add_widget(self.name_sportsman_input)
        fio_sportsman_input.add_widget(self.patronymic_sportsman_input)

        self.type_of_sport = Button(text="Select type of sport", background_color=LUV)
        d1 = CustomDropDown2()
        self.type_of_sport.bind(on_release=d1.open)
        d1.bind(on_select=lambda instance, x: setattr(self.type_of_sport, 'text', x))

        self.compound = Button(text="Select compound", background_color=LUV)
        d2 = CustomDropDown1()
        self.compound.bind(on_release=d2.open)
        d2.bind(on_select=lambda instance, x: setattr(self.compound, 'text', x))
        self.category = Button(text="Select category", background_color=LUV)
        d3 = CustomDropDown3()
        self.category.bind(on_release=d3.open)
        d3.bind(on_select=lambda instance, x: setattr(self.category, 'text', x))
        pos = GridLayout(cols=1)
        position = Button(text="Position", background_color=LUV)
        self.position_input = TextInput()
        pos.add_widget(position)
        pos.add_widget(self.position_input)

        num = GridLayout(cols=1)
        number_of_titles = Button(text="Number of titles", background_color=LUV)
        self.number_of_titles_input = TextInput()
        num.add_widget(number_of_titles)
        num.add_widget(self.number_of_titles_input)

        status = Button(text="Status of record", background_color=LUV)
        self.status_of_process = Button(background_color=GRAY)

        create_button = Button(text="Create new sportsman", on_press=lambda x: self.create_field(),
                               background_color=BLUE)
        back_button = Button(text="Back to menu", on_press=lambda x: set_screen("menu"),
                             background_color=BLUE)

        new_field.add_widget(fio_sportsman_text)
        new_field.add_widget(fio_sportsman_input)

        new_field.add_widget(self.type_of_sport)
        new_field.add_widget(self.compound)
        new_field.add_widget(self.category)
        new_field.add_widget(pos)
        new_field.add_widget(num)
        new_field.add_widget(status)
        new_field.add_widget(self.status_of_process)
        new_field.add_widget(back_button)
        new_field.add_widget(create_button)

        self.add_widget(new_field)

    def clear_all(self):

        self.name_sportsman_input.text = ''
        self.surname_sportsman_input.text = ''
        self.patronymic_sportsman_input.text = ''
        self.type_of_sport.text = 'Select type of sport'
        self.compound.text = 'Select compound'
        self.category.text = 'Select category'
        self.position_input.text = ''
        self.number_of_titles_input.text = ''

        self.name_sportsman_input.background_color = GRAY
        self.surname_sportsman_input.background_color = GRAY
        self.patronymic_sportsman_input.background_color = GRAY
        self.number_of_titles_input.background_color = GRAY
        self.position_input.background_color = GRAY

    def on_enter(self, *args):
        pass

    def on_leave(self, *args):
        self.clear_all()
        self.status_of_process.text = ''
        self.status_of_process.background_color = LUV

    def is_not_empty(self, input_):
        if input_.text == '':
            input_.background_color = RED
            return False
        else:
            input_.background_color = LUV
            return True

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = RED
            return False

    def check(self):
        if all((
                self.is_not_empty(self.name_sportsman_input),
                self.is_not_empty(self.surname_sportsman_input),
                self.is_not_empty(self.patronymic_sportsman_input),
                self.is_not_empty(self.type_of_sport),
                self.is_not_empty(self.compound),
                self.is_not_empty(self.category),
                self.is_not_empty(self.position_input),
                self.is_type_is_int(self.position_input),
                self.is_not_empty(self.number_of_titles_input),
                self.is_type_is_int(self.number_of_titles_input),
        )):
            return True

    def create_field(self):
        if self.check():
            sportsman = Sportsman(
                self.name_sportsman_input.text,
                self.surname_sportsman_input.text,
                self.patronymic_sportsman_input.text,
                self.compound.text,
                self.type_of_sport.text,
                self.position_input.text,
                self.number_of_titles_input.text,
                self.category.text,

            )

            self._controller.add_(sportsman)
            self.clear_all()
            self.status_of_process.background_color = GREEN
            self.status_of_process.text = 'Sportsman added'
        else:
            self.status_of_process.background_color = RED
            self.status_of_process.text = 'Error!!!'


class RemoveScreen(Screen):
    def __init__(self, **kw):
        super(RemoveScreen, self).__init__(**kw)
        self._controller = db_controller

        self.choice = 0
        select_remove = BoxLayout(orientation="vertical")
        self.menu_label = Label(text="Choose category to delete sportsman ", font_size=40, color=P)

        sportsman_fio_or_type_of_sport_remove_button = Button(
            text="Sportsman name, last name and patronymic or type of sport", font_size=30, background_color=LUV,
            size_hint=(1, .4),
            on_press=lambda x: self.set_choice(1, sportsman_fio_or_type_of_sport_remove_button))
        number_of_titles_remove_button = Button(
            text="Number of titles", font_size=30, background_color=LUV, size_hint=(1, .4),
            on_press=lambda x: self.set_choice(2, number_of_titles_remove_button))
        sportsman_fio_or_category_remove_button = Button(
            text="Sportsman name, last name and patronymic or category", font_size=30, background_color=LUV,
            size_hint=(1, .4),
            on_press=lambda x: self.set_choice(3, sportsman_fio_or_category_remove_button))

        self.choice_buttons = list()

        self.choice_buttons.append(sportsman_fio_or_type_of_sport_remove_button)
        self.choice_buttons.append(number_of_titles_remove_button)
        self.choice_buttons.append(sportsman_fio_or_category_remove_button)

        self.remove_input = TextInput()
        go_back_buttons = BoxLayout(size_hint=(1, .5), )
        remove_button = Button(text="Remove sportsman", on_press=lambda x: self.remove_field(),
                               background_color=BLUE)
        back_button = Button(text="Back to menu", on_press=lambda x: set_screen("menu"),
                             background_color=BLUE)

        select_remove.add_widget(self.menu_label)
        select_remove.add_widget(sportsman_fio_or_type_of_sport_remove_button)
        select_remove.add_widget(number_of_titles_remove_button)

        select_remove.add_widget(sportsman_fio_or_category_remove_button)

        select_remove.add_widget(self.remove_input)
        go_back_buttons.add_widget(back_button)
        go_back_buttons.add_widget(remove_button)
        select_remove.add_widget(go_back_buttons)
        self.add_widget(select_remove)

    def on_leave(self, *args):
        self.menu_label.text = "Choose category to delete sportsman"
        self.choice = 0
        self.remove_input.background_color = GRAY
        self.remove_input.text = ""

    def set_choice(self, choice, choice_button):
        self.choice = choice
        for button in self.choice_buttons:
            button.background_color = GRAY
        choice_button.background_color = GREEN

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = RED
            return False

    def remove_field(self):
        is_removed = False
        if 0 < self.choice < 4:
            if self.remove_input.text == "":
                self.remove_input.background_color = RED
            else:
                match self.choice:
                    case 1:
                        is_removed = self._controller.delete_by_sportsman_fio_or_type_of_sport(self.remove_input.text)
                    case 2:
                        if self.is_type_is_int(self.remove_input):
                            is_removed = self._controller.delete_by_number_of_titles(self.remove_input.text)
                        else:
                            self.massage_wrong_input()
                            return
                    case 3:
                        is_removed = self._controller.delete_by_sportsman_fio_or_category(self.remove_input.text)

                if is_removed:
                    self.menu_label.text = "Sportsman removed"
                else:
                    self.menu_label.text = "No such sportsman"
                self.remove_input.background_color = GRAY
        else:
            self.menu_label.text = "Choice category of remove"

    def massage_wrong_input(self):
        self.menu_label.text = "Invalid input"


class ShowScreen(Screen):
    fields_on_screens = 5

    def __init__(self, **kw):
        super(ShowScreen, self).__init__(**kw)
        self.list_of_screens = []
        self.index_of_screen = 0
        self.choice = 0
        self.present_fields_screen = None

        self._controller = db_controller

        test_layout = GridLayout(cols=5, padding=[0, 300, 0, 80])
        travel_layout = AnchorLayout(anchor_x='left', anchor_y="bottom")
        search_columns = GridLayout(cols=2, padding=[0, 0, 0, 80], row_force_default=True,
                                    row_default_height=(300 / 5))
        amount_of_pages = Button(text="Amount of records on page", background_color=LUV)
        self.amount_of_pages_input = TextInput()

        search_sportsman_by_fio_or_type_of_sport = Button(
            text="Search by sportsman name, last name and patronymic or type of sport",
            background_color=LUV,
            on_press=lambda x: self.set_search(1, search_sportsman_by_fio_or_type_of_sport))
        self.sportsman_fio_or_type_of_sport_input = TextInput()

        search_sportsman_by_number_of_titles = Button(
            text="Search by number of titles",
            background_color=LUV,
            on_press=lambda x: self.set_search(2, search_sportsman_by_number_of_titles)
        )
        self.sportsman_number_of_titles_input = TextInput()

        search_sportsman_by_fio_or_category = Button(
            text="Search by sportsman name, last name and patronymic or category",
            background_color=LUV,
            on_press=lambda x: self.set_search(3, search_sportsman_by_fio_or_category))
        self.sportsman_fio_or_category_input = TextInput()

        self.search_info = Button(text="SEARCH", background_color=LUV,
                                  on_press=lambda x: self.search())
        search = Button(text="ALL", background_color=LUV,
                        on_press=lambda x: self.show(self._controller.get_all_()))
        self.search_buttons = list()

        self.search_buttons.append(search_sportsman_by_fio_or_type_of_sport)
        self.search_buttons.append(search_sportsman_by_number_of_titles)
        self.search_buttons.append(search_sportsman_by_fio_or_category)

        search_columns.add_widget(search_sportsman_by_fio_or_type_of_sport)
        search_columns.add_widget(self.sportsman_fio_or_type_of_sport_input)
        search_columns.add_widget(search_sportsman_by_number_of_titles)
        search_columns.add_widget(self.sportsman_number_of_titles_input)
        search_columns.add_widget(search_sportsman_by_fio_or_category)
        search_columns.add_widget(self.sportsman_fio_or_category_input)

        search_columns.add_widget(search)
        search_columns.add_widget(self.search_info)
        search_columns.add_widget(amount_of_pages)
        search_columns.add_widget(self.amount_of_pages_input)

        columns_names = GridLayout(cols=6)
        sportsman_fio = Button(text="Sportsman", size_hint_x=None, size_hint_y=None, width=200, height=60,
                               background_color=GREEN)
        compound = Button(text="Compound", size_hint_y=None, size_hint_x=None, width=200, height=60,
                          background_color=GREEN)
        type_of_sport = Button(text="Type of sport", size_hint_y=None, width=200, height=60, background_color=GREEN)
        position = Button(text="Position", size_hint_y=None, width=200, height=60, background_color=GREEN)
        number_of_titles = Button(text="Number of titles", size_hint_y=None, width=200, height=60,
                                  background_color=GREEN)
        category = Button(text="Category", size_hint_y=None, width=200, height=60, background_color=GREEN)

        columns_names.add_widget(sportsman_fio)
        columns_names.add_widget(compound)
        columns_names.add_widget(type_of_sport)
        columns_names.add_widget(position)
        columns_names.add_widget(number_of_titles)
        columns_names.add_widget(category)

        navigation_panel = BoxLayout()
        number_of_page_boxlayout = BoxLayout(orientation="vertical")
        index_of_page_boxlayout = BoxLayout(orientation="vertical")
        number_of_elements_boxlayout = BoxLayout(orientation="vertical")

        back_button = Button(text="Back to menu", on_press=lambda x: set_screen("menu"),
                             size_hint_y=None, height=80, background_color=BLUE)
        first_page_button = Button(text="First page", on_press=lambda x: self.set_present_fields_screen(0),
                                   size_hint_y=None, height=80, background_color=BLUE)
        last_page_button = Button(text="Last page",
                                  on_press=lambda x: self.set_present_fields_screen(len(self.list_of_screens) - 1),
                                  size_hint_y=None, height=80, background_color=BLUE)
        next_page_button = Button(text="Next page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen + 1),
                                  size_hint_y=None, height=80, background_color=BLUE)
        past_page_button = Button(text="Past page",
                                  on_press=lambda x: self.set_present_fields_screen(self.index_of_screen - 1),
                                  size_hint_y=None, height=80, background_color=BLUE)
        number_of_page_text = Button(text="№ page",
                                     size_hint_y=None, height=40, background_color=BLUE)
        index_of_page_text = Button(text="Count pages",
                                    size_hint_y=None, height=40, background_color=BLUE)
        number_of_elements_text = Button(text="Count el",
                                         size_hint_y=None, height=40, background_color=BLUE)
        self.number_of_page_text = Button(text=str(self.index_of_screen),
                                          size_hint_y=None, height=40, background_color=BLUE)
        self.index_of_page_text = Button(text=str(len(self.list_of_screens)),
                                         size_hint_y=None, height=40, background_color=BLUE)
        self.number_of_elements_text = Button(text=str(len(self._controller.get_all_())),
                                              size_hint_y=None, height=40, background_color=BLUE)

        number_of_page_boxlayout.add_widget(number_of_page_text)
        number_of_page_boxlayout.add_widget(self.number_of_page_text)

        index_of_page_boxlayout.add_widget(index_of_page_text)
        index_of_page_boxlayout.add_widget(self.index_of_page_text)

        number_of_elements_boxlayout.add_widget(number_of_elements_text)
        number_of_elements_boxlayout.add_widget(self.number_of_elements_text)

        navigation_panel.add_widget(back_button)
        navigation_panel.add_widget(first_page_button)
        navigation_panel.add_widget(past_page_button)
        navigation_panel.add_widget(next_page_button)
        navigation_panel.add_widget(last_page_button)
        navigation_panel.add_widget(number_of_page_boxlayout)
        navigation_panel.add_widget(index_of_page_boxlayout)
        navigation_panel.add_widget(number_of_elements_boxlayout)
        travel_layout.add_widget(navigation_panel)
        test_layout.add_widget(columns_names)
        self.add_widget(search_columns)
        self.add_widget(travel_layout)
        self.add_widget(test_layout)

    def set_search(self, search, choice_button):
        self.choice = search
        for button in self.search_buttons:
            button.background_color = GRAY
        choice_button.background_color = GREEN

    def is_type_is_int(self, input_):
        try:
            int(input_.text)
            return True
        except Exception:
            input_.background_color = RED
            return False

    def search(self):
        if 0 < self.choice < 4:
            match self.choice:
                case 1:
                    if self.sportsman_fio_or_type_of_sport_input.text == '':
                        self.sportsman_fio_or_type_of_sport_input.background_color = RED
                    else:
                        try:
                            inf = self.sportsman_fio_or_type_of_sport_input.text
                            found_items = self._controller.search_by_sportsman_fio_or_type_of_sport(inf)
                            self.sportsman_fio_or_type_of_sport_input.background_color = GRAY
                            self.show(found_items)
                            self.clear_search_fields()
                        except Exception:
                            self.massage_wrong_input()
                case 2:
                    if self.sportsman_number_of_titles_input.text == '':
                        self.sportsman_number_of_titles_input.background_color = RED
                    else:
                        print(self.sportsman_number_of_titles_input.text)
                        if self.is_type_is_int(self.sportsman_number_of_titles_input):
                            self.sportsman_number_of_titles_input.background_color = GRAY
                            print(self.sportsman_number_of_titles_input.text)
                            found_items = self._controller.search_by_number_of_titles(
                                int(self.sportsman_number_of_titles_input.text)
                            )
                            self.clear_search_fields()
                            self.show(found_items)
                            self.clear_search_fields()
                case 3:
                    if self.sportsman_fio_or_category_input.text == '':
                        self.sportsman_fio_or_category_input.background_color = RED
                    else:
                        try:
                            inf = self.sportsman_fio_or_category_input.text
                            found_items = self._controller.search_by_sportsman_fio_or_category(inf)
                            self.sportsman_fio_or_category_input.background_color = GRAY
                            self.show(found_items)
                            self.clear_search_fields()
                        except Exception:
                            self.massage_wrong_input()


        else:
            if self.present_fields_screen:
                self.remove_widget(self.present_fields_screen)
            self.present_fields_screen = GridLayout(
                cols=5, padding=[0, 360, 0, 80],
                row_force_default=True,
                row_default_height=100)
            not_found = Button(text="Choose variant of searching")
            self.present_fields_screen.add_widget(not_found)
            self.add_widget(self.present_fields_screen)

    def massage_wrong_input(self):
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)
        self.present_fields_screen = GridLayout(
            cols=1, padding=[0, 360, 0, 80],
            row_force_default=True,
            row_default_height=100)
        not_found = Button(text="Invalid input")
        self.present_fields_screen.add_widget(not_found)
        self.add_widget(self.present_fields_screen)

    def show(self, list_of_fields):
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)
        if not list_of_fields:
            self.present_fields_screen = GridLayout(
                cols=1, padding=[0, 360, 0, 80],
                row_force_default=True,
                row_default_height=100)
            not_found = Button(text="Nothing found")
            self.present_fields_screen.add_widget(not_found)
            self.add_widget(self.present_fields_screen)
            return
        self.list_of_screens = []
        self.index_of_screen = 0
        self.number_of_elements_text.text = str(len(list_of_fields))
        if self.amount_of_pages_input.text:
            if self.is_type_is_int(self.amount_of_pages_input):
                ShowScreen.fields_on_screens = int(self.amount_of_pages_input.text)

        counter_of_screens = ShowScreen.fields_on_screens
        number_of_screens = 0
        for field in list_of_fields:
            if ShowScreen.fields_on_screens == counter_of_screens:
                counter_of_screens = 0
                record = GridLayout(cols=6, padding=[0, 360, 0, 80], row_force_default=True,
                                    row_default_height=(360 - 80) / ShowScreen.fields_on_screens)
                self.list_of_screens.append(record)
                number_of_screens += 1

            sportsman = f"{field.sportsman_name} {field.sportsman_last_name} {field.sportsman_patronymic}"
            record.add_widget(Button(text=sportsman, width=200, font_size=12, size_hint_x=None))
            record.add_widget(Button(text=field.compound, width=200, font_size=12))
            record.add_widget(Button(text=field.type_of_sport, width=200, font_size=12))
            record.add_widget(Button(text=field.position, width=200, font_size=12))
            record.add_widget(Button(text=str(field.number_of_titles), width=200, font_size=12))
            record.add_widget(Button(text=field.category, width=200, font_size=12))
            counter_of_screens += 1

        self.present_fields_screen = self.list_of_screens[self.index_of_screen]
        self.number_of_page_text.text = str(self.index_of_screen + 1)
        self.index_of_page_text.text = str(len(self.list_of_screens))
        self.add_widget(self.present_fields_screen)

    def set_present_fields_screen(self, index_of_screen):
        if -1 < index_of_screen < len(self.list_of_screens):
            self.index_of_screen = index_of_screen
            self.remove_widget(self.present_fields_screen)
            self.present_fields_screen = self.list_of_screens[index_of_screen]
            self.add_widget(self.present_fields_screen)
            self.number_of_page_text.text = str(self.index_of_screen + 1)

    def clear_search_fields(self):

        self.sportsman_fio_or_type_of_sport_input.text = ''
        self.sportsman_number_of_titles_input.text = ''
        self.sportsman_fio_or_category_input.text = ''
        self.sportsman_fio_or_type_of_sport_input.background_color = GRAY
        self.sportsman_number_of_titles_input.background_color = GRAY
        self.sportsman_fio_or_category_input.background_color = GRAY

    def on_leave(self, *args):
        for button in self.search_buttons:
            button.background_color = GRAY
        self.choice = 0
        self.clear_search_fields()
        if self.present_fields_screen:
            self.remove_widget(self.present_fields_screen)


class ChooseFile(Screen):

    def __init__(self, **kw):
        super(ChooseFile, self).__init__(**kw)
        self.file = ""
        Window.clearcolor = (2.55, 2.29, 2.04, 1)
        self.lib_was_chosen = False
        choice = BoxLayout(orientation="vertical")
        menu1 = Label(text="Choosing a base for program", font_size=50, size_hint=(1, .2), color=P)
        choice1 = GridLayout(cols=4, spacing=50, padding=30, size_hint=(1, .6), )
        create_lib_box = BoxLayout(orientation="vertical")
        create_lib = Button(text="Create base", font_size=30, background_color=LUV,
                            on_press=lambda x: self.create_file(self.create_lib_input.text, create_lib))
        self.create_lib_input = TextInput()
        create_lib_box.add_widget(create_lib)
        create_lib_box.add_widget(self.create_lib_input)
        self.file_buttons = list()
        self.file_buttons.append(create_lib)

        pattern = re.compile("\w+.xml")
        for file in os.listdir("."):
            if re.match(pattern, file):
                print(file)
                new_lib = Button(text=file, font_size=30,
                                 on_press=self.set_library, background_color=LUV)
                choice1.add_widget(new_lib)
                self.file_buttons.append(new_lib)

        menu = Button(text="Choose Base", font_size=48, size_hint=(1, .2), background_color=P,
                      on_press=lambda x: self.create_menu())

        choice.add_widget(menu1)
        choice1.add_widget(create_lib_box)
        choice.add_widget(choice1)
        choice.add_widget(menu)

        self.add_widget(choice)

    def create_file(self, file, create_button):
        self.lib_was_chosen = False
        for button in self.file_buttons:
            button.background_color = GRAY
        pattern = re.compile("\w+.xml")
        if re.match(pattern, file):
            if file not in os.listdir("."):
                create_button.disabled = True
                dom_tree = minidom.Document()
                pass_table = dom_tree.createElement("pass_table")
                dom_tree.appendChild(pass_table)
                dom_tree.writexml(open(file, 'w'),
                                  indent="  ",
                                  addindent="  ",
                                  newl='\n')
                dom_tree.unlink()
                self.lib_was_chosen = True
                global db_controller
                db_controller = DataBaseController(file)
                create_button.background_color = GREEN
                create_button.text = "Base selected"
            else:
                create_button.background_color = RED
                create_button.text = "This base already exists"
        else:
            create_button.background_color = RED
            create_button.text = "Invalid input"

    def input_library(self, file, choice_button):
        self.lib_was_chosen = False
        for button in self.file_buttons:
            button.background_color = P
        if self.file_search_input.text in os.listdir("."):
            self.lib_was_chosen = True
            global db_controller
            db_controller = DataBaseController(file)
            choice_button.background_color = GREEN
            choice_button.text = "Base selected"
        else:
            choice_button.background_color = RED
            choice_button.text = "No such base"

    def set_library(self, choice_button):
        self.lib_was_chosen = True
        for button in self.file_buttons:
            button.background_color = GRAY
        self.file = "./" + choice_button.text
        global db_controller
        db_controller = DataBaseController(self.file)
        choice_button.background_color = GREEN

    def create_menu(self):
        if self.lib_was_chosen:
            sm.add_widget(MenuScreen(name="menu"))
            sm.add_widget(AddScreen(name="add"))
            sm.add_widget(RemoveScreen(name="remove"))
            sm.add_widget(ShowScreen(name="show"))
            set_screen("menu")


sm = ScreenManager()
sm.add_widget(ChooseFile(name="choice"))


def set_screen(screen_name):
    sm.current = screen_name


class MyApp(App):
    def build(self):
        return sm
