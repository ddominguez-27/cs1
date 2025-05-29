#password keeper


'''
Flowerpot:
Author: Daniel Dominguez
Description: A password keeper with a User interface that allows you to add, view, encrypt, and decrypt passwords for later use. made with love
Date: 5/28/25
Bugs: none if you follow the instructions... there are a couple fail safes, but I haven't tried everything.
I tried to make the user keyword without a global variable, but I didn't know how to use 'wrapper functions' so i had to use it
Sources:
a lot of the tkinter format is just adapted from the following sources:
https://www.tutorialspoint.com/printing-a-list-to-a-tkinter-text-widget
https://www.geeksforgeeks.org/python-gui-tkinter/
https://www.geeksforgeeks.org/python-tkinter-text-widget/
https://tkdocs.com/tutorial/text.html


'''




import tkinter as tk    #main part of my funtion

encryption_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ",", "<", ">", " ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", '"', "'", "/", "?", "~", ":", "\\", "}", "{"] #all characters that can be used in a url

user_keyword = "" #the one global variable i had to use



def show_instructions(text_box):
    '''
    Desc: Shows the instructions for how to use the password keeper
    Args: text_box: allows access to the text box
    Returns: nothing but updates the text box with instructions
    '''
    
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, "INSTRUCTIONS:\nTo add an entry, type in the text box in the format:\nwebsite username password (with a space seperating each of them)\nThen press the button\n\nTo view your entries, simply press the view my kept passwords button.\n\nTo set a 'keyword' (or password), just type it in and then press the button\n^^^ remember this before you terminate the program!!\n\nTo encrypt your entries, press the encrypt button. Then copy and paste it somewhere else to your liking\n\nTo decrypt your entries, paste the encrypted text into the text box and press the decrypt button\n\n crucial step!: have fun :D")
def print_lists(website_list, username_list, password_list, text_box, pwk_label_note):
    '''
    Desc: Prints the lists of websites, usernames, and passwords to the text box
    Args: 3 lists: website_list, username_list, password_list, text_box: to access the text box, pwk_label_note: to acess the label to update the label
    Returns: nothing but updates the text box with the lists
    '''
    text_box.delete(1.0, tk.END)
    for i in range(len(website_list)):
        text_box.insert(tk.END, f"Entry {i + 1}:\nWebsite: {website_list[i]}\nUsername: {username_list[i]}\nPassword: {password_list[i]}\n\n")
        pwk_label_note.config(text="Note: editing these will not change the information in file", fg="red")
def add_to_lists(website_list, username_list, password_list, text_box, pwk_label_note):
    '''
    Desc: adds an entry to the lists of websites, usernames, and passwords
    Args: 3 lists: website_list, username_list, password_list, text_box: to access the text box, pwk_label_note: to update the label
    Returns: nothing, but updates the lists and text box with the new entry
    '''
    user_input = text_box.get("1.0", tk.END).strip()
    entry = user_input.split()
    if len(entry) == 3:
        website_list.append(entry[0])
        username_list.append(entry[1])
        password_list.append(entry[2])
        pwk_label_note.config(text="Entry added! nice job :)", fg="green")
    else:
        pwk_label_note.config(text="wrong format :\ , please enter (with a space seperating them): website username password", fg="red")
    text_box.delete("1.0", tk.END)
def encrypt(website_list, username_list, password_list, text_box, pwk_label_note):
    '''
    Desc: first, compiles the lists into one string, then encrypts it using the keyword, and finally updates the text box with the encrypted string
    Args: 3 lists: website_list, username_list, password_list, text_box: to access the text box, pwk_label_note: to update the label, 
    Returns: nothing but updates the text box with the encrypted string for the user to copy
    '''
    global user_keyword
    if user_keyword == "":
        pwk_label_note.config(text="no keyword set!", fg="red")
        return
    if len(website_list) == 0:
        pwk_label_note.config(text="nothing to encrypt yet!", fg="red")
    else:
        combined = combine_lists(website_list, username_list, password_list)
        encrypted = encryption(True, combined, user_keyword)
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, encrypted)
        pwk_label_note.config(text="encrypted and ready to copy", fg="green")
def decrypt(website_list, username_list, password_list, text_box, pwk_label_note):
    '''
    Desc: Decrypts the text in the text box using the keyword, and then splits it back into the 3 lists, and updates the file
    Args: 3 lists: website_list, username_list, password_list, text_box: to access the text box, pwk_label_note: to update the label, 
    Returns: nothing but updates the lists and text box wtith lists
    '''
    global user_keyword

    encrypted_text = text_box.get("1.0", tk.END).strip()
    if user_keyword == "":
        pwk_label_note.config(text="no keyword set!", fg="red")
        return
    if encrypted_text == "":
        pwk_label_note.config(text="please paste something to decrypt", fg="red")
        return
    decrypted = encryption(False, encrypted_text, user_keyword)
    website_list_temp, username_list_temp, password_list_temp = split_combined_string(decrypted)
    for i in range(len(website_list_temp)):
        website_list.append(website_list_temp[i])
        username_list.append(username_list_temp[i])
        password_list.append(password_list_temp[i])
    pwk_label_note.config(text="done decrypting and put in file!", fg="green")
    text_box.delete("1.0", tk.END)


