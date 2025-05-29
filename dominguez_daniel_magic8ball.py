import random    #imports random library
import time     #imports time library

while True:         #forever loop
    options =  ["yes", "no", "absolutley not", "maybe", "definitely", "affirmitive"] #makes a list under list variable options
    quantity_options = ["a gazillion", "twelve", "like 6", "a lot"] #makes a list under list variable quantity_options
    time_options = ["soon", "now", "later", "maybe later", "tommorow", "like a week probably"] #makes a list under list variable time_options
    identity_options = ["it was me", "you", "probably", "the person to your left", "you, definitley"] #makes a list under list variable identity_options
    userinput = input("ask away\n") #prompts user for input displaying message "ask away" and assigning answer to userinput variable

    if "how many" in userinput or "how much" in userinput: #checks for "how many" or "how much" in user input
        print("determining the future...")    #display message "determining the future..."
        time.sleep(1.5)     #stops for 1.5 seconds
        print(random.choice(quantity_options)) #picks random item from quantity_optionslist and prints it
        time.sleep(1.5)     #stops for 1.5 seconds
    elif "when" in userinput:
        print("determining the future...")    #display message "determining the future..."
        time.sleep(1.5) #stops for 1.5 seconds
        print(random.choice(time_options)) #picks random item from time_options list and prints it
        time.sleep(1.5) #stops for 1.5 seconds
    elif "who" in userinput:
        print("determining the future...")    #display message "determining the future..."
        time.sleep(1.5) #stops for 1.5 seconds
        print(random.choice(identity_options)) #picks random item from identity_options list and prints it
        time.sleep(1.5) #stops for 1.5 seconds
    elif "is" in userinput or "will" in userinput or "do" in userinput or "does" in userinput or "are" in userinput or "am" in userinput: #checks for words am, is, will, do, does, are in userinput
        print("determining the future...")    #display message "determining the future..."
        time.sleep(1.5) #stops for 1.5 seconds
        print(random.choice(options)) #picks random item from options list and prints it
        time.sleep(1.5) #stops for 1.5 seconds
    
    
    else:
        time.sleep(1) #stops for 1 seconds
        print("i dont know that one") #displays message "i dont know that one"
        time.sleep(1) #stops for 1 seconds
        print("yet...") #displays message "yet..." (mysteriously)
