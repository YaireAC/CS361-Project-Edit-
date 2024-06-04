import subprocess
import psutil
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

registered_users = {}

def get_username_by_name(name):
    for username, user_info in registered_users.items():
        if user_info["name"] == name:
            return username
    return None

def login():
    print(Fore.YELLOW + "=== Login ===")
    print(Fore.CYAN + "Choose login method:")
    print(Fore.CYAN + "1. Username + Password")
    print(Fore.CYAN + "2. Name + Password")
    print(Fore.RED + "Beware little information is required. Therefore you can easily get hacked")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
    elif choice == "2":
        name = input("Enter name: ")
        username = get_username_by_name(name)
        if not username:
            print(Fore.RED + "Name not found. Please try again.")
            login()
            return
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        login()
        return

    password = input("Enter password: ")

    if username in registered_users and registered_users[username]["password"] == password:
        print(Fore.GREEN + "Login successful!")
        print(Fore.YELLOW + "🏠")  # Display home symbol
        main_menu(username)
    else:
        print(Fore.RED + "Invalid username or password.")
        choice = input("Do you want to register? (yes/no): ").lower()
        if choice == "yes":
            register()
        else:
            print("Goodbye!")

def register():
    print(Fore.YELLOW + "=== Registration ===")
    name = input("Enter your name: ")
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    registered_users[username] = {"name": name, "password": password, "saved_artists": []}
    print(Fore.GREEN + "Registration successful!")
    print(Fore.CYAN + "Welcome to Music Fashion App, " + name + "!")

def settings(username):
    print(Fore.YELLOW + "=== Settings ===")
    print(Fore.CYAN + "1. Change password")
    print(Fore.CYAN + "2. Delete account")
    print(Fore.CYAN + "3. Go back to main menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_password = input("Enter new password: ")
        registered_users[username]["password"] = new_password
        print(Fore.GREEN + "Password changed successfully!")
        settings(username)
    elif choice == "2":
        confirm = input("Are you sure you want to delete your account? This action cannot be undone. (yes/no): ").lower()
        if confirm == "yes":
            del registered_users[username]
            print(Fore.GREEN + "Account deleted successfully!")
            return "deleted"
        else:
            print("Account deletion cancelled.")
            settings(username)
    elif choice == "3":
        return "back_to_menu"
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
        settings(username)

def run_microservice(script_name):
    process = subprocess.Popen(['python', script_name])
    return process

def manage_saved_artists():
    print("Starting Microservice A...")
    process_a = run_microservice('microA.py')
    process_a.wait()  # Wait for Microservice A to finish

    print("Microservice A finished. Starting Microservice B...")
    process_b = run_microservice('microB.py')
    process_b.wait()  # Wait for Microservice B to finish

    print("Microservice B finished. Starting Microservice C...")
    process_c = run_microservice('microC.py')
    process_c.wait()  # Wait for Microservice C to finish

    # Demonstrate that each is running in a separate process
    print(Fore.YELLOW + f"Main Program PID: {psutil.Process().pid}")
    print(Fore.GREEN + f"Microservice A PID: {process_a.pid}")
    print(Fore.CYAN + f"Microservice B PID: {process_b.pid}")
    print(Fore.MAGENTA + f"Microservice C PID: {process_c.pid}")


def main_menu(username):
    while username in registered_users:
        print(Fore.YELLOW + f"=== Welcome, {registered_users[username]['name']} ===")
        print(Fore.CYAN + "1. Manage your artists")
        print(Fore.CYAN + "2. Search by Country")
        print(Fore.CYAN + "3. Search for artists by genre")
        print(Fore.CYAN + "4. Settings")
        print(Fore.CYAN + "5. Logout (X)")

        option = input("Enter your choice: ")

        if option == "1":
            manage_saved_artists()
        elif option == "2":
            print("eventually...")
        elif option == "3":
            print("eventually...")
        elif option == "4":
            result = settings(username)
            if result == "deleted":
                return
            elif result == "back_to_menu":
                continue
        elif option == "X" or option == "5":
            print("Logging out...")
            return
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

def main():
    while True:
        print(Fore.BLUE + "=== Music Fashion App ===")
        print(Fore.CYAN + "Welcome to Music Fashion App!")
        print(Fore.CYAN + "Whether you're a new user or returning, we've got something special for you!")
        print(Fore.CYAN + "Unlock your personalized fashion journey now.")
        print(Fore.CYAN + "1. Login")
        print(Fore.CYAN + "2. Register")
        print(Fore.CYAN + "3. Quit (X)")

        option = input("Enter your choice: ")

        if option == "1":
            login()
        elif option == "2":
            register()
        elif option == "X" or option == "3":
            print("Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
