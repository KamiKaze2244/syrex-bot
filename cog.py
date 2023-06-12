import discord
from discord.ext import commands
import serverdata
import random
import time

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    
    @commands.command()
    async def yazdır(self, ctx, *, mesaj):
        await ctx.message.delete()
        await ctx.send(mesaj)

    @commands.command()
    async def selam(self, ctx):
        await ctx.send("selamm!! c:")

    @commands.command()
    async def espiri(self, ctx):
            e = random.randint(1,5)
            if e==1:
                await ctx.send("Al işte..")
                time.sleep(1)
                await ctx.send("Annen s*k*şte :)")
            elif e==2:
                await ctx.send("Tuvaletteki 10’a ne denir? ")
                time.sleep(1)
                await ctx.send("Sifon")
            elif e==3:
                await ctx.send("Yemeğin suyuna kim bandı?")
                time.sleep(1)
                await ctx.send("Koli bandı")
            elif e==4:
                await ctx.send("Siviller hangi dili konuşur? ")
                time.sleep(1)
                await ctx.send("Sivilce")
            elif e==4:
                await ctx.send("Bozuk paran var mı? ")
                time.sleep(1)
                await ctx.send("Yok çünkü hepsini tamir ettirdim")
            elif e==5:
                await ctx.send("Küçük su bitikintisine ne denir? ")
                time.sleep(1)
                await ctx.send("Sucuk")


    @commands.command()
    async def piç(self, ctx, *, name):
        b = random.randint(1,3)
        if b ==1:
            await ctx.send(f"oha ilk defa bir piç görüyorumm **{name}** aynı götverene benziyorsunn :face_with_hand_over_mouth: ")
        elif b==2:
            await ctx.send(f"senin ne işin var lan burada **{name}** piçler giremez yazmıyormuydu defol buradan")
        elif b==3:
            await ctx.send(f"jale hocanın çocuğumusunuz acaba **{name}**?")
        await ctx.message.delete()
    
    @commands.command()
    async def orospu(self, ctx, *, name):
        a = random.randint(1,3)
        if a==1:
            await ctx.send(f"aha orospu evladı varmış burada **{name}** aynı bana benziyorsun :joy: ")
        elif a==2:
            await ctx.send(f"1 vuruş kaç kuruş **{name}**")
        elif a==3:
            await ctx.send(f"**{name}** nekadara vurduruyon :) ")
        await ctx.message.delete()
        

    @commands.command()
    async def kanalbelirle(self, ctx, kanal:discord.TextChannel):
        try:
            serverdata.set_channel(kanal)
            await ctx.send("kanal belirlendi")
        except:
            await ctx.send("bir hata oldu")

    @commands.command()
    async def yardım(self, ctx):

        await ctx.send("""`Komutlar;           
s!selam             
s!random            
s!espiri            
s!hentai            
s!piç @etiket       
s!orospu @etiket    `   
                       """)

    @commands.command()
    async def random(self, ctx,):
        n = random.randint(1,12)
        if n==1:
            await ctx.send("al yarasın koçuma benim!")
            await ctx.send("https://media.discordapp.net/attachments/1079058681045471406/1079060582721921124/doublepica.gif")
        elif n==2:
            await ctx.send("oy kalktı :face_with_hand_over_mouth:")
            await ctx.send("https://media.discordapp.net/attachments/1016993729032228864/1051932086040272967/xbox-2.gif")
        elif n==3:
            await ctx.send("https://media.discordapp.net/attachments/798273810838847509/1041632085514915851/femboy_says_discord_13-1.gif")
        elif n==4:
            await ctx.send("https://media.discordapp.net/attachments/975391283549986877/1007319080669290546/pervers_meme.gif")
        elif n==5:
            await ctx.send("https://tenor.com/view/vegan-porn-carrot-porn-happy-gif-14676153")
        elif n==6:
            await ctx.send("https://media.discordapp.net/attachments/1108196366007664660/1109231436822753421/2.gif")
        elif n==7:
            await ctx.send("https://media.discordapp.net/attachments/781495154786697226/1012061678155866112/caption.gif")
        elif n==8:
            await ctx.send("https://media.discordapp.net/attachments/1004744879500447906/1022530147561259058/MUAHAHAHAH.gif")
        elif n==9:
            await ctx.send("https://tenor.com/view/punching-boxing-penis-gif-18222057")
        elif n==10:
            await ctx.send("https://media.discordapp.net/attachments/947903750155173900/990593282063093800/spin.gif")
        elif n==11:
            await ctx.send("kime oy verirdin :) aramızda kalsın ben **salak apoya** basarım :shushing_face:")
            await ctx.send("https://media.discordapp.net/attachments/923665531989557288/1107415736906960927/Yeni_proje.gif")
        elif n==12:
            await ctx.send("https://tenor.com/view/cum-the-cum-here-comes-the-cum-gif-18740280")

    @commands.command()
    async def hentai(self, ctx,): 
        d = random.randint(1,40)
        if d == 1:
            return await ctx.send("https://v.redd.it/7plqor46tx4b1/DASH_480.mp4") 
        elif d == 2:
            return await ctx.send("https://v.redd.it/0c6z2brpwr4b1/DASH_480.mp4")
        elif d ==3:
            return await ctx.send("https://v.redd.it/o4xqy5rifp4b1/DASH_480.mp4")
        elif d==4:
            return await ctx.send("https://v.redd.it/1gphzegbi64b1/DASH_480.mp4")
        elif d==5:
            return await ctx.send("https://v.redd.it/e75djtill34b1/DASH_480.mp4")
        elif d==6:
            return await ctx.send("https://v.redd.it/ed31han5nu3b1/DASH_480.mp4")
        elif d==7:
            return await ctx.send("https://v.redd.it/g3jt8eqdu23b1/DASH_480.mp4")
        elif d==8:
            return await ctx.send("https://v.redd.it/ouargub58y1b1/DASH_480.mp4")
        elif d==9:
            return await ctx.send("https://v.redd.it/zc5sokus5gza1/DASH_480.mp4")
        elif d==10:
            return await ctx.send("https://v.redd.it/zeff11qa3z0b1/DASH_480.mp4")
        elif d==11:
            return await ctx.send("https://v.redd.it/zeff11qa3z0b1/DASH_480.mp4")
        elif d==12:
            return await ctx.send("https://v.redd.it/syvfea8411ta1/DASH_480.mp4")
        elif d==13:
            return await ctx.send("https://v.redd.it/z2plwgg5tu4b1/DASH_480.mp4")
        elif d==14:
            return await ctx.send("https://v.redd.it/1hdt9obvbu4b1/DASH_480.mp4")
        elif d==15:
            return await ctx.send("https://v.redd.it/qktlbt27x8va1/DASH_480.mp4")
        elif d==16:
            return await ctx.send("https://v.redd.it/ibt38x2rrwwa1/DASH_480.mp4")
        elif d==17:
            return await ctx.send("https://v.redd.it/y5oo844kbl7a1/DASH_480.mp4")
        elif d==18:
            return await ctx.send("https://v.redd.it/u85seh1z4o4a1/DASH_480.mp4") 
        elif d==19:
            return await ctx.send("https://v.redd.it/6s8tztjp8x3b1/DASH_480.mp4")
        elif d==20:
            return await ctx.send("https://v.redd.it/7ff1wazvc7v91/DASH_480.mp4")
        elif d==21:
            return await ctx.send("https://imgur.com/380nRMV")
        elif d==22:
            return await ctx.send("https://v.redd.it/fszovo0c3k4b1/DASH_480.mp4")
        elif d==23:
            return await ctx.send("https://v.redd.it/qqc03hi3tqn91/DASH_480.mp4")
        elif d==24:
            return await ctx.send("https://v.redd.it/g5ln5avimkm91/DASH_480.mp4")
        elif d==25:
            return await ctx.send("https://v.redd.it/xyhmil4i09na1/DASH_480.mp4")
        elif d==26:
            return await ctx.send("https://v.redd.it/gtmj47azq3j91/DASH_480.mp4")
        elif d==27:
            return await ctx.send("https://v.redd.it/b4bugt6ckth91/DASH_480.mp4")
        elif d==28:
            return await ctx.send("https://v.redd.it/lpjuves050f91/DASH_480.mp4")
        elif d==29:
            return await ctx.send("https://v.redd.it/zbxa2qyji9391/DASH_480.mp4")
        elif d==30:
            return await ctx.send("https://v.redd.it/3r101dqydac91/DASH_480.mp4")
        elif d==31:
            return await ctx.send("https://v.redd.it/k0eky1mf5t991/DASH_480.mp4")
        elif d==32:
            return await ctx.send("https://v.redd.it/xjekcm38x5991/DASH_480.mp4")
        elif d==33:
            return await ctx.send("https://imgur.com/KefSELR")
        elif d==34:
            return await ctx.send("https://v.redd.it/s3w61lmmur691/DASH_480.mp4")
        elif d==35:
            return await ctx.send("https://v.redd.it/nb1r0qw9oh7a1/DASH_480.mp4")
        elif d==36:
            return await ctx.send("https://v.redd.it/51y6pnz1jj591/DASH_480.mp4")
        elif d==37:
            return await ctx.send("https://v.redd.it/auuqxjk3xzha1/DASH_480.mp4")
        elif d==38:
            return await ctx.send("https://v.redd.it/dtqyp0lz80591/DASH_480.mp4")
        elif d==39:
            return await ctx.send("https://v.redd.it/90tnlcwt0b591/DASH_480.mp4")
        elif d==40:
            return await ctx.send("https://v.redd.it/51y6pnz1jj591/DASH_480.mp4")
            




async def setup(bot):
    await bot.add_cog(Moderation(bot))