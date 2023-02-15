import requests
import os
import datetime
from bs4 import BeautifulSoup

PT_ID = 0
PT_CLASS = 1

def getElementByID(session, URL, id):
    page = session.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find(id=id)


def getElementByClass(session, URL, elemClass):
    page = session.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find_all(class_=elemClass)


def getElements(session, URL, ptype, id):
    if ptype == PT_ID:
        return getElementByID(session, URL, id)
    elif ptype == PT_CLASS:
        return getElementByClass(session, URL, id)


def processResult(result):
    title = result.find('div', class_='alacarte__text-wrapper')
    link = result.find('a')['href']
    return (title.text.strip(), link)


with requests.Session() as session:
    results = getElements(session, "https://www.nbcnews.com/", PT_CLASS, "alacarte")
    articleData = map(processResult, results)
    for title, link in articleData:
        print(title)
        print(link, '\n')
