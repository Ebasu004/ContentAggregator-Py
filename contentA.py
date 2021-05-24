import requests
import os
import datetime
from bs4 import BeautifulSoup

PT_ID = 0
PT_CLASS = 1


def getElementByID(URL, id):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find(id=id)


def getElementByClass(URL, elemClass):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find(class_=elemClass)


def getElements(URL, ptype, id):
    """
    Return a list of elements that match a certain criteria.

    URL: String containing the url.
    ptype: ---
    ids: ---

    Return: List containing elements found, or None if no elements are found.
    """
    if ptype == PT_ID:
        return getElementByID(URL, id)
    elif ptype == PT_CLASS:
        return getElementByClass(URL, id)


for results in getElements("https://www.nbcnews.com/", PT_CLASS, "alacarte"):
    title = results.find('div', class_='alacarte__text-wrapper')
    link = results.find('a')['href']

    print(title.text.strip())
    print(link, '\n')

# ---------------------------------------------------------------------------------
# URL = 'https://www.nbcnews.com/'
# page = requests.get(URL)

# soup = BeautifulSoup(page.content, 'html.parser')

# results = soup.find(class_='alacarte')

# for top in results:
#     desc = top.find('div', class_='alacarte__text-wrapper')
#     link = top.find('a')['href']

#     print(desc.text.strip())
#     print(link,'\n')

# ---------------------------------------------------------------------------------
