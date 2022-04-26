'''
    4/26: Okayy so because this is the first time editing this, heres what I had in mind: main/start method to fetch the json file of the character and initialize all the variables. 
Then we have another character.menu()/character.edit() sort of menu with options like gold* , skills menu**, HP, and personality stats*** (charisma, 
persuasion, etc.)****. HP, gold, maybe personality can be shown on menu. Can prob do a stylized text-based menu for now but hopefully make the leap to 
actual webpage. 

* (side note, it could be pretty cool to add a sort of memo system, like a check book to look at the last n transactions)
** (another side note, since some abilities are daily, we could have a day counter and 
a sort of cooldown mechanic. Doesn't have to disable skills just needs to put up message that it was used.could make a "day" button to signify the new day
and "refresh" the cds.) 
*** These need to be added to the json through the character.edit() on the first time around. Use a dictionary and have prewritten attributes (option to add custom
ones is a maybe at this point)
**** note: after further investigation with how to python reads jsons and how I can get them to read what I want, I think I want to just call a bunch of get() 
functions for attributes/gold/hp/skills list. 
'''
def refresh():
    # ^name subject to change. Functions are to: open {name}.json, read json materials and collect input to call other methods. Did some testing,
    # saving my work on onlineGDB in case I need to refer back. Can pass lists of dicts as arguments through methods. Very helpful
    
def getHP():
    # should be easy as HP is a standalone attribute
    
def getPersona():
    # should be called with the dict of the json that is for personality. prints personality list
    
def getSkillList():
    # called with the dict of json for skills debating whether or not to just make it for one skill or not. prints skill list
    
def getGold():
    #similar to HP should be easy as it is standalone. 
