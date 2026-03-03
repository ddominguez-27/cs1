"""
Shakespeare
Author: Daniel Dominguez
Date: 2/19/26
Sources: Mr. Campbell, assignment instruction, # Code: https://www.py4e.com/code3/count2.py
Description: Opens 2 files and writes data to excel, and graphs frequency, to run different file
Completed: 1-5
Log: 1.0

"""


import string
import matplotlib.pyplot as plt


def dictionary_analysis(fname, csvname):



    try:
        fhand = open(fname)
    except:
        print('File cannot be opened:', fname)
        exit()


    junk_words = [
        'the', 'and', 'to', 'of', 'a', 'i', 'you', 'my', 'in', 'that', 'it',
        'is', 'not', 'with', 'his', 'this', 'but', 'for', 'as', 'he', 'be',
        'on', 'by', 'or', 'we', 'do', 'so', 'me', 'your', 'have', 'are', 'o', 'all', 'our', 'if', 'at', 'thou'
    ]

    counts = dict()
    for line in fhand:
        line = line.rstrip()
        line = line.translate(line.maketrans("", "", string.punctuation))
        line = line.lower()
        words = line.split()
        for word in words:
            if word not in counts and word not in junk_words:
                counts[word] = 1
            else:
                if word not in junk_words:
                    counts[word] += 1

    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    print(sorted_counts)
    

    with open(csvname, 'w') as output:
        output.write("Word,Count\n")
        for word, count in sorted_counts.items():
            output.write(f"{word},{count}\n")        

    top_words = list(sorted_counts.keys())[:30]
    top_counts = list(sorted_counts.values())[:30]

    plt.figure(figsize=(12,6))
    plt.bar(top_words, top_counts)
    plt.xticks(rotation=45)
    plt.xlabel('Word')
    plt.ylabel('Count')
    plt.title('Top 30 Words by appearence')

    plt.show()



def main():

    dictionary_analysis("Hamlet.txt", 'Hamlet.csv')
    dictionary_analysis("ComedyofErrors.txt", 'Comedyoferrors.csv')

    

main()