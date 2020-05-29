import os
import pickle
import random
import sys
from random import choices
from time import sleep
from colorama import init

from Villains import (
    DeathIG, DiabetesIG, GoblinIG, HoytIG, RickIG, ScroogeIG, SkeletonIG,
    VampireIG, WalyIG, WerepIG, ZombieIG)

init()
os.system("mode con: cols=137 lines=30")
    
def capital(text):
    capitalized_message = " ".join([word.capitalize() for word in text.split(" ")])
    return capitalized_message

class Weapon:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.damage = 0
        self.weaponclass = ""
        self.condition = ""
        self.special = ""
        self.durability = 0

    def weapon_details(self, weaponID):
        with open("WEAPONS.txt", "r", encoding="utf8") as f:
            for line in f:
                _parts = line.split(",")
                if str(weaponID) == _parts[0]:
                    self.name = _parts[0]
                    self.price = _parts[1]
                    self.damage = _parts[2]
                    self.weaponclass = _parts[3]
                    self.condition = _parts[4]
                    self.special = _parts[5]
                    self.durability = _parts[6]
                    break

class Player:
    def __init__(self, name, maxhealth, base_attack, pots, magicdefense, magicattack, classn, armor, weapon, currweapon, description, gold=0 ):
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
        self.currweapon = currweapon
        self.description = description
        self.gold = gold

    @property
    def attack(self):
        attack = self.base_attack
        weapon = Weapon()
        weapon.weapon_details(str(self.currweapon).capitalize())
        if PlayerIG.currweapon == self.currweapon:
            attack += weapon.damage
        return attack

def savel():
    if os.path.exists("savefile") == True:
        answer = "Saved Game Found"
        print("\033[12;38f", answer)
        print("")
    else:
        answer = "No Saved Game Found"
        print("\033[12;34f", answer)
        print("")

def main():
    os.system("cls||clear")
    mTitle()
    sTitle()
    savel()
    option = input("->  ").lower()
    if option.lower() == "start":
        setup1()
    elif option.lower() == "load":
        if os.path.exists("savefile") == True:
            os.system("cls||clear")
            with open("savefile", "rb") as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Savegame has been loaded. Good Luck!")
            input("Press Enter to Continue")
            start1()
        else:
            print("There is no save file.")
            input("Press Enter to Continue")
            main()
    elif option.lower() == "exit":
        sys.exit()
    else:
        main()

def setup1():
    global PlayerIG
    os.system("cls||clear")
    print("Please choose something for your name..")
    option = input("Name-> ")
    PlayerIG = Player(option, "", "", "", "", "", "", "", "", "", "", "")
    setup2()
    
def classdesc():
    print("--------------------------------------------------------------------------------------------------------------------------------------")
    print("|Rogue   |Health: 70  | Attack: 7  | Potions: 1 | Armor: 0 | Weapon: Rusty Dagger    | Gold: 40 | Description: I am very, very sneaky.|")
    print("|Mage    |Health: 70  | Attack: 4  | Potions: 2 | Armor: 0 | Weapon: Stick           | Gold: 15 | Description: You're a Wizard Harry  |")
    print("|Warrior |Health: 120 | Attack: 10 | Potions: 0 | Armor: 0 | Weapon: Fists           | Gold: 10 | Description: Brutal                 |")
    print("|Ranger  |Health: 80  | Attack: 8  | Potions: 1 | Armor: 0 | Weapon: Battle-worn Bow | Gold: 10 | Description: Pew Pew Arrow..beamz?. |")
    print("|Priest  |Health: 50  | Attack: 5  | Potions: 5 | Armor: 0 | Weapon: Stick           | Gold: 5  | Description: Praise be to Yevon.    |")
    print("--------------------------------------------------------------------------------------------------------------------------------------")

def setup2():
    global PlayerIG
    print("Choose from Ranger, Mage, Warrior, Priest, Rogue")
    classdesc()    
    choice = input("Class-> ").lower()
    if choice == "warrior":
        PlayerIG = Player(PlayerIG.name,120,10,0,2,0,"Warrior",0,['Fists'],['Fists'],"Brutal.",10)
        start1()
    elif choice == "mage":
        PlayerIG = Player(PlayerIG.name,70,4,2,5,10,"Mage",0,['Stick'],['Stick'],"You're a Wizard Harry.",15) 
        start1()
    elif choice == "ranger":
        PlayerIG = Player(PlayerIG.name,80,8,1,2,0,"Ranger",0,['Battle-worn Bow'],['Battle-worn Bow'],"Not Your Average Walker Texas Ranger.",10) 
        start1()
    elif choice == "priest":
        PlayerIG = Player(PlayerIG.name,50,5,5,7,4,"Priest",0,['Stick'],['Stick'],"Praise be to Yevon.",5) 
        start1()
    elif choice == "rogue":
        PlayerIG = Player(PlayerIG.name,70,7,1,1,0,"Rogue",0,['Rusty Dagger'],['Rusty Dagger'],"A cloud of smoke and he appears. The master of suprise!",40) 
        start1()
    elif choice == "god":
        if os.path.exists("adminaccess") == True:
            PlayerIG = Player(PlayerIG.name,100,100,100,100,100,"Admin",100,['Admin'],['Admin'],"",1000) 
            start1()
        else:
            print("Nice try")
            print("Try Again")
            input("Press Enter to Continue")
            setup2()
    else:
        os.system("cls||clear")
        print("Incorrect class, try again")
        setup2()


