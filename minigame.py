import random


MIN_PLAYERS = 1
MAX_PLAYERS = 4
MAX_SCORE = 30


def roll_die() -> int:
    return random.randint(1, 6)


def get_player_count() -> int:
    while True:
        raw_value = input(f"Enter the number of players ({MIN_PLAYERS}-{MAX_PLAYERS}): ").strip()

        if not raw_value.isdigit():
            print(f"Invalid input. Please enter a number between {MIN_PLAYERS} and {MAX_PLAYERS}.")
            continue

        players = int(raw_value)
        if MIN_PLAYERS <= players <= MAX_PLAYERS:
            return players

        print(f"Invalid input. Please enter a number between {MIN_PLAYERS} and {MAX_PLAYERS}.")


def play_game(players: int, target_score: int = MAX_SCORE) -> None:
    scores = [0] * players

    while max(scores) < target_score:
        for player_index in range(players):
            user_input = input(
                f"Player {player_index + 1}, press Enter to roll the dice (or type 'q' to quit): "
            ).strip().lower()
            if user_input in {"q", "quit", "exit"}:
                print("Game ended early.")
                return

            roll_result = roll_die()
            scores[player_index] += roll_result

            print(f"Player {player_index + 1} rolled a {roll_result}.")
            print(f"Player {player_index + 1}'s current score: {scores[player_index]}")

            if scores[player_index] >= target_score:
                print(f"Player {player_index + 1} wins with a score of {scores[player_index]}!")
                return


def main() -> None:
    players = get_player_count()
    print(f"Number of players: {players}")
    play_game(players)


if __name__ == "__main__":
    main()
