import random

#What's the point of xp?

#xp based of of attack and armor? # armor + health + attack / 4 * 2 = xp? idk
#total defense (which isn't implemented) should be possibly a defense variable +/* armor +/* health
#should xp incrase the player, weapon or armor or all three?
#im sure there's a better way to do this as well.. maybe Class Monster ->Skeleton, etc?

class skeleton:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(5, 10)
        self.health = self.maxhealth
        self.attack = random.randint(1, 6)
        self.gold = random.randint(1, 15)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 5)
        self.chance = random.randint(10, 20)
        self.description = "You could say he has a -bone- to pick with you."
SkeletonIG = skeleton("Skeleton")

class rick:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(999999, 999999999)
        self.health = self.maxhealth
        self.attack = random.randint(999999, 999999999)
        self.gold = random.randint(0, 1)
        self.xp = random.randint(1000000, 10000000)
        self.armor = random.randint(999999, 999999999)
        self.chance = 0.000001
        self.description = "Good Luck."
RickIG  = rick("Rick")

class diabetes:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(5, 15)
        self.health = self.maxhealth
        self.attack = random.randint(10, 20)
        self.gold = random.randint(1, 10)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 5)
        self.chance = random.randint(10, 30)
        self.description = "DIABEETUSSS!"
DiabetesIG = diabetes("Diabeetus")
        
class goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(5, 30)
        self.health = self.maxhealth
        self.attack = random.randint(5, 15)
        self.gold = random.randint(1, 15)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 5)
        self.chance = random.randint(10, 80)
        self.description = "Don't let them near your women."
GoblinIG = goblin("Goblin")  

class vampire:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(10, 20)
        self.health = self.maxhealth
        self.attack = random.randint(10, 20)
        self.gold = random.randint(1, 10)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 10)
        self.chance = random.randint(6, 66)
        self.description = "Sookie...."
VampireIG = vampire("Vampire")

class scrooge:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(30, 60)
        self.health = self.maxhealth
        self.attack = random.randint(50, 60)
        self.gold = random.randint(100, 150)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(2, 10)
        self.chance = random.randint(2, 20)
        self.description = "He's rich!"
ScroogeIG = scrooge("Scrooge") 
      
class hoyt:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(5, 15)
        self.health = self.maxhealth
        self.attack = random.randint(1, 100)
        self.gold = random.randint(10, 100)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 2)
        self.chance = random.randint(10, 20)
        self.description = "You leave my Hoyt alone, you devil whore!"
HoytIG = hoyt("Maxine Fortenberry")

class zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(2, 10)
        self.health = self.maxhealth
        self.attack = random.randint(1, 10)
        self.gold = random.randint(1, 13)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 3)
        self.chance = random.randint(10, 90)
        self.description = "Braaainnzzzz?!"
ZombieIG = zombie("Zombie")  
     
class werep:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(5, 20)
        self.health = self.maxhealth
        self.attack = random.randint(5, 20)
        self.gold = random.randint(1, 10)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 3)
        self.chance = random.randint(10, 30)
        self.description = "They're so pretty."
WerepIG = werep("Werepanther")

class waly:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(5, 20)
        self.health = self.maxhealth
        self.attack = random.randint(5, 20)
        self.gold = random.randint(1, 10)
        self.xp = random.randint(50, 200)
        self.armor = random.randint(0, 3)
        self.chance = random.randint(10, 30)
        self.description = "mmmmm. cheekahn good."
WalyIG = waly("Floating Disembodied Head of Colonel Sanders")        

class death:
    def __init__(self, name):
        self.name = name
        self.maxhealth = random.randint(400, 1000)
        self.health = self.maxhealth
        self.attack = random.randint(50, 100)
        self.gold = random.randint(1000, 1987)
        self.xp = random.randint(250, 500)
        self.armor = random.randint(3, 10)
        self.chance = 0.1
        self.description = "Big Bad Bossman"
DeathIG = death("Death")