import discord
from discord.ext import commands
import time
from settings import token
from settings import channelid
 

Bot = commands.Bot(command_prefix= "s!", intents= discord.Intents.all())

print("\n")

@Bot.event
async def on_ready():
    channel = Bot.get_channel(int(channelid))
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
    time.sleep(2)
    print("bot başarıyla çalıştırıldı!")
    await channel.send(f"**{Bot.user.name}**, Çalıştırıldı!")
    print("\n")

            
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
async def developer(ctx):
    await ctx.send("**Discord Bot Developer**, `Kamikaze#0011` **Github ->** https://github.com/KamiKaze2244")

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
