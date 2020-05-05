import os
import pickle
import random
import sys
from random import choices
from time import sleep
from colorama import init

from Villains import (
    DeathIG, DiabetesIG, GoblinIG, HoytIG, RickIG, ScroogeIG, SkeletonIG,
    VampireIG, WalyIG, WerepIG, ZombieIG
)

#if they can enter number of or description of all references they get special prize?
#Enemies are way underpowered........
#warrior can oneshot most....

class Weapon: #looks good
    def __init__(self):
        self.Name = ""
        self.lowprice = 0
        self.highprice = 0
        self.lowdamage = 0
        self.highdamage = 0
        self.weaponclass = ""
        self.condition = ""
        self.special = ""
        self.durability = 0
        
    def weapon_details(self,weaponID): #looks good
        with open('WEAPONS.txt', 'r', encoding="utf8") as f:
            for line in f:
                parts = line.split(",")
                if str(weaponID) == parts[0]:
                    self.name = parts [0]
                    self.lowprice = parts [1]
                    self.highprice = parts [2]
                    self.lowdamage = parts [3]
                    self.highdamage = parts [4]
                    self.weaponclass = parts [5]
                    self.condition = parts [6]
                    self.special = parts [7]
                    self.durability = parts [8]
                    break
     
    def weapon_info(self): #looks good.. Will i ever really use this?
        print("\nName:            ", self.name)
        print("Low Price:         ",self.lowprice)
        print("High Price:        ",self.highprice)
        print("\nLow Damage:        ",self.lowdamage)
        print("High Damage:       ",self.highdamage)
        print("Weapon Class:      ",self.weaponclass)
        print("Condition:         ",self.condition)
        print("Special Ability:   ",self.special)
        print("Durability:        ",self.durability)  
        
class Player: #looks good.. #when did i add all this extra stuff!?
    def __init__(self, name, maxhealth, base_attack, pots, magicdefense, magicattack, classn, armor, weapon, currweapon, description, gold=0):
        self.name = name
        self.maxhealth = maxhealth
        self.health = self.maxhealth
        self.base_attack = base_attack
        self.pots = pots
        self.magicdefense = magicdefense
        self.magicattack = magicattack
        self.classn = classn
        self.armor = armor
        self.weapon = weapon
        self.currweapon =  currweapon
        self.description = description
        self.gold = gold
        

    @property   
    def attack(self): #looks good
        attack = self.base_attack
        weapon = Weapon()
        weapon.weapon_details(str(self.currweapon).capitalize())
        if PlayerIG.currweapon == self.currweapon:
            highdamage = int(weapon.highdamage)
            lowdamage = int(weapon.lowdamage)
            idgaf = random.randint(lowdamage, highdamage)
            attack += idgaf
        return attack

def savel(): #looks good
    if os.path.exists("savefile") == True:
        answer = "Saved Game Found"
        print ('\033[12;38f',answer)
        print('')
    else:
        answer = "No Saved Game Found"
        print ('\033[12;34f',answer)
        print('')

 

def main(): #looks good
    os.system('cls||clear')
    mTitle()
    sTitle()    
    savel()    
    option = input("->  ").lower()
    if option.lower() == "start":
        setup1()
    elif option.lower() == "load":
        if os.path.exists("savefile") == True:
            os.system('cls||clear')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Savegame has been loaded. Good Luck!")
            input('Press Enter to Continue')
            start1()
        else:
            print("There is no save file.")
            input('Press Enter to Continue')
            main()
    elif option.lower() == "exit":
        sys.exit()
    else:
        main()


def setup1(): #Should i make pretty borders for these functions as well?
    global PlayerIG
    os.system('cls||clear')
    print("Please choose something for your name..")
    option = input("Name-> ")
    PlayerIG = Player(option,'','','','','','','','','','','')
    setup2()
    
