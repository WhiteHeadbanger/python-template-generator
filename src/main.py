import menu

MAIN_MENU = menu.Menu(
    name = "Main Menu",
    description = "Please select an option",
    options = {
        "Templates": "Templates",
    }
)

TEMPLATES = MAIN_MENU.add_submenu_text(
    name = "Templates",
    description = "Choose a template first.",
    options = {
        "Flask": "Flask",
    }
)

FLASK = TEMPLATES.add_submenu_text(
    name = "Flask",
    description = "Select 'Config' first if you want to customize the setup",
    options = {
        "Start": menu.start,
        "Config": menu.config
    }
)

def menu_loop(current_menu):
    choice = current_menu.show_options()
    sub_menu = current_menu.handle_selection(choice)
    if sub_menu is not None:
        return sub_menu
    
    return current_menu

def main():
    current_menu = MAIN_MENU
    
    while True:
        sub_menu = menu_loop(current_menu)
        current_menu = sub_menu




if __name__ == "__main__":
    main()