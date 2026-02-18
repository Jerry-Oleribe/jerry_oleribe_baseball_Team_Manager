# main.py
# Coordinates UI + business objects + CSV (Sections 1–3)

import db
import ui
from objects import Player, Lineup


def display_lineup(lineup: Lineup) -> None:
    print()
    print(" Player                     POS    AB     H    AVG")
    print(ui.DASH)
    for i, player in enumerate(lineup, start=1):
        print(f"{i:<2} {player.full_name:<25} {player.position:<5} "
              f"{player.at_bats:>5} {player.hits:>5} {player.batting_average:>6.3f}")
    print()


def add_player(lineup: Lineup) -> None:
    print()
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    pos = ui.get_position("Position: ")
    ab = ui.get_nonneg_int("At bats: ")
    hits = ui.get_nonneg_int("Hits: ")

    try:
        player = Player(first, last, pos, ab, hits)
    except ValueError as e:
        print(e)
        return

    lineup.add_player(player)
    print(f"{player.full_name} was added.")


def remove_player(lineup: Lineup) -> None:
    print()
    if len(lineup) == 0:
        print("Lineup is empty.")
        return

    number = ui.get_int("Number: ")
    index = number - 1
    if index < 0 or index >= len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.remove_player(index)
    print(f"{player.full_name} was deleted.")


def move_player(lineup: Lineup) -> None:
    print()
    if len(lineup) == 0:
        print("Lineup is empty.")
        return

    current_num = ui.get_int("Current lineup number: ")
    current_idx = current_num - 1
    if current_idx < 0 or current_idx >= len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(current_idx)
    print(f"{player.full_name} was selected.")

    new_num = ui.get_int("New lineup number: ")
    new_idx = new_num - 1
    if new_idx < 0 or new_idx >= len(lineup):
        print("Invalid lineup number.")
        return

    lineup.move_player(current_idx, new_idx)
    print(f"{player.full_name} was moved.")


def edit_position(lineup: Lineup) -> None:
    print()
    if len(lineup) == 0:
        print("Lineup is empty.")
        return

    number = ui.get_int("Lineup number: ")
    index = number - 1
    if index < 0 or index >= len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(index)
    print(f"You selected {player.full_name} POS={player.position}")

    pos = ui.get_position("Position: ")
    try:
        player.position = pos
        print(f"{player.full_name} was updated.")
    except ValueError as e:
        print(e)


def edit_stats(lineup: Lineup) -> None:
    print()
    if len(lineup) == 0:
        print("Lineup is empty.")
        return

    number = ui.get_int("Lineup number: ")
    index = number - 1
    if index < 0 or index >= len(lineup):
        print("Invalid lineup number.")
        return

    player = lineup.get_player(index)
    print(f"You selected {player.full_name} AB={player.at_bats} H={player.hits}")

    ab = ui.get_nonneg_int("At bats: ")
    hits = ui.get_nonneg_int("Hits: ")

    try:
        player.update_stats(ab, hits)
        print(f"{player.full_name} was updated.")
    except ValueError as e:
        print(e)


def main() -> None:
    # Section 2/3 style: optional game date prompt and display
    game_date_str, days_until = ui.get_game_date()

    players = db.read_lineup("players.csv")
    lineup = Lineup(players)

    while True:
        ui.display_header(game_date_str, days_until)
        option = ui.prompt_menu_option()

        if option == "1":
            display_lineup(lineup)
        elif option == "2":
            add_player(lineup)
            db.write_lineup(lineup.to_list(), "players.csv")
        elif option == "3":
            remove_player(lineup)
            db.write_lineup(lineup.to_list(), "players.csv")
        elif option == "4":
            move_player(lineup)
            db.write_lineup(lineup.to_list(), "players.csv")
        elif option == "5":
            edit_position(lineup)
            db.write_lineup(lineup.to_list(), "players.csv")
        elif option == "6":
            edit_stats(lineup)
            db.write_lineup(lineup.to_list(), "players.csv")
        elif option == "7":
            print("Bye!")
            break
        else:
            print("Invalid menu option. Please try again.")

        print()


if __name__ == "__main__":
    main()
