import requests
import json
import requests
import time
from datetime import datetime
import time 

def sendmsg(msg):
    string = msg 
    url = 'https://api.telegram.org/YOURBOTURL/sendMessage' #your bot url here
    myobj = {'chat_id': 'YOURCHATID', 'text': msg} #your chat id here
    x = requests.post(url, data = myobj)

peoples_steamid_array = [["76561198078532888", "Name1"], ["76561198076135234", "Name2"], ["76561198105050455", "Name3"], ["76561198102330034", "Name4"], ["76561198127896843", "Name5"], ["76561198079828153", "Name6"]] #first SteamID. second Name of your choice

people_online = []
people_online_counter = 0
current_online = 0 

try:
    while True:

        for person in peoples_steamid_array:
            response = requests.get("http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=YOURKEYHERE&steamids={}".format( person[0]) ) #add steam api key here
            if response.status_code == 200:
                online_status = response.json()['response']['players'][0]['personastate']

                if(online_status == 1):
                    if(person[1] not in people_online):
                        people_online.append(person[1])
                        people_online_counter =+ 1
                
                if(online_status == 0 or online_status == 3):
                    if(person[1] in people_online):
                        people_online.remove(person[1])
                        people_online_counter =- 1
                
            else:
                print("error with api call")
        
        print("People online: " , people_online)

        if( len(people_online) >= 3 and len(people_online) > current_online ):
            string_people_online = ""
            for person in people_online:
                string_people_online +=  person + ", "
            
            sendmsg(string_people_online + "sind Online" )
	    print("timeouted 30 * 60")
            time.sleep(60 * 60) #20 min timeout after sending msg
            

        current_online = len(people_online)
        time.sleep(30) #20 secs

except Exception as e:
    print(e)


   
