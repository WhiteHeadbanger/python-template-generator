import menu

MAIN_MENU = menu.Menu(
    name = "Main Menu", 
    options = {
        "Templates": menu.templates,
    })

TEMPLATES = menu.Menu(
    name = "Templates",
    description = "Choose a template first.",
    parent = MAIN_MENU,
    options = {
        "Flask": menu.flask
    })

FLASK = menu.Menu(
    name = "Flask",
    description = "Select 'Config' first if you want to customize the setup",
    parent = TEMPLATES,
    options = {
        "Start": menu.start,
        "Config": menu.config
    }
)

def menu_loop(current_menu):
    choice = current_menu.show_options()
    return current_menu.handle_selection(choice)

def main():
    current_menu = MAIN_MENU
    
    while True:
        sub_menu = menu_loop(current_menu)
        current_menu = sub_menu




if __name__ == "__main__":
    main()