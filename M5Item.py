class M5Item(M5MenuItem):
    
    def __init__(self, text, function, args=None):
        """
        : text: description to be used
        : function: the function to be called
        """
        super(M5Item, self).__init__(text=text)
        
        self.function = function
        
        if args is not None:
            self.args = args
        else:
            self.args = []

        self.returned_value = None
        
    def action(self):
        self.returned_value = self.function(*self.args)
        return self.returned_value