def setup2(): #looks good #Do I need multiple globals of the same thing?
    global PlayerIG
    print("Choose from Ranger, Mage, Warrior, Priest, Rogue")
    choice = input("Class-> ").lower()
    if choice == "warrior":
        PlayerIG = Player(PlayerIG.name,120,10,0,2,0,"Warrior",0,['Fists'],['Fists'],"Brutal.",10)
        start1()
    elif choice == "mage":
        PlayerIG = Player(PlayerIG.name,70,4,2,5,10,"Mage",0,['Old Staff'],['Old Staff'],"You're a Wizard Harry.",15) 
        start1()
    elif choice == "ranger":
        PlayerIG = Player(PlayerIG.name,80,8,1,2,0,"Ranger",0,['Warn Bow'],['Warn Bow'],"Not Your Average Walker Texas Ranger.",10) 
        start1()
    elif choice == "priest":
        PlayerIG = Player(PlayerIG.name,50,5,5,7,4,"Priest",0,['Old Staff'],['Old Staff'],"Praise be to Yevon.",5) 
        start1()
    elif choice == "rogue":
        PlayerIG = Player(PlayerIG.name,70,7,1,1,0,"Rogue",0,['Rusty Dagger'],['Rusty Dagger'],"A cloud of smoke and he appears. The master of suprise!",40) 
        start1()
    elif choice == "god":
        PlayerIG = Player(PlayerIG.name,100,100,100,100,100,"Admin",100,['Admin'],['Admin'],"",1000) 
        start1()
    else:
        os.system('cls||clear')
        print("Incorrect class, try again")
        setup2()

