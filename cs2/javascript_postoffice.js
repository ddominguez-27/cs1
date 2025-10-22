


//checks the values && assigns a number to it
function size_tracker(l, h, w) {
    let size_tracked = 0
    switch (l, h, w) {
    case (3.5 <= l <= 4.25) && (3.5 <= h <= 6) && (.007 <= w <= .016):
        size_tracked = 1;
        break;
    case (4.25 <= l <= 6) && (6 <= h <= 11.5) && (.007 <= w <= .016):
        size_tracked = 2;
        break;
    case (3.5 <= l <= 6.125) && (5 <= h <= 11.5) && (.016 <= w <= .25):
        size_tracked = 3;
        break;
    case (6.125 <= l <= 24) && (11 <= h <= 18) && (.25 <= w <= .5):
        size_tracked = 4;
        break;
    case (l + 2*w +2*h) <= 86:
        size_tracked = 5;
        break;
    case (l + 2*w +2*h) <= 130:
        size_tracked = 6;
        break;
    default:
        size_tracked = 0;
    return(size_tracked)
    }}


//attempts data conversion && if not returns empty values
function data_conversion(l, h, w, zip1, zip2) {
    try {
        return(Number(l), Number(w), Number(h), Number(zip1), Number(zip2));
     } catch(err) {
        return 0, 0, 0, 0, 0
    }}

//returns a zone value from a zip value
function zone_counter(zip) {
    switch(zip) {
    case 1 <= zip <= 6999:
        return 1
    case zip <= 19999:
        return 2
    case zip <= 35999:
        return 3
    case zip <= 62999:
        return 4
    case zip <= 84999:
        return 5
    case zip <= 99999:
        return 6
    default:
        return 0
    }}
    
//takes in dimensions && zone different && returns a monetary value
function money(dm, zd):
    parcel_price = [0, .2, .37, .37, .6, 2.95, 3.95]
    zone_price = [0, .03, .03, .04, .05, .25, .35]
    price = parcel_price[dm] + (zone_price[dm]*zd)
    return price

//main function
function main():
    while True:
        //takes in data && splits it up at the commas
        data = input("please insert data (Length, Height, Width, Origin_Zipcode, Destiation_Zipcode)")
        data = list(data)
        data_list = ["", "", "", "", "", ""]
        data_list_counter = 0
        for i in data:    #checking if an item is a comma if not add it to the data list
            if i == ",":
                if data_list_counter < 5:   #ensures that
                    data_list_counter += 1
                pass
            else:
                data_list[data_list_counter] += i
        //removes any extra zeroes
        for i in range(len(data_list)):
            data_list[i] = data_list[i].strip()
        
        //converts the variables into their proper data classes
        l, h, w, zip1, zip2, = data_conversion(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4])

        //checks to see if the try accept failed or if the parcel does not conform to the packages list

        size_value = size_tracker(l, w, h)
        if ((l or h or w or zip1 or zip2 or size_value) == 0) or data_list[5]:
            print("Input does not conform to possible values")
            continue

        //converts zip codes into zones
        zone1 = zone_counter(zip1)
        zone2 = zone_counter(zip2)

        //variable that is prepping to format correctly- 
        //size trakcer takes the dimensions && returns a value representing the parcel size
        //takes the positive difference of the zones with absolute value
        //money function takes the 2 values && turns it into a value
        //then turns it into a float        
        correct_money = float(money(size_value, abs(zone1 - zone2)))

        //formats the float with 2 decimal points
        correct_money = f"{correct_money:.2f}"
        //removes the first zero
        correct_money = correct_money.lstrip("0")

        print(correct_money)
        return(correct_money)
        




main()