def start1():
    os.system("cls||clear")
    print("----------------------------------------------")
    print("| Welcome %s" % PlayerIG.name)
    print("| Class: %s" % PlayerIG.classn)
    print("|\t", PlayerIG.description)
    print("| Health: %i/%i" % (PlayerIG.health, PlayerIG.maxhealth))
    print("| Current Weapon: %s" % str(PlayerIG.currweapon).replace("[", "").replace("]", "").replace("'", ""))
    print("|\t\t    (%i damage)" % PlayerIG.attack)
    print("| Potions: %i      Gold: %i" % (PlayerIG.pots, PlayerIG.gold))
    print("----------------------------------------------")
    print("  Inventory                        Fight    ")
    print("  Shop                             Save     ")
    print("                 Exit                       ")

    option = input("Option-> ").lower()
    if option.lower() == "fight":
        prefight()
    elif option.lower() == "shop":
        shop()
    elif option.lower() == "save":
        os.system("cls||clear")
        with open("savefile", "wb") as f:
            pickle.dump(PlayerIG, f)
            print("Your progress has been saved!")
        input("Press Enter to Continue")
        start1()
    elif option.lower() == "exit":
        sys.exit()
    elif option.lower() == "inventory":
        inventory()
    else:
        start1()
    
def inventory():
    def printmenu():
        os.system("cls||clear")
        print("--------------------------------------")
        print("|             Inventory              |")
        print("|        Info, Equip or Back         |")
        print("--------------------------------------")
    printmenu()
    print("| Potions: %i      Gold: %i" % (PlayerIG.pots, PlayerIG.gold))
    print("| Current Weapon: %s" % str(PlayerIG.currweapon).replace("[", "").replace("]", "").replace("'", ""))
    print("--------------------------------------")
    print("|      All Weapons in Inventory      |")
    print("--------------------------------------")
    for weapon in PlayerIG.weapon:
        print("|",weapon)
    option = input("-> ").lower()
    
    if option.lower() == "info":
        printmenu()
        print("|Enter a weapon for more information|")
        print("-------------------------------------")

        for weapon in PlayerIG.weapon:
            print(weapon)
        option = input("-> ").lower()
        if capital(option) in PlayerIG.weapon:
            weapon = Weapon()
            weapon.weapon_details(capital(option))
            variable = capital(option)
            print("\nName:              %s" % weapon.name)
            print("Price:               %s" % weapon.price)
            print("Damage:              %s" % weapon.damage)
            print("Weapon Class:        %s" % weapon.weaponclass)
            print("Condition:           %s" % weapon.condition)
            print("Special Ability:     %s" % weapon.special)
            print("Durability:          %s" % weapon.durability)
            option = input("-> ").lower()
            if option.lower() == "back":
                inventory()
            if option.lower() == "equip":
                PlayerIG.currweapon = variable
                print("Changed weapon to %s" % PlayerIG.currweapon)
                input("Press Enter")
            else:
                inventory()
        else:
            print("You do not own that item")
            input("Press Enter")
            inventory()
    elif option.lower() == "equip":
            equip()
    elif option.lower() == "back":
        start1()
    else:
        print("Unknown command, try again")
        input("Press Enter to Continue")
        start1()

def equip():
    os.system("cls||clear")
    print("-------------------------------------")
    print("|  Type the weapon name to equip it |")
    print("|    *==Type back to leave==*       |")
    print("| These are your available weapons  |")
    print("-------------------------------------")
    for weapon in PlayerIG.weapon:
        print(weapon)
    option = input("Choose Your Weapon:").lower()

    if capital(option) == PlayerIG.currweapon:
        print("You're currently already holding %s" % PlayerIG.currweapon)
        input("Press Enter to Continue")
        equip()
    elif option.lower() == "back":
        inventory()
    elif capital(option) in PlayerIG.weapon:
        PlayerIG.currweapon = option.lower()
        print("Changed weapon to %s" % PlayerIG.currweapon)
        input("Press Enter")
        equip()
    else:
        print("ERROR SHOP")


