######################################################
## MENU CLASS
######################################################

class Menu:

    def __init__(self, name: str = "Menu", description: str = None, parent=None, options=None):
        self.name = name
        self.description = description
        self.parent = parent
        self.options = options
        self.children = []

        if parent:
            parent.add_submenu(self)
            self.options["Back"] = self.go_back
        elif self.options is not None:
            self.options["Exit"] = self.exit_program

    def add_submenu(self, menu: "Menu"):
        self.children.append(menu)

    def show_options(self):
        print(f"{self.name:-^21}")
        for index, option in enumerate(self.options.items()):
            option_name = option[1].__name__.replace("_", " ").capitalize()
            #option_name = option_name.replace("_", " ").capitalize()
            print(f"{index+1}. {option_name}" if callable(option[1]) else f"{index+1}. {option[1]}")
        print("-" * 21)
        print("\n")
        return input(">> ")

    def handle_selection(self, choice):
        choice = int(choice)

        if self.parent is None and choice == len(self.options):
            self.options["Exit"]()
            return None

        if choice == len(self.options):
            return self.options["Back"]()
        
        if self.children:
            child = self.children[choice - 1]
            print(child.description)
            return child

        selected_option = list(self.options.values())[choice - 1]
        if callable(selected_option):
            selected_option()
        return self.parent

    @staticmethod
    def exit_program():
        print("Exiting program...")
        exit()

    def go_back(self):
        return self.parent
        

######################################################
## SUBMENUS
######################################################

def templates():
    pass

def flask():
    pass

def start():
    print()

def config():
    print()