def set_keyword(text_box, pwk_label_note):
    '''
    Desc: Sets the keyword for encryption and decryption
    Args: text box: to acess textbox, pwk_label_note: same as text box, 
    Returns:
    '''
    global user_keyword
    keyword = text_box.get("1.0", tk.END).strip()
    if keyword == "":
        pwk_label_note.config(text="cant use that (lack of) keyword !", fg="red")
    else:
        user_keyword = keyword
        pwk_label_note.config(text="keyword set! another great job :)", fg="green")
        text_box.delete("1.0", tk.END)
    return user_keyword








def encryption(encrypter, user_word, keyword):
    '''
    Desc: can encrypt or decrypt a string based on the keyword 
    Args: encrypter: true or false to determine whether it encrpyts or decrpyts, user_word: the string to be en or decrypted, keyword: the keyword to use for cryptions
    Returns: string: the en or decrypted string
    '''
    keyshift = list(keyword)
    for i in range(len(keyshift)):
        keyshift[i] = encryption_list.index(keyshift[i]) + 1
    list_counter = 0
    user_list = list(user_word)
    new_list = []
    for i in user_list:
        if i == "万" or i == "乘":   #skips over these characters, and just passes them through, so that they can be identified, and not break the functoin
            new_list.append(i)
            continue
        if encrypter:     
            encrypt_index = encryption_list.index(i)+keyshift[list_counter]  #this one and the next one shift and unshift the string according to the keyshift on the encryption list
            if encrypt_index >= len(encryption_list):
                encrypt_index -= len(encryption_list)
        else:
            encrypt_index = encryption_list.index(i)-keyshift[list_counter]
            if encrypt_index < 0:
                encrypt_index += len(encryption_list)
        list_counter += 1
        if list_counter >= len(keyshift):  #fixes the index based on whether it is encrypting or decrypting and prevents it from breaking, resetting the loop properly
            list_counter = 0
        new_list.append(encryption_list[encrypt_index])
    new_string = "".join(new_list)
    return new_string


def combine_lists(website_list, username_list, password_list):
    '''
    Desc: Combines the 3 lists into one string- I used 2 random chinese charavters unlikely to be used by the user - i guess this is a source of error
    Args: 3 lists: website_list, username_list, password_list
    Returns: string: 1 combined string
    '''
    combined_list = ""
    for i in range(len(website_list)):
        combined_list += website_list[i] + "万" + username_list[i] + "万" + password_list[i] + "乘"   #differenciate the items in the lsit and then the end of the list to make parralel arrays
    return combined_list




def split_combined_string(combined_string):
    '''
    Desc: Splits the combined string back into  3 lists
    Args: combined_string: a string that has been combined with the combine_lists function
    Returns: original 3 lists: website_list, username_list, password_list
    '''
    website_list = []
    username_list = []
    password_list = []
    comb_entries = combined_string.split("乘")
    for i in comb_entries:
        comb_parts = i.split("万")
        if len(comb_parts) == 3:
            website_list.append(comb_parts[0])
            username_list.append(comb_parts[1])
            password_list.append(comb_parts[2])
    return website_list, username_list, password_list




def main():
    '''
    Desc: Main function to run the whole password keeper, main gui component
    Args: none
    Returns: none
    '''

    website_list = []
    username_list = []
    password_list = []
    root = tk.Tk()    #creates the main window
    root.title("Password Keeper!!")
    root.geometry("1100x800+150+50")
    pwk_label_title1 = tk.Label(root, text="welcome, to", font=("Comic Sans MS", 20))    #lots of tedious labels and boxes...
    pwk_label_title1.pack(pady=3)
    pwk_label_title2 = tk.Label(root, text="PASSWORD KEEPER!!!", font=("Impact", 70))
    pwk_label_title2.pack(pady=3)
    pwk_label_desc = tk.Label(root, text="what would you like to do?", font=("Comic Sans MS", 15))
    pwk_label_desc.pack(pady=10)
    instructions_button = tk.Button(root, text="press for instructions", font=("Georgia", 12), command=lambda: show_instructions(text_box))
    instructions_button.pack(pady=5)
    add_button = tk.Button(root, text="Add an entry!!", command=lambda: add_to_lists(website_list, username_list, password_list, text_box, pwk_label_note))
    add_button.pack(pady=5)
    view_button = tk.Button(root, text="View my kept passwords!!", command=lambda: print_lists(website_list, username_list, password_list, text_box, pwk_label_note))
    view_button.pack(pady=5)
    set_keyword_button = tk.Button(root, text="Set Keyword", command=lambda: set_keyword(text_box, pwk_label_note))
    set_keyword_button.pack(pady=5)
    encrypt_button = tk.Button(root, text="Encrypt", command=lambda: encrypt(website_list, username_list, password_list, text_box, pwk_label_note))
    encrypt_button.pack(pady=5)
    decrypt_button = tk.Button(root, text="Decrypt", command=lambda: decrypt(website_list, username_list, password_list, text_box, pwk_label_note))
    decrypt_button.pack(pady=5)
    pwk_label_note = tk.Label(root, text="This is the text box, where all the magic (will) happen", font=("Comic Sans MS", 12), fg="gray")
    pwk_label_note.pack(pady=2)
    text_box = tk.Text(root, height=10, width=60, font=("Arial", 12))
    text_box.pack(pady=2)
    exit_button = tk.Button(root, text="TERMINATE PROGRAM", command=root.destroy, font=("Comic Sans MS", 12), fg="red")
    exit_button.pack(pady=5)
    pwk_label_note2 = tk.Label(root, text="(button above NOT reccomended! password keeper is AWESOME!!!!!!!)", font=("Comic Sans MS", 12), fg="gray")
    pwk_label_note2.pack(pady=2)
    root.mainloop()




main()





