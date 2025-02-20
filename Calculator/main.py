from cli_calc import cli_calculator
from gui_calc import gui_calculator


def main():
    choice = input("Choose mode: Type 'cli' for command line or 'gui' for graphical interface: ")
    
    if choice == "cli":
        cli_calculator()
    elif choice == "gui":
        gui_calculator()
    else:
        print("Invalid choice! Please enter 'cli' or 'gui'.")
        main()

# Run program
main()




