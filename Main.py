from colorama import init
import os
from time import sleep
import pickle
import sys
import random
from Weapons import *
from Villains import SkeletonIG, RickIG, DiabetesIG, GoblinIG, VampireIG, ScroogeIG, HoytIG, ZombieIG, WerepIG, WalyIG, DeathIG
from random import choices

#Introduce Armor System
#inventory add printed back command

class Player:
    def __init__(self, name, maxhealth, base_attack, pots, magicdefense, magicattack, classn, armor, weapon, currweapon, description, gold=0, xp=0):
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
        self.xp = xp

    @property 
    def attack(self): 
        attack = self.base_attack
        if str(PlayerIG.currweapon).replace('[','').replace(']','').replace("'",'') in cweapatk:
            attack += cweapatk.get(str(PlayerIG.currweapon).replace('[','').replace(']','').replace("'",''))
        return attack

def savel():
    if os.path.exists("savefile") == True:
        answer = "Saved Game Found"
        print ('\033[12;38f',answer)
        print('')
    else:
        answer = "No Saved Game Found"
        print ('\033[12;34f',answer)
        print('')

 

def main():
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
            option = input("-> ").lower()
            start1()
        else:
            print("There is no save file.")
            option = input("-> ").lower()
            main()
    elif option.lower() == "exit":
        sys.exit()
    else:
        main()


def setup1():
    global PlayerIG
    os.system('cls||clear')
    option = input("Name: ")
    PlayerIG = Player(option,'','','','','','','','','','','','',)
    setup2()
    
def setup2():
    global PlayerIG
    print("Choose from ranger, mage, warrior, priest, rogue")
    choice = input("Class: ").lower()
    if choice == "warrior":
        PlayerIG = Player(PlayerIG.name,120,10,0,2,0,"Warrior",0,['fists'],['fists'],"Brutal.",10,0)
        start1()
    elif choice == "mage":
        PlayerIG = Player(PlayerIG.name,70,4,2,5,10,"Mage",0,['old staff'],['old staff'],"You're a Wizard Harry.",15,0) 
        start1()
    elif choice == "ranger":
        PlayerIG = Player(PlayerIG.name,80,8,1,2,0,"Ranger",0,['warn bow'],['warn bow'],"Not Your Average Walker Texas Ranger.",10,0) 
        start1()
    elif choice == "priest":
        PlayerIG = Player(PlayerIG.name,50,5,5,7,4,"Priest",0,['old staff'],['old staff'],"Praise be to Yevon.",5,0) 
        start1()
    elif choice == "rogue":
        PlayerIG = Player(PlayerIG.name,70,7,1,1,0,"Rogue",0,['rusty dagger'],['rusty dagger'],"A cloud of smoke and he appears. The master of suprise!",40,0) 
        start1()
    elif choice == "god":
        PlayerIG = Player(PlayerIG.name,100,100,100,100,100,"Admin",100,['admin'],['admin'],"",1000,0) 
        start1()
    else:
        os.system('cls||clear')
        print("Incorrect class, try again")
        setup2()

def start1():
    os.system('cls||clear')
    print("Welcome %s.." % PlayerIG.name)
    print("Class: %s" % PlayerIG.classn)
    print("Attack: %i" % PlayerIG.attack)
    print("Current Weapon: %s" % PlayerIG.currweapon)
    print("Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("Potions: %i" % PlayerIG.pots)
    print("Gold: %i\n" % PlayerIG.gold)
    print("Fight")
    print("Shop")
    print("Save")
    print("Exit")
    print("Inventory")
    option = input("-> ").lower()
    if option.lower() == "fight":
        prefight()
    elif option.lower() == "shop":
        shop()
    elif option.lower() == "save":
        os.system('cls||clear')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("Your progress has been saved!")
        option = input("-> ").lower()
        start1()
    elif option.lower() == "exit":
        sys.exit()
    elif option.lower() == "inventory":
        inventory()
    else:
        start1()

def inventory():
    os.system('cls||clear')
    print("What would you like to do in here?")
    print("Equip")
    print("Back")
    
    option = input("-> ").lower()
    if option.lower() == "equip":
        equip()
    elif option.lower() == "back":
        start1()
    else:
        start1()

def equip():
    os.system('cls||clear')
    print("-------------------------------------")
    print("|  Type the weapon name to equip it |")
    print("|       Type back to leave          |")
    print("| These are your available weapons  |")
    print("-------------------------------------")
    for weapon in PlayerIG.weapon:
        print(weapon)
    option = input("-> ").lower()
    if option.lower() == PlayerIG.currweapon:
        print("You're currently already holding %s" % PlayerIG.currweapon)
        option = input("-> ").lower()
        equip()
    elif option.lower() == "back":
        inventory()
    elif option.lower() in PlayerIG.weapon:
        PlayerIG.currweapon = option.lower()
        print("Changed weapon to %s" % PlayerIG.currweapon) #display attack increase?
        option = input("-> ").lower()
        equip()
    else:
        print("Something went wrong")
        
        
        
        
        
def prefight():
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


def fight():
    os.system('cls||clear')
    print("%s             vs                %s\n" % (PlayerIG.name, enemy.name))
    print("%s's Health: %d/%d                       %s's Health: %i/%i\n" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health, enemy.maxhealth))
    print("Potions %i\n" % PlayerIG.pots)
    print("Attack")
    print("Drink potion")
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


