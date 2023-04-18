from typing import Any


def players_repr(players: list[dict], verbose: bool) -> None:
    if verbose:
        print(">>>> TEAM:")

    for player in players:
        print(f"{player['name']=}, {player['age']=}")


def players_add(players: list[dict]) -> list[dict]:
    name = input('Введите имя игрока: ')
    age = input('Введите возраст игрока: ')
    number = int(input('Введите номер игрока: '))

    players.append({'name': name, 'age': age, 'number': number})


def players_del(players: list[dict], name: str) -> list[dict]:
    pass


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    pass


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    players_33: list[dict] = players_find(players=team, field="age", value=33)

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"Enter your choice {options}:")):
            break

        if user_input == "add":
            # players_add(...)
            pass



if __name__ == "__main__":
    main()