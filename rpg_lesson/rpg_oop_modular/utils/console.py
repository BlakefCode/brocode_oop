import os
# Clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prompt the user to press Enter to continue
def press_enter():
    input("\nPress Enter to continue...\n")

# Print a border for visual separation
def print_border():
    print("=" * 80)