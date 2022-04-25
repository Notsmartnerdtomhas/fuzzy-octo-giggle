#Thomas Demianovich
#Python Final Project READme File


"""
Some challenges I faced while completing this project was that
I initially tried to use Pyppetteer and asyncio as the way to open up the web browser
and then to navigate throughout the web page to get the specific information i
needed. I kept on having problems with it that I saw selenium was an alternative option.
I began to learn how to navigate through websites by inspecting the web page and how they
stored information. Something I did not include in my code was if the card was foil or not
exluding promo's that were only printed in foil. I started to code this where once a magic set
was selected, it would open that specific version webpage, however, it started to get complicated
with the market price being nested into new lines where more pathways needed to be identified.
I felt that just pulling the card's market price off of the initial web page that had all of
versions listed was good enough as I try to stay away from foils as I had some warp pretty badly
became virtually unplayable. Another thing I didn't do in this project after a decklist was recorded
and overall price found, there wasn't a way 1) to refresh the page to get the updated prices and
2) create a function that allows card to be selected and then deleted/replaced. I do think I will try to
create these function over the summer as I found that my one budget deck (that when constructed cost roughly $75)
has doubled in price (to about $150) with some card now becoming more expensive. I also might try to modify
the code to be used for other magic formats like Modern where more than 1 copy of each card can be used.
To do this, I would add a extra input for quantity and then have that saved into the excel file as well.
This project taught me new functions in python and to learn more about the different modules that it
has access to, as well as using resources online to gain an understanding how these modules function.

"""