def start1(): #Finished for now!
    os.system('cls||clear')
    print("----------------------------------------------")
    print("| Welcome %s" % PlayerIG.name)
    print("| Class: %s" % PlayerIG.classn)
    print("|\t", PlayerIG.description)
    print("| Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("| Current Weapon: %s" % str(PlayerIG.currweapon).replace("[","").replace("]","").replace("'",""))
    print("|\t\t    (%i damage)" % PlayerIG.attack)
    print("| Potions: %i      Gold: %i" % (PlayerIG.pots, PlayerIG.gold))
    print('----------------------------------------------')
    print("  Inventory                        Fight    ")
    print("  Shop                             Save     ")
    print("                 Exit                       ")
    
    option = input("Option-> ").lower()
    if option.lower() == "fight":
        prefight()
    elif option.lower() == "shop":
        shop()
    elif option.lower() == "save":
        os.system('cls||clear')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("Your progress has been saved!")
        input('Press Enter to Continue')
        start1()
    elif option.lower() == "exit":
        sys.exit()
    elif option.lower() == "inventory":
        inventory()
    else:
        start1()

def inventory(): #looks good
    os.system('cls||clear')
    print("-------------------------------------")
    print("|     Unneeded Inventory Screen     |")
    print("|          Equip or Back            |")
    print("|         (Yeop, That's it)         |")
    print("-------------------------------------")
    
    option = input("-> ").lower()
    if option.lower() == "equip":
        equip()
    elif option.lower() == "back":
        start1()
    else:
        start1()

def equip(): #looks good?
    os.system('cls||clear')
    print("-------------------------------------")
    print("|  Type the weapon name to equip it |")
    print("|       Type back to leave          |")
    print("| These are your available weapons  |")
    print("-------------------------------------")
    for weapon in PlayerIG.weapon:
        print(weapon)
    option = input('Choose Your Weapon:').lower()
    if option.lower() == PlayerIG.currweapon:
        print("You're currently already holding %s" % PlayerIG.currweapon)
        input('Press Enter to Continue')
        equip()
    elif option.lower() == "back":
        inventory()
    elif option.lower() in PlayerIG.weapon:
        PlayerIG.currweapon = option.lower()
        print("Changed weapon to %s" % PlayerIG.currweapon) #display attack increase?
        input("Press Enter").lower()
        equip()
    else:
        print('ERROR SHOP')
        
        
        
        
        
def prefight(): #looks good, probably finished till something ELSE gets implemented
    population = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    weights = SkeletonIG.chance, RickIG.chance, DiabetesIG.chance, GoblinIG.chance, VampireIG.chance, ScroogeIG.chance, HoytIG.chance, ZombieIG.chance, WerepIG.chance, WalyIG.chance, DeathIG.chance, 
    results = choices(population,  weights)
    global enemy
    if results[0] == 1:
        enemy = SkeletonIG
    elif results[0] == 2:
        enemy = RickIG
    elif results[0] == 3:
        enemy = DiabetesIG
    elif results[0] == 4:
        enemy = GoblinIG
    elif results[0] == 5:
        enemy = VampireIG
    elif results[0] == 6:
        enemy = ScroogeIG
    elif results[0] == 7:
        enemy = HoytIG
    elif results[0] == 8:
        enemy = ZombieIG
    elif results[0] == 9:
        enemy = WerepIG
    elif results[0] == 10:
        enemy = WalyIG
    elif results[0] == 11:
        enemy = DeathIG
    else:
        enemy = SkeletonIG 
    fight()


def fight(): #This could probably be prettier
    os.system('cls||clear')
    print("----------------------------------------------------------")
    print("|{}             -vs-             {}".format(PlayerIG.name, enemy.name))
    print("|Health: {}/{}                  Health: {}/{}".format(PlayerIG.health, PlayerIG.maxhealth, enemy.health, enemy.maxhealth))
    print("|Potions {}                    {}".format(PlayerIG.pots, enemy.description))
    print('---------------------------')
    print("Drink potion")
    print("Attack")
    print("Run")
    option = input("-> ").lower()
    if option.lower() == "attack":
        attack()
    elif option.lower() == "drink potion":
        drinkpot()
    elif option.lower() == "run":
        run()
    else:
        fight()


def attack(): #fix this
    os.system('cls||clear')
    PAttack = PlayerIG.attack #implement armor system. # shit, i removed the miss system...
    EAttack = enemy.attack   #why isn't death listed?
    
    if PAttack == PlayerIG.attack / 2:
        os.system('cls||clear')
        print("Silly player, missing is for kids.")
        input("Press enter to continue")
    else:
        enemy.health -= PAttack
        os.system('cls||clear')
        print("You dealt %i damage" % PAttack)
        input("Press enter to continue") 
    if enemy.health <= 0:
        win()
    if EAttack == enemy.attack / 2:
        os.system('cls||clear')
        print("Phew! That was a close one.")
        input('Press Enter to Continue')
    else:
        PlayerIG.health -= EAttack
        os.system('cls||clear')
        print("%s did %i damage!" % (enemy.name, EAttack))
        input("Press enter to continue")
    if PlayerIG.health <=0:
        dead()
    else:
        fight()
    
def drinkpot(): #looks good
    os.system('cls||clear')
    if PlayerIG.pots == 0:
        print("You currently have no potions.")
    else:
        PlayerIG.health += 50
        PlayerIG.pots -= 1
        if PlayerIG.health > PlayerIG.maxhealth:
            PlayerIG.health = PlayerIG.maxhealth 
        print("You drink the special 'potion'.")
        
    input("Press enter to continue")
    fight()
    
def run(): #looks good
    os.system('cls||clear')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You ran away like a little girl.")
        input("Press enter to continue")
        start1()
    else:
        print("Way to fail at running away.")
        input('Press Enter to Continue')
        os.system('cls||clear')
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack/2:
            print("Phew! That was a close one.")
            input('Press Enter to Continue')
        else:
            print("%s did %i damage!" % (enemy.name, EAttack))
            input('Press Enter to Continue')
        if PlayerIG.health <=0:
            dead()
        else:
            fight()
        

def win(): #looks good
    os.system('cls||clear')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.gold
    print("You won against %s." % enemy.name)
    print("You found %i gold." % enemy.gold)
    input("Press enter to continue")
    start1()
    
    
def dead(): #looks good
    os.system('cls||clear')
    print("You've died.")
    input("Press enter to continue")
    boot()

def shop(): #needs fixed
    os.system('cls||clear')
    print("-----------------------------------")
    print("|       Shhhawwwwp??!?!?          |")
    print("|  Type the weapon name to buy it |")
    print("|       Type back to leave        |")
    print("|These are your available weapons |")
    print("|     Yeah I know it's ugly       |")
    print("|     Aviailable Gold: %s         |" % PlayerIG.gold )
    print("-----------------------------------")
    #
    #
    #  List[Weapon - Price (mind - maxd)]
    #
    #
    
    option = input("Choose a Weapon:")
    prevdamage = PlayerIG.attack
    capitalized_message = " ".join([
        word.capitalize()
        for word in option.split(" ")
    ])
    with open('WEAPONS.txt', 'r', encoding="utf8") as f:
                for line in f:
                    parts = line.split(",")
                    print("CM",capitalized_message)
                    print("p0", parts[0])
                    if 1 == 1:
                        weapon = Weapon()
                        weapon.weapon_details(capitalized_message)
                        highprice = int(weapon.highprice)
                        lowprice = int(weapon.lowprice)
                        idgaf = random.randint(lowprice, highprice)
                        if PlayerIG.gold >= idgaf:
                            PlayerIG.gold -= idgaf
                            PlayerIG.weapon.append(capitalized_message)
                            ld = int(weapon.lowdamage)
                            hd = int(weapon.highdamage)
                            idgaf2 = random.randint(ld,hd)
                            print('Acquired %s!' % option) #Show damage increase?
                            print("Damage Difference roughly of: ",idgaf2 - prevdamage)
                            input('Press Enter to Continue')
                            shop()
                        else:
                            print('You do not have enough gold.')
                            print('Available Gold =',PlayerIG.gold)
                            input('Press Enter to Continue')
                            shop()
                    elif option.lower() == "back":
                        start1()
                    else:
                        print("Something went wrong.")
                        input('Press Enter to Continue')
                        shop()
        
        


def print_slow (text): #looks good
    print ('\033[14;32f'  , end = ' ')
    for x in text:                    
        print (x, end='', flush=True) 
        sleep (0.20)
    print ()
text = ' E..n..j..o..y.... mwahahahahaha....?'


def  mTitle(): #looks good
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string
    print('# ______  ______   ______       ______  __  __   ______       __       __  __   __       ______   #') # pylint: disable=anomalous-backslash-in-string
    print('#/\  ___\/\  __ \ /\  == \     /\__  _\/\ \_\ \ /\  ___\     /\ \     /\ \/\ \ /\ \     /\___  \  #') # pylint: disable=anomalous-backslash-in-string
    print('#\ \  __\\\ \ \/\ \\\ \  __<     \/_/\ \/\ \  __ \\\ \  __\     \ \ \____\ \ \_\ \\\ \ \____\/_/  /__ #') # pylint: disable=anomalous-backslash-in-string
    print('# \ \_\   \ \_____\\\ \_\ \_\      \ \_\ \ \_\ \_\\\ \_____\    \ \_____\\\ \_____\\\ \_____\ /\_____\#') # pylint: disable=anomalous-backslash-in-string
    print('#  \/_/    \/_____/ \/_/ /_/       \/_/  \/_/\/_/ \/_____/     \/_____/ \/_____/ \/_____/ \/_____/#') # pylint: disable=anomalous-backslash-in-string
    print('#                                                                                                 #') # pylint: disable=anomalous-backslash-in-string
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string

def sTitle(): #looks good
    print('#                                       Welcome!                                                  #') # pylint: disable=anomalous-backslash-in-string
    print('#           Start                                                    Load                         #') # pylint: disable=anomalous-backslash-in-string
    print('#           Exit                                                     Help                         #') # pylint: disable=anomalous-backslash-in-string
    print('#                                                                                                 #') # pylint: disable=anomalous-backslash-in-string
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string

def mbTitle(): #looks good
    print("#                           Welcome to Pythonatron's Python Game: For The Lulz                    #") # pylint: disable=anomalous-backslash-in-string
    print('#                                        Semi-Basic Text RPG                                      #') # pylint: disable=anomalous-backslash-in-string
    print('#                                 Basic Commands: Start, Load, Exit                               #') # pylint: disable=anomalous-backslash-in-string
    print('#                               Maybe some hidden commands.. Who knows?                           #') # pylint: disable=anomalous-backslash-in-string
    print("#                               There's a total of 9 references in here                           #") # pylint: disable=anomalous-backslash-in-string
    print('#                                      Can you find them all?                                     #') # pylint: disable=anomalous-backslash-in-string
    print('#                                     Press enter to continue                                     #')
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string

def boot(): #Do i really need a start screen for the start screen?
    init()
    os.system('mode con: cols=101 lines=30')
    mTitle()
    mbTitle()
    #print_slow (text) #disable for testing... its.. so... slow..
    print("")
    print("")
    input('')
    sTitle()
    main()
def debugboot():
    init()
    setup1()
    
boot()
