#pip install pyshorteners

import pyshorteners

url = input('enter the url: ')


def shortenurl(url):

    s = pyshorteners.Shortener()
    print("Short url: ")
    print(s.tinyurl.short(url))


shortenurl(url)