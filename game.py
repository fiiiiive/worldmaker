'''
    4/26: Okayy so because this is the first time editing this, heres what I had in mind: main/start method to fetch the json file of the character and initialize all the variables. 
Then we have another character.menu()/character.edit() sort of menu with options like gold* , skills menu**, HP, and personality stats*** (charisma, 
persuasion, etc.). HP, gold, maybe personality can be shown on menu. Can prob do a stylized text-based menu for now but hopefully make the leap to 
actual webpage. 

* (side note, it could be pretty cool to add a sort of memo system, like a check book to look at the last n transactions)
** (another side note, since some abilities are daily, we could have a day counter and 
a sort of cooldown mechanic. Doesn't have to disable skills just needs to put up message that it was used.could make a "day" button to signify the new day
and "refresh" the cds.) 
*** These need to be added to the json through the character.edit() on the first time around. Use a dictionary and have prewritten attributes (option to add custom
ones is a maybe at this point)
'''
def refresh():
    # ^name subject to change. Functions are to: open {name}.json, use the parts of the json to grab certain variables 
    
