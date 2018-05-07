class Room:
    """
    Representation of a room in Adventure
    """

    def __init__(self, id, name, description):
        """
        Initialize a Room
        give it an id, name and description
        """
        # TODO
        pass

    def __str__(self):
        """
        Returns a string representation of the room like so:
        "room <id>: <name>"
        i.e. "room 1: Inside Building"
        """
		# TODO
        pass

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))

class Object:
    """
    Representation of an Object in Adventure
    """

    def __init__(self, name, description):
        """
        Initialize an Object
        give it a name and description
        """
        # TODO
        pass

    def __str__(self):
        """
        Returns a string representation of the object like so:
        "<name>: <description>"
        i.e. "KEYS: a set of keys"
        """
        # TODO
        pass

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __hash__(self):
        return hash(repr(self))

def loadRooms(filename):
    """
    load rooms from filename
    returns a list of Room objects
    """
    with open(filename, "r") as f:
        # TODO
        pass

def loadObjects(filename):
    """
    load objects from filename
    returns a list of Object objects
    """
    with open(filename, "r") as f:
        # TODO
        pass

def play():
    """
    Play the Adventure game
    """

    game = "Tiny"
    rooms = loadRooms(f"{game}Rooms.txt")
    # objects = loadObjects("f{game}Objects.txt")

    # TODO

if __name__ == "__main__":
    # stap 1
    # print("stap 1")
    # rooms = loadRooms("TinyRooms.txt")
    # for room in rooms:
    #     print(room)

    # stap 2
    # print("stap 2")
    # rooms = loadRooms("TinyRooms.txt")
    # print(rooms[0].move("WEST")) # should print room 2: End of road
    # print(rooms[0].move("IN")) # should print room 3: Inside building
    # print(rooms[0].move("WEST").move("EAST")) # should print room 1: Outside building
    # print(rooms[0].move("OUT")) # should print: None

    pass
