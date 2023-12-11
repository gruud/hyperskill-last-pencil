"""Last Pencil Hyperskill Project implementation."""


def print_pencils(pencils_number):
    """Print a pencil <pencils_number> times"""
    print("|" * pencils_number)


def get_player_input(player_name):
    """Get the next player number of pencils to remove"""
    return int(input(f"{player_name}'s turn:"))


def main():
    """Main program"""

    # Use a players' list to easily iterate over the players
    players = ["John", "Jack"]
    pencils_number = int(input("How many pencils would you like to use:"))
    starting_player = input(f"Who will be the first ({players[0]}, {players[1]}):")

    next_player = players.index(starting_player)

    while pencils_number > 0:
        print_pencils(pencils_number)
        pencils_to_remove = get_player_input(players[next_player])

        pencils_number -= pencils_to_remove
        next_player = (next_player + 1) % len(players)


if __name__ == "__main__":
    main()