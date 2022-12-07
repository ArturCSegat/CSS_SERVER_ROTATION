import time
import os
from mapqueue import Queue

fila = Queue(".\maps")

print(f"CurrentMap: {fila.current_map}")
print(f"NextMap: {fila.next_map}")

print(fila.current_map[32:-4])
os.system(f"start C:\steamcmd\css_ds\srcds.exe -console -game cstrike -secure +maxplayers 22 +map {fila.current_map[32:-4]}")

def killandrestart():
    os.system('taskkill /F /FI "WindowTitle eq  Counter-Strike: Source" /T')
    fila.switchMaps()
    os.system(f"start C:\steamcmd\css_ds\srcds.exe -console -game cstrike -secure +maxplayers 22 +map {fila.current_map[32:-4]}")

while True:
    time.sleep(25)
    killandrestart()
