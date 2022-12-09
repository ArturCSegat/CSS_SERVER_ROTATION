# Optimized Map Rotation for Counter Strike Source Servers

## DESCRIPTION
An attempt at optimizing disk space usage on Counter-Strike: Source servers by downloading the map files off a cloud service mid-match and keeping only 1 or 2 map files locally on the server machine, so to not keep a huge pool of maps downloaded at all times. Once the next map file has been downloaded, waits until a specified amount of time runs out and restarts the server, deleting the previous match's map.

Also planned discord integration so players can change/request maps mid match.

## TODO

* refactoring of server runner
* discord integration
