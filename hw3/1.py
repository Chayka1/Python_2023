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
    

    options = ["repr", "add", "del", "find", "get", "exit"]

    while True:
        if not (user_input := input(f"Enter your choice {options}: \n")):
            break

        if user_input == "add":
            name = input('Введите имя игрока: ')
            age = int(input('Введите возраст игрока: '))
            number = int(input('Введите номер игрока: '))
            player = {'name': name, 'age': age, 'number': number}

            players_add(team, player)
            print('Игрок успешно добавлен!')

        elif user_input == 'find':
            field = input('Введите переменную котороя может присутствовать в списке: ')
            value = int(input('Введите значение этой переменной: '))
            print(players_find(team, field, value))
        
        elif user_input == 'get':
            pass

        elif user_input == 'del':
            name = input('Введите имя игрока: ')
            print(players_del(team, name))

        elif user_input == 'repr':
            players_repr(team)
        
        elif user_input == 'exit':
            break
            



if __name__ == "__main__":
    main()