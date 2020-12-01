from .menu_item import MenuItem

class FunctionItem(MenuItem):

    def __init__(self, title, function, args=None, menu=None):
        super(FunctionItem, self).__init__(title=title, menu=menu)

        self.function = function
        self.returned_value = None

        if args is not None:
            self.args = args
        else:
            self.args = []


    def action(self):

        self.returned_value = self.function(*self.args)
        return self.returned_value
