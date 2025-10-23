"""
Author: Daniel Dominguez
Sources: Mr. Campbell, Assignment sheet
Description: Returns a value which represents the cost of the price to ship based on parcel dimensions and starting and ending zipcodes
Bugs: none that i know of
Challenges: none that i know of

"""




"""

Args: l (float), h (float), w (float)
Return: 0-7 (int)


description: checks the values and assigns a number to it representing package type

"""
def size_tracker(l, h, w):
    size_tracked = 0
    if (3.5 <= l <= 4.25) and (3.5 <= h <= 6) and (.007 <= w <= .016):
        size_tracked = 1
    elif (4.25 <= l <= 6) and (6 <= h <= 11.5) and (.007 <= w <= .016):
        size_tracked = 2
    elif (3.5 <= l <= 6.125) and (5 <= h <= 11.5) and (.016 <= w <= .25):
        size_tracked = 3
    elif (6.125 <= l <= 24) and (11 <= h <= 18) and (.25 <= w <= .5):
        size_tracked = 4
    elif (l + 2*w +2*h) <= 86:
        size_tracked = 5
    elif (l + 2*w +2*h) <= 130:
        size_tracked = 6
    else:
        size_tracked = 0
    return(size_tracked)


"""

Args: l (float), h (float), w (float), zip1 (int), zip2 (int)
Return: l (string), h (string), w (string), zip1 (string), zip2 (string)


description: attempts to convert to proper variable types and if not returns null values

"""
def data_conversion(l, h, w, zip1, zip2):
    try:
        return(float(l), float(w), float(h), int(zip1), int(zip2))
    except Exception:
        return 0, 0, 0, 0, 0
    
"""

Args: zip (int)
Return: int from 0-6


description: converts zip code into zone and returns null value if not possible

"""
def zone_counter(zip):
    if 1 <= zip <= 6999:
        return 1
    elif zip <= 19999:
        return 2
    elif zip <= 35999:
        return 3
    elif zip <= 62999:
        return 4
    elif zip <= 84999:
        return 5
    elif zip <= 99999:
        return 6
    else:
        return 0
    
"""

Args: dm (int), zd, (int)
Return: price (float)


description: takes dimensions (package type) and zone difference and calulates the price

"""

def money(dm, zd):
    parcel_price = [0, .2, .37, .37, .6, 2.95, 3.95]
    zone_price = [0, .03, .03, .04, .05, .25, .35]
    price = parcel_price[dm] + (zone_price[dm]*zd)
    return price



"""

Args: n/a
Return: prints formatting price


description: main function that calls all functions to return price from a string of values

"""
#main function
def main():
    while True:
        #takes in data and splits it up at the commas
        data = input("please insert data (Length, Height, Width, Origin_Zipcode, Destiation_Zipcode)")
        data = list(data)
        data_list = ["", "", "", "", "", ""]
        data_list_counter = 0
        for i in data:    #checking if an item is a comma if not add it to the data list
            if i == ",":
                if data_list_counter < 5:   #ensures that there are not more commans than nesecary
                    data_list_counter += 1
                pass
            else:
                data_list[data_list_counter] += i
        #removes any extra zeroes
        for i in range(len(data_list)):
            data_list[i] = data_list[i].strip()
        #converts the variables into their proper data classes
        l, h, w, zip1, zip2, = data_conversion(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4])
        

        #checks to see if the try accept failed or if the parcel does not conform to the packages list

        size_value = size_tracker(l, w, h)
        if any(not x for x in (l, h, w, zip1, zip2, size_value)) or data_list[5]:
            print("UNMAILABLE")
            continue
        
        #converts zip codes into zones
        zone1 = zone_counter(zip1)
        zone2 = zone_counter(zip2)

        #variable that is prepping to format money value correctly 
        #size trakcer takes the dimensions and returns a value representing the parcel size
        #takes the positive difference of the zones with absolute value
        #money function takes the 2 values and turns it into a value
        #then turns it into a float        
        correct_money = float(money(size_value, abs(zone1 - zone2)))

        #formats the float with 2 decimal points & removes the leading zeros at the start
        correct_money = f"{correct_money:.2f}".lstrip("0")

        print(correct_money)
        




main()
