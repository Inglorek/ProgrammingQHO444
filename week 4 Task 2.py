def display_in_box(hello):
    """Display the word inside an ASCII art box."""
    # The top and bottom edges need to be 4 characters wider than the word
    # (2 for the '+' corners and 2 for the spaces of padding inside the box).
    border = "+" + "-" * (len(hello) + 2) + "+"
    print(border)
    print("| " + hello + " |")
    print(border)

def display_lower(Hello):
    """Display the Hello inside an ASCII art box.
By """
    print(Hello.lower())

def display_upper(Hello):
    """Display the word in upper-case, e.g. HELLO."""
    print(Hello.upper())

def display_Mirrored(Hello):
    """Display the Hello inside an ASCII art box."""
    mirrored = Hello[::-1]
    print(word + " | " + mirrored)


def display_repeat(Hallo):
    """Ask how many times to display the word, then display it that many
    times alternating between upper-case and lower-case."""
    # Keep asking until the user types a valid whole number.
    while True:
        try:
            times = int(input("How many times should the word be displayed? "))
            if times < 1:
                print("Please enter a number of 1 or more.")
                continue
            break
        except ValueError:
            print("That is not a whole number. Please try again.")

    # Loop from 0 to times-1. Even counts print upper-case, odd counts print
    # lower-case, which gives the alternating pattern.
    for i in range(times):
        if i % 2 == 0:
            print(hello.upper())
        else:
            print(hello.lower())


def run_program():
    """Prompt the user for a word and a menu option, then carry out the action."""
    hello = input("Enter a word: ")

    # Display the menu of options.
    print("\nChoose an option:")
    print("1) Display in a Box")
    print("2) Display Lower-case")
    print("3) Display Upper-case")
    print("4) Display Mirrored")
    print("5) Repeat")
    option = input("Enter option number (1-5): ")

    print()  # blank line before the output

    # Call the function that matches the option entered.
    if option == "1":
        display_in_box(hello)
    elif option == "2":
        display_lower(hello)
    elif option == "3":
        display_upper(hello)
    elif option == "4":
        display_mirrored(hello)
    elif option == "5":
        display_repeat(hello)
    else:
        print("Invalid option. Please run the program again and choose 1-5.")


# Start the program.
run_program()
