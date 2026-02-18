# db.py
# Data layer: reads/writes players.csv (NO input/print)

import csv
from objects import Player


def _split_full_name(full_name: str) -> tuple[str, str]:
    """Split 'First Last' -> (first, last). Keeps multi-part first names."""
    parts = full_name.strip().split()
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return " ".join(parts[:-1]), parts[-1]


def read_lineup(filename: str = "players.csv") -> list[Player]:
    """Read the CSV file and return a list of Player objects.

    Expected CSV row format (4 columns):
        full_name, position, at_bats, hits
    """
    players: list[Player] = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 4:
                    continue
                full_name, pos, ab, hits = row[0], row[1], row[2], row[3]
                first, last = _split_full_name(full_name)
                players.append(Player(first, last, pos, ab, hits))
    except FileNotFoundError:
        # Rubric: handle missing file
        return []

    return players


def write_lineup(players: list[Player], filename: str = "players.csv") -> None:
    """Write Player objects back to CSV using the same 4-column format."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for p in players:
            writer.writerow([p.full_name, p.position, p.at_bats, p.hits])
