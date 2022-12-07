import os, time
import random
import shutil

def random_map(folder): #global for __init__ usage

    map = random.choice(os.listdir(folder))
    return map


class Queue:

    def __init__(self, folder):

        self.folder = folder
        
        origin = folder # redundant lol??

        self.current_name = random_map(origin)

        self.next_name = self.current_name

        while(self.next_name == self.current_name): # so current and next are always different
            self.next_name = random_map(origin)

        shutil.copy(f"{origin}/{self.current_name}", './server_queue/current.txt') #so names are constanst just change the content
        shutil.copy(f"{origin}/{self.next_name}", './server_queue/next.txt')
        

        self.current_map = './server_queue/current.txt' #just path
        self.next_map = './server_queue/next.txt'

    
    def switchMaps(self):

        previous = self.current_name # saving the previously played map so you dont play it twice
        

        shutil.copy(self.next_map, self.current_map) #switches content



        self.current_name = self.next_name # switches name

        while (self.next_name == self.current_name or self.next_name == previous): # so current and next are always different
            self.next_name = random_map(self.folder)
            shutil.copy(f"{self.folder}/{self.next_name}", self.next_map)
        

    def showQueue(self):

        print(f"The current map is {self.current_name} and the next one is {self.next_name}")


 # random debug code

""" queue = Queue('.\maps') 

queue.showQueue()

time.sleep(5)

queue.switchMaps()

queue.showQueue() """










