import requests
import bs4

def request_one():
    result = requests.get("https://quotes.toscrape.com/")

    soup = bs4.BeautifulSoup(result.text, "lxml")
    for quote in soup.select('.web'):
        (quote.getText())

    for author in soup.select('.author'):
        print(author.getText())

    for tag in soup.select('.tag'):
        print(tag.getText())

def request_two():
    authors = []
    for page in range(0,10):
        result = requests.get("http://quotes.toscrape.com/page/{}/".format(page))
        soup = bs4.BeautifulSoup(result.text, "lxml")
        for un_author in soup.select('.author'):
            authors.append(un_author.getText())

        

    ali = set(authors)
    print(ali)

request_one()

request_two()