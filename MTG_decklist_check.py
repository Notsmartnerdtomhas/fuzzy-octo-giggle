#Thomas Demianovich
#Python Final Project
#Magic the Gathering Price checker

#from pyppeteer import launch 
#import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def main():
    cardName = 'Karador, Ghost Chieftain' #input("What is the magic Card?")

    #cardSet = input("What is the magic Card set?")
    #foil = input("Foil?")
    urlFront = "https://www.tcgplayer.com/search/all/product?q="
    urlEnd = "&view=grid"
    url = urlFront
    cardNameSplit = cardName.split()
    for section in cardNameSplit:
        url += section
        if section != cardNameSplit[-1]:
            url += "%20"
    url+= urlEnd
    print(url)
    setUp(url) #<--- cap sensitive
    #asyncio.get_event_loop().run_until_complete(async_main(url))

def setUp(url):
    browser = webdriver.Firefox(executable_path = 'C:/Users/demia/Downloads/geckodriver-v0.31.0-win64/geckodriver')

    browser.get(url)
    a = browser.find_element(By.CLASS_NAME,'search-result__subtitle')
    #'search-result__subtitle')
    parent = a.find_element_by_xpath('..')
    parent2 = parent.find_element_by_xpath('..')
    print(a.get_attribute('innerHTML')) #<-- only outputs one set
    print(parent2.get_attribute('href'))

    price = browser.find_element(By.CLASS_NAME,'price')
    browser.quit()
"""
async def async_main(url): # <--- Define function
    browser = await launch(headless = True)
    page = await browser.newPage()

    await page.goto(url, timeout = 0)

    page_content = await page.content()

    print(page_content)

    await browser.close()
"""
main()
#Test url with Karador, Ghost Chieftain
#https://www.scrapingbee.com/blog/pyppeteer/
