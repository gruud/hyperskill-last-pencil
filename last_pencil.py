import random
"""Last Pencil Hyperskill Project implementation."""


class Game:
    """The last pen Game class.

    Attributes:
        - players : a list of the players playing the game
        - pencil_number: The number of pencil left in the game
        - current_player: The player currently playing
        - winner: The winner of the game
        - too_many_pencils_removed: Indicates that the last player tried to
          remove too many pencils and had to pass
        - invalid_pencils_number: Indicate whether the number of pencils
          given by the player is too high or not
    """
    def __init__(self):
        self.players = []
        self.pencils_number = 0
        self.current_player = None
        self.winner = None
        self.too_many_pencils_removed = False
        self.invalid_pencils_number = False
        self.bot = None

    def set_players(self, players):
        """Set the players of the game"""
        self.players = players
        return self

    def start(self):
        """Start and run the game until someone wins"""
        self.set_starting_pencil_numbers()
        self.set_starting_player()
        self.bot = len(self.players) - 1

        while self.winner is None:
            self.print_pencils()
            if self.current_player == self.bot:
                pencils_to_remove = self.bot_plays()
            else:
                pencils_to_remove = self.player_plays()

            self.pencils_number -= pencils_to_remove
            self.check_winner()
            self.switch_to_next_player()

        self.print_winner()

    def check_winner(self):
        """Check if someone has won the game"""
        if self.pencils_number == 0:
            self.winner = self.get_next_player()

    def bot_plays(self):
        """Get the nex bot move for the game.

        The bot itself does not take input (simply displaying the standard
        message). The bot checks for the number of pencil, which has a recurrent
        pattern every four numbers (1-4, 5-9, ...). Therefore:

            number_of_pencils % 4 gives the next move to play.

        If number_of_pencils == 1, the bot takes the last pencil and loses
        """
        print(self.get_play_message())
        choice = None

        if self.pencils_number == 1:
            choice = 1
        else:
            pencil_situation = self.pencils_number % 4
            if pencil_situation == 0:
                choice = 3
            elif pencil_situation == 1:
                choice = random.randint(1, 3)
            elif pencil_situation == 2:
                choice = 1
            elif pencil_situation == 3:
                choice = 2

        print(choice)
        return choice

    def player_plays(self):
        """Let the human player play his turn

        Prints the play message based on the last outcome, then checks
        if user input is invalid, he needs to input some valid data first
        Returns the valid number of pens to remove
        """
        while True:
            pencils = input(self.get_turn_message())
            if not self.is_integer_input(pencils) or int(pencils) not in range(1, 4):
                # The input is not a valid integer. The players gets to enter a new value
                self.invalid_pencils_number = True
                continue

            pencils_removed = int(pencils)
            if pencils_removed > self.pencils_number:
                # The user entered a faulty value : loses his turn, no pencil is removed
                self.too_many_pencils_removed = True
                continue
            else:
                # Valid play - return removed pens count / Reinit messages
                self.too_many_pencils_removed = False
                self.invalid_pencils_number = False
                return pencils_removed

    def get_turn_message(self):
        """Get the invitation to play messages based on the last move."""
        if self.too_many_pencils_removed:
            message = "Too many pencils were taken"
        elif self.invalid_pencils_number:
            message = "Possible values: '1', '2' or '3'"
        else:
            message = self.get_play_message()

        self.invalid_pencils_number = False
        self.too_many_pencils_removed = False
        return message

    def switch_to_next_player(self):
        """Sets the next current player"""
        self.current_player = self.get_next_player()

    def get_next_player(self):
        """Get the index of the next player"""
        return (self.current_player + 1) % len(self.players)

    def set_starting_pencil_numbers(self):
        """Get the number of pencils from user input."""
        user_input = input("How many pencils would you like to use:")

        # Iterate until the input is a positive integer
        while True:
            if not self.is_integer_input(user_input) or user_input.startswith("-"):
                user_input = input("The number of pencils should be numeric")
                continue

            pencils = int(user_input)
            if pencils <= 0:
                user_input = input("The number of pencils should be positive")
            else:
                self.pencils_number = pencils
                break

    def get_play_message(self):
        """Get the standard play message"""
        return f"{self.players[self.current_player]}'s turn:"

    def set_starting_player(self):
        """Set the index of the starting player from user input"""
        starting_player = input(f"Who will be the first ({self.players[0]}, {self.players[1]}):")
        while starting_player not in self.players:
            starting_player = input(f"Choose between '{self.players[0]}' and '{self.players[1]}'")
        self.current_player = self.players.index(starting_player)

    def print_pencils(self):
        """Print a pencils representation in CLI"""
        print("|" * self.pencils_number)

    def print_winner(self):
        """Print the winner's name"""
        print(f"{self.players[self.winner]} won!")

    @staticmethod
    def is_integer_input(user_input):
        """Check if integer conversion is possible for a given string input"""
        try:
            int(user_input)
            return True
        except ValueError:
            return False


def main():
    """Main program"""
    (Game()
     .set_players(["John", "Jack"])
     .start())


if __name__ == "__main__":
    main()
