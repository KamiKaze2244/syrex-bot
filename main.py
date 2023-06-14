import discord
from discord.ext import commands
import time
import serverdata

#bu mesaj şimdilik

Bot = commands.Bot(command_prefix= "s!", intents= discord.Intents.all())

token = input("tokeni girin : ")

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
    
@Bot.command()
@commands.has_permissions(manage_messages=True)
async def sil(ctx, amount=5):
    await ctx.channel.purge(limit=amount+1)
    await ctx.send(f'{amount} adet mesaj silindi!')
    
@Bot.command()
@commands.has_permissions(manage_roles=True)
async def sustur(ctx, member: discord.Member):
    mute_role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not mute_role:
        # Eğer "Muted" adında bir rol yoksa, rolü oluşturabilirsiniz.
        mute_role = await ctx.guild.create_role(name='Muted')
        # Gerekli kanallardan mesaj yazma iznini kaldırın
        for channel in ctx.guild.channels:
            await channel.set_permissions(mute_role, send_messages=False)
    
    await member.add_roles(mute_role)
    await ctx.send(f'{member.mention} susturuldu.')

@Bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Hoşgeldin mesajını göndereceğiniz kanalı belirtin
    if channel is not None:
        await channel.send(f'Hoş geldin {member.mention}!')  # Hoşgeldin mesajını gönderin
        
      
@Bot.command()
async def play(ctx):
    time.sleep(2)
    await ctx.send("bir hata oluştu ")


Bot.run(token)
