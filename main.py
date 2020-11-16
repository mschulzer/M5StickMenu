from M5StickMenu import *


def main():
    
    menu = M5StickMenu(landscape=True)
    
    item1 = M5Item("Menu item #1", tprogram_a, [1])
    item2 = M5Item("Menu item #2", tprogram_b, [2])
    item3 = M5Item("Menu item #3", tprogram_c, [3])
    item4 = M5Item("Menu item #4", tprogram_a, [4])
    
    menu.add(item1)
    menu.add(item2)
    menu.add(item3)
    menu.add(item4)
    
    menu.produce()
    
    btnA.wasPressed(menu.menuScroll)
    btnB.wasPressed(menu.menuChosen)

    
    
def tprogram_a(item_index):
	print("Menu item %d pressed" % (item_index))
    
    
def tprogram_b(item_index):
    global menu_present
    menu_present = 0    # ugly hack
    
    lcd.clear()
    lcd.font(lcd.FONT_Default)
    lcd.print("Menu item %d " % (item_index), 10, 10)

def tprogram_c(item_index):
    global menu_present
    menu_present = 0    # ugly hack
    
    lcd.clear()
    lcd.font(lcd.FONT_Default)
    lcd.print("Menu item %d " % (item_index), 10, 10)


if __name__ == "__main__":
    main()
