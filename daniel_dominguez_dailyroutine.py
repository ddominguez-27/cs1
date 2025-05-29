def wrong(wrongcount):   
    if wrongcount == 0:
        print("wrong")
        wrongcount += 1
    elif wrongcount > 0 and wrongcount < 5:
        print("wrong again")
        wrongcount += 1
    elif wrongcount == 5:
        print("you are getting a lot of these wrong")
        wrongcount += 1
    else:
        print("wrong again... unsurprisingly")
    return wrongcount
def main():
    print("woken up")
    lateness = 0
    late = 0
    wrongcount = 0

    while True:
        while True:
            if lateness == 3:
                print("you are now running late...")
            elif lateness > 5:
                print("you are too late to make it to school")
                break
            sleep = str.lower(input("is it time to wake up? yes/no\n"))
            if sleep == "yes":
                print("get up")
                break
            elif sleep == "no":
                lateness += 1  
                print("sleepy time")
            else:
                wrongcount = wrong(wrongcount)
        if lateness > 5:
           break                
        while True:
            if lateness > 3:
                print("you are running late")
                print("take a quick shower")
                break
            elif lateness == 3:
                timesave = str.lower(input("would you like to take a quick shower to save some time? yes/no\n"))
                if timesave == "yes":
                    print("you took a quick shower and are no longer running late")
                    lateness -= 1
                    break
                elif timesave == "no":
                    print("you took a normal amount of time and are still running late")
                else:
                    wrongcount = wrong(wrongcount)
            elif lateness < 3:
                print("you took a normal amount of time to take a shower")

        print("eat breakfast")

        while True:
            eggs = str.lower(input("eggs? yes/no\n"))

            if eggs == "yes":
                print("you have eggs")
                break
            elif eggs == "no":
                print("you dont have eggs")
                break
            else:
                wrongcount = wrong(wrongcount)
        while True:
            comfy = str.lower(input("comfiest shoes? yes/no\n"))

            if comfy == "yes":
                print("you decide to wear the comfy shoes")
                break
            elif comfy == "no":
                print("you decide to wear the nicer shoes")
                break
            else:
                wrongcount = wrong(wrongcount)
        while True:
            if lateness >= 3:
                print("you are running late so you do not have time to pick matching socks with your shoes")
                break
            elif lateness < 3:
                while True:
                    socks = str.lower(input("do you want to find socks that match? yes/no\n"))
                    if socks == "yes":
                        print("you get socks that match")
                        break
                    elif socks == "no":
                        print("you dont get socks that match")
                        break
                    else:
                        wrongcount = wrong(wrongcount)
        print("you put shoes and socks on")
        print("you go to school")
        print(wrongcount)
main()
while True:
    again = str.lower(input("another day? yes/no\n"))
    if again == "yes":
        main()
    else:
        print("doesnt matter")
        main()



