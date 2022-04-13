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
def help():
    # print help menu
    print("Character creator is a way for you to make your own DND character and keep track of attributes, abilities, and other in game information.\n" +
        "From the main menu you can use a list of commands such as:\n\n" +
        "    * \'edit\': Create, edit, or delete existing characters. \n" +
        "         - \'Create\' will write a new file using information on your character given by you\n" +
        "         - \'Edit\' allows players to add or delete attributes or abilities to existing characters.\n" +
        "         - \'Delete\' allows players to delete existing characters.\n\n" +
        # add other commands here
        "    * \'exit\': Exit the program.")
    input("\n**********************************************************************************************************\nPress ENTER to return to the main menu")
    main()

# Edit characters 
def edit():
    # edit() code is old main() code for character

    name = input("What is the name of your character? ")
    name = name.capitalize()
    try:
        f = open(f"{name}.txt", "r")
        print("Here is your character: ")
        print(f.read())
    except:
        
        age = int(input("\nWhat is " + name + "'s age? "))
    
        race = input("\nWhat is " + name + "'s race? ")
        race = race.capitalize()
    
        cls = input("\nWhat is " + name + "'s class? ")
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
            exit()
        else:
            ablts(name)
            exit()

def delete(name):
    os.remove(f"{name}.txt")
    return

# Main Menu code
def main():
    cmd = input("Welcome to Character Creator! What would you like to do today? \nEnter \'help\' for more options.\n")
    cmd = cmd.lower()
    while cmd != "exit":
        if cmd == "edit":
            # edit() code is old main() code
            edit()

        elif cmd == "help":
            # help() call here
            help()
        elif cmd == "delete":
            if os.path.exists(f"{name}.txt"):
                delete(name)
            else:
                print("This file does not exist")
        else:
            # handle unknown commands
            cmd = input(f"Unknown command \'{cmd}\'.\nPlease enter a command or use \'help\' for a list of commands")
    
    exit()

# Driver
if __name__ == "__main__":
    main()
