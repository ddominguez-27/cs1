import random    #import random library

name = input("What is your name?\n")   #asks user for name and set response to name variable
print(f"Good luck {name}...")   #print good luck name using the variable
words = ["computer", "science", "programming", "python", "logic", "board", "game", "condition"]  #defines list 'words' with those words inside the brakets
games = 0    #creates 'games' variable and sets it to zero
wins = 0     #creaters 'wins' variable and sets it to zero

while True:   #forever loop
    word = random.choice(words)   #sets 'word' variable to a random item from "words" list
    display = list(word)  #sets display to a list of all the letters in word
    random.shuffle(display)  #shuffles all elements in the list 'display'
    display = "".join(display)  #combines every element in list into 1 string
    turns = 5   #creates variable turns and sets it to 5

    while turns > 0:    #while turns is greater than 0
        guess = input(f"Unscramble '{display}'!\nEnter the real word here:") #shows "display variable" and asks user to unscrabmble it, setting answer to "guess" variable 
        
        if guess == word:  #if guess is word
            print("You got it!")  #print message
            wins += 1    #adds 1 to wins 
            break  #end foreer loop
        while True:   #forever loop
            scramble = str.lower(input("You didn't get the word right. Would you like to rescramble?\nEnter Y/N: "))  #asks user if they would like a rescramble and sets answer to "scramble variable"
            if scramble == "n": #if scramble is "n"
                break #end forever loop
            elif scramble == "y": #if scramble is y
                display = list(word)  #sets display to a list of all the letters in word
                random.shuffle(display)  #shuffles all elements in the list 'display'
                display = "".join(display)  #combines every element in list into 1 string
                break #end forever loop
            else:   #if guess is anything else
                print("invalid response") #display message
        turns -= 1  #removes 1 from turns variable
    print(f"The word was {word}")   #display message with word variable
    games += 1   #adds 1 to games variable
    
    while True:   #forever loop
        play_again = str.lower(input(f"{name}, you have won {wins} out of {games} games. Would you like to play again?\nEnter Y/N: "))  #tells user their wins to games played ratio using "name" "games" and "wins", asks if theyd like to play again and sets it to variable "play again"
        
        if play_again == "n":  #if variable = n
            exit() #end code
        elif play_again == "y":  #if variable = y
            break #break forever loop
        else:   #if variable is anything else
            print("invalid response")   #display message