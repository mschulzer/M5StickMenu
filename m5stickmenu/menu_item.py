class MenuItem(object):
    def __init__(self, title, menu=None):
        if len(title) > 50 or len(title) == 0:
            print('Menu title too long')
        self.title = title
