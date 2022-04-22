#Thomas Demianovich
#Python Final Project
#Magic the Gathering Price checker

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv
import time

browser = webdriver.Firefox(executable_path = 'C:/Users/demia/Downloads/geckodriver-v0.31.0-win64/geckodriver')



def main():
    Sum_cost = 0
    cardName = input("What is the magic Card?")

    #cardSet = input("What is the magic Card set?")
    #foil = input("Foil?")
    urlFront = "https://www.tcgplayer.com/search/magic/product?q="
    urlEnd = "&view=grid"
    url = urlFront
    cardNameSplit = cardName.split()
    for section in cardNameSplit:
        url += section
        if section != cardNameSplit[-1]:
            url += "%20"
    url+= urlEnd
    #print(url)
    
    info = setUp(url) #<--- cap sensitive

    file = open(cardNameSplit[0].replace(",","")+".csv",'w',newline = "")
    row = ['Card Name', 'Set', 'Market Price']
    writer = csv.writer(file)
    writer.writerow(row)
    writer.writerow([cardName,info[0],info[1]])
    Sum_cost+= float(info[1].replace("$",""))
    #print(Sum_cost)
    
    while True:
        NextCard = input("What is the magic Card or enter 'quit' to stop?")
        if NextCard == 'quit':
            break
        url = urlFront
        NextCardSplit = NextCard.split()
        for section in NextCardSplit:
            url += section
            if section != NextCardSplit[-1]:
                url += "%20"
        url+= urlEnd
        
        time.sleep(1/10) #<-- 1/10 of a second delay
        #print(url)
        info = setUp(url) #<--- cap sensitive

        file = open(cardNameSplit[0].replace(",","")+".csv",'a',newline = "")
        writer = csv.writer(file)
        writer.writerow([NextCard,info[0],info[1]])
        Sum_cost+= float(info[1].replace("$",""))
    print('Total Cost',"$"+str(Sum_cost))
    writer.writerow([None])
    writer.writerow(['Total',None,"$"+str(Sum_cost)])



    browser.quit()
    

def setUp(url):
    
    #time.sleep(1/10) #<-- 1/10 of a second delay
    #print(url)
    browser.get(url)
    time.sleep(2)
    #a = browser.find_element(By.CLASS_NAME, 'search-results')
    a = browser.find_elements_by_css_selector('span.search-result__subtitle')
    #print(a.find_element_by_xpath(".//*").get_attribute('innerHTML'))
    #print(a)

    number = 0
    for subtitle in a:
        magic_set = subtitle.get_attribute('innerHTML')
        number +=1
        print(number, magic_set)

    
    b = browser.find_elements_by_css_selector('span.search-result__market-price--value')
    for price in b:
        card_price = price.get_attribute('innerHTML')
        #print(card_price)
        
    card_set = int(input('Enter card set from listed options/ associated number'))
    print(b[card_set-1].get_attribute('innerHTML'))
    
    
    return [a[card_set-1].get_attribute('innerHTML'),b[card_set-1].get_attribute('innerHTML')]
   

main()


