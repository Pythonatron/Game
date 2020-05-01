import random
#Tiered System?
WEAPONS = {
        "class":"warrior","weapon":"fists","price":0,"lowdamage":1,"highdamage":3,
        "class":"warrior","weapon":"mace","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"lance","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"spear","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"halberd","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"cutlass","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"longsword","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"war hammer","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"greatsword","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"battle axe","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"morning star","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"warrior","weapon":"brass knuckles","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"mpusr","weapon":'old staff',"price":0,"lowdamage":1,"highdamage":3,
        "class":"rogue","weapon":"small dagger","price":0,"lowdamage":1,"highdamage":3,
        "class":"rogue","weapon":"dagger","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"ranger","weapon":"worn bow","price":0,"lowdamage":1,"highdamage":3,
        "class":"ranger","weapon":"bow","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"ranger","weapon":"crossbow","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"ranger","weapon":"long bow","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"ranger","weapon":"short bow","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"any","weapon":"slice of pizza","price":2.95,"lowdamage":1,"highdamage":9, #divide by 100!
        "class":"any","weapon":"red sai","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"any","weapon":"blue sword","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"any","weapon":"pepper spray","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"any","weapon":"purple bo staff","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"any","weapon":"orange nunchucks","price":random.randint(10,80),"lowdamage":1,"highdamage":8,
        "class":"any","weapon":"zeus lightning": ,"price":random.randint(5000,10000),"lowdamage":5000,"highdamage":10000,
        "class":"admin","weapon":"admin": ,"price":random.randint(5000000000,10000000000),"lowdamage":50000000000000,"highdamage":100000000000000,        
}       