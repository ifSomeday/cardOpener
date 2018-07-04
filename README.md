# cardOpener
automatically opens both kinds of TI7 player card packs

# requirements
* python 3 : Tested on 3.6.1rc1
* `steam` : https://github.com/ValvePython/steam/
* `dota2` : https://github.com/ValvePython/dota2/
* these packages will automatically install their dependencies, which include `gevent`, `protobuf`, `requests`
* a valve web api key : http://steamcommunity.com/dev/apikey

# install
* Install Python3.x, which includes pip
* download (clone) this repository to a folder
* using pip, install steam/dota2 following instructions on their repo (linked above)
* navigate to where you downloaded this repository
* Close Steam on your desktop
* (Optional) Edit cardOpener.py with a text editor. Change the line `OPEN_SPEED = 0.2`. The number indicates the number of seconds to wait after opening one pack before moving on to another. The more packs you have to open, the bigger this should be. If you have less than 50, a speed of 0 is fine
* run script with `python cardOpener.py` and follow the instructions

# Issues?
bother me on steam/discord please
