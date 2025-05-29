#cat 🐈
#w3 schools used

import random                              #random library imported
import time                                #import time

coins = 10       #defines coins variale, starting the user with 10 coins
coinbet = 0    #defines variable
mb = 0         #    "     "
sr = 0         #    "     "
dt = 1         #    "     "
ma = 0         #    "     "
es = 0         #    "     "
cb = 0         #    "     "
def crit(critchance):              #function that allows for 'critical hits' to be added
    global coins                    #allows coins variable to be uesd anywhere
    if critchance >= 100:           # checks to see if critchance variable is more than 100 (meaning the comp crit hit chance)
        critchance -= 100           #removes 100 from the variable making it functoin normal again
        if random.randint(1,critchance) == 1:           #runs a random number generator between 1 and the critchance variable and checks if its 1
            print("Computer hit a critical hit and won!")          #if it is the computer hit a critical hit and won
            coins -= int(coinbet)                       #coins bet by the user are removed from coins variable
            print("You lost",coinbet, "coins")          #displays message
        else:                                           #if the random number generator wasn't 1 (no crit)
            print("You won!\nGained", coinbet, "coins")         #display message
            coins += int(coinbet)                       #coinbet amount is added to coins variable
    elif critchance < 100:                                  #checks to see if the critchance variable is less than 100 (user crit chance)
        if random.randint(1,critchance) == 1:                                         #same as above
            print("You hit a critical hit and won!\nGained", coinbet, "coins")
            coins += coinbet
        else:
            print("You lost!\nYou sent",coinbet,"coins down the drain :(")
            coins -= coinbet
    time.sleep(1)  #pause for 1 second


def main():        #function which is the main rock paper scizzors code
    global coinbet, coins         #allows variables to be used anywhere in code 
    options = ["Rock!", "Paper!", "Scissors!"]     #creates variable with options rock paper or scissors
    while True:    #forever loop

        if coins < 5:         #checks if coins are less than 5
            print("You are broke and the bank takes pity on you.\nGained 5 pity coins")     #displays message
            time.sleep(1)   #pauses breifly for 1 seconds
            coins += 5              #adds 5 to coins variable


     

        usernumber = input("Choose your weapon! Rock (1), Paper (2), or Scissors(3)! (4 to quit)\n")    #userinput is 1 2 or 3 for rock paper or scissors
        if usernumber  == "1" or usernumber  == "2" or usernumber  == "3":                         #checks to make sure that the user inputted an integer from 1-3
            userchoice = options[int(usernumber) - 1]                   #grabs the element using the number as an index
            computerchoice = random.choice(options)                    #computer input is randomly selected from options list
            while True:                 #forever loop
                print("You have", coins, "coins.")          #displays message with 
                try:
                    coinbet = int(input("How many coins would you like to bet?\n"))
                    if coinbet <= coins:
                        break
                    else: 
                        print("Please type an amount that you actually have.")
                except ValueError:
                    print("Please type an integer.")
            print("User has chosen...")                         #display message
            time.sleep(1)
            print(userchoice)           #display what user has chosen with user choice variable
            time.sleep(1)
            print("Computer has chosen...")                 #display what computer has chosen
            time.sleep(1)
            print(computerchoice)
            time.sleep(1)
            if userchoice == computerchoice:      #if user input = to computer input 
                if cb == 1:
                    print("I̵͕̾t̸͇͗̆̕͝s̵̭̔͋̈̾ͅ ̶̰͇̰̻̀̇̂ą̷̫̼̏̉̅ͅ ̵̟̺̬̺͗̓t̷̡̙͈͔͛i̵͙̾̀̿̄e̷̛̗͈̽͝ͅ!̶̭̮͚͒  The Contra Band overrides and grants you the win!")    #displays message
                    time.sleep(1)   
                    coins += coinbet   #adds coins bet to coins variable
                    print("You gained",coinbet,"coins")    #displays message with coins variable
                else:
                    print("Its a tie!")                                        #print tie
            elif userchoice == "Scissors!":                #elif user input equals scissors
                if computerchoice == "Rock":        #if computer input = rock
                    crit(dt * (10 + mb + sr))                        
                else:                                    #if computer input = paper (by process of elimination)
                    crit(dt * (10 + ma) + 100)                              
            elif userchoice == "Rock!":                             #elif user input equals rock
                if computerchoice == "Paper!":                                    #if computer input = paper
                    crit(dt * (10 + mb + sr))                                  
                else:                                    #if computer input = scissors 
                    crit(dt * (10 + ma) + 100)                                
            else:                                    #elif user input equals paper
                if computerchoice == "Scissors!":             #if cmputer is scissors
                    crit(dt * (10 + mb + sr))                                
                else:                                    #if computer input = rock
                    crit(dt * (10 + ma) + 100)                               
        elif usernumber == "4":                 #checks if userinput is 4
            print("you quit!")     #display quit message
            break               #break forever loop
        else:                       #if userinput wasnt one of the options
            print("Not gonna work")   #display message 
            
