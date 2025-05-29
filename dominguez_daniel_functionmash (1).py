#song

import random
import time
def chorus(ohs):
    '''
    Prints the chorus of a song, with the ability to include something at the start of the chorus
    Args:
        ohs (str)
    Returns:
        print: chorus (sometimes with something at the start)
        '''
    print(f"""
{ohs}Forgiving who you are, for what you stand to gain
Just know that if you hide, it doesn't go away
When you get out of bed, don't end up stranded
Horrified with each stone on the stage, my little dark age
""")




def sing_song():
    '''
    Prints the song
    Args:
        None
    Returns:
        print: song with chorus
        '''
    print("""
Breathing in the dark, lying on its side
The ruins of the day painted with a scar
And the more I straighten out, the less it wants to try
The feelings start to rot, one wink at a time

          """)
    chorus("Oh-Oh, ")
    print("""
Picking through the cards, knowing what's nearby
The carvings on the face say they find it hard
And the engine's failed again, all limits of disguise
The humor's not the same, coming from denial""")
    chorus("Oh-Oh, ")
    chorus("")
    print("""
Giddy with delight, seeing what's to come
The image of the dead, dead ends in my mind
Policemen swear to God, love seeping from their guns
I know my friends and I would probably turn and run
If you get out of bed, come find us heading for the bridge
Bring a stone, all the rage, my little dark age
          """)
    chorus("")
    print("All alone, open-eyed, burn the page, my little dark age")   #this was a kyle kelly song request



def add(num1, num2):
    '''
    Function description:

    Args:
        num1 (int): first num
        num2 (int): first num
    Returns:
        print: sum of num1 and num2
    '''
    print(num1 + num2)

def print_list(list1):

    '''
    Function description:
        prints a list out
    Args:
        list1 (list): a list
    Returns:
       print: list
    '''
    for i in list1:
        print(i)

def in_list(list1, item):
    '''
    Function description:
        check if element is in list
    Args:
        list1 (list): a list
        item (str): a word

    Returns:
        print boolean: true or false
    '''
    print(item in list1)

def is_integer(num):
    '''
    Function description:
        check if element is an integer
    Args:
        num (string): user input

    Returns:
        prints boolean: true or false
    '''
    if type(num) == float:
        return False
    try:
        num = int(num)
        return True
    except:
        return False

def get_integers():
    ''''
    Function description:
        gets 2 elements from the user and checks if they are integers
    Args:
        n/a
    Returns:
        return int: user_num & user_num2
    '''
    while True:

        user_num = input("pick a number please")
        user_num2 = input("pick another number please")
        
        if is_integer(user_num2) and is_integer(user_num):
            return int(user_num), int(user_num2)
def get_random():
    '''
    Function description:
        gets a random integer between two user ints
    Args:
        None
    Returns:
        print int: random integer
        '''
    a, b = get_integers()
    print(random.randint(a, b))





def count_vowels(item):
    '''
    Function description:
        counts how many vowels are in a string
    Args:
        item (string): user input
    Returns:
        print string: contains integer amount of vowels
        '''
    x = 0
    y_counter = 0
    list1 = list(item.lower())
    print(list1)
    for i in list1:
        if i in ["a", "u", "e", "i", "o"]:
            x += 1
        if i == "y":
             y_counter += 1
    print(f"Your input has {x} vowels.")  
    if y_counter > 0:
         print(f"Honorable mentions: you have {y_counter} 'y's ")
    return True

def get_initials(name):
    '''
    Function description:
        gets the initials of an input
    Args:
        name (string): user input
    Returns:
        print string: contains the initials of the input
        '''
    initial_list = []
    name_list = list(name.lower())
    initial_list.append(name_list[0])
    for i in range(len(name_list)):
         if name_list[i] == " ":
            initial_list.append(name_list[i+1])
    initial_list = "".join(initial_list)
    print(f"your initials are {initial_list.upper()}\n")

def reverse_string(item):
    '''
    Function description:
        reverses a string
    Args:
        item (string): user input
    Returns:
        print string: reversed string
        '''
    list1 = list(item)
    reversed_list = []
    for i in range(len(list1)):
        reversed_list.append(list1[(len(list1))-i-1])
    reversed_list = "".join(reversed_list)
    print(reversed_list)
def is_palindrome(item):
    '''
    Function description:
        checks if a string is a palindrome
    Args:
        item (string): user input
    Returns:
        print boolean: true or false
        '''
    list1 = list(item)
    reversed_list = []
    for i in range(len(list1)):
        reversed_list.append(list1[(len(list1))-i-1])
    reversed_list = "".join(reversed_list)
    print(item == reversed_list)
def main():
    '''
    Function description:
        main function that runs the program
    Args:
        n/a
    Returns:
        n/a
    '''
    apples = ["red oranges", "other oranges", "oranges"]

    while True:
            time.sleep(1)
            option = input('''
What would you like to do? 
1. Sing a song 
2. Add two numbers
3: Print a list
4: Check if an item is in a list
5: Check if a input is an integer
6. Gets 2 numbers from the user
7: Get a random number between two numbers
8: Count the vowels in a string
9: Get the initials of a name
10: Reverse a string
11: Check if an input is a palindrome
12: Exit
''')

            if option == '1':
                    sing_song()
            elif option == '2':
                add(get_integers())
            elif option == '3':
                print_list(apples)
            elif option == '4':
                in_list(apples, input("pick a word\n"))
            elif option == '5':
                print(is_integer(input("pick a number\n")))
            elif option == '6':
                get_integers()
            elif option == '7':
                get_random()
            elif option == '8':
                count_vowels(input("pick a word\n"))
            elif option == '9':
                get_initials(input("pick a name\n"))
            elif option == '10':
                reverse_string(input("pick a string to reverse\n"))
            elif option == '11':
                is_palindrome(input("pick a string to check if it is a palindrome\n"))
            elif option == '12':
                print("end bye")
                break
            else:
                print("try again please")

                 
main()


    


    