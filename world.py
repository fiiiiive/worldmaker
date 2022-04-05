class World:
    name = "World"
    subWorlds = set( )
    descript = list()
    def __init__(self, name):
        self.name = name
     
    def getDescript():
        print(f"Use Ctrl-D or Ctrl-Z ( windows ) to save {name}'s backstory.")
        while True:
        try:
            line = input()
        except EOFError:
            break
        descript.append(line)
