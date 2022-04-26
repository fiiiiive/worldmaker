# worldmaker
A way for GMs and players to keep track of characters in DND

Hello! My name is fiiiiive and I am trying to teach myself Python right now. My family and I have a pretty decent DND campaign going 
and I thought it would be fun to code something to help my cousin, the GM, keep track of his notes, as well as a way for us players 
to cut back on paper a bit too.

By the end I want this project to have the following:

*For GM:*

- Ability to create an Object called World that holds Regions, Landmarks, Enemies, and Notable Figures
- Ability to create backstories/descriptions for Worlds, Regions, and Landmarks
- Ability to have separate lists of enemies and notable figures that they can write to include backstories, stats, abilities, etc.
- Ability to have lists of flora and fauna for said regions and landmarks
- Ability to save the above Worlds
- Ability to write a backup/save progress from a session (write out the summary of the session and save it so next time can open. 
- Ability to make all of the above optional. Should a place be barren of landmarks, flora, characters, etc. GMs should have the option to make it so
- Finally, the ability to quickly access all of the above quickly. If the party is fighting a R.O.U.S. in Mordor, the GM should be able to open up a page on that enemy and place so they can accurately depict the story

*For players:*

- Ability to create multiple characters (for multiple campaigns)
- Ability to give characters backstories, stats, currency, and gear
- Ability to open one and keep it open for the duration of the campaign 
- Ability to make adjustments to everything in real time, so that players can utilize the program while playing
- Ability to write notes during the game. If important information is said, players should have the option to write it down
- Ability to access all of their gear, currency, stats page, etc. quickly and efficiently
- Ability to save all of the above in order to come back for multiple sessions

## Goals I hope to implement one day:

Some of these are more ambitious than others, but these are just other features I think would be nice but are definitely not what I deem necessary (yet):

- Calendars for Worlds (Holidays, maybe even lunar cycles, etc.)
- Ability for GMs and players to get the same map. For now, my workaround is the notes page for players so that they can do the work themselves, but in the future I would love for players to be able to read the map the GM made for themselves
- Ability for GMs and players to interact in real time
- If I come up with more ideas they will be added here
## Updates:
It is currently 4/26 when I am starting this, about a month or so into this project, but this is a way for me to log what I am thinking about, problems I am trying to overcome, new things I found out/learned, etc.
- Before 4/26: Wrote out World.py but still debated using objects for it, decided to work on character.py. Got a mostly functional character.py, still thinking of ways to improve it. Improvements over the month have included: learning JSON and changing ".txt" files I was writing in, to .json's so I can read/access attributes, abilities, etc faster
- 4/26: Started this blog, thinking of making this its own thing separate of README. Created the game.py file and wrote out what I hope for that part of the project. Looked back at world.py, thinking I might go the same route as character and use JSON instead of python objects. Assuming I port it to a website in JavaScript that'll probably make it easier.
