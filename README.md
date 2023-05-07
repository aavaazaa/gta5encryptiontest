# GTA 5 PS3 encryption server testing

Right now this project is **NOT** an emulator for R* services (yet). This is mostly a test bench that could talk to the game through HTTP requests.

## The goal

As you might know the GTA Online for PS3 and Xbox 360 was officially shut down. But recently https://twitter.com/Tervel1337 has discovered that the online could work on the very first patches (1.06-1.12) on those consoles as the game allows you to create a temporary character on those versions, and it's infrastructure relies on PSN/Xbox Live for matchmaking. You can even run it in RPCS3 which provides RPCN, the PSN service emulation and connect to other people. Unfortunately due to shut down those versions, being fully functional, could not save progress and if you're running on RPCS3 you cannot join other players in jobs.

The main goal of this project is to make a server that can be compatible with the PS3 or Xbox 360 versions of the GTA V which will fill missing parts for the game at least in those tasks:

- Download job data (for RPCS3)
- Save online game data and load it afterwards

Still the project is nowhere near it, so right now it's mostly a test bench.

## Notes on accepting commits, if you want to help

While this can theoretically be used with other versions of GTA V on other platforms (well, theoretically, as those versions handle authorization and matchmaking differently) - right now the project is only focused on PS3 (maybe Xbox 360 version) of GTA V as those versions have it's online service shut down and the goal is to revive it. Commits regarding PC, Xbox One, PS4, Xbox Series S/X, PS5 will **NOT** be accepted in the near future as we don't want to interfere with current versions of official GTA Online service.

## Statement on donations

Any form of donations except code from anyone or from anywhere is **NOT** accepted. This is strictly a fan and non-commercial project. We, as a community, only want to earn the lost functionality, in this case, GTA Online for very first generation.

## Special thanks

The FiveM code gave me better understanding of what's going on with the encryption. So thank you guys.

## Install

`pip3 install -r requirements.txt`

## Start

`python3 testserver.py`

You also need a DNS server. Some routers can do this, or you can use something like `dnsmasq`. You need to point the host `prod.ros.rockstargames.com` to the IP of a server where your script is running. After that you're free to use this DNS server on your console/RPCS3 instance.

In RPCS3 you can use the IP/Host switch instead: `prod.ros.rockstargames.com=x.x.x.x`

## Additional scripts

This project has scripts to test the encryption - `clientdecode.py` and `serverdecode.py`. Client script can decrypt client data while server script can decrypt or encrypt server data. Such data could be obtained from the Wireshark (you should right click at the urlencoded encrypted data or encrypted XML then copy as a hex stream and paste it in the file you need).