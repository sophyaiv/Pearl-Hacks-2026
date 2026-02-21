def print_divider():
    print("\n" + "=" * 40 + "\n")


def get_choice(options):
    """
    Displays numbered options and returns
    the user's selected option.
    """

    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        choice = input("Choose an option: ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return options[choice - 1]

        print("Invalid choice. Try again.")
