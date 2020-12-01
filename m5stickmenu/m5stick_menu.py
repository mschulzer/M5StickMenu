from m5stack import lcd
from .generic_m5stick import GenericM5Stick

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

        for i in range(len(self.items)+1):
            if i != 0 and i % self.lines == 0:
                self.lim.append(i)

        if self.lim[-1] != len(self.items):
            self.lim.append(len(self.items))

        if len(self.items) == 0:
            lcd.print(' ... tilbage >', 55, 55)
            return self
        elif len(self.items) <=self.lines:
            for i in range(len(self.items)):
                if self.current_option == i:
                    lcd.print('>', 5, 10+(self.num_rows*20))
                    lcd.print(self.items[i].title, 20, 10+(self.num_rows*20))
                else:
                    lcd.print(self.items[i].title, 20, 10+(self.num_rows*20))
                self.num_rows += 1

        else:

            if self.current_option <= 2:
                for k in range(self.lines):
                    if self.current_option == k:
                        lcd.print('>', 5, 10+(self.num_rows*20))
                        lcd.print(self.items[k].title, 20, 10+(self.num_rows*20))
                    else:
                        lcd.print(self.items[k].title, 20, 10+(self.num_rows*20))
                    self.num_rows += 1

            for n in range(len(self.lim)-1):
                if self.current_option >= self.lim[n] and self.current_option < self.lim[n+1]:
                    for i in range(self.lim[n], self.lim[n+1]):
                        if self.current_option == i:
                            lcd.print('>', 5, 10+(self.num_rows*20))
                            lcd.print(self.items[i].title, 20, 10+(self.num_rows*20))
                        else:
                            lcd.print(self.items[i].title, 20, 10+(self.num_rows*20))

                        self.num_rows += 1


        return self
