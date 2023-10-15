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

if __name__ == "__main__":
    python_articles = get_latest_news()

    if python_articles:
        print("Latest Articles in the Python section:")
        for index, article in enumerate(python_articles, 1):
            print(f"{index}.{article}")
    else:
        print("No atricle found")
    #main()