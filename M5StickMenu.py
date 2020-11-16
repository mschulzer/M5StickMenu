class M5StickMenu():
    
    def __init__(self, landscape=True):
        
        self.items = list()
        
        if landscape:
            lcd.orient(lcd.LANDSCAPE)
            
        lcd.font(lcd.FONT_Ubuntu)
        lcd.clear()
        lcd.rect(3, 1, 157, 18, color=0XFFFFFF) # initialize with white rect -- should probably be placed in self.produce()
        
        self.current_option = 0
        self.selected_option = -1
        
        """ DEBUG
        print('menu_present: ' + str(menu_present))
        print('self.current_option: ' + str(self.current_option))
        """
        
    def add(self, item):
        
        self.items.append(item)
        return self
        
    def produce(self, index=0):
        
        if len(self.items) == 0:
            return self
            
        else:
            i = 2
            j = 0
            for item in self.items:
                lcd.print(self.items[j].text + '\n', 10, i)
                i = i + 18
                j = j + 1
        
        if index is not 0:
            self.index = index
        else:
            self.index = 0
        
        
        if self.index == 1:
            lcd.rect(3, 1, 157, 18, color=0X000000)
            lcd.rect(3, 19, 157, 18, color=0XFFFFFF)
        elif self.index == 2:
            lcd.rect(3, 19, 157, 18, color=0X000000)
            lcd.rect(3, 37, 157, 18, color=0XFFFFFF)
        elif self.index == 3:
            lcd.rect(3, 37, 157, 18, color=0X000000)
            lcd.rect(3, 56, 157, 18, color=0XFFFFFF)
        elif self.index == 4:
            #lcd.rect(3, 1, 157, 18, color=0X000000)
            lcd.rect(3, 56, 157, 18, color=0X000000)
            lcd.rect(3, 1, 157, 18, color=0XFFFFFF)
        
        return self
    
    def menuScroll(self):
        
        if self.current_option == 0:
            lcd.rect(3, 1, 157, 18, color=0X000000)
            lcd.rect(3, 19, 157, 18, color=0XFFFFFF)
        elif self.current_option == 1:
            lcd.rect(3, 19, 157, 18, color=0X000000)
            lcd.rect(3, 37, 157, 18, color=0XFFFFFF)
        elif self.current_option == 2:
            lcd.rect(3, 37, 157, 18, color=0X000000)
            lcd.rect(3, 56, 157, 18, color=0XFFFFFF)
        elif self.current_option == 3:
            #lcd.rect(3, 1, 157, 18, color=0X000000)
            lcd.rect(3, 56, 157, 18, color=0X000000)
            lcd.rect(3, 1, 157, 18, color=0XFFFFFF)
            
        if self.current_option == len(self.items) - 1:
            self.current_option = 0
        else:
            self.current_option += 1
        
        return self
    
    def menuChosen(self):
        global menu_present     # ugly hack
        
        if menu_present == 1:
            action_result = self.items[self.current_option].action()
            if isinstance(action_result, MyMenu):
                return action_result
        else:
            lcd.clear()
            lcd.font(lcd.FONT_Ubuntu)
            self.produce(self.current_option)   # where did we come from?
            
            menu_present = 1    # ugly hack
            
        return self
