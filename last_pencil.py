"""Last Pencil Hyperskill Project implementation."""


def print_pencils(pencils_number):
    """Print a pencil <pencils_number> times"""
    print("|" * pencils_number)


def print_start_player(player_name):
    """Print an engaging sentence for the starting player"""
    print(f"{player_name} is going first!")


def main():
    """Main program"""
    pencils_number = int(input("How many pencils would you like to use:"))
    first_player = input("Who will be the first (John, Jack):")

    print_pencils(pencils_number)
    print_start_player(first_player)


if __name__ == "__main__":
    main()