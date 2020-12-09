from menu import *
from m5stack import lcd
from m5stack import btnA, btnB
import time


def main():
    # setup LCD
    lcd.clear()
    lcd.orient(lcd.LANDSCAPE_FLIP)
    
    menu = M5StickMenu()
    submenu = M5StickSub(menu)
    
    punkt1 = MenuElement("1. Haender", tryk, [1])
    punkt2 = MenuElement("2. Ben", tryk, [2])
    submenu_item = SubmenuElement("3. Arme", submenu, menu)
    
    submenu.add_element(MenuElement("3.1. Fingergang", tryk, [31]))
    submenu.add_element(MenuElement("3.2. Armloeft", tryk, [32]))
    submenu.add_element(MenuElement("Tilbage", subExit, [submenu]))
    
    punkt4 = MenuElement("4. Fingre", tryk, [4])
    
    menu.add_element(punkt1)
    menu.add_element(punkt2)
    menu.add_element(submenu_item)
    menu.add_element(punkt4)
    
    menu.start()
    
    while True:
        if btnA.wasPressed():
            menu = menu.down()
            
        if btnB.wasPressed():
            menu = menu.enter()
            
        time.sleep(0.01)
    
def tryk(index):
    lcd.clear()
    lcd.print("Du trykkede [%d] " % index, 10, 10)


def subExit(submenu):
    return submenu.exit()



if __name__ == "__main__":
    main()
