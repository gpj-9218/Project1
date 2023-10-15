import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

def get_latest_news():
    url = "https://www.python.org/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
   
    latest_news = []
   
    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        latest_news=[]

        for article in soup.select(".blog-widget li"):
            title=article.a.text.strip()
            latest_news.append(title)

        return latest_news
    else:
        print(f"Failed to retrieve Data. status_codes:{response.status_code}")
        return []

def count_words_and_frequency(news):
    words = []
    for article in news:
        text = re.sub(r'\W+', ' ', article)
        words.extend(text.lower().split())
    word_count = len(words)
    word_frequency = Counter(words)
    return word_count, word_frequency

def main():
    latest_news = get_latest_news()
    word_count, word_frequency = count_words_and_frequency(latest_news)
    print(f"Total words: {word_count}""\n")
    print(f"Word Frequency: {word_frequency}")

if __name__ == "__main__":
    python_articles = get_latest_news()

    if python_articles:
        print("Latest Articles in the Python section:")
        for index, article in enumerate(python_articles, 1):
            print(f"{index}.{article}")
    else:
        print("No atricle found")
    main()


