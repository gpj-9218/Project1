import re
from collections import Counter

def count_word_frequency(file_path):
    with open(file_path, 'r') as file:
        data = file.read().lower()

    words = re.findall(r'\b\w+\b', data)
    word_count = Counter(words)

    return word_count

if __name__ == "__main__":
    file_path = "D:\\Next Hike\\data_scrapeddata.txt"
    word_frequency = count_word_frequency(file_path)

    for word, frequency in word_frequency.items():
        print(f"{word}: {frequency}")

