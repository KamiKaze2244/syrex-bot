import discord
from discord.ext import commands
import time
import serverdata


Bot = commands.Bot(command_prefix= "s!", intents= discord.Intents.all())

token = input("tokeni girin : ")
print("\n")

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
@commands.has_permissions(administrator=True)
async def sil(ctx, silis=5):
    await ctx.channel.purge(limit=silis+1)
    await ctx.send(f'{silis} adet mesaj silindi!')
    
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

@Bot.command()
async def sunucubilgi(ctx):
member_count = len(ctx.guild.members)
await ctx.send(f"""`Sunucu bilgileri;¹
Sunucudaki anlık aktif kişi sayısı : {member_count}`""")
   
@Bot.command()
async def github(ctx):
    user = ctx.author
    await user.send("https://github.com/KamiKaze2244")

@Bot.event
async def on_member_join(member):
    channel = member.guild.system_channel  # Hedeflenen oda ID'sini buraya girin
    if channel is not None: #burası olmasada çalışır eğer channel id girilmediyse terminalde hata verir program durur
        await channel.send(f"Merhaba {member.mention}, hoş geldin!")

@Bot.event
async def on_member_remove(member):
    channel = member.guild.system_channel
    if channel is not None: #burası olmasada çalışır eğer channel id girilmediyse terminalde hata verir program durur
        await channel.send(f"Görüşürüz {member.name}, hoşça kal!")
        
      
@Bot.command()
async def play(ctx):
    time.sleep(2)
    await ctx.send("bir hata oluştu ")


Bot.run(token)
