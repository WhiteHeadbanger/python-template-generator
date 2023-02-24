######################################################
## MENU CLASS
######################################################

class Menu:
    def __init__(self, name: str = "Menu", description: str = None, parent = None, options = None):
        self.name = name
        self.description = description
        self.parent = parent
        self.options = options
        self.children = []

        if self.options is not None:
            if self.parent:
                #parent.add_submenu(self)
                self.options["Back"] = self.go_back
            else:
                self.options["Exit"] = self.exit_program

    def add_submenu(self, menu: "Menu"):
        self.children.append(menu)

    def add_submenu_text(self, name, description, options=None):
        submenu = Menu(name = name, description = description, parent = self, options = options)
        self.add_submenu(submenu)
        return submenu

    def show_options(self):
        print(f"{self.name:-^21}")
        for index, option in enumerate(self.options.items()):
            option_name = option[1].__name__.replace("_", " ").capitalize() if callable(option[1]) else option[1]
            print(f"{index+1}. {option_name}")
        print("-" * 21)
        print("\n")
        return input(">> ")

    def handle_selection(self, choice):
        choice = int(choice)

        if self.parent is None and choice == len(self.options):
            return self.options["Exit"]()

        if choice == len(self.options):
            return self.options["Back"]()

        selected_option = list(self.options.values())[choice - 1]

        if isinstance(selected_option, Menu):
            return selected_option

        if callable(selected_option):
            selected_option()
            return self

        return self.children[choice - 1]

    @staticmethod
    def exit_program():
        print("Exiting program...")
        exit()

    def go_back(self):
        return self.parent






