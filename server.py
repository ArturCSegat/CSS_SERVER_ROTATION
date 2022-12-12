import os
from mapqueue import Queue
class Server:

    def __init__(self, max_players, match_duration, server_origin):
        
        self.server_origin = server_origin
        self.max_players = max_players
        self.match_duration = match_duration * 60
        self.queue = Queue("./maps", f'{server_origin}/cstrike/maps')

    def startServer(self):
        os.system(f"start {self.server_origin}\srcds.exe -console -game cstrike -secure +maxplayers {self.max_players} +map {self.queue.current_map.name}")

    def nextMap(self):
        self.killServer()
        self.queue.switchMaps()
        self.startServer()
    
    def killServer(self):
        os.system('taskkill /F /FI "WindowTitle eq  Pe Conco Server" /T') # finds a window with name "Counter-Strike: Source"

