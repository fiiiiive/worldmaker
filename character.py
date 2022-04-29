import os
import json

# Write abilities to characters file
# using JSON for characters now 
def ablts(name):
    os.system("cls")
    x = dict()
    y = list()
    ability = input("What is the ability's name? (Enter \'0\' to exit): ")
    ability = ability.capitalize()
    while ability != '0':
        description = input("What does the ability do? ")
        description = description.capitalize()
        x[ability] = description
        ability = input("What is the ability's name? (Enter \'0\' to exit): ")
        ability = ability.capitalize()
    y.append(x)
    z = json.dumps(y)
    with open(f"{name}.json", "a") as outfile:
        json.dump(z, outfile)

# Help Menu print
def assist(page, name):
    os.system("cls")
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
        input("\n**********************************************************************************************************\nPress ENTER to return to the main menu ")
        os.system("cls")
        menu()
    elif page == "character":
        print(page.upper())
        print("The Character page is a way for you to interact with your DND characters with commands like:\n\n")
        print(f"    * \'play\': Open the in-game menu to play as {name}\n\n")
        print(f"    * \'abilities\': Add or delete abilities from {name}\n\n")
        print(f"    * \'see\': Open {name}'s profile and see their description\n\n")
        print("    * \'back\': Go back to the main menu to select a different character or exit.")
        input("\n**********************************************************************************************************\nPress ENTER to return to the main menu ")
    os.system("cls")
    charac(name)

# Edit characters 
def charac(name):
    # charac() code is old main() code for character
    # open any existing file or make new character if file does not exist
    try:
        f = open(f"{name}.json", "r")
        print(f"{name} found")
        f.close()
    except:
        print(f"Creating {name}...")
        age = int(input(f"\nWhat is {name}'s age? "))
    
        race = input(f"\nWhat is {name}'s race? ")
        race = race.capitalize()
    
        ech = input(f"\nWhat is {name}'s class? ")
        ech = ech.capitalize()
    
        x = {
            "Name" : name,
            "Age" : age,
            "Race" : race,
            "Class" : ech,
        }

        os.system("cls")
        print(f"Now please enter attributes for {name}.")
        st = input("Strength (STR): ")
        co = input("Constitution (CON): ")
        de = input("Dexterity (DEX): ")
        it = input("Intelligence (INT): ")
        wi = input("Wisdom (WIS): ")
        ch = input("Charisma (CHA): ")
        
        max = hp = input("Max HP: ")
        
        x[maxHP] = hp
        x["STR"] = st
        x["CON"] = co
        x["DEX"] = de
        x["INT"] = it
        x["WIS"] = wi
        x["CHA"] = ch
        
        
        with open(f"{name}.json", "w") as outfile:
            json.dump(x, outfile)
        
    finally:
        choice = input(f"\nWhat would you like to do with {name}? (Enter \'assist\' for more options) ")
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
                f = open(f"{name}.json", "r")
                print(f"Name: {name}", end="            ")
                print(f"Age: {age}")
                print(f"Race: {race}", end="            ")
                print(f"Class: {ech}")
                print(f"HP: {hp} / {maxHP}\n")
                print("Attributes\n**********************************************************************************************************\n")
                print(f"STR: {st}", end="            ")
                print(f"CON: {co}")
                print(f"DEX: {de}", end="            ")
                print(f"INT: {it}")
                print(f"WIS: {wi}", end="            ")
                print(f"CHA: {ch}")
                input("Press ENTER to return")
                os.system("cls")
                charac(name)
            elif choice == 'assist':
                assist("character", name)
            else:
                choice = input("Invalid choice. Enter your command or enter \'assist\' for more options ")
        os.system("cls")        
        # After typing 'back' go to the menu
        menu()

def delete(name):
    os.system("cls")
    os.remove(f"{name}.json")
    print(f"{name} has been deleted")
    os.system("cls")
    main()

# menu() code main function of the code
def menu():
    
    cmd = input("What would you like to do today? \nEnter \'assist\' for more options.\n")
    cmd = cmd.lower()
    while cmd != "exit":
        if cmd == "character":
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
            if name == "back":
                menu()
            if os.path.exists(f"{name}.json"):
                delete(name)
            else:
                print("This file does not exist")
        else:
            # handle unknown commands
            cmd = input(f"Unknown command \'{cmd}\'.\nPlease enter a command or use \'assist\' for a list of commands\n")
    
    exit()
def main():
    os.system("cls")
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
