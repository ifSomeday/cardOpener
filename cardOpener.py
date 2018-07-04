from gevent import monkey
monkey.patch_ssl()

from steam import SteamClient
from dota2 import Dota2Client
from dota2.enums import EDOTAGCMsg
from steam import WebAPI
import time

client = SteamClient()
dota = Dota2Client(client)

OPEN_SPEED = 0.2

api_key = ''
api = ''

print("\n\nDue to limitations imposed by valve (fuck you skin gambling) you will need:")
print("\t1. An API KEY")
print("\t2. Your profile and inventory temporarily set to public")
print("API keys can be optained easily from: http://steamcommunity.com/dev/apikey\n\n")

while True:
    api_key = input("Enter your API key: ")
    try:
        api = WebAPI(key = api_key)
        break
    except:
        print("invalid key")

print("You will now be prompted to log in. You will not see any input when entering password.")

@client.on('logged_on')
def start_dota():
    print("Logged into steam, starting dota")
    dota.launch()
    pass

@dota.on('ready')
def ready0():
    print("Preparing to open.\nSometimes, if requests are recieved too fast they will be ignored.\nThe bot will go through several iterations to open all of them")
    res = get_inventory()
    print("Inventory retreived")
    packs = find_packs(res)
    if(len(packs) == 0):
        print("no packs found, exiting...")
        client.logout()
        exit()
    while(len(packs) > 0):
        print("found " + str(len(packs)) + " card packs")

        print("opening packs", end='')
        open_packs(packs)
        print("opening complete")

        res = get_inventory()
        packs = find_packs(res)
        if(len(packs) > 0):
            print("not all packs opened... trying again")
    client.logout()
    exit()

@dota.on('notready')
def reload():
    print("out of dota. If you have more packs to open, restart the program...")
    pass

def get_inventory():
    res = api.IEconItems_570.GetPlayerItems(steamid=client.user.steam_id)['result']
    while(not res['status'] == 1):
        if(res['status'] == '15'):
            print("Inventory or profile private. Please make both public.")
        else:
            print("failed:\n\tstatus: " + str(res['status']) + "\n\tdetails: " + str(res['statusDetail']))
        print("Trying again in 30 seconds...")
        time.sleep(30)
        res = api.IEconItems_570.GetPlayerItems(steamid=client.user.steam_id)['result']
    return(res)

def find_packs(inventory):
    pack_ids = []
    for item in inventory['items']:
        ##TI7 = 17297 17272
        if(item['defindex'] == 17430 or item['defindex'] == 17431):
            pack_ids.append(item['id'])
    return(pack_ids)

def open_packs(packs):
    i = 0
    for pack in packs:
        i += 1
        jobid = dota.send(EDOTAGCMsg.EMsgClientToGCOpenPlayerCardPack, {'player_card_pack_item_id' : pack})
        if(not OPEN_SPEED == 0):
            time.sleep(OPEN_SPEED)
        if(i % 5 == 0):
            print('.', end='', flush=True)
    print("")

client.cli_login()
client.run_forever()
