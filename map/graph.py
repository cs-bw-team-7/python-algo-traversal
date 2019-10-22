
from room import Room
from player import Player
from world import World
import requests

world = World()
player = Player("Name", world.startingRoom)

        


traversalPath = [] # starts empty, need to go to every room
visited = {}


def find_path(previous=None):  # set previous to None, no previous direction
    currRoomID = player.currentRoom.room_id

    for i in visited:
        if i == currRoomID:
            print(f"Already found room {currRoomID}")
            return
    visited[currRoomID] = {}
    print(f"Adding room {currRoomID} to visited")
    
    exits = player.currentRoom.getExits()

    
    for direction in exits:
        if direction == 'n' and previous !=  direction:
            Travel('n')
            traversalPath.append('n')
            find_path('s')
            Travel('s')
            traversalPath.append('s')

        elif direction == 's' and previous !=  direction:
            Travel('s')
            traversalPath.append('s')
            find_path('n')
            Travel('n')
            traversalPath.append('n')

        elif direction == 'e' and previous !=  direction:
            Travel('e')
            traversalPath.append('e')
            find_path('w')
            Travel('w')
            traversalPath.append('w')

        elif direction == 'w' and previous !=  direction:
            Travel('w')
            traversalPath.append('w')
            find_path('e')
            Travel('e')
            traversalPath.append('e')



def Travel(direction):
    print(f"Direction: {direction}")
    player.travel(direction)
    

find_path()
print(f"Traversal Path: {traversalPath}")



r =requests.post('https://t7-api.herokuapp.com/init') 
r.header = 'Authorization: Token ac6e9fac44b48a6974eb8add0a3715184057be52'
print(r.text)

