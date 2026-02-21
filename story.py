from config import INVENTORY, STARTING_MONEY, CUPCAKE_PRICE
from utils import print_divider, get_choice

money = STARTING_MONEY


def start_bakery(player_name):
    print_divider()
    print(f"Welcome to your bakery, {player_name}!")
    print("Your goal is to earn as much money as possible.")
    print_divider()

    while True:
        print(f"Money: ${money}")
        print(f"Inventory: {INVENTORY}")

        choice = get_choice([
            "Bake cupcakes",
            "Help customer",
            "Restock ingredients",
            "Exit game"
        ])

        if choice == "Bake cupcakes":
            bake_cupcakes()

        elif choice == "Help customer":
            help_customer()

        elif choice == "Restock ingredients":
            restock()

        elif choice == "Exit game":
            print("Thanks for playing!")
            break


def bake_cupcakes():
    # TODO:
    # Check if there are enough ingredients
    # If yes, reduce ingredients and increase cupcakes
    # If not, print an error message

    pass


def help_customer():
    # TODO:
    # If cupcakes > 0:
    #   decrease cupcakes
    #   increase money
    # Else:
    #   tell user they need to bake more

    pass


def restock():
    # TODO:
    # Ask user which ingredient to restock
    # Each restock costs $3
    # Deduct money and increase ingredient count

    pass
