from .menu_item import MenuItem

class SubmenuItem(MenuItem):
    def __init__(self, title, submenu, menu=None):
        super(SubmenuItem, self).__init__(title=title, menu=menu)

        self.submenu = submenu
        if menu:
            self.submenu.parent = menu

    def action(self):
        return self.submenu.start()