def prefight():
    population = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    weights = (
        SkeletonIG.chance,
        RickIG.chance,
        DiabetesIG.chance,
        GoblinIG.chance,
        VampireIG.chance,
        ScroogeIG.chance,
        HoytIG.chance,
        ZombieIG.chance,
        WerepIG.chance,
        WalyIG.chance,
        DeathIG.chance,
    )
    results = choices(population, weights)
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
        enemy = DeathIG
    fight()


def fight():
    os.system("cls||clear")
    print("----------------------------------------------------------")
    print("|{}             -vs-             {}".format(PlayerIG.name, enemy.name))
    print(
        "|Health: {}/{}                  Health: {}/{}".format(
            PlayerIG.health, PlayerIG.maxhealth, enemy.health, enemy.maxhealth
        )
    )
    print("|Potions {}                    {}".format(PlayerIG.pots, enemy.description))
    print("---------------------------")
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


def attack():  # fix this
    os.system("cls||clear")
    PAttack = (
        PlayerIG.attack
    )  # implement armor system. # shit, i removed the miss system...
    EAttack = enemy.attack

    if PAttack == PlayerIG.attack / 2:
        os.system("cls||clear")
        print("Silly player, missing is for kids.")
        input("Press enter to continue")
    else:
        enemy.health -= PAttack
        os.system("cls||clear")
        print("You dealt %i damage" % PAttack)
        input("Press enter to continue")
    if enemy.health <= 0:
        win()
    if EAttack == enemy.attack / 2:
        os.system("cls||clear")
        print("Phew! That was a close one.")
        input("Press Enter to Continue")
    else:
        PlayerIG.health -= EAttack
        os.system("cls||clear")
        print("%s did %i damage!" % (enemy.name, EAttack))
        input("Press enter to continue")
    if PlayerIG.health <= 0:
        dead()
    else:
        fight()


def drinkpot():
    os.system("cls||clear")
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
    os.system("cls||clear")
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You ran away like a little girl.")
        input("Press enter to continue")
        start1()
    else:
        print("Way to fail at running away.")
        input("Press Enter to Continue")
        os.system("cls||clear")
        EAttack = random.randint(enemy.attack / 2, enemy.attack)
        if EAttack == enemy.attack / 2:
            print("Phew! That was a close one.")
            input("Press Enter to Continue")
        else:
            print("%s did %i damage!" % (enemy.name, EAttack))
            input("Press Enter to Continue")
        if PlayerIG.health <= 0:
            dead()
        else:
            fight()


def win():
    os.system("cls||clear")
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.gold
    print("You won against %s." % enemy.name)
    print("You found %i gold." % enemy.gold)
    input("Press enter to continue")
    start1()


def dead():
    os.system("cls||clear")
    print("You've died.")
    input("Press enter to continue")
    boot()

def stringcheck(file,string):
    with open(file, 'r') as read:
        for line in read:
            if string in line:
                return True
    return False


