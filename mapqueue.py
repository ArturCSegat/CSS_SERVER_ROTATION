import os, time
import random
import shutil

def random_map(folder): #global for __init__ usage

    map = random.choice(os.listdir(folder))
    return map

def clear_dir(folder):

    for f in os.listdir(folder):
        os.remove(f"./{folder}/{f}")


class Queue:

    def __init__(self, folder):



        self.folder = folder
        
        origin = folder # redundant lol??

        current_name = random_map(origin)

        next_name = current_name

        while(next_name == current_name): # so current and next are always different
            next_name = random_map(origin)

        shutil.copy(f"{origin}/{current_name}", f"./server_queue/{current_name}") #so names are constanst just change the content
        shutil.copy(f"{origin}/{next_name}",f"./server_queue/{next_name}")
        

        self.current_map = f"./server_queue/{current_name}" #just path
        self.next_map = f"./server_queue/{next_name}"

    
    def switchMaps(self):

        previous = self.current_map # saving the previously played map so you dont play it twice

        shutil.copy(self.next_map, self.current_map) #switches content
        
        os.remove(self.current_map)

        self.current_map = self.next_map # switches state in class


        next_path = self.current_map

        while(f"./server_queue/{next_path}" == f"./server_queue/{self.current_map}" or f"./server_queue/{next_path}" == f"./server_queue/{previous}"): # fds gambiarra doida
            next_path = random_map(self.folder)
        
        self.next_map = f"./server_queue/{next_path}"
        shutil.copy(f"./{self.folder}/{next_path}", self.next_map)






       

                    
            
        

    def showQueue(self):

        print(f"The current map is {self.current_map} and the next one is {self.next_map}")


 # random debug code

queue = Queue('.\maps') 

queue.showQueue()

time.sleep(5)

queue.switchMaps()

queue.showQueue()










