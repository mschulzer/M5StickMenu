from menu import *
from m5stack import lcd
from m5stack import btnA, btnB
import time


def main():
    
    # Initialiser menuen
    test_menu = M5StickMenu()
    
    # Definer punkter til menuen
    punkt1 = MenuElement("1. Haender", tryk, [1])
    punkt2 = MenuElement("2. Ben", tryk, [2])
    punkt3 = MenuElement("3. Fingre", tryk, [3])
    
    # Foej punkterne til menuen
    test_menu.add_element(punkt1)
    test_menu.add_element(punkt2)
    test_menu.add_element(punkt3)
    
    test_menu.start()
    
    
    while True:

        if btnA.wasPressed():
            test_menu = test_menu.down()

        if btnB.wasPressed():
            test_menu = test_menu.enter()
            
        time.sleep(0.01)

   
   

# Brugerdefinerede funktioner
def tryk(index):
    print('Du trykkede %d' % index)




if __name__ == "__main__":
    main()
    
    