def shop():
    os.system("cls||clear")
    print("-------------------------------------")
    print("|        Shhhawwwwp??!?!?           |")
    print("|  Type the weapon name to buy it   |")
    print("|        Type back to leave         |")
    print("| These are your available weapons  |")
    print("|      Yeah I know it's ugly        |")
    print("|      Aviailable Gold: ( %s )      |" % PlayerIG.gold)
    print("-------------------------------------")
    
   #I am sure there's a more elegant way to do this, but I don't know it.
    if PlayerIG.classn == "Warrior":
        with open('WEAPONS.txt','r') as fp:
            lines = fp.read().splitlines()
            for l in lines:
                if 'warrior' in l:
                    print('{name} is {gold} gold, {damage} damage'.format(name = l.split(',',maxsplit=1)[0],gold = l.split(',')[1],damage = l.split(',')[2]))
    elif PlayerIG.classn == "Mage":
        with open('WEAPONS.txt','r') as fp:
            lines = fp.read().splitlines()
            for l in lines:
                if 'mage' in l:
                    print('{name} is {gold} gold, {damage} damage'.format(name = l.split(',',maxsplit=1)[0],gold = l.split(',')[1],damage = l.split(',')[2]))
    elif PlayerIG.classn == "Ranger":
        with open('WEAPONS.txt','r') as fp:
            lines = fp.read().splitlines()
            for l in lines:
                if 'ranger' in l:
                    print('{name} is {gold} gold, {damage} damage'.format(name = l.split(',',maxsplit=1)[0],gold = l.split(',')[1],damage = l.split(',')[2]))
    elif PlayerIG.classn == "Priest":
        with open('WEAPONS.txt','r') as fp:
            lines = fp.read().splitlines()
            for l in lines:
                if 'priest' in l:
                    print('{name} is {gold} gold, {damage} damage'.format(name = l.split(',',maxsplit=1)[0],gold = l.split(',')[1],damage = l.split(',')[2]))
    elif PlayerIG.classn == "Rogue":
        with open('WEAPONS.txt','r') as fp:
            lines = fp.read().splitlines()
            for l in lines:
                if 'rogue' in l:
                    print('{name} is {gold} gold, {damage} damage'.format(name = l.split(',',maxsplit=1)[0],gold = l.split(',')[1],damage = l.split(',')[2]))
    elif PlayerIG.classn == "Admin":
        with open('WEAPONS.txt','r') as fp:
            lines = fp.read().splitlines()
            for l in lines:
                if 'admin' in l:
                    print('{name} is {gold} gold, {damage} damage'.format(name = l.split(',',maxsplit=1)[0],gold = l.split(',')[1],damage = l.split(',')[2]))
    else:  
        print("Unknown Player Class?")

    prevdamage = PlayerIG.attack
    option = input("-> ").lower()
    if option.lower() == "back":
        start1()
    elif option.lower() == "exit":
        sys.exit()
    else:
        if stringcheck('WEAPONS.txt',capital(option)):
            weapon = Weapon()
            weapon.weapon_details(capital(option))
            if PlayerIG.gold >= weapon.price:
                PlayerIG.gold -= weapon.price
                PlayerIG.weapon.append(capital(option))
                print("Acquired %s!" % option)
                print("Damage Difference roughly of: ", weapon.damage - prevdamage)
                print("You now have %i Gold!" % PlayerIG.gold)
                input("Press Enter to Continue")
                shop()
            else:
                print("You do not have enough gold.")
                print("Available Gold =", PlayerIG.gold)
                input("Press Enter to Continue")
                shop()
        else:
            print("Something went wrong.")
            input("Press Enter to Continue")
            shop()


def print_slow(text):
    print("\033[15;32f", end=" ")
    for x in text:
        print(x, end="", flush=True)
        sleep(0.20)
    print()


text = " E..n..j..o..y.... mwahahahahaha....?"


def mTitle():
    print(
        "###################################################################################################"
    )  
    print(
        "# ______  ______   ______       ______  __  __   ______       __       __  __   __       ______   #"
    ) # pylint: disable=anomalous-backslash-in-string 
    print(
        "#/\  ___\/\  __ \ /\  == \     /\__  _\/\ \_\ \ /\  ___\     /\ \     /\ \/\ \ /\ \     /\___  \  #"
    ) # pylint: disable=anomalous-backslash-in-string
    print(
        "#\ \  __\\\ \ \/\ \\\ \  __<     \/_/\ \/\ \  __ \\\ \  __\     \ \ \____\ \ \_\ \\\ \ \____\/_/  /__ #"
    ) # pylint: disable=anomalous-backslash-in-string
    print(
        "# \ \_\   \ \_____\\\ \_\ \_\      \ \_\ \ \_\ \_\\\ \_____\    \ \_____\\\ \_____\\\ \_____\ /\_____\#"
    ) # pylint: disable=anomalous-backslash-in-string
    print(
        "#  \/_/    \/_____/ \/_/ /_/       \/_/  \/_/\/_/ \/_____/     \/_____/ \/_____/ \/_____/ \/_____/#"
    ) # pylint: disable=anomalous-backslash-in-string
    print(
        "#                                                                                                 #"
    )  
    print(
        "###################################################################################################"
    )

def sTitle():
    print(
        "#                                       Welcome!                                                  #"
    )
    print(
        "#           Start                                                    Load                         #"
    )
    print(
        "#           Exit                                                     Help                         #"
    )
    print(
        "#                                                                                                 #"
    )
    print(
        "###################################################################################################"
    )


def mbTitle():
    print(
        "#                           Welcome to Pythonatron's Python Game: For The Lulz                    #"
    )
    print(
        "#                                        Semi-Basic Text RPG                                      #"
    )
    print(
        "#                                 Basic Commands: Start, Load, Exit                               #"
    )
    print(
        "#                                   --Insert witty  comments here-                                #"
    )
    print(
        "#                                                                                                 #"
    )
    print(
        "#                                      Can you find them all?                                     #"
    )
    print(
        "#                                                                                                 #"
    )
    print(
        "#                                     Press enter to continue                                     #"
    )
    print(
        "###################################################################################################"
    )


def boot():
    mTitle()
    mbTitle()
    print_slow(text)
    print("")
    print("")
    input("")
    sTitle()
    main()


def debugboot():
    init()
    setup1()


debugboot()
#boot()