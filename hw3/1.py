from typing import Any


def players_repr(players: list[dict]) -> None:
    print(">>>> TEAM:")

    for player in players:
        print(f"{player['name']=}, {player['age']=}")


def players_add(players: list[dict], player: dict) -> list[dict]:
    players.append(player)

    return players
    

def players_del(players: list[dict], name: str) -> list[dict]:
    for player in players:
        if player['name'] == name:
            players.remove(player)
    
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    playing_people_with_this_attribute = []

    for player in players:
        if player[field] == value:
            playing_people_with_this_attribute.append(player)

    return playing_people_with_this_attribute


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    """If multiple players with same name - return the first one."""


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    players_33: list[dict] = players_find(players=team, field="age", value=33)
    print(players_33)
    print()
    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"Enter your choice {options}:")):
            break

        if user_input == "add":
            name = input('Введите имя игрока: ')
            age = input('Введите возраст игрока: ')
            number = int(input('Введите номер игрока: '))
            player = {'name': name, 'age': age, 'number': number}

            players_add(team, player)
        elif user_input == 'find':
            field = input('Введите переменную котороя может присутствовать в списке: ')
            value = int(input('Введите значение этой переменной: '))

            players_find(team, field, value)
            



if __name__ == "__main__":
    main()