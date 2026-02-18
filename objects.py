# objects.py
# Business layer: Player + Lineup classes (NO input/print)

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")


class Player:
    """Represents one baseball player in the lineup."""

    def __init__(self, first_name: str, last_name: str, position: str, at_bats: int, hits: int):
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.position = position  # validates through setter
        self.update_stats(at_bats, hits)  # validates

    # --- name properties ---
    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def full_name(self) -> str:
        # Murach-style full name
        return f"{self.__first_name} {self.__last_name}".strip()

    # --- position (validated) ---
    @property
    def position(self) -> str:
        return self.__position

    @position.setter
    def position(self, value: str) -> None:
        value = value.strip().upper()
        if value not in POSITIONS:
            raise ValueError("Invalid position.")
        self.__position = value

    # --- stats ---
    @property
    def at_bats(self) -> int:
        return self.__at_bats

    @property
    def hits(self) -> int:
        return self.__hits

    def update_stats(self, at_bats: int, hits: int) -> None:
        at_bats = int(at_bats)
        hits = int(hits)

        if at_bats < 0 or hits < 0:
            raise ValueError("At bats and hits must be 0 or greater.")
        if hits > at_bats:
            raise ValueError("Hits can't be greater than at bats.")

        self.__at_bats = at_bats
        self.__hits = hits

    @property
    def batting_average(self) -> float:
        # Section 1 spec: if at_bats is 0, avg is 0.0
        if self.__at_bats == 0:
            return 0.0
        return self.__hits / self.__at_bats


class Lineup:
    """Stores and manages a list of Player objects."""

    def __init__(self, players=None):
        self.__players = list(players) if players else []

    def add_player(self, player: Player) -> None:
        self.__players.append(player)

    def remove_player(self, index: int) -> Player:
        return self.__players.pop(index)

    def move_player(self, old_index: int, new_index: int) -> None:
        player = self.__players.pop(old_index)
        self.__players.insert(new_index, player)

    def get_player(self, index: int) -> Player:
        return self.__players[index]

    def __len__(self) -> int:
        return len(self.__players)

    def __iter__(self):
        # Iterator implementation (rubric)
        return iter(self.__players)

    def to_list(self):
        # Safe copy for db layer
        return list(self.__players)
