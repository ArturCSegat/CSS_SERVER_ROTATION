class Map:

    def __init__(self, dir, name):

        self.dir = dir
        self.name = name[:-4] # Removes the file extension from the map
        self.path = f"{dir}/{name}"

    