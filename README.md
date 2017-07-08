# cardOpener
automatically opens both kinds of TI7 player card packs

# requirements
* python 3 : Tested on 3.6.1rc1
* `steam` : https://github.com/ValvePython/steam/
* `dota2` : dota2-0.2.8.willr.zip, based on https://github.com/ValvePython/dota2
* these packages will automatically install their dependencies, which include `gevent`, `protobuf`, `requests`
* a valve web api key : http://steamcommunity.com/dev/apikey

# install
* download this repository to a folder
* using pip, install steam following instructions on their repo
* navigate to where you downloaded this repository
* in the folder with dota2-0.2.8.willr.zip, open a command prompt and run `pip install dota2-0.2.8.willr.zip`
* if you have a previous version of `dota2` installed, run `pip install --no-deps --upgrade --force-reinstall dota2-0.2.8.willr.zip`
* run script with `python cardOpener.py` and follow the instructions

# Issues?
bother me on steam/discord please
