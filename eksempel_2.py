from menu import *
from m5stack import lcd
from m5stack import btnA, btnB
import time

    #M5 tager dig et skridt ned ??
    #under 3 menupunkter ??
    #kald dem noget andet ...

def main():
    # setup LCD
    lcd.clear()
    lcd.orient(lcd.LANDSCAPE_FLIP)
    
    menu = M5StickMenu()
    submenu = M5StickSub(menu)
    
    punkt1 = FunctionItem("1. Haender", tryk, [1])
    punkt2 = FunctionItem("2. Ben", tryk, [2])
    submenu_item = SubmenuItem("3. Arme", submenu, menu)
    
    submenu.add_item(FunctionItem("3.1. Fingergang", tryk, [31]))
    submenu.add_item(FunctionItem("3.2. Armloeft", tryk, [32]))
    submenu.add_item(FunctionItem("Tilbage", subExit, [submenu]))
    
    punkt4 = FunctionItem("4. Fingre", tryk, [4])
    
    menu.add_item(punkt1)
    menu.add_item(punkt2)
    menu.add_item(submenu_item)
    menu.add_item(punkt4)
    
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
