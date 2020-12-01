from m5stickmenu import *


def main():
    
    # Initialiser menuen
    mymenu = M5StickMenu()
    
    # Definer punkter til menuen
    punkt1 = FunctionItem("1. Haender", tryk, [1])
    punkt2 = FunctionItem("2. Ben", tryk, [2])
    punkt3 = FunctionItem("3. Fingre", tryk, [3])
    
    # Foej punkterne til menuen
    mymenu.add_item(punkt1)
    mymenu.add_item(punkt2)
    mymenu.add_item(punkt3)
    
    mymenu.start()
    
    
    while True:

        if btnA.wasPressed():
            mymenu = mymenu.down()

        if btnB.wasPressed():
            mymenu = mymenu.enter()
            
        time.sleep(0.01)

   
   

# Brugerdefinerede funktioner
def tryk(index):
    print('Du trykkede %d' % index)




if __name__ == "__main__":
    main()
    
    