def attack():
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
    else:
        PlayerIG.health -= EAttack
        os.system('cls||clear')
        print("%s did %i damage!" % (enemy.name, EAttack))
        input("Press enter to continue")
    if PlayerIG.health <=0:
        dead()
    else:
        fight()
    
def drinkpot(): 
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
    
def run():
    os.system('cls||clear')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You ran away like a little girl.")
        input("Press enter to continue")
        start1()
    else:
        print("Way to fail at running away.")
        option = input(" ").lower()
        os.system('cls||clear')
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack/2:
            print("Phew! That was a close one.")
        else:
            print("%s did %i damage!" % (enemy.name, EAttack))
            option = input(" ").lower()
        if PlayerIG.health <=0:
            dead()
        else:
            fight()
        

def win():
    os.system('cls||clear')
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.gold
    print("You won against %s." % enemy.name)
    print("You found %i gold." % enemy.gold)
    input("Press enter to continue")
    start1()
    
    
def dead():
    os.system('cls||clear')
    print("You've died.")
    input("Press enter to continue")

def shop():
    os.system('cls||clear')
    print("-----------------------------------")
    print("|       Shhhawwwwp??!?!?          |")
    print("|  Type the weapon name to buy it |")
    print("|       Type back to leave        |")
    print("|These are your available weapons |")
    print("|     Yeah I know it's ugly       |")
    print("| But I don't know how to fix it! |")
    print("|     Aviailable Gold: %s         |" % PlayerIG.gold )
    print("-----------------------------------")
    it = iter(weapr.items())
    for item in it:
        try:
            n = next(it)
        except StopIteration:
            print('{}: {}'.format(*item))
        else:
            print('{}: {} gold'.format(*item), '\t     {}: {} gold'.format(*n))
    
    option = input("-> ").lower() 
    if option in weapr:
        if PlayerIG.gold >= weapr[option]:
            os.system('cls||clear')
            PlayerIG.gold -= weapr[option]
            PlayerIG.weapon.append(option)
            print("Acquired %s!" % option)
            option = input(" ").lower 
            shop()
        else:
            os.system('cls||clear')
            print('You do not have enough gold.')
            option = input(" ").lower()
            shop()
    elif option.lower() == "back":
        start1()
    else:
        os.system('cls||clear')
        print("Something went wrong.")
        option = input(" ").lower()
        shop()
        


def print_slow (text):
    print ('\033[14;32f'  , end = ' ')
    for x in text:                    
        print (x, end='', flush=True) 
        sleep (0.20)
    print ()
text = ' E..n..j..o..y.... mwahahahahaha....?'


def  mTitle():
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string
    print('# ______  ______   ______       ______  __  __   ______       __       __  __   __       ______   #') # pylint: disable=anomalous-backslash-in-string
    print('#/\  ___\/\  __ \ /\  == \     /\__  _\/\ \_\ \ /\  ___\     /\ \     /\ \/\ \ /\ \     /\___  \  #') # pylint: disable=anomalous-backslash-in-string
    print('#\ \  __\\\ \ \/\ \\\ \  __<     \/_/\ \/\ \  __ \\\ \  __\     \ \ \____\ \ \_\ \\\ \ \____\/_/  /__ #') # pylint: disable=anomalous-backslash-in-string
    print('# \ \_\   \ \_____\\\ \_\ \_\      \ \_\ \ \_\ \_\\\ \_____\    \ \_____\\\ \_____\\\ \_____\ /\_____\#') # pylint: disable=anomalous-backslash-in-string
    print('#  \/_/    \/_____/ \/_/ /_/       \/_/  \/_/\/_/ \/_____/     \/_____/ \/_____/ \/_____/ \/_____/#') # pylint: disable=anomalous-backslash-in-string
    print('#                                                                                                 #') # pylint: disable=anomalous-backslash-in-string
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string

def sTitle():
    print('#                                       Welcome!                                                  #') # pylint: disable=anomalous-backslash-in-string
    print('#           Start                                                    Load                         #') # pylint: disable=anomalous-backslash-in-string
    print('#           Exit                                                     Help                         #') # pylint: disable=anomalous-backslash-in-string
    print('#                                                                                                 #') # pylint: disable=anomalous-backslash-in-string
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string

def mbTitle():
    print("#                           Welcome to Pythonatron's Python Game: For The Lulz                    #") # pylint: disable=anomalous-backslash-in-string
    print('#                                        Semi-Basic Text RPG                                      #') # pylint: disable=anomalous-backslash-in-string
    print('#                                 Basic Commands: Start, Load, Exit                               #') # pylint: disable=anomalous-backslash-in-string
    print('#                               Maybe some hidden commands.. Who knows?                           #') # pylint: disable=anomalous-backslash-in-string
    print('#                                  No Peeking at the Code Either!                                 #') # pylint: disable=anomalous-backslash-in-string
    print('#                                                                                                 #') # pylint: disable=anomalous-backslash-in-string
    print('#                                    Press enter to continue                                      #')
    print('###################################################################################################') # pylint: disable=anomalous-backslash-in-string

def boot():
    init()
    os.system('mode con: cols=101 lines=30')
    mTitle()
    mbTitle()
    #print_slow (text)
    print("")
    print("")
    input('')
    sTitle()
    main()