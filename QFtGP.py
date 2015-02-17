import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

# Make variables 
pstrength = 0
pdefense = 0
phealth = 0
pmaxhp = 0
pintelligence = 0
pname = "null"
mstrength = 0
mdefense = 0
mhealth = 0
mname = "null"
mdamge = 0
pdamage = 0
bcounter = 0

messagebox.showinfo("welcome", "Welcome to 'Quest For The Golden Python'")

pname = simpledialog.askstring("Name?", "What is the name of your brave warrior?")

statsq = simpledialog.askstring("Roll?", "Are you ready to roll for your stats?(yes/no)")
while statsq != "yes":
    statsq = simpledialog.askstring("Roll?", "Are you ready to roll for your stats now?(yes/no)")

pstrength = random.randint(3, 8)
pdefense = random.randint(1, 6)
pmaxhp = random.randint(35, 65)
phealth = pmaxhp

messagebox.showinfo("Stats", "You rolled a {} for strength.".format (pstrength)+\
                    "You rolled a {} for defense.".format (pdefense)+\
                    "You rolled a {} for health.".format (phealth))

mstrength = pdefense+3
mdefense = pstrength-5
if mstrength < 1:
    mstrength = 1
mhealth = 25
mname = "Little Green Slime"

messagebox.showinfo("Dun Dun Duhhh", "A {} appears!".format (mname))

messagebox.showinfo("Battle", "Now that you have stats lets go through your first battle.")
while mhealth > 0:
    messagebox.showinfo("Battle", "The {} has {} health.".format (mname, mhealth)+
                          "You have {} health.".format (phealth))
    while 1 == 1:
        bchoice = simpledialog.askstring("Battle", "What would you like to do?(fight/heal/run)")
        if bchoice == "run":
            messagebox.showinfo("Battle", "You can't run from this tutorial.")
        elif bchoice == "heal":
            messagebox.showinfo("Battle", "You have 0 potions and 0 intelligence.")
        elif bchoice == "fight":
            break
        else:
            continue
    mdamage = (pstrength - mdefense)
    pdamage = (mstrength - pdefense)
    mhealth -= (mdamage)
    phealth -= (pdamage)
    messagebox.showinfo("Battle", "You dealt {} damage.".format (mdamage)+
                        "You took {} damage.".format (pdamage))
    if mhealth <= 0:
        messagebox.showinfo("Battle", "You have vanquished the {}.".format (mname))
    if phealth <= 0:
        messagebox.showinfo("Battle", "You were killed by the {}.".format (mname))
        break
messagebox.showinfo("Battle", "The battle is over.")

messagebox.showinfo("Yay", "You fought well. Let's go to the local village.")

messagebox.showinfo("Village", "As you enter the village a man wearing brown bag thing " +
                    "for a shirt and a very obnoxious yellow hat approuches you.")

messagebox.showinfo("Village", "He tells you he's the mayor and some villagers have been " +
                    "attacked in the local dark forest of doom and he wants your help.")

while 1==1:
    messagebox.showinfo("Heal", "Your wounds are healed by the magic of this village.")
    phealth = pmaxhp
    
    tchoice = simpledialog.askstring("Action", "What would you like to do? (shop/goto/talk/stats)")
    if tchoice == "shop":
        messagebox.showinfo("Shop", "You walk up to the building with 'SHOP' written on it in red paint." +
                            "You reach for the door, but you realize that is just painted on too.")
    elif tchoice == "stats":
        messagebox.showinfo("Stats", "Your strength is {}. Your defense is {}. ".format (pstrength, pdefense) +
                            "Your health is {}. Your intelligence is {}.".format (phealth, pintelligence))
    elif tchoice == "talk":
        messagebox.showinfo("Talk", "You ask the mayor what he said because you weren't listening last time." +
                            "The mayor sighs and tells you that some villagers have been attacked " +
                            "in the local dark forest of doom and he wants your help.")
    elif tchoice == "goto":
        messagebox.showinfo("GoTo", "You head into the dark forest looking for trouble. It is not long until " +
                            "you find something to fight...")
        
        mname = "Rabid Wolf"
        mstrength = random.randint (1, 5)
        mdefense = random.randint (1, 3)
        mhealth = random.randint (15, 30)
        if bcounter > 3:
            mname = "golden Wolf"
            mstrength = random.randint (2, 6)
            mdefense = random.randint (2, 4)
            mhealth = random.randint (30, 45)
            bcounter = 0

        while mhealth > 0:
            messagebox.showinfo("Battle", "The {} has {} health.".format (mname, mhealth)+
                          "You have {} health.".format (phealth))
            while 1 == 1:
                bchoice = simpledialog.askstring("Battle", "What would you like to do?(fight/heal/run)")
                if bchoice == "run":
                    messagebox.showinfo("Battle", "You escape from the battle.")
                    break
                elif bchoice == "heal":
                    messagebox.showinfo("Battle", "You have 0 potions.")
                    if pintelligence > 0:
                        messagebox.showinfo("Battle", "You use your intelligence to make basic " +
                                            "medicine out of the stuff lying around. You gain 5 health.")
                        if phealth + 5 <= pmaxhp:
                            phealth += 5
                        else:
                            phealth = pmaxhp
                elif bchoice == "fight":
                    break
                else:
                    continue
            if bchoice == "run":
                break
            mdamage = (pstrength - mdefense)
            pdamage = (mstrength - pdefense)
            mhealth -= (mdamage)
            phealth -= (pdamage)
            messagebox.showinfo("Battle", "You dealt {} damage.".format (mdamage)+
                                "You took {} damage.".format (pdamage))
            if mhealth <= 0:
                messagebox.showinfo("Battle", "You have vanquished the {}.".format (mname))
                bcounter += 1
                while 1==1:
                    schoice = simpledialog.askstring("Upgrade", "You gained a stat point! What stat would " +
                                                     "you like to upgrade? (strength/defense/health/intelligence)")
                    if schoice == "strength":
                        pstrength += 1
                        break
                    elif schoice == "defense":
                        pdefense += 1
                        break
                    elif schoice == "health":
                        pmaxhp += 5
                        phealth = pmaxhp
                        break
                    elif schoice == "intelligence":
                        pintelligence += 1
                        break
                    else:
                        continue
            if phealth <= 0:
                messagebox.showinfo("Battle", "You were killed by the {}.".format (mname))
                break
        messagebox.showinfo("Battle", "The battle is over. You return to the village.")
        mhealth = 0

        
    else:
        continue
        
    

messagebox.showinfo("Sorry", "There is nothing more. We are still developing the game. " +
                    "Thanks for playing!")
