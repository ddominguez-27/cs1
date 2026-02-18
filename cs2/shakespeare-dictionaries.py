import string

import pandas as pd
import plotly.express as px


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()


junk_words = [
    'the', 'and', 'to', 'of', 'a', 'i', 'you', 'my', 'in', 'that', 'it',
    'is', 'not', 'with', 'his', 'this', 'but', 'for', 'as', 'he', 'be',
    'on', 'by', 'or', 'we', 'do', 'so', 'me', 'your', 'have', 'will'
]

counts = dict()
for line in fhand:
    line = line.rstrip()
    # First two parameters are empty strings
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

df = pd.DataFrame(list(counts.items()), columns=['Word', 'Count'])
df = df.sort_values(by='Count', ascending=False)
# clearing junk words:


print(sorted_counts)
fig = px.bar(df.head(30), x='Word', y='Count', title='Top 30 Word Counts')
fig.show()