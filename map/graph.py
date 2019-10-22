
import requests
import json
body = {
  "key": "value"
}




# url = 'https://t7-api.herokuapp.com/init'
# headers = {"Authorization": "Token ac6e9fac44b48a6974eb8add0a3715184057be52"}   
# r =requests.post(url, headers=headers, data = json.dumps(body)) 
# print(r.json())

class Room:
    def __init__(self, title, description, room_id=0, x=None, y=None):
        self.room_id = room_id
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __str__(self):
        return f"\n-------------------\n\n{self.name}\n\n   {self.description}\n\n{self.getExitsString()}\n"
    def printRoomDescription(self, player):
        print(str(self))
    def getExits(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.w_to is not None:
            exits.append("w")
        if self.e_to is not None:
            exits.append("e")
        return exits
    def getExitsString(self):
        return f"Exits: [{', '.join(self.getExits())}]"
    def connectRooms(self, direction, connectingRoom):
        if direction == "n":
            self.n_to = connectingRoom
            connectingRoom.s_to = self
        elif direction == "s":
            self.s_to = connectingRoom
            connectingRoom.n_to = self
        elif direction == "e":
            self.e_to = connectingRoom
            connectingRoom.w_to = self
        elif direction == "w":
            self.w_to = connectingRoom
            connectingRoom.e_to = self
        else:
            print("INVALID ROOM CONNECTION")
            return None
    def getCoords(self):
        return [self.x, self.y]


        self.visited = {}
        self.rooms = []

    def find_path(previous=None):
        currRoomID = room.room_id

 


url = 'https://t7-api.herokuapp.com/move'
headers = {"Authorization": "Token ac6e9fac44b48a6974eb8add0a3715184057be52", 'Content-Type': 'application/json'}  
r =requests.post(url, headers=headers) 
print(r.json())



