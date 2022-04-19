import os

# Write abilities to characters file
def ablts(name):
    os.system("clear")
    f = open(f"{name}.txt", "a")
    
    ability = input("What is the ability's name? (Enter \'0\' to exit): ")
    ability = ability.capitalize()
    while ability != '0':
        description = input("What does the ability do? ")
        description = description.capitalize()
        f.write(f"\n*******************************\n{ability}:\n{description}\n\n")
        
        ability = input("What is the ability's name? (Enter \'0\' to exit): ")
        ability = ability.capitalize()
    
    f.close()

# Help Menu print
def assist(page, name):
    os.system("clear")
    # print assist menu for separate pages. Each section of code will call its version of the menu
    # main menu. Added name parameter so that you can return to charac() instead of having to go all the way back to menu()
    print("Character creator is a way for you to make your own DND character and keep track of attributes, abilities, and other in game information.\n")
    if page == "menu":
        print(page.upper())
        print("From the main menu you can use a list of commands such as:\n\n" +
            "    * \'character\': Create, edit, or play a campaign with existing characters. \n\n" +
            "    * \'delete\': Delete existing characters.\n\n" +
            # add other commands here
            "    * \'exit\': Exit the program.")
            menu()
    elif page == "character":
        print(page.upper())
        print("The Character page is a way for you to interact with your DND characters with commands like:\n\n" +
            "    * \'play\': Open the in-game menu to play a campaign\n\n" +
            "    * \'abilities\': Add or delete abilities from your character\n\n" +
            "    * \'see\': Open your character's profile and see their description\n\n" +
            "    * \'back\': Go back to the main menu to select a different character or exit.")
        input("\n**********************************************************************************************************\nPress ENTER to return to the main menu")
        charac()

# Edit characters 
def charac(name):
    # charac() code is old main() code for character
    # open any existing file or make new character if file does not exist
    try:
        f = open(f"{name}.txt", "r")
        print(f"{name} found")
        f.close()
    except:
        print(f"Creating {name}...")
        age = int(input(f"\nWhat is {name}'s age? "))
    
        race = input(f"\nWhat is {name}'s race? ")
        race = race.capitalize()
    
        cls = input(f"\nWhat is {name}'s class? ")
        cls = cls.capitalize()
    
        f = open(f"{name}.txt", "w")
    
        f.write(f"{name}\n******************************\n")
        f.write(f"Age: {age}\n")
        f.write(f"Race: {race}\n")
        f.write(f"Class: {cls}")
        f.write(f"\n******************************\nAbilities for {name}:\n")
        f.close()
    
    finally:
        choice = input(f"\nWhat would you like to do with {name}? ")
        choice = choice.lower()
    
        while choice != "back":
            # choices here. I'm thinking like 
            # 'play': open an in-game menu where they can use character in real time 
            # 'abilities': add or get rid of abilities
            # 'see': reads player file and displays information
            # 'assist': displays these commands for new users
            # 'back': while loop above obviously gates this but its still want it to be an option 
            if choice == "play":
                # game(name) below probably will fall under another file
                break
            elif choice == "abilities":
                ablts(name)
                charac(name)
            elif choice == 'see':
                # Above code already confirms that the file exists. reading it 
                f = open(f"{name}.txt", "r")
                print(f.read())
                input("Press ENTER to return")
                charac(name)
            elif choice == 'assist':
                assist("charac", name)
            else:
                choice = input("Invalid choice. Enter your command or enter \'assist\' for more options ")
                
        # After typing 'back' go to the menu
        menu()

def delete(name):
    os.system("clear")
    os.remove(f"{name}.txt")
    print(f"{name} has been deleted")
    main()

# menu() code main function of the code
def menu():
    os.system("clear")
    cmd = input("What would you like to do today? \nEnter \'assist\' for more options.\n")
    cmd = cmd.lower()
    while cmd != "exit":
        if cmd == "charac":
            # charac() code is old main() code
            # handles character creation and editing
            # code from charac() moved here to avoid redundancy when charac() is called multiple times
            
            name = input("What is the name of your character? ")
            name = name.capitalize()
            charac(name)
        
        elif cmd == "assist":
            # assist() call here
            assist("menu", "fiiiiive")
        elif cmd == "delete":
            name = input("What character would you like to delete? ")
            if os.path.exists(f"{name}.txt"):
                delete(name)
            else:
                print("This file does not exist")
        else:
            # handle unknown commands
            cmd = input(f"Unknown command \'{cmd}\'.\nPlease enter a command or use \'assist\' for a list of commands")
    
    exit()
def main():
    
    # I don't want the user to constantly be welcomed every time they finish 
    # creating/editing/deleting so I wanted to add this to keep to one time 
    # only. Menu() is the main code that I want to be looping through for continued use. 
    
    print("**************************************************\n\n" + 
        "          Welcome to Character Creator!\n\n" +
        "**************************************************\n")
    menu()
    
# Driver
if __name__ == "__main__":
    main()
