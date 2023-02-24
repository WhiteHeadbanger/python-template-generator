import os
import subprocess

# Get the current working directory
working_dir = os.getcwd()

default_config = {
    "working_dir": working_dir,
    "venv": False,
    "git_init": False,
    "mvc": False,
    "vscode": False
}

def start():
    project_name = input("Project name (this will be used as the name of the main folder in your project): ")
    confirm_working_directory = False

    while not confirm_working_directory:
        confirm_working_directory = input(
            f"This will create a directory named {project_name} in {default_config['working_dir']}\nIs that correct? (y/n): "
            ).lower() == "y"

        if not confirm_working_directory:
            new_working_directory = input("New working directory (full path): ")
            default_config["working_dir"] = new_working_directory    
    
    print("Creating the directory structure...")

    # Create the project main directory
    dir_path = os.path.join(default_config["working_dir"], project_name)
    os.mkdir(dir_path)


    if default_config["venv"]:
        # Create the virtual environment
        print("Creating venv environment...")
        venv_dir = "venv"
        subprocess.run(["python", "-m", "venv", venv_dir], cwd = dir_path, check = True)
        
        # Activate the virtual environment
        activate_script = f"{venv_dir}\\Scripts\\activate.bat"
        subprocess.run(activate_script, cwd = dir_path, shell=True, check=True)
        
        # Install Flask
        subprocess.run(["pip", "install", "flask"], cwd = dir_path, check = True)
        
        # Check the version
        flask_version = subprocess.run(["python", "-c", "import flask; print(flask.__version__)"], cwd = dir_path, stdout=subprocess.PIPE , check=True)
        print(flask_version.stdout.decode('utf-8'))

    if default_config["git_init"]:
        print("Initializing git...")
        # Initialize git
        subprocess.run(["git", "init"], cwd = dir_path, check = True)
        
        print("Creating .gitignore...")
        file_name = '.gitignore'
        file = open(os.path.join(dir_path, file_name), 'w')
        file.close()
        
        print("Creating README.md ...")
        file_name = 'README.md'
        file = open(os.path.join(dir_path, file_name), 'w')
        file.close()

    if default_config['mvc']:
        print("Creating MVC pattern structure...")
        init_file = '__init__.py'

        controllers_path = os.path.join(dir_path, 'controllers')
        os.mkdir(controllers_path)
        file = open(os.path.join(controllers_path, init_file), 'w')
        file.close()

        routes_path = os.path.join(dir_path, 'routes')
        os.mkdir(routes_path)
        file = open(os.path.join(routes_path, init_file), 'w')
        file.close()

        models_path = os.path.join(dir_path, 'models')
        os.mkdir(models_path)
        file = open(os.path.join(models_path, init_file), 'w')
        file.close()

    # Create Static and Templates folder in order for Flask to work
    print("Creating 'static' folder...")
    static_dir = os.path.join(dir_path, 'static')
    css_dir = os.path.join(static_dir, 'css')
    js_dir = os.path.join(static_dir, 'js')
    images_dir = os.path.join(static_dir, 'images')
    os.mkdir(static_dir)
    os.mkdir(css_dir)
    os.mkdir(js_dir)
    os.mkdir(images_dir)

    print("Creating 'templates' folder...")
    templates_dir = os.path.join(dir_path, 'templates')
    os.mkdir(templates_dir)

    # Create __init__.py in source directory
    file = open(os.path.join(dir_path, '__init__.py'), 'w')
    file.close()
    
    if default_config['vscode']:
        print("Opening VSCode...")
        subprocess.run(["C:\\Users\\White\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code.cmd", "."], cwd = dir_path, check = True)


def config():
    
    def ask_questions():
        setup_venv = input("Setup venv? (y/n): ").lower() == "y"
        git_init = input("Git init? (y/n): ").lower() == "y"
        use_mvc = input("Use MVC pattern? (y/n): ").lower() == "y"
        start_vscode = input("Start VSCode? (y/n): ").lower() == "y"

        return {
            "venv": setup_venv,
            "git_init": git_init,
            "mvc": use_mvc,
            "vscode": start_vscode
        }

    config = ask_questions()
    
    default_config.update({"venv": config["venv"]})
    default_config.update({"git_init": config["git_init"]})
    default_config.update({"mvc": config["mvc"]})
    default_config.update({"vscode": config["vscode"]})
    