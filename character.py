import os

# Write abilities to characters file
def ablts(name):
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
def assist():
    # print help menu
    print("Character creator is a way for you to make your own DND character and keep track of attributes, abilities, and other in game information.\n" +
        "From the main menu you can use a list of commands such as:\n\n" +
        "    * \'edit\': Create or edit existing characters. \n\n" +
        "    * \'delete\': Delete existing characters.\n\n" +
        # add other commands here
        "    * \'exit\': Exit the program.")
    input("\n**********************************************************************************************************\nPress ENTER to return to the main menu")
    main()

# Edit characters 
def edit():
    # edit() code is old main() code for character

    name = input("What is the name of your character? ")
    name = name.capitalize()
    # open any existing file or make new character if file does not exist
    try:
        f = open(f"{name}.txt", "r")
        print("Here is your character: ")
        print(f.read())
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
        choice = input("\nWould you like to add abilities at this time? ")
        choice = choice.lower()
    
        while choice[0] != 'n' and choice[0] != 'y':
            print("Unknown answer")
            choice = input("Would you like to add abilities at this time? ")
            choice = choice.lower()
    
    
        if choice[0] == 'n':
            main()
        else:
            ablts(name)
            main()

def delete(name):
    os.remove(f"{name}.txt")
    print("Deleted")
    main()

# menu() code main function of the code
def menu():
    cmd = input("What would you like to do today? \nEnter \'help\' for more options.\n")
    cmd = cmd.lower()
    while cmd != "exit":
        if cmd == "edit":
            # edit() code is old main() code
            # handles character creation and editing
            edit()
        
        elif cmd == "help":
            # help() call here
            help()
        elif cmd == "delete":
            name = input("What character would you like to delete? ")
            if os.path.exists(f"{name}.txt"):
                delete(name)
            else:
                print("This file does not exist")
        else:
            # handle unknown commands
            cmd = input(f"Unknown command \'{cmd}\'.\nPlease enter a command or use \'help\' for a list of commands")
    
    exit()
def main():
    print("**************************************************\n\n" + 
        "          Welcome to Character Creator!\n\n" +
        "**************************************************\n")
    menu()
    
# Driver
if __name__ == "__main__":
    main()