def itemshop():     #defines item shop function
    global coins, mb, sr, dt, ma, es, cb    #allows those functions to be used anywhere
    print("What would you like to buy? (type 'quit' to quit)") #display message
    while True:             #forever loop
        shop_page = str.lower(input("|Offensive items| (1)\n|Defensive items| (2)\n| s̷̝͆e̵̦̔c̵̛̞rë̴̞t̶̎ ̵͙̏i̸͗͜t̷̬̀e̶͓͐m̷͉͗s̶  | (?)\n'0' to quit\n"))  #defines a variable as an input to that message
        if shop_page == "1":    #if user input is 1
            print("You have",coins,"coins")      #displays how main coins the user has based in the coins variable
            userpurchase = str.lower(input(f"""   
Skull Ring: +20% critical hit rate - 15 coins (SR)
Meteorite Bracer: +40% critical hit rate - 25 coins (MB)
Devil's Tail: Critical hit rate x2 for both user and computer - 50 coins (DT)
"""))           #print that ^ and set the userinput to that variable
            if userpurchase == "mb":    # if user inputs mb
                if coins > 25 and not mb == -4:    #checks if the user has enough coins and if the user has not yet purchased it
                    coins -= 25   #removes coins from variable
                    print("Purchasing...")  # displays message
                    time.sleep(1)   #pause for 1 second
                    print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠑⠉⠛⠻⠿⣴⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⡄⠐⠀⠀⠀⠀⠀⣀⡄⠀⠀⣀⣀⡀⠀⠀⠀⠪⣝⠺⢵⢦⠀⠀
⠀⢠⠂⣰⣿⠿⠟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢤⣳⡈⢿⢧⠀
⠀⣾⣆⠙⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣐⠞⠃⣺⣾⠀
⣾⠋⣹⣧⣀⠀⠉⠙⠓⠦⠤⠤⠤⣀⠀⢀⣀⣀⠀⠀⠤⠤⠒⠋⣀⣤⣤⢿⠙⣄
⣿⣼⠉⡇⠈⠑⠒⠦⢤⣤⣤⣀⡀⠈⣷⡏⠀⣠⣤⣤⣴⣶⣿⣿⣿⣿⡿⣸⡇⢸
⢸⡟⢺⠇⠀⠀⠀⠀⠀⠀⠸⠉⢫⠞⠋⠑⢾⠛⠋⣿⣽⣿⣿⣿⣿⣿⣿⡝⣷⠁
⠀⢿⣌⡓⢄⡀⠀⠀⠀⠲⣶⠀⣿⡂⠀⡠⣾⠀⣠⣶⡿⢿⣿⣿⣿⠿⠋⡰⠋⠀
⠀⠈⠱⢽⣣⣬⣓⡂⠀⠠⠼⠾⠇⢙⣦⡖⠡⢾⠿⠧⠴⠟⠛⢉⡁⠄⠊⠀⠀⠀
⠀⠀⠀⠀⠈⠉⢛⣿⣿⣿⣶⣶⣦⣾⣽⡗⢦⣤⣴⣖⣾⡟⠉⠀⠀⠀⠀⠀⠀⠀
You purchased the Meteorite Bracer""") #cool ascii art
                    mb = -2    #sets mb variable to -2 ( critical hit modifier)
                    time.sleep(1)   #pauses for 1 second
                else: #if the if statement didnt work
                    print("Unable to purchase")   #display message
            if userpurchase == "sr":   #if user input is sr
                if coins > 15 and not sr == -2:   #if user has enough coins and havent purchased it yet
                    coins -= 15   #removes coins from users coins
                    print("Purchasing...")    #displays message
                    time.sleep(1)           #pause for 1 second
                    print("""
        ⠀⠀⠀⠀⠀⢀⣀⣤⣤⣶⣿⣿⣿⢶⣷⣦⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⢻⡷⢶⣾⣶⣮⣿⣾⣿⠿⠛⣛⣷⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⢸⣧⠀⢻⣿⣿⡿⠻⣿⣼⣿⣿⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡀⠸⣿⣷⣬⣿⣿⣷⡼⠟⢿⣿⣿⣿⡟⣿⡗
