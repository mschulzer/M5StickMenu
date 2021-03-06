from m5stack import lcd

class GenericM5Stick(object):

    def __init__(self, parent=None):
        self.elements = list()
        self.parent = parent
        self.current_option = 0
        self.selected_option = -1

    def start(self):
        self.current_option = 0
        self.selected_option = -1
        self.produce()
        return self

    def add_element(self, element):
        element.menu = self
        self.elements.append(element)
        return self

    def down(self):
        if self.current_option == len(self.elements) - 1:
            self.current_option = 0
        else:
            self.current_option += 1

        self.produce()
        return self

    def enter(self):

        action_result = self.elements[self.current_option].action()
        if isinstance(action_result, GenericM5Stick):
            return action_result

        return self

    def exit(self):
        if self.parent is not None:
            self.parent.produce()

        return self.parent


class M5StickMenu(GenericM5Stick):
    def __init__(self):
        super(self.__class__, self).__init__()

    def clearDisplay(self):
        lcd.clear()

        lcd.orient(lcd.LANDSCAPE_FLIP)
        lcd.font(lcd.FONT_Ubuntu)

        return self

    def produce(self):
        self.clearDisplay()
        self.num_rows = 0
        self.lines = 3
        self.lim = []

        for i in range(len(self.elements)+1):
            if i != 0 and i % self.lines == 0:
                self.lim.append(i)

        if len(self.elements) >=3 and self.lim[-1] != len(self.elements):
            self.lim.append(len(self.elements))

        if len(self.elements) == 0:
            lcd.print(' ... tilbage >', 55, 55)
            return self
        elif len(self.elements) <=self.lines:
            for i in range(len(self.elements)):
                if self.current_option == i:
                    lcd.print('>', 5, 10+(self.num_rows*20))
                    lcd.print(self.elements[i].title, 20, 10+(self.num_rows*20))
                else:
                    lcd.print(self.elements[i].title, 20, 10+(self.num_rows*20))
                self.num_rows += 1

        else:

            if self.current_option <= 2:
                for k in range(self.lines):
                    if self.current_option == k:
                        lcd.print('>', 5, 10+(self.num_rows*20))
                        lcd.print(self.elements[k].title, 20, 10+(self.num_rows*20))
                    else:
                        lcd.print(self.elements[k].title, 20, 10+(self.num_rows*20))
                    self.num_rows += 1

            for n in range(len(self.lim)-1):
                if self.current_option >= self.lim[n] and self.current_option < self.lim[n+1]:
                    for i in range(self.lim[n], self.lim[n+1]):
                        if self.current_option == i:
                            lcd.print('>', 5, 10+(self.num_rows*20))
                            lcd.print(self.elements[i].title, 20, 10+(self.num_rows*20))
                        else:
                            lcd.print(self.elements[i].title, 20, 10+(self.num_rows*20))

                        self.num_rows += 1


        return self


class M5StickSub(M5StickMenu):
    def __init__(self, generic_m5stickmenu):
        super(M5StickMenu, self).__init__(generic_m5stickmenu)


class MenuItem(object):
    def __init__(self, title, menu=None):
        if len(title) > 50 or len(title) == 0:
            print('Menu title too long')
        self.title = title

class MenuElement(MenuItem):

    def __init__(self, title, function, args=None, menu=None):
        super(MenuElement, self).__init__(title=title, menu=menu)

        self.function = function
        self.returned_value = None

        if args is not None:
            self.args = args
        else:
            self.args = []


    def action(self):

        self.returned_value = self.function(*self.args)
        return self.returned_value

class SubmenuElement(MenuItem):
    def __init__(self, title, submenu, menu=None):
        super(SubmenuElement, self).__init__(title=title, menu=menu)

        self.submenu = submenu
        if menu:
            self.submenu.parent = menu

    def action(self):
        return self.submenu.start()
