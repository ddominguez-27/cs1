print("welcome")
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


def data_conversion(l, h, w, zip1, zip2):
    try:
        return(float(l), float(w), float(h), int(zip1), int(zip2))
    except Exception:
        return 0, 0, 0, 0, 0
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
        return 
def money(dm, zd):
    parcel_price = [0, .2, .37, .37, .6, 2.95, 3.95]
    zone_price = [0, .03, .03, .04, .05, .25, .35]
    price = parcel_price[dm] + (zone_price[dm]*zd)
    return price
def main():
    while True:
        data = input("please insert data (Length, Height, Width, Origin_Zipcode, Destiation_Zipcode)")
        data = list(data)
        data_list = ["", "", "", "", ""]
        data_list_counter = 0
        for i in data:
            if i == ",":
                data_list_counter += 1
                pass
            else:
                data_list[data_list_counter] += i
        for i in range(len(data_list)):
            data_list[i] = data_list[i].strip()
        print(data_list)
        l, h, w, zip1, zip2, = data_conversion(data_list[0], data_list[1], data_list[2], data_list[3], data_list[4])
        print(size_tracker(l, w, h))

        zone1 = zone_counter(zip1)
        zone2 = zone_counter(zip2)
        zone_dif = abs(zone1 - zone2)

        correct_money = money(size_tracker(l, w, h), zone_dif)
        
        correct_money = correct_money.lstrip('0')
        print(correct_money)
        




main()
