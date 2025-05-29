'''
flowerpot: 
Author: Daniel Dominguez
Description: a "food-o-matic, s make a list of food combinations with their price and addons (randomly) and then add to get total price. coupons included!
Date: 4/7/25
Bugs (should be none for this one!): none (although the naming is weird, some left over from the check in)
Challenges: one item has a random price, promo codes with limits, checks for integer input, gets a final price
Sources: w3 schools
'''


import time
import random  #random library imported

mmotd = random.randint(10, 20)  #generates a random integer when the while true loop restarts
foods = ["Peashooter Salad", "Crazy Dave's Brain", "Taco", "Kyle's Brain", "Mystery Meat of the Day Sandwich", "Spicy Potato Mine Fries"]   #makes a list named food
prices = [29, 79, 6, 69, mmotd, 19]   #makes a (parralel) list called prices, contains integers 
addons = ["Crazy Dave's Hot Sauce", "Singing", "Flute", "no salt", "Love", "mayo"]  #makes a list called addons with addon names
promotions = ["SORRYFORBURNINGDOWNYOURHOUSE15", "HAVEFUN11IILL1IL1IL"]  #makes a list called promotions with those things in it

while True:   #while true loop
    total_price = 0   #(re)sets the totalprice variable to 0

    try:   #try functoin that checks to make sure it works
        quantity = int(input("how many foods?"))     #tries to make the quantity variable (a string right now) into an integer
    except:    #if it fails (not an integer inputted)
        print("how about an integer next time")    #print statement
        continue    #restart while true loop

    promo_request = input("Would you like to enter a promotional code? (Type 1 for yes)")   #creates variable promorequest and assign it the input 
    
    if promo_request == "1":  #if user input is 1
        attempts = 0    #(re)sets the attempts variable to 0
        
        while True:
            promo_attempt = str.upper(input(f"You have {6-attempts} attempts. Please enter a Promo Code: (q to quit) ")) #prints statement and remove 1 every time it repeats
            
            if promo_attempt == "Q" or attempts >= 5 or promo_attempt in promotions:    #if one of those conditions is true
                if promo_attempt in promotions:  #if the inputted statement is within the above list
                    print("Promo code applied!")   #prints statement
                    time.sleep(1)  #waits 1 second
                break   #breaks loop
            attempts += 1   #add 1 to attempt counter
    else:
        promo_attempt = "NULL"   #just to define the variable
    for i in range(quantity):   #for 'index' in the size of the variable quantity
        randchoice = random.randint(0, 5)   #picks a random integer 0-4, representing the index of the paralell arrays (to be reused)

        print(f'''
    Dish #{i+1}: {foods[randchoice]} with {random.choice(addons)} 
    Price: ${prices[randchoice]}
    ''')  #print that whole statements with the right number of the parellel array and a random index of the addons
        total_price += prices[randchoice]    #adds the price to the total price variable
        time.sleep(.2)

    if promo_attempt == promotions[0]:    #if total price = the element in index 
        total_price = total_price*0.85    #removes 15% from total price
    elif promo_attempt == promotions[1] and total_price >= 100:  #if promo input is the same as the index 1 element and total price is more than 100
        total_price = total_price-20                #remove 20 from total price
    print(f'Your total price is ${total_price}')   #print the total price in that statement 
