import os
import base64
import sys 

def capital(text):
    capitalized_message = " ".join([word.capitalize() for word in text.split(" ")])
    return capitalized_message

def create():
    print("Input password?")
    passwd = input("Password?")
    #add password for my amusement?
    #add class
    #add enemy
    if os.path.exists("adminaccess") == True:
        with open("adminaccess") as a:
            lines = a.readlines()
            if lines[2] == base64.b64encode(passwd).encode("utf-8"):
                print("Access granted? This probably isn't very secure...")
            else:
                print("Access denied:")
                print("Cleaning up")
                os.remove("Create.py")
                os.remove("adminaccess")
                sys.exit()
        
  
# print(base64.b64encode("password".encode("utf-8")))
# cGFzc3dvcmQ=
# print(base64.b64decode("cGFzc3dvcmQ=").decode("utf-8"))
# password


    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("|        Welcome Creator          |")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("|Add Weapon, Add Class, Add Enemy |")
    print("*Add Weapon only currently working*")
    print("|      Choose your destiny.       |")
    print("*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*_*")
    print("for now i'd suggest getting it right")
    print("the first time otherwise you will get")
    print("a 'none' value if you mess up.. yay?")
    choice = input("->").lower()
    if choice == "add weapon":
        addweapon = []
        
        #Name
        print("Name of Weapon: ")
        name = input("->")
        addweapon.append(capital(name))
        
        #Price
        addweapon.append(weaponprice())
        
        #Damage
        addweapon.append(weapondmg())
        
        #Class
        print("Which class can wield weapon?")
        print("any, ranger, mage, rogue, warrior, priest")
        #print(auto list classes incase of added ones)
        #class = input("->")
        #addweapon.append(class)
        #any user for testing
        addweapon.append("any")
        
        #Condition
        addweapon.append(weaponcnd())
        
        #Special
        print("special")
        print("N/A")
        addweapon.append("none")
                
        #Durability
        addweapon.append(weapondur())
        
        with open("testweap.txt","a",encoding="utf-8") as f:
            f.write('\n' + str(addweapon).replace("'",'').strip().replace(" ",'').strip("'").strip("[]"))
            f.close
        print("Weapon added")
    if choice == "add class":
        pass
    if choice == "add enemy":
        pass
    else:
        print("2L2Q")      
        print("https://www.youtube.com/watch?v=wiyYozeOoKs")

def weapondmg():
    print("Weapon Base Damage: ")
    print("0-20")
    dmg = input("->")
    if int(dmg) >= 21 or int(dmg) <= 0:
        print("Invalid Number. Try again.")
        weapondmg()
    else:
        return dmg
    
def weaponcnd():
    conditions = ["poor", "good", "great", "super", "awesome", "epic"]
    print("Starting condition of weapon")
    print("poor, good, great, super, awesome, and epic")
    cnd = input("->").lower()
    if cnd in conditions:
        return cnd
    else:
        print("Invailed condition. try again")
        weaponcnd()

def weapondur():
    print("durability")
    print("1-250")
    dur = input("->")
    if int(dur) >= 251 or int(dur) <= 0:
        print("Invailed number try again")
        weapondur()
    else:
        return dur
        
def weaponprice():
    print("price of weapon")
    print("0-1000")
    price = input("->")
    if int(price) >= 1001 or int(price) <= 0:
        print("invailed number try again")
        weaponprice()
    else:
        return price
    