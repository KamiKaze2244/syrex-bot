import discord
from discord.ext import commands
import time
import serverdata

Bot = commands.Bot(command_prefix= "s!", intents= discord.Intents.all())

@Bot.event
async def on_ready():
    await Bot.load_extension("cog") 
    print("""
   _____               __   __
  / ____|              \ \ / /
 | (___  _   _ _ __ ___ \ V / 
  \___ \| | | | '__/ _ \ > <  
  ____) | |_| | | |  __// . \ 
 |_____/ \__, |_|  \___/_/ \_
          __/ |               
         |___/  
    
    """)
    time.sleep(3)
    print("son güncellemeler kontrol ediliyor...")
    time.sleep(4)
    print("bot başarıyla çalıştırıldı!")
    print("\n")

    
    async def on_member_join(self, member):
        channelID = serverdata.get_channel(member.guild)
        if channelID != None or channelID != '0':
            channel = self.get_channel(channelID)
            if channel:
                await channel.send("Sunucumuza {} isimli bir kullanıcı katıldı!".format(member.mention))
            else:
                return
            
@Bot.event
async def on_member_join(member: discord.Member):
    print(member.name, "sunucuya katıldı")
    print("\n")

@Bot.event
async def on_member_remove(member: discord.Member):
    print(member.name, "sunucudan ayrıldı")
    print("\n")

@Bot.event
async def on_guild_channel_create(channel: discord.TextChannel):
    print(channel.name, "isimli bir oda oluşturuldu")
    print("\n")

@Bot.event
async def on_guild_channel_delete(channel: discord.TextChannel):
    print(channel.name, "isimli bir oda silindi")
    print("\n")
    
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} messages deleted.')



Bot.run("MTExNjczNDQ4ODg4MjQ2MjgzMA.Gd8Dqf.VFDSw96932zdFGCXeuCFk-WDtWL5MfYE_46JNY")