⠀⠀⠀⠀⠀⠀⢀⡾⣯⣿⠇⢀⣿⣿⡟⠻⣿⠏⠀⠀⢸⢿⣿⣿⣿⣸⡇
⠀⠀⠀⠀⠀⢠⣾⣿⡿⠡⣴⣿⠿⢻⣿⣦⣝⣷⣄⠀⣘⣿⠋⠸⣿⣼⡇
⠀⠀⠀⠀⣰⣿⣿⠟⠃⢰⣿⠏⣠⣾⠏⠀⠀⠉⠉⢻⣿⡏⠀⠐⢧⣿⠀
⠀⠀⠀⣰⣿⣿⠏⠀⢀⣾⠋⣴⡿⠃⠀⠀⠀⠀⢀⣾⡟⠀⠀⢀⣾⠃⠀
⠀⠀⣼⣫⣿⡏⠀⣠⣾⠃⣼⡟⠁⠀⠀⠀⠀⢰⣿⣿⠁⠀⣀⣾⡇⠀⠀
⠀⢠⣟⣿⣿⠷⠶⣻⠏⣰⡿⠁⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⣹⣿⠁⠀⠀
⠀⣼⢹⣿⠋⠀⢠⡟⢦⣿⠇⠀⠀⠀⠀⠀⣼⡿⠃⠀⠀⣼⠟⠁⠀⠀⠀
⠀⣯⣿⣟⠀⣀⣾⢡⣾⠏⠀⠀⠀⠀⢀⣾⡿⠁⠀⢀⣼⠏⠀⠀⠀⠀⠀
⢰⣿⣿⣿⡼⣼⡇⣼⡟⠀⠀⠀⢀⣠⣿⠟⠀⠀⢀⣾⠋⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⠀⣿⠇⠀⠀⣴⣿⣿⠋⢀⡠⣤⡾⠁⠀⠀⠀⠀⠀⠀⠀
⢸⢿⣿⣿⣿⡏⢰⣿⠀⣠⣾⣿⣿⣿⡿⢿⣵⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣷⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⢣⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢾⣿⣿⣷⠶⠿⣿⣿⣿⡿⣻⡵⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠳⣾⣿⣿⣷⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
You purchased the Skull Ring""") #cool ascii art
                    sr = -2   #sets the sr to -2 (crit hit modifier)
                    time.sleep(1)   #pauses for 1 second
                else:  #if the if statement didnt work
                    print("Unable to purchase")  #display message


            if userpurchase == "dt": #checks if user input is dt
                if coins > 50 and not dt == .5:   #checks if user has the coins and if user has not purchased it yet
                    coins -= 50          #removes the 50 coins from the user
                    print("Purchasing...")     #displays message
                    time.sleep(1) #pause for 1 sec
                    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⣤⠤⣤⠠⠶⠾⠟⡲⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠶⢚⣛⣭⣽⣯⣿⣷⡕⡄⠀⠀⠈⢊⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⠖⣋⣥⣶⣾⣿⣿⢿⣏⡿⣟⣾⣿⢸⡄⢈⣤⣸⢼⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⠞⢋⣰⣾⣿⢻⡻⡷⣽⣽⣾⣿⣿⣿⣿⣿⣸⣿⣟⣿⣟⡾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⡞⠁⣠⣾⣿⢧⣏⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢿⣿⣾⡟⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡺⡙⠀⣼⣿⣛⡿⣯⣿⣿⣿⡿⡿⠟⠙⠉⠁⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⡾⠥⡇⢸⣟⣶⣻⣿⣿⢿⠏⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⠇⠄⢸⠋⣼⣻⣿⡿⠕⠀⠀⠀⠀⠀⠀⠀⢀⣀⢠⣤⠴⠶⠶⠲⢶⡒⠒⠓⠒⠶⠦⣄⡀⠀⠀⠀⠀⠀⠀
⣿⡰⠂⠀⠫⣽⣻⣿⣿⡀⢀⣀⣤⠴⠶⠚⠋⠉⢉⡀⠀⠚⠀⡘⠃⠀⢑⡠⠆⢀⠘⠀⡀⠉⡃⢆⡄⠀⠀⠀
⢸⡇⢶⠆⢀⡀⠉⠉⠿⠉⠉⣁⠀⠀⢸⠀⣆⠀⢀⣇⣀⣶⡾⣿⣾⣿⣿⣷⣿⣿⣿⣷⣶⣀⢰⢀⠈⣇⡀⠀
⠀⢳⣜⢂⡀⠀⠐⠃⠀⡀⠀⣈⢀⣤⣀⣤⣶⣾⣾⣿⣿⣿⣿⣿⠛⠻⠛⠉⠋⠉⠉⠙⠿⡿⣧⣈⡂⢸⣶⡀
⠀⠀⠉⠿⢿⣟⣷⣷⣿⣽⣿⣿⣾⣷⣿⡿⣿⠿⠟⠙⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣖⢁⣾⣿⡇
⠀⠀⠀⠀⠈⠉⠛⠙⠙⠛⠋⠙⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣡⣿⣿⣿⡅
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠟⣭⣿⣿⣿⠯⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠦⠋⣱⣪⣿⣿⣿⣿⠟⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⢖⣿⣀⡤⠖⣋⢁⢦⣴⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⠖⢃⡡⠴⠓⣉⣡⣤⣷⣾⣿⠟⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡴⠖⠋⠥⠒⠭⠤⠔⠛⠛⠙⠛⠛⡷⣿⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣞⠬⠤⠤⢤⣤⠦⡶⣶⢶⡚⠞⠿⠛⠋⠛⠛⠛⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
You purchased the Devil's Tail""")   #cool ascii art
                    fe = .5    #sets variable to .5 (modifies crit chance variable)
                    time.sleep(1)   #pauses for 1 second
                else:      #if the if statement didnt work
                    print("Unable to purchase")
   

        elif shop_page == "2":
            print("You have",coins,"coins")      #displays how main coins the user has based in the coins variable
            userpurchase = str.lower(input(f"""
Mighty Armlet: -20% computer critical hit rate - 20 coins (MA)
Elevating Shoes: -40% copmuter critical hit rate - 30 coins (ES)
"""))         #prompts user for input and displays ^ message
            if userpurchase == "ma":    #if user input is ma
                if coins > 20 and not ma == 2:    #check that the user has enough coins and has not purchased it yet
                    coins -= 20    #removes coins from inventory
                    print("Purchasing...")    #displays message
                    time.sleep(1)   #pauses for 1 second
                    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠿⣿⡿⠶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠋⠀⢸⣿⡇⠀⠈⠹⡻⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠶⠟⠋⣡⣴⣿⠏⢸⣿⡇⢰⣿⣷⣄⠀⠙⠻⠷⣦⣤⣀⡀⠀⠀⠀⠀
