import os
import json
import cog
source= "./veriler/sunucular.json"

def set_channel(channel):
    channelID=channel.id
    guildID=channel.guild.id

    if os.path.isfile(source):
        with open(source, 'r') as fp:
            myGuild = json.load(fp)
            
            if guildID in myGuild:
                myGuild[guildID]['hgkanali']=channelID
                with open(source, "w") as fp:
                    json.dump(myGuild,fp,indent=4)
            else:        
                myGuild[guildID] = {}
                myGuild[guildID]['hgkanali']=channelID
                with open(source, "w") as fp:
                    json.dump(myGuild,fp,indent=4)

    else:
        myGuild = {}
        myGuild[guildID] = {}
        myGuild[guildID]['hgkanali']=channelID
        with open(source, "w") as fp:
            json.dump(myGuild,fp,indent=4)

def get_channel(guild):
    guildID = guild.id
    if os.path.isfile(source):
        with open(source,'r') as fp:
            myGuild = json.load(fp)
        if guildID in myGuild:
            try:
                return myGuild[guildID]['hgkanali']
            except KeyError:
                return None
            else:
                return None
    else:
        return None
