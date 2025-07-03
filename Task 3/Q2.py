""" Create a Python script that reads a text file and counts the frequency 
    of each word. Use a dictionary to store the word counts and display 
    the top 10 most frequent words. """

# Steps to perform:
# 1. First read a text file.
# 2. Counts every word and store the values against every word.
# 3. Dictionary will be used to store word counts.
# 4. Display 10 most frequent words.

from collections import Counter
import string

def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.lower().translate(translator)

def count_words(text):
    words = text.split()
    return Counter(words)

def display_top_10(word_counts):
    top_words = word_counts.most_common(10)
    print("Top 10 most frequent words:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    filename = "textfile.txt"
    text = read_file(filename)
    cleaned = clean_text(text)
    word_counts = count_words(cleaned)
    display_top_10(word_counts)