⠀⢀⣄⣤⣶⡿⢛⣛⣭⣶⣶⣾⣿⣿⢟⢫⠀⢸⡟⡇⢰⣿⣿⠿⡿⢶⣦⣤⣄⡀⠉⠹⣷⣦⣤⡤
⣰⣿⡟⢛⣿⣿⣿⣿⣿⣿⠿⠟⡛⠛⠋⢊⣴⢯⣭⡽⢬⣉⠉⠛⠑⠀⠀⠀⠈⠙⠿⡏⠀⠈⢿⣷
⢿⣿⠃⣸⣯⡙⣿⡿⠟⢫⣿⣿⠃⠀⡠⠛⠀⣼⣿⠅⢀⡹⢆⢀⠀⠀⠀⠀⠀⠀⣄⠆⢀⣠⣄⣽
⢻⡏⢸⣇⠘⠿⣿⣇⣌⣼⣿⡿⠖⠈⣠⣴⡾⣿⣿⠂⢼⣿⣮⣉⠣⢀⠀⠀⠄⠀⢸⣇⣘⣶⣿⣿
⣾⡇⣸⣟⢷⣤⣀⣈⣉⣉⣀⣤⣴⣿⢿⣿⠁⣼⣿⡁⢺⣿⡟⠿⣷⣾⣦⣌⣧⣖⣯⣷⣿⣿⢿⣿
⣹⡇⣿⣿⣮⣿⣟⣿⡟⠉⠉⢉⣷⣾⡟⠃⣴⣿⣿⣿⣦⡽⣷⣤⣀⣋⣿⡿⣿⣿⡟⣿⣣⣿⢲⣿
⢸⡇⣿⣀⣿⢸⣿⣿⡧⢀⣰⡿⠋⠉⢠⣾⠋⠁⠀⠀⠙⣿⣽⣟⠛⢻⣿⣿⡷⣿⣿⡏⣿⢀⢺⣿
⢸⡇⢿⣟⣿⣸⣿⣿⠁⠸⣿⣧⣄⠀⣿⡇⠀⠀⠀⣴⣿⣿⡿⣿⠠⢿⣿⣿⣿⣿⣿⣞⣿⣀⣹⣿
⢽⣧⢺⡏⣷⣟⢻⣿⠀⠀⡄⠈⠘⣧⠸⣷⡓⠋⢻⡿⢉⣽⢰⣿⣷⣿⣿⣿⣿⣿⡻⣿⡧⣿⣿⢮
⠘⣿⡼⣷⡾⣿⣿⠃⠀⠀⡉⡄⠀⠙⣧⡉⢻⣶⣶⣶⠟⢫⣿⣿⣿⣿⡟⣸⣿⣿⣿⡿⢡⣿⣏⡧   
⠀⠙⢿⣟⣷⡌⠻⠃⡀⠀⢳⣈⣂⣰⣿⣿⠠⣿⡷⠀⢠⣿⣿⣿⣿⢛⣴⣿⣿⣿⠟⣱⡿⢛⡺⠇
⠀⠀⠀⠀⠉⠻⣷⣄⡈⠙⠈⠻⢿⣯⣭⣿⠀⣿⣿⡅⢸⣿⣿⣿⣿⣿⠿⢟⣫⣴⠿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⣿⣷⣶⣤⣄⣀⣈⣀⣠⣿⣿⡃⠀⢉⣩⣵⣥⣶⡿⠿⠛⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠉⠙⠻⢿⢿⣿⣿⣿⣿⠷⢿⣿⣿⣿⡿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
You purchased the Mighty Armlet""")   #cool ascii art
                    ma = +2    #sets variable which modifies crit chance
                    time.sleep(1)   #pauses for 1 second
                else: 
                    print("Unable to purchase")
            if userpurchase == "es":
                if coins > 30 and not es == 4:
                    coins -= 30
                    print("Purchasing...")
                    time.sleep(1)
                    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⡄⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢊⡿⣟⣰⢾⣇⣀⠾⡶⢖⣫⣭⠿⣷⡀⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣫⡴⣏⡷⡰⢋⣴⣿⣏⡴⣹⣟⠧⡠⠀⠈⠚⣄⠑⡥
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢚⣵⣯⠷⢛⡥⡣⣼⣿⣿⣿⢃⣿⡝⢦⡁⠀⠀⠀⣿⣴⣷
⠀⠀⢀⡀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⡀⡄⣖⣭⣾⣿⠻⣊⠴⡫⣮⡿⣏⣷⣿⡗⣼⣟⠾⣡⠂⠀⠀⣶⠟⡟⠁
⢠⠞⠁⠀⠀⠩⡇⠀⠀⠀⠀⢀⠀⣀⣠⠟⠠⡁⢷⣐⣫⣵⣾⠿⣋⢧⠱⡋⣵⡼⢿⡝⣾⣿⣿⡟⣰⣿⣞⡿⢄⢃⠀⢠⡽⢸⣷⠀
⡞⠀⢠⣆⣦⣳⠏⠀⠀⠀⠖⠉⣀⡟⢸⣦⣤⠙⠎⢭⠭⠱⢆⣋⣭⣴⣾⡟⡯⣯⣷⣿⠿⠋⡍⣰⣿⣿⢾⡽⡎⠤⢀⢶⢃⣿⣿⠀
⣯⠀⠘⢿⡉⠀⠀⠀⠀⣠⡷⣚⢁⡀⣴⡾⠃⠀⢀⣠⠖⠘⠛⢯⣇⣧⣳⠾⠟⠛⣁⣠⣤⣋⣴⣿⣿⣿⡿⣞⠛⢀⣿⢏⣾⣿⣿⠄
⢸⢦⠀⠨⣑⠛⠃⠐⠋⠀⢉⡿⡷⠟⡛⣁⠦⣙⡾⠁⠀⠀⠀⢀⢿⣻⣼⣾⣿⣶⠋⠁⠈⠁⠉⠉⢿⣿⣻⢤⣣⣾⢋⣾⣿⡿⣻⡄
⠘⣞⣆⡀⠙⢆⠲⢤⠠⣄⡘⣳⣅⣲⠱⡟⣴⣿⠇⠀⠀⣴⠦⣜⡼⣿⢿⣿⠿⠋⠀⢠⣄⡀⢠⡲⡌⢻⣟⣾⡛⣫⣾⣿⡿⢣⣿⡇
⠀⠘⣞⡷⣄⡈⠑⢎⡱⢦⠹⡔⡪⢝⣷⣩⢾⣿⠀⠀⠀⠹⣿⠋⠀⢹⡀⠘⣇⡀⣤⣩⠏⠹⣿⠧⡙⠒⠋⣣⣾⣿⣽⠟⣡⣳⣷⠀
⠀⠀⠈⠻⢷⣯⣳⣶⡶⣞⢷⡻⢿⣻⣌⣿⣳⣽⡀⠀⠀⠐⢌⡃⢰⢈⣳⠷⠢⣍⠭⠶⣦⣻⡟⢣⠀⣴⡿⣿⣠⣿⢩⣶⣿⣿⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠁⠁⠀⠀⠁⠀⠁⠀⠀⠈⣧⠐⣆⠀⠀⠳⣄⠀⠀⠉⠁⠀⠓⣤⡛⢭⠘⣄⢺⣿⣴⣟⢏⣵⣿⡿⣿⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡄⠈⢧⡀⠐⢈⢇⢣⠒⡔⢢⡐⡘⠿⣦⢝⡤⣿⢻⣧⣹⣿⣿⣿⠞⠋⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⠀⠙⣆⠀⠈⠆⡫⠜⣥⢚⡥⢳⢎⠿⢲⣿⢾⣷⣿⠉⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣔⣢⡝⣶⣄⠀⠑⢢⡙⢬⠓⣎⣼⢶⣾⣿⣾⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⣿⣳⣿⣷⣦⣤⣤⣾⡿⣟⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠋⠋⠑⠋⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
You purchased the Elevating Shoes""")
                    es = 4   #sets variable to 4 (modifies crit chance variable for comp)
                    time.sleep(1)   #pauses for 1 second
                else: 
                    print("Unable to purchase")
        elif shop_page == "secret":   #checks if user input is secret
            print("Secret shop opened")   #displays message
            time.sleep(1)   #pauses for 1 second
            print("You have",coins,"coins")      #displays how main coins the user has based in the coins variable
            userpurchase = str.lower(input(f"""
Contra Band: Overrides a tie, and grants user the win 100% of the time - 50 coins (CB)
"""))
            if userpurchase == "cb":    #if user input is cb
                if coins > 50 and not ma == 1:    #check that the user has enough coins and has not purchased it yet
                    coins -= 50    #removes coins from inventory
                    print("Purchasing...")    #displays message
                    time.sleep(1)   #pauses for 1 second
                    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠒⠀⠲⢶⣶⣄⣠⡤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡏⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣞⠲⠦⢄⡀⡀⠀⠉⠙⠛⠿⢷⣾⣿⣷⡶⠦⢤⣤⠊⠠⢃⠸⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣦⣅⣀⡈⠐⠢⣔⡢⢄⡀⠀⠀⠉⠻⣧⣠⠞⠁⠀⣰⠋⡆⢇⢋⣗⣒⡦⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢷⠎⣿⠓⣂⡉⢯⣁⠨⣛⣦⠀⢀⡝⠁⠀⣠⠞⡉⠰⢣⢘⠘⡸⡀⠀⢁⣀⣈⠉⠀⠐⠒⠠⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣸⡘⡄⠘⠴⠿⢹⠀⢻⣋⣦⠹⠷⠋⠀⣈⣴⣃⠀⠁⠠⠈⡄⣆⢣⣷⠊⠁⠀⠀⠈⠉⠉⠁⠐⠒⠒⠊⠑⢢⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣝⣳⡌⠢⠤⠴⠊⡠⠟⢉⣤⡒⣪⣽⣬⠉⠀⠈⠉⠙⠒⠦⢥⡈⢿⠻⣦⣤⠖⠒⠒⠢⠄⠀⠀⢀⣀⣀⢀⠀⢃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠿⢿⡂⣈⡶⢋⠄⣪⣝⣽⠿⣿⡿⠿⠿⠏⠹⣶⣶⣤⣄⡀⠈⠂⣄⠙⢎⣥⡷⣧⣬⠭⢛⣀⡀⠀⠀⠀⣿⠞⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣨⡵⠋⡰⠋⣀⣿⡟⠛⢉⣀⣤⣤⣶⠶⠤⣤⣀⡙⠃⢿⣶⣄⠈⠢⡀⢻⣄⠏⣴⣿⡏⣸⣿⡿⠛⣻⠁⠀⠀⠀⠀
