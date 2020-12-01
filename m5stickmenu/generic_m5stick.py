class GenericM5Stick(object):

    def __init__(self, parent=None):
        self.items = list()
        self.parent = parent
        self.current_option = 0
        self.selected_option = -1

    def start(self):
        self.current_option = 0
        self.selected_option = -1
        self.produce()
        return self

    def add_item(self, item):
        item.menu = self
        self.items.append(item)
        return self

    def down(self):
        if self.current_option == len(self.items) - 1:
            self.current_option = 0
        else:
            self.current_option += 1

        self.produce()
        return self

    def enter(self):

        action_result = self.items[self.current_option].action()
        if isinstance(action_result, GenericM5Stick):
            return action_result

        return self

    def exit(self):
        if self.parent is not None:
            self.parent.produce()

        return self.parent
