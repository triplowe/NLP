import matplotlib.pyplot as plt
from operator import itemgetter
from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd

# nltk.download("stopwords")

from nltk.corpus import stopwords

stops = stopwords.words("english")

print(stops)

blob = TextBlob("Today is a beautiful day.")

print(blob.words)


#expression, iteration, condition
# is the word in the list of word stops "is a" are stop words
cleanlist = [word for word in blob.words if word not in stops]

print(cleanlist)


blob = TextBlob(Path("RomeoandJuliet.txt").read_text())

print(blob.words.count("joy"))

print(blob.word_counts["juliet"])

#print(blob.noun_phrases.count("lady capulet"))

print(blob.words.count("thou"))


# add stop words
more_stops = ["thee", "thou", "thy"]

stops += more_stops

items = blob.word_counts.items()

# print(items)


# for i in items goes through each word and if the word is not in our list of stop words it makes it into the list
clean_items = [i for i in items if i[0] not in stops]


# printing first 10
print(clean_items[:10])
# this allows us to choose an element in the item to grab

# reverse=True is descending order
sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True)

# this sorts it alphabeticallly
print(sorted_list[:10])

# want to stop top 20 words that appear the most
top20 = sorted_list[:20]

df = pd.DataFrame(top20, columns=["word", "count"])

print(df)


df.plot.bar(x="word", y="count", legend=False,
            color=["y", "c", "m", "b", "g", "r"])

plt.gcf().tight_layout()

plt.show()
