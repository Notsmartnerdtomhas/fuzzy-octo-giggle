#Thomas Demianovich
#Python Final Project
#Magic the Gathering Price checker
import pyppeteer
import asyncio

def main():
    cardName = input("What is the magic Card?")

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
    asyncio.get_event_loop().run_until_complete(async_main(url))
main()


async def async_main(url): # <--- Define function
    browser = await launch(headless = True, executablePath = '/usr/bin/chromium-browser')
    page = await browser.newPage()

    await page.goto(url, timeout = 0)

    page_content = await page.content()

    print(page_content)

    await browser.close()


#Test url with Karador, Ghost Cheiftain
#https://www.scrapingbee.com/blog/pyppeteer/
