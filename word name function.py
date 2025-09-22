#flower pot


import random

def request_name():
    name = input("what is ur name \n ")

def reverse_string(name): #done
    reversed_string = ""
    list_name = list(name)
    while True:
        reversed_string += list_name[-1]
        list_name.pop()
        if list_name == []:
            break
    print(reversed_string)




def vowel_counter(name):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_counter = 0
    for i in name:
        if i in vowels:
            vowel_counter += 1
    print(vowel_counter)
def consonant_counter(name):
    vowels = ["a", "e", "i", "o", "u"]
    consonant_counter = 0
    for i in name:
        if i in vowels:
            continue
        consonant_counter += 1
    print(consonant_counter)
def vowel_tracker(name):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for ii in name:  
        if ii == "a":
            a += 1
        elif ii == "e":
            e += 1
        elif ii == "i":
            i += 1
        elif ii == "o":
            o += 1
        elif ii == "u":
            u += 1
        else:
            pass
    print(f"you have {a} a's, {e} e's, {i} i's, {o} o's, and {u} u's")




def string_lower(name):
    new_list = list(name)
    string_lowered = ""
    for i in range(len(new_list)):
        char = new_list[i]
        int_value = ord(char)
        if int_value < 91 and int_value > 64:
            int_value += 32
            char_2 = chr(int_value)
            string_lowered += char_2
        else:
            string_lowered += char
    print(string_lowered)


def string_upper(name):
    new_list = list(name)
    string_uppered = ""
    for i in range(len(new_list)):
        char = new_list[i]
        int_value = ord(char)
        if int_value > 97 and int_value <123:
            int_value -= 32
            char_2 = chr(int_value)
            string_uppered += char_2
        else:
            string_uppered += char
    print(string_uppered)

def return_name(name, place):
    list_string = list(name)
    next_word = ""
    split_list = []
    for i in list_string:
        if i == " ":
            split_list.append(next_word)
            next_word = ""
        else:
            next_word += i
    if next_word:
        split_list.append(next_word)
    middle_names = ""
    if place == 1:
        print(split_list[0])
    elif place == 2:
        print(split_list[-1])
    elif place == 3:
        for i in split_list[1:-1]:
            middle_names += f"{i} "
        print(middle_names)
    else:
        pass
def tf_hyphen(name):
    hyphen_check = False
    list_string = list(name)
    next_word = ""
    next_letter = ""
    split_list = []
    for i in list_string:
        if i == " ":
            split_list.append(next_word)
            next_word = ""
        else:
            next_word += i
    list_string = split_list
    for i in list_string[-1]:
        if i == "-":
            hyphen_check = True
    print(hyphen_check)
def tf_palindrome(name):
    list_string = list(name)
    next_word = ""
    split_list = []
    for i in list_string:
        if i == " ":
            split_list.append(next_word)
            next_word = ""
        else:
            next_word += i
    if next_word:
        split_list.append(next_word)
    first_name = split_list[0]
    if split_list[0] == first_name[::-1]:
        print(True)
    else:
        print(False)
def random_name(name):
    list_string = list(name)
    new_string = []
    joined_string = ""
    while list_string:
        random_int = random.randint(0, len(list_string))
        joined_string += list_string[random_int]
        list_string.remove(list_string[random_int])
    print(joined_string)
def initials(name):
    list_string = list(name)
    initials = ""
    initials += list_string[0]
    for i in range(len(list_string)):
        if list_string[i] == " " or list_string[i] == "-":
            initials += list_string[i+1]
    print(initials)

    






def main():
    while True:
        name = input("what is ur name (press enter to use last entered name)\n")
        
        if name == "":
            name = last_name_instance
        last_name_instance = name
        choice = input('''what would you like to do? (enter number)
1) Reverse your name
2) Turn your name lowercase
3) Turn your name uppercase
4) Return names at a specific location
5) Count the vowels in your name
6) Count the consonants in your name
7) Check for a hypen in your name
8) Check if your name is a palindrome
9) Randomize your name (fun!)
10) Get the initials of your name
11) Count the instances of each vowel''')
        if choice == "1":
            reverse_string(name) #done
        elif choice == "2":
            string_lower(name) #done
        elif choice == "3":
            string_upper(name) #done
        elif choice == "4":
            position_choice = input('''What would you like? (enter number)
1) Return only your first name
2) Return only your last name
3) Return all your middle names''')
            return_name(name, position_choice)
        elif choice == "5":
            vowel_counter(name)  #done
        elif choice == "6":
            consonant_counter(name)
        elif choice == "7":
            tf_hyphen(name)
        elif choice == "8":
            tf_palindrome(name)
        elif choice == "9":
            random_name(name) #done
        elif choice == "10":
            initials(name)
        elif choice == "11":
            vowel_tracker(name)
        else:
            pass
    


    


main()