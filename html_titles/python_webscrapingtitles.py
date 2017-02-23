'''Web Scraping: Page Titles'''
__author__ = 'MorandoNicolo'


# -- IMPORT

import urllib.request as u
import re as r


# -- VARIABILI

booldebug = True
f = open('titles.txt', 'w')
regex = '<title>(.+?)</title>'
urls = ("https://www.google.it/", "http://www.repubblica.it/")
pattern = r.compile(regex)


# -- FUNZIONI

def web_scraping(regex, urls, pattern, f):
    
    for cont in range(len(urls)):
        htmlfile = u.urlopen(urls[cont])
        htmltext = htmlfile.read()
        title = pattern.findall(str(htmltext))
        if booldebug:
            print((title))
        f.write(str(title))
        f.write('\n')
    f.close()
        
    
# -- ELABORAZIONE

if __name__ == '__main__':
    
    web_scraping(regex, urls, pattern, f)

