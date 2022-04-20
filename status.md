# Status Report

#### Your name

Thomas Demianovich

#### Your section leader's name

Jemery Fan

#### Project title

Magic The Gathering EDH deck cost finder 

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

So far, I was able to create a function that puts together a url for the inputted card name for TCGplayer. This opens up to the general page for the certain card where all versions are shown.

#### What have you not done for your project yet?

I have not created a function the execute the pathway for the selected set, foil/non-foil, or promo which the market price can be selected. I also did not create the function that will store all of this information into a list that will be later used to calculated the sum price of the completed deck.

#### What problems, if any, have you encountered?

I have been having problem with creating the code for the pathway to navigate TCGplayer. I have been trying to use asyncio to access the website and to run concurrent code to gather all the information for each available option so when the user selects one of them, the name,price, and set can be stored. The pathway issue might be because of not having the proper access/ permission for the browser. I'm looking into different libraries to be used.