⣀⣄⣀⠀⠀⠀⠀⠠⠤⠤⠤⠤⠦⠴⠟⢁⠊⠠⣼⠟⢁⡴⣟⡭⢞⣯⣭⡽⠿⠭⣓⡮⣝⠷⣄⠉⠰⣷⡀⠘⡄⠹⡆⠳⡀⢉⡵⢋⣴⡿⠃⠀⠀⠀⠀⠀
⠈⠙⠻⢷⡒⠶⣄⡠⣤⣤⣀⣀⣀⣀⣠⠆⢀⣞⠁⡴⡫⣪⠕⢊⠟⠉⠉⠙⢦⣀⣄⢩⡗⢽⣮⠓⢄⠙⣿⣄⠸⡠⢹⡶⢈⣉⣀⣚⡟⢇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠑⠂⠍⣒⠽⣲⡤⣭⣋⡏⠀⣾⠃⣨⡞⡱⠃⠀⣾⠀⡔⠐⠀⢸⣿⣿⠛⢻⣦⡁⠱⡈⣆⠘⣷⡄⢱⢡⣷⣶⠾⢿⠛⠋⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢳⠯⣙⡉⠁⢰⡗⣰⢻⢰⠃⢰⠖⠛⢷⣧⣤⣶⣿⣿⣿⣶⣾⣿⠑⠀⣱⢸⡀⢻⣗⠘⡆⢸⣧⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⣸⡇⡄⢸⡇⠉⠀⢸⠀⣻⣄⣄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠐⡎⠇⠸⡇⠀⣧⣁⠈⠉⠂⠤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠔⣏⠀⢀⠻⣧⢣⣾⣷⢢⣠⢸⠸⣯⡉⣻⣿⣿⣿⣿⡿⣧⡹⣿⣿⣿⠙⢠⡆⢀⣄⣸⣇⢀⡇⠈⡙⠲⠦⣄⡀⠉⠂⠄⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡇⠠⠈⢢⣸⠀⠸⡞⡜⣽⣎⣿⡄⠇⢻⣿⣿⣿⣿⣿⣟⢻⠸⣧⡘⣿⠛⠁⣸⣼⡿⣼⣭⡟⡜⢿⣿⣿⣿⣿⡟⠛⠷⠤⠒⠤⠈⢒⣄
⠀⠀⠀⠀⠀⠀⠀⡏⠢⡈⠓⠍⠳⣄⡻⣰⡙⢿⡟⣝⣆⢠⡙⣿⢿⣿⡿⢿⢸⡇⢻⢷⡘⣇⢠⣿⡿⢣⣿⡿⡝⣠⠞⠒⡖⠉⠀⠀⠉⠉⠉⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠮⡚⠢⢀⠀⠌⠙⠿⣵⣌⠻⣬⡺⢷⣝⠾⣤⣟⣁⣸⣈⣷⣈⣇⣩⣿⡿⠏⠠⡾⢛⢕⣴⠛⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡢⣄⠀⢑⠢⡈⠳⣕⢌⡻⢦⡙⠿⣶⡬⣽⣧⣾⣿⢿⡿⠟⠉⠀⠂⢀⣐⣵⠟⠁⠀⠀⠀⣹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⢕⠬⡱⣄⠠⡈⢳⠈⠐⢭⣙⡲⠲⠥⢭⡯⠥⠶⠐⢂⡈⢤⣲⣷⣋⡥⠄⠐⠒⠊⠉⠁⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢮⡻⣷⣌⢪⡆⠀⠘⡏⠙⠛⢲⡶⠒⠒⠂⣨⢟⡛⠋⠉⠀⠀⠀⡀⣀⠤⠄⡲⢂⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠪⡻⣶⣿⠀⠀⢹⠀⣤⡾⠃⣠⣠⡾⠛⢉⡡⠤⠐⠠⠤⠖⠛⢃⣈⠤⠔⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡻⡇⠀⠈⢻⠟⢁⢞⣾⣿⠧⢁⣀⡀⠤⠔⠒⠒⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⠀⣴⢃⡴⣱⠿⠕⠒⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⡿⣫⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
You purchased the Contra Band""")   #cool ascii art
                    cb = 1    #sets variable which modifies tie part of main function
                    time.sleep(1)   #pauses for 1 second
                else:
                    print("Unable to purchase")    #displays message
            

        elif shop_page == "0":   #if user input is 0
            break    #break forever loop
        else:   #if user input is anything else
            print("Shop page does not exist")       #display message


while True:     #forever loop
    main_menu = input("What would you like to do?\nPlay Rock, Paper, Scissors (1)\nOpen the Item Shop (2)\n")   #main_menu variable that is based off of a user input
    if main_menu == "1":    #if user input is 1
        main()    #run the 'main' function
    elif main_menu == "2":    #if user input is 2
        itemshop()   #run itemshop function
    else:     #if user didnt enter any of the above
        print("Wasn't an option")    #display message 