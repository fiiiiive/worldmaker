def ablts(name):
    f = open(f"{name}.txt", "a")
    
    ability = input("What is the ability's name? (Enter \'0\' to exit): ")
    ability = ability.capitalize()
    while ability != '0':
        description = input("What does the ability do? ")
        description = description.capitalize()
        f.write(f"*******************************\n{ability}:\n{description}\n\n")
        
        ability = input("What is the ability's name? (Enter \'0\' to exit): ")
        ability = ability.capitalize()
    
    f.close()

def main():
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
    
        f.write(f"{name}******************************\n")
        f.write(f"Age: {age}\n")
        f.write(f"Race: {race}\n")
        f.write(f"Class: {cls}")
        f.write(f"******************************\nAbilities for {name}:\n")
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

        
        

    

if __name__ == "__main__":
    main()
