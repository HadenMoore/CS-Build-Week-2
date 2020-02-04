import requests
import json
import time

jason_prince_api_key = "Token ece07b1e0e2fc9e8a6c86ae269422e9afb9de66d"

headers = {
    'Authorization': jason_prince_api_key,
    'Content-Type': 'application/json'
}


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.base_url = "https://lambda-treasure-hunt.herokuapp.com/api"

#---------------------------INIT---------------------------#
    def init(self):
        endpoint = "/adv/init/"
        res = requests.get(
            self.base_url + endpoint,
            headers=headers
        )
        print(res.text)

#---------------------------TREASURE---------------------------#
    def take(self):
        endpoint = "/adv/take/"
        data = {
            "name": "treasure"
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} TAKING TREASURE')

    def drop(self):
        endpoint = "/adv/drop/"
        data = {
            "name": "treasure"
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} DROPPING TREASURE')

    def sell(self):
        endpoint = "/adv/sell/"
        data = {
            "name": "treasure"
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} SELL TREASURE')

    def sell_confirm(self):
        endpoint = "/adv/sell/"
        data = {
            "name": "treasure",
            "confirm": "yes"
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} SELL CONFIRM TREASURE')

#---------------------------MOVE---------------------------#
    def move(self, direction):
        print(f'Direction: {direction}')
        endpoint = "/adv/move/"
        data = {
            "direction": direction
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        next_room = json.loads(res.text)
        self.current_room = next_room
        print(f'{next_room} Here is our new room.')

    def wise_move(self, direction, room):
        print(f'Direction: {direction} Room: {room}')
        endpoint = "/adv/move/"
        data = {
            "direction": direction,
            "next_room": room
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        next_room = json.loads(res.text)
        self.current_room = next_room
        print(f'{next_room} Here is our new room.')

#---------------------------STATUS AND EXAMINE---------------------------#
    def status(self):
        endpoint = "/adv/status/"
        res = requests.post(
            self.base_url + endpoint,
            headers=headers
        )
        print(f'------- {res.text} STATUS')

    def examine(self):
        endpoint = "/adv/examine/"
        data = {
            "name": "Wishing Well"
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} WISHING WELL INFO')

#---------------------------EQUIPMENT (WEAR AND UNDRESS)---------------------------#
    def wear(self, item):
        endpoint = "/adv/wear/"
        data = {"name": item}
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} WEAR')

    def undress(self, item):
        endpoint = "/adv/undress/"
        data = {"name": item}
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} UNDRESS')

#---------------------------NAME CHANGER---------------------------#
    def change_name(self, name):
        endpoint = "/adv/change_name/"
        data = {
            "name": name
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} CHANGE NAME')

#---------------------------FAST MOVE---------------------------#
    def dash(self, direction, number_of_rooms, sequential_room_ids):
        endpoint = "/adv/dash/"
        data = {
            "direction": direction,
            "num_rooms": number_of_rooms,
            "next_room_ids": sequential_room_ids
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} DASH')

    def flight(self, direction):
        endpoint = "/adv/fly/"
        data = {
            "direction": direction
        }
        res = requests.post(
            self.base_url + endpoint,
            headers=headers,
            data=json.dumps(data)
        )
        print(f'------- {res.text} FLY')


jason = Player("Jason", 0)

jason.init()
