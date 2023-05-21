import random
import os
import sys
from time import sleep
def slowprint(text):
  for x in text:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.07)
def slowprint2(text):
  for x in text:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.000001)
# Colors
Blue="\033[0;34m"
Cyan="\033[1;36m"
White="\033[0;37m" 
Green="\033[0;32m"
Orange ="\033[0;33m"
Pink = "\033[1;31m"
DarthMaul = """
                                   
                              ,-'_ `-.                              
                              ::".^-. `.                            
                              ||<    >. \                           
                              |: _, _| \ \                          
                              : .'| '|  ;\`.                        
                              _\ .`  '  | \ \                       
                            .' `\ *-'   ;  . \                      
                           '\ `. `.    /\   . \                     
                         _/  `. \  \  :  `.  `.;                    
                       _/ \  \ `-._  /|  `  ._/                     
                      / `. `. `.   /  :    ) \                      
                      `;._.  \  _.'/   \ .' .';                     
                      /     .'`._.* /    .-' (                      
                    .'`._  /    ; .' .-'     ;                      
                    ; `._.:     |(    ._   _.'|                     
                    `._   ;     ; `.-'        |                     
                     |   / .-'./ .'  \ .     /:                     
                     |  +.'  \ `-.   .\ *--*' ;\                    
                     ;.' `. \ `.    /` `.    /  .                   
                    /.L-'\_: L__..-*     \   ".  \                  
                   :/ / .' `' ;   `-.     `.   \  .                 
                   / /_/     /              \   ;  \                
              |  _/ /       /          \     `./    .               
            `   .  ;       /    .'      `-.   ;      \              
           --  /  /  --   ,    /           `"' \      .             
          .   .  '       /   .'                 `.     \            
             /  /    `  /   /                  |  `-.   .           
        --  .  '   \   /                         `.  `-._\          
       .   /  /       : `*.                    :   `.    `-.        
          .  '    `   |    \                    \    `-._   `-._    
     --  /  /   \     :     ;                    \              |   
   .    .  '           ;                          `.  \      :  ;   
       /  /   `       : \    \                      `. `._  /  /    
  --  .  '  \         |  `.   `.                      `-. `'  /\    
     /  .             ;         `-.              \       `-..'  ;   
 `  .  '   `          |__                     |   `.         `-._.  
_  :  /  \         ;`-.                  :     `-.           ; 
    `"  `               |   `.                 \       `*-.__.-*"' \
' /  . \                ;_.  :`-._              `._                /
                       /   `  . ; `"*-._                       _.-` 
                     .'"'    _;  `-.__                     _.-`     
                     `-.__.-"         `""---...___...--**"' |       
                                                  `.____..--'
"""

user = """ 
      .-.
    __|=|__
   (_/`-`\_)
   //\___/\\
   <>/   \<>
    \|_._|/
     <_I_>
      |||
     /_|_\ 
"""

slowprint(Green + "Type in 1 or 2  ")
hello = input("")
if hello == "1":
  slowprint(Pink + "This is you:")
  slowprint2(White + DarthMaul)
if hello == "2":
  slowprint(Pink + "This is you:")
  slowprint2(White + user)
letters = "a", "b", "c", "d"
slowprint(Cyan + "\nWelcome to a text version of The Hollow. The aim is to get out of the game before getting killed. And be careful, there is also another team playing against you.")
slowprint(Orange + " \nWhat is your name?")
name = input("")
os.system("clear")
slowprint(Green + "You wake up in a room with nobody except you. You have no memories and are unable to figure out where you are. You try to find an object to help you exit, but only find a piece of paper saying ")
slowprint(White + name)
slowprint(Green + " on it and a typewriter at the corner of the room. There is only one passageway for air, which is a vent at the top of the room. You look around the room and see that the four walls and the ceiling is made of bricks and the floor is stone. You figure out that the piece of paper says your name on it. You need to figure out a way to get out of the room, so you think of all the options you have to do."+ Pink + "\n(a)try pounding on the walls" + Cyan + "\n(b)go up to the typewriter" + Blue + "\n(c)try climbing up to the vent" + Orange + "\n(d)give up and sit sulking." + Green + "\nWhat do you do? Type in the letter you want to do.")
decision1 = input("")
os.system("clear")
if decision1 == "a":
  deathoptions = "A load of water came through the vent and drowned you. You lost the game!","A load of poisonous gas came though the air vent and suffocated you. You lost the game!","You pounded the walls so hard that all the bricks fell on you and you suffocated. You lost the game!"
  methodofdeath = random.choice(deathoptions)
  slowprint(Pink + methodofdeath)
