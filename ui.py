# ui.py
# Presentation layer: input/output only

from datetime import date, datetime
from objects import POSITIONS

LINE_LEN = 64
LINE = "=" * LINE_LEN
DASH = "-" * LINE_LEN


def display_header(game_date_str: str | None = None, days_until: int | None = None) -> None:
    print(LINE)
    print(" Baseball Team Manager")
    print(f" CURRENT DATE: {date.today().isoformat()}")
    if game_date_str:
        print(f" GAME DATE:    {game_date_str}")
    if days_until is not None:
        print(f" DAYS UNTIL GAME: {days_until}")
    print(" MENU OPTIONS")
    print(" 1 – Display lineup")
    print(" 2 – Add player")
    print(" 3 – Remove player")
    print(" 4 – Move player")
    print(" 5 – Edit player position")
    print(" 6 – Edit player stats")
    print(" 7 - Exit program")
    print(" POSITIONS")
    print(" " + ", ".join(POSITIONS))
    print(LINE)


def prompt_menu_option() -> str:
    return input("Menu option: ").strip()


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_nonneg_int(prompt: str) -> int:
    while True:
        value = get_int(prompt)
        if value < 0:
            print("Number must be 0 or greater. Please try again.")
        else:
            return value


def get_position(prompt: str = "Position: ") -> str:
    while True:
        pos = input(prompt).strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Please try again.")


def get_game_date() -> tuple[str | None, int | None]:
    """Ask for a game date (YYYY-MM-DD). Return (date_str, days_until) or (None, None)."""
    raw = input("GAME DATE (YYYY-MM-DD) - press Enter to skip: ").strip()
    if raw == "":
        return None, None

    try:
        game_dt = datetime.strptime(raw, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. GAME DATE will be skipped.")
        return None, None

    today = date.today()
    if game_dt > today:
        return raw, (game_dt - today).days
    return raw, None
