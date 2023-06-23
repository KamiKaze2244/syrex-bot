import discord
from discord.ext import commands
import serverdata
import random
import time

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def yazdır(self, ctx, *, mesaj):
        await ctx.message.delete()
        await ctx.send(mesaj)
        
    @commands.command()
    async def selam(self, ctx):
        await ctx.send("selamm!! c:")

    @commands.command()
    async def zenci(self, ctx):
        await ctx.send("yapma dostum böyle bir komut yok hiç komik değilsin :ı")
        
    @commands.command()
    async def niga(self, ctx):
        await ctx.send("yapma dostum böyle bir komut yok hiç komik değilsin :ı")


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
s!play              
s!hentai            
s!boobs             
s!developer         
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
        
    @commands.command()
    async def boobs(self, ctx):
        b = random.randint(1, 20)
        if b == 1:
            await ctx.send("https://thechive.com/wp-content/uploads/2021/11/Bad-09_18_20-GIF-04-2.mp4?attachment_cache_bust=3875256")
        elif b ==2:
            await ctx.send("https://thechive.com/wp-content/uploads/2021/11/Bad-02_28_20-GIF-21-dbsciacca_rainbow.mp4?")
        elif b ==3:
            await ctx.send("https://thechive.com/wp-content/uploads/2021/11/Bad-02_28_20-GIF-21-dbsciacca_rainbow.mp4?attachment_cache_bust=3875253")
        elif b ==4:
            await ctx.send("https://i.gifer.com/1myU.gif")
        elif b ==5:
            await ctx.send("https://blovjob.com/content/2022/09/soft-tits-gifs_001.gif")
        elif b ==6:
            await ctx.send("https://nudebabes.realnakedgirls.net/wp-content/uploads/2019/12/perfect-example-of-perfection-bobobobobobobobobo-1577202032lc84p.mp4?_=1")
        elif b ==7:
            await ctx.send("https://cdn.sex.com/images/pinporn/2019/10/23/22032940.gif?width=620")
        elif b ==8:
            await ctx.send("https://64.media.tumblr.com/49f7f6c914b99e962397e8c56eb78660/tumblr_pia5djKFUT1wntbg1o2_400.gif")
        elif b ==9:
            await ctx.send("https://tse1.mm.bing.net/th?id=OIP.SWqFAyeeMM_LCUtrNENZXwAAAA&pid=15.1")
        elif b ==10:
            await ctx.send("https://tse1.mm.bing.net/th?id=OIP.QKDnbAd9Iboo7VYARW5cEwHaKz&pid=15.1")
        elif b ==11:
            await ctx.send("http://static-ca-cdn.eporner.com/photos/828196.gif")
        elif b == 12:
            await ctx.send("http://static-ca-cdn.eporner.com/gallery/Yc/mq/qtyhj3HmqYc/40637-squeeze-and-release.gif")
        elif b ==13:
            await ctx.send("https://cdn5-images.motherlessmedia.com/images/7CB3ED0.gif")
        elif b ==14:
            await ctx.send("https://tse3.mm.bing.net/th?id=OIP.eAvbn4FlDSHKmfvWKEQwxAAAAA&pid=15.1")
        elif b ==15:
            await ctx.send("https://tse3.mm.bing.net/th?id=OIP.kyz30Md4YRaZ55ck19y1uwHaFj&pid=15.1")
        elif b ==16:
            await ctx.send("https://www.pbh2.com/wordpress/wp-content/uploads/2015/08/bouncing-boobs-gifs.gif")
        elif b ==17:
            await ctx.send("https://i.gifer.com/78f6.gif")
        elif b ==18:
            await ctx.send("https://cdn.sex.com/images/pinporn/2018/07/24/19760644.gif?width=620")
        elif b ==19:
            await ctx.send("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2EwZjlhODU3OTA0MTQ4ZDM5ZmM4OWM2ODA4OTA4MTU2NTg4MmE1MSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/jxwPJ8ro1lM8E/giphy.gif")
        elif b ==20:
            await ctx.send("https://cdn.sex.com/images/pinporn/2019/06/12/21313092.gif?width=620")
    
    @commands.command()
    async def sarkı(self, ctx):
        b = random.randint(1,8)
        if b ==1:
            await ctx.send("https://www.youtube.com/watch?v=Rw3fkAd8NCU")
        elif b ==2:
            await ctx.send("https://www.youtube.com/watch?v=Z2suDDoiiDc")
        elif b ==3:
            await ctx.send("https://www.youtube.com/watch?v=0IrnPGapTdQ")
        elif b ==4:
            await ctx.send("https://youtu.be/OIpEDP8YB7w")
        elif b ==5:
            await ctx.send("https://www.youtube.com/watch?v=Opm7Z6ZJ9vI")
        elif b ==6:
            await ctx.send("https://www.youtube.com/watch?v=ydAUUcPrOVY")
        elif b ==7:
            await ctx.send("https://www.youtube.com/watch?v=IhbRI2lDDHE")
        elif b ==8:
            await ctx.send("https://www.youtube.com/watch?v=ZD08o1q3JIY")



async def setup(bot):
    await bot.add_cog(Moderation(bot))