if decision1 == "c":
  deathoptions = "A load of water came through the vent and drowned you. You lost the game!","A load of poisonous gas came though the air vent and suffocated you. You lost the game!","Instead of climbing up to the vent, you jumped up to the vent. Sadly you jumped so high that on the way down you broke both your legs. You lost the game!", "Some snakes came out of the walls and attacked you. You lost the game!"
  methodofdeath = random.choice(deathoptions)
  slowprint(Pink + methodofdeath)
if decision1 == "d":
  deathoptions = "A load of water came through the vent and drowned you. You lost the game!","A load of poisonous gas came though the air vent and suffocated you. You lost the game!","Some snakes came out of the walls and attacked you. You lost the game!"
  methodofdeath = random.choice(deathoptions)
  slowprint(Pink + methodofdeath)
if decision1 not in letters:
  slowprint(Pink + "You lost the game, becuase you weren't that quick.")
if decision1 == "b":
  slowprint(Cyan + "You go to the typewriter and examine it. Then you see that something has already been written on the page." + White + "'Type in the two words that will help you the most.'" + Cyan + " You realise that you need to type in something, but don't know what. You lift up the typewriter and see the letters " + Orange + "ephelapsel" + Cyan + " and see the pattern " + Orange + "_ _ _ _   _ _ _ _ _ _" + Cyan + ". You then realise that you are supposed to write two words, the first one 4 letters, and the second one 6 letters, and that " + White + "ephelapsel" + Cyan + " is a jumbled up version of the two words.You are desperate to get out of the room, so you think.")
  slowprint(Orange + "\nWhat are the two words?")
  twowords = input("")
  twowordslower = twowords.lower()
  os.system("clear")
  if twowordslower == "help please":
    slowprint(Blue + "Just after you press the e, you realise that you are sitting on a swirl of blue mist. As you realise that, you fall through the mist, realising that it was a portal. When you land, you realise are in another room, but this time with 5 doors. Then a weird guy comes in the room and tells you that behind each door is a portal and that 1 of the portals is safe and the rest of the portals can get you killed. He asks you to pick a portal.\n" + Orange + "Which one will you pick? Type in a number between 1 and 5.")
    portals = "1","2","3","4","5"
    choiceportal = input("")
    safeportal = random.choice(portals)
    os.system("clear")
    if safeportal == choiceportal:
      slowprint(Cyan + "You land very softly. When you look around, you see that you are in a desert. You feel like drinking some water. As you feel that, a water fountain erupts from the ground. You stare at it. Then you stare at another piece of land and try to make a water fountain there. That also works. Then you here a voice from behind you: it's Weirdy! He tells you that you have special water powers which will help you defeat the sand monster. Before you get to ask him what he means, he disappears. You hear a loud thumping noise and turn around, then realise you Weirdy means. In front of you is a 30 feet tall sand monster, in the stance which looks like he is about to punch you away. You start running away and see another portal at the opposite direction of the sand monster. Then you remember your water powers. You think about what to do." + Orange + "\nDo you " + Green + "(a)Blast the sand monster with water " + Orange + "\nor " + Blue + "\n(b)run to the portal?")
      decision2 = input("")
      os.system("clear")
      if decision2 == "a":
        slowprint(White + "You blast the sand monster with water and the sand monster turns into millions of pieces. You then run to the portal and go to another world.")
        directions = "left","right"
        directions2 = "left", "right", "straight"
        slowprint(Green + "You land in a long alleyway. You travel ahead, and then see that you have an option of left or right." + Orange + "\nWhich way do you go?")
        choicedirection1 = input("")
        cd1 = choicedirection1.lower()
        rightdirection1 = random.choice(directions)
        os.system("clear")
        if cd1 == rightdirection1:
          slowprint(Blue + "You go more into the maze and face another set of options. " + Orange + "Do you go left or right?")
          choicedirection2 = input("")
          cd2 = choicedirection2.lower()
          rightdirection2 = random.choice(directions)
          os.system("clear")
          if cd2 == rightdirection2:
            slowprint(Cyan + "You go more into the maze and face another set of options. " + Orange + "Do you go left or right?")
            choicedirection3 = input("")
            cd3 = choicedirection3.lower()
            rightdirection3 = random.choice(directions)
            os.system("clear")
            if cd3 == rightdirection3:
              slowprint(White + "You go more into the maze and face another set of options. " + Orange + "Do you go left, right or straight?")
              choicedirection4 = input("")
              cd4 = choicedirection4.lower()
              rightdirection4 = random.choice(directions2)
              os.system("clear")
              if cd4 == rightdirection4:
                slowprint(Blue + "You go more into the maze and face another set of options. " + Orange + "Do you go left, right or straight?")
                choicedirection5 = input("")
                cd5 = choicedirection5.lower()
                rightdirection5 = random.choice(directions2)
                os.system("clear")
                if cd5 == rightdirection5:
                  slowprint(Cyan + "You turn the final turn and find yourself, next to another portal. " + Orange + "\nDo you " + White +  "\n(a)Go into the portal" + Orange + " \nor " + Cyan + "(b)Ignore the portal and explore the land?" + Orange + "\nType in the letter of the choice you want to do.")
                  portalornot = input("")
                  os.system("clear")
                  if portalornot == "a":
                    slowprint(Cyan + "You land softly and realise that it is grass. Then, Weirdy appears and tells you that to win the game, you have to get a trident that shoots electricity called Thunderstorm. Then he disappears again. You then see a poster with the picture of Thunderstorm. You read the poster and ss that in order to get Thunderstorm, you have to pick and drink a vial of gorgon's blood. If the gorgon's blood is from her right side, you get Thunderstorm, but if it is from her left side, you die and don't get it Thunderstorm. At the bottom of the poster, it says," + White + " 'If you are interested, please go to Vulcan Cafe.' " + Cyan + "You follow some signs and see a boy also wanting Thunderstorm. A gorgon comes up to you and asks you if you are there for the weapon. You say yes and she pulls out two vials of her blood. She then asks you to pick." + Orange + " \nDo you pick vial number 1 or 2? Type in the number you want to pick.")
                    oneortwochoice = input("")
                    oneortwonumbers = "1","2"
                    oneortworight = random.choice(oneortwochoice)
                    if oneortwochoice == oneortworight:
                      slowprint(Green + "You drink the vial and after a while, the gorgon hands you Thunderstorm. You then see a portal at the corner of the cafe and go in it.")
                      os.system("clear")
                      slowprint(Green + "You land at your feet at the edge of a volcano. You look inside the volcano and see that a 30 foot lava monster is staring at you. You know that you have to do something, but don't know what." + Orange + "\nWhat do you do, do you " + White + "\n(a)throw Thunderstorm at the monster " + Blue + "\n(b)spray the monster with water or " + Cyan + "\n(c)do nothing " + Orange + "\nType in the letter you want to do  ")
                      aborc = input("")
                      os.system("clear")
                      if aborc == "c":
                        slowprint(Blue + "The lava monster slowly goes back to sleep. You see a portal. " + Orange + "\nWhat do you do? Do you " + White + "\n(a)go inside the portal or " + Cyan + "\n(b)slide down the volcano. " + Orange + "Type in the letter you want to do  ")
                        slideornot = input("")
                        os.system("clear")
                        if slideornot == "a":
                          slowprint(Blue + "You land in another desert and see a guy in long black robes. He turns to you and intoduces himself to you as Death. He then tells you that he has what you need to make your weapon work: a keycard. He explains that Thunderstorm has an electric scanner, so only when the card is scanned, Thunderstorm will work. He then pulls out a keycard, and you ask him for it, but he says that you have to do a favour for him." + Orange + "\nDo you" + Green + "\n(a)Ask him what favour you have to do or" + White + "\n(b)Try to snatch the card out of his hands" + Orange + "\nType in the letter you want to do ")
                          snatchornot = input("")
                          os.system("clear")
                          if snatchornot == "a":
                            slowprint(Green + "You ask him what favour he wants and he says he wants you to die. You gasp and then start do decide what to do. " + Orange + "\nDo you" + Green + "\n(a)Stab yourself with Thunderstorm" + Cyan + "\n(b)Decline his offer and hope to find a way without Death's help" + Orange + "\nType in the letter you want to do ")
                            deathornot = input("")
                            if deathornot == "a":
                              slowprint(Cyan + "Death was really happy by your dedication to getting the card, and resurrects you. He then hands you the card and tells you to step in a portal. As soon as he says that, a portal appears. You go though it. Press enter to continue.")
                              input("")
                              os.system("clear")
                              slowprint(Green + "You land in another desert. In front of you, you see the Greek God Zeus standing with his lightning bolt. He sees you ans says " + White + "'You are just in time for the battle, let's start.' " + Green + "You don't understand what he means, but he immediately strikes lightning from his lightning bolt at you. You dodge the lightning and turn Thunderstorm in shooting position. During the game, you can" + Blue + "\n(a)Attack" + Cyan + "\n (b)Boost or" + White + "\n(d)Defend. " + Orange + "\nPress enter to continue")
                              input("")
                              zeusscore = 5
                              yourscore = 5
                              for i in range(5):
                                os.system("clear")
                                lettersabc = "a","b","d"
                                zeuschoice = random.choice(lettersabc)
                                slowprint(Orange + "Type in the letter you want to do ")
                                yourchoice2 = input("")
                                yourchoice = yourchoice2.lower()
                                if yourchoice == "a" and zeuschoice == "a":
                                  slowprint(White + "You and Zeus both attacked. Both of you dodged the lightning.")
                                if yourchoice == "a" and zeuschoice == "b":
                                  slowprint(Green + "You attacked while Zeus attempted to have a boost. Fortunately for you, you attacked Zeus and Zeus couldn't have his boost.")
                                  zeusscore = zeusscore - 1
                                if yourchoice == "a" and zeuschoice == "d":
                                  slowprint(Blue + "You attcked while Zeus defended, so your shot didn't hit Zeus.")
                                if yourchoice == "b" and zeuschoice == "a":
                                  slowprint(Pink + "You tried to boost while Zeus attcked. Unfortunately for you, Zeus attacked you and you couldn't have your boost.")
                                  yourscore = yourscore + 1
                                if yourchoice == "b" and zeuschoice == "b":
                                  slowprint(Cyan + "You and Zeus both boosted.")
                                  zeusscore = zeusscore + 1
                                  yourscore = yourscore + 1
                                if yourchoice == "b" and zeuschoice == "d":
                                  slowprint(Green + "You boosted while Zeus defended.")
                                  yourscore = yourscore + 1
                                if yourchoice == "d" and zeuschoice == "a":
                                  slowprint(Cyan + "Zeus tried to attack but you defended it.")
                                if yourchoice == "d" and zeuschoice == "b":
                                  slowprint(Pink + "You defended hoping for Zeus to attack, but he boosted instead.")
                                  zeusscore = zeusscore + 1
                                if yourchoice == "d" and zeuschoice == "d":
                                  slowprint(Blue + "Both of you defended.")
                                if yourchoice not in lettersabc:
                                  slowprint("You just stood there while Zeus attacked.")
                                  yourscore = yourscore - 1
                              if yourscore == zeusscore:
                                slowprint(Pink + "\nZeus finished you off with a cloud of lightning. You lost the game!")
                              if yourscore > zeusscore:
                                slowprint(Green + "\nYou won the game!")
                              if yourscore < zeusscore:
                                slowprint(Pink + "\nZeus finished you off with a cloud of lightning. You lost the game!")
                            sleep(2)

                            if deathornot != "a":
                              slowprint(Pink + "Death got angered by your choice and killed you. You lost the game!")
                          if snatchornot != "a":
                            slowprint(Pink + "Death got angered by your choice and killed you. You lost the game!")
                        if slideornot != "a":
                          slowprint(Pink + "The lava monster suddenly woke up and ate you. You lost the game!")
                      if aborc != "c":
                        slowprint(Pink + "You made the lava monster very angry and he ate you. You lost the game!")
                        #Carry on from here#
                    if oneortwochoice != oneortworight:
                      slowprint(Pink + "You drink the vial and feel an immense lot of pain. You die and lose the game!")
                  if portalornot != "a":
                    slowprint(Pink + "A minotaur appeared and ate you. You lost the game!") 
                if cd5 != rightdirection5:
                  slowprint(Pink + "A minotaur appeared and ate you. You lost the game!") 
              if cd4 != rightdirection4:
                slowprint(Pink + "A minotaur appeared and ate you. You lost the game!")    
            if cd3 != rightdirection3:
              slowprint(Pink + "A minotaur appeared and ate you. You lost the game!") 
          if cd2 != rightdirection2:
            slowprint(Pink + "A minotaur appeared and ate you. You lost the game!") 
        if cd1 != rightdirection1:
          slowprint(Pink + "A minotaur appeared and ate you. You lost the game!") 
        #the weapon is called Thunderstorm and can be activated by a card with a barcode. The weapon has a scanner so it will know when the card is scanned.#
      if decision2 != "a":
        slowprint(Pink + "You were too slow in running and you got sucked in the sand monster's sand tornado. You lost the game!")
      #add part 2 from here#
    if safeportal != choiceportal:
      slowprint(Pink + "You go into the portal.\n")
      deathoptions = "You landed in an ocean and you drowned. You lost the game!","A load of poisonous gas came though the air and suffocated you. You lost the game!","Some snakes surrounded you and attacked you. You lost the game!"
      methodofdeath = random.choice(deathoptions)
      slowprint(Pink + methodofdeath)
  if twowordslower != "help please":
    slowprint(Pink + "Those were not the words.\n")
    deathoptions = "A load of water came through the vent and drowned you. You lost the game!","A load of poisonous gas came though the air vent and suffocated you. You lost the game!","Some snakes came out of the walls and attacked you. You lost the game!"
    methodofdeath = random.choice(deathoptions)
    slowprint(Pink + methodofdeath)
else:
  slowprint(Pink + "That is not an option. You have lost the game!")
slowprint(Green + "Thanks to all the people that upvoted: @MORGANISTHEBEST , @CoolJames1610 , @HZLPY , @nk1rwc , @FunnyLamma , @NeilGolchha , @mkhoi ,  @JBYT27 , @Zuhdi28 , @SotoAyam ,@RARA12SPQR , @DannyIsCoding , @Chrysaor102 , @DeepakChoudhar2 , @medcho , @Krsoslav , @henryeth , @syflexer , @Anvaysharma , @studentAlfredAl , @NobertoCruz , @Makutunga , @elijahnik1 , @Lodish , @UltraNecrosma , @CrazyGamerJT , @IvanGonzalez2 , @MilanaGerrish , @Warhawk947 , @Axrevyn , @AndreySloan , @ZacPlayz , @BobTheTomatoPie , @sebasvivas1 ")
#This is all the people that upvoted my first part#
#Add all the people that upvoted my other parts#
