import time
import os
from mapqueue import Queue

# sets the queue to the maps folder. Don't worry, this isn't hardcoded like most other paths in here.       Either way, temporary
fila = Queue(".\maps")

# test stuff
print(f"CurrentMap: {fila.current_map}")
print(f"NextMap: {fila.next_map}")

#print(fila.current_map[32:-4])
os.system(f"start C:\steamcmd\css_ds\srcds.exe -console -game cstrike -secure +maxplayers 22 +map {fila.current_map[32:-4]}")
# the weird shit (32:-4) excludes the path section of the map file name and file extension with period included. Not very elegant

# Does exactly what the function name says:
def killandrestart():
    os.system('taskkill /F /FI "WindowTitle eq  Counter-Strike: Source" /T') # finds a window with name "Counter-Strike: Source" (does not conflict with actual Counter Strike Source process)
    fila.switchMaps() # forgot what this does but ACSEGAT told me to add it in so yeah
    os.system(f"start C:\steamcmd\css_ds\srcds.exe -console -game cstrike -secure +maxplayers 22 +map {fila.current_map[32:-4]}") # restarts the server

# while the script runs...
while True:
    time.sleep(25) # wait some amount of time then restarts the server ( you can change this to any period of time specified in seconds, kept 25 here for debugging purposes )
    killandrestart() # bye bye server! tell people to rejoin
