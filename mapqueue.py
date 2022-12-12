import os, time
import random
import shutil
from map import Map

def random_map_name(folder): #global for __init__ usage

    map = random.choice(os.listdir(folder))
    return map

def clear_dir(folder):

    for f in os.listdir(folder):
        os.remove(f"./{folder}/{f}")


class Queue:

    def __init__(self, map_pool, queue_folder):

        self.map_pool = map_pool #useful variable for future functions, references where the files will be picked from
        self.queue_folder = queue_folder # references where the files will be sent to

        current_map_name = random_map_name(map_pool)

        self.current_map = Map(queue_folder, current_map_name) # generates map object for queue object
        shutil.copy(f"{map_pool}/{current_map_name}", self.current_map.path) # creates the object generated in target folder

        next_map_name = current_map_name

        while(next_map_name == current_map_name): # this loops makes sure tha next_map != current_map
            next_map_name = random_map_name(map_pool)

        self.next_map = Map(queue_folder, next_map_name)
        shutil.copy(f"{map_pool}/{next_map_name}", self.next_map.path)

    
    def switchMaps(self):


        previous = self.current_map.name # saving the previously played map so you dont play it twice

        shutil.copy(self.next_map.path, self.current_map.path) #switches content
        
        os.remove(self.current_map.path) #clears the queue of last map

        self.current_map = Map(self.next_map.dir, self.next_map.name_extension) # copyes next_map into current_map

        while(self.next_map.name == self.current_map.name or self.next_map.name == previous): # checks so that next_map is differente from both current_map and previous
            # the [:-4] int the while condition is so the names are compared without the file extentions
            self.next_map = Map(self.next_map.dir, random_map_name(self.map_pool))



        shutil.copy(f"{self.map_pool}/{self.next_map.name_extension}", self.next_map.path) #aplies new next_map




    def showQueue(self): # mainly debug purpose

        print(f"The current map is {self.current_map.name} and the next one is {self.next_map.name}")





# random debug code
""" q = Queue("./maps", "./server_queue")

q.showQueue()

time.sleep(5)

q.switchMaps()
q.showQueue() """









