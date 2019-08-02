import discord
from discord.ext import commands
import os
import traceback
import random
import math
import base64
import json
import re
import os
import datetime
import time
import asyncio
import requests
import io
import aiohttp
import textwrap
from PIL import Image,ImageDraw,ImageFont,ImageFilter

bot = commands.Bot(command_prefix='_',help_command=None)
client = discord.Client()
urulv = 0
routcount = 0
talklist = []
talkcount = []
nusi = ""
token = os.environ['DISCORD_BOT_TOKEN']
limit = 0
bosyuflag = 0
bosyulist = []

frdic={"ウルタン":b'NzI3NC0wNjkyLTQ1MTY=',"デコピン【R】":b'MDg1Ny0wODgzLTE3ODc=',"鮪":b'NTk4Ny0zOTkxLTQ0ODE=',"千秋":b'MTE1My0xOTU4LTc1MDM=',"リアル":b'MjcwNy01NjMyLTI5OTU=',
      "流星(Light)":b'NDY2OC02OTUzLTEzOTE=',"闇":b'Mjk5Ni0zOTM2LTU4NjQ=',"ゆっくりはやくタロウ":b'MTM5Ni02ODg4LTIyOTM=',"あげパン":b'MTc5Mi03NzUzLTY4OTE=',
      "ログ":b'ODU2Ni0yOTg4LTQ5NjE=',"ちゅんちゅん":b'NjAwMS0zNDk5LTMzMjg=',"goa":b'MjU4OS0yMDE3LTI0MTA=',"taki":b'MjMyMS04NTM2LTEyMzM=',"りある":b'MzUxOC02NDYyLTQ4OTk=',
      "カービィ":b'NTU1OC03NzYwLTkzOTk=',"カッシー":b'NTU0Mi0zNjM4LTQ4OTQ=',"さいつお":b'NjIyMi04NDk4LTc3OTk=',"root-1":b'MjkxNy00NTk1LTIyOTg=',"かろーら":b'MTE5My05Mzc4LTc0MTM=',
      "まさば":b'NTkzMy0xNzQ4LTEwMDU=',"ぬらねこX":b'MTUwMi03MzI4LTYxMjc=',"ThreeThird":b'MDM4Mi0zNjU2LTE5MDU=',"ゆうなぎ.":b'NTQwNi0xNzIyLTg5MDA=',"agelock":b'ODIwOS0zNjA1LTUzMDk=',
      "ゆどーふ":b'MTE4OS0yOTU4LTM0ODg='}

for i in frdic:
        frdic[i]=base64.b64decode(frdic[i]).decode("utf-8")

imdic={"スプラシューター":"DB3eW8uUIAAmtkG","スプラシューターコラボ":"DEr1IYZUMAEL5ti","スプラシューターベッチュー":"DnAkWdSV4AAJWlR",
       "パブロ":"DFUzvT2UAAAiHAd","パブロ・ヒュー":"DOQmbrpVAAA7u9d","パーマネント・パブロ":"D28vURdUcAQ4uc9",
       "ショッツル鉱山":"DZbK2EDVAAAuvbI","フジツボスポーツクラブ":"C3K5Ou1VcAAG-2z","マンタマリア号":"DIEFuh-UIAAAz_w"}

@bot.event
async def on_ready():
    print("動作を開始しました。")
    discord.opus.load_opus(libopus)
    if not discord.opus.is_loaded():
            raise RunTimeError('Opus failed to load')

    starttime = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).minute
    print("starttime:"+str(starttime))
    timediff = 60-starttime

    channel = bot.get_channel(572803866400391218)
    await bot.change_presence(activity=discord.Game(name='ウルタンアンチ'))

    await asyncio.sleep(timediff*60)
    print("ループ開始")
    nsyu = 0
    while 1:
            await asyncio.sleep(3600*2)
            print("n週目")
            string = random.choice(("ウルタンは反社と関わりを持ったため無期限謹慎処分になったことがある",\
                                "ウルタンはまさばより偏差値が高い",\
                                "ウルタンは文の最後の文字を二回書いたり語尾に小文字を付けがちでそれが不評だったのでメンヘラ化したらしい",\
                                "ウルタン㊙情報\nかっこいい（本人投稿）",\
                                "あげパンはYouTubeで毎日動画を投稿しているが、彼の動画の下ネタシーン集を収集する「Agepan Mania」というアカウントがある。\n"\
                                "「ウルタンは抜ける」「パンパンパンパンパン！パンパン！スーパーあげパンボム」"\
                                "「ベバンダ、リア、ゥ」などが有名である。",\
                                "くそ！","root-1は本来は存在しない数字なので彼の存在も幻覚である","誰がSSーM㊙情報じゃい！",
                                "くそ！とはリアルくんの隠喩である","かろーらはノンケ向け淫夢動画からエロゲに目覚めた",\
                                "I sue you for fraudulent charges and property damage charges!\nYou understand the reason, isn't it?"\
                                "Because you beat everyone with such a trick and destroyed save data! Please ready to be prepared for it."\
                                "Sue you before long. I also bring a trial. You must go the court whatever you say. Please be prepare the Palimony!"\
                                "You are a criminal! Please look forward to being thrown into jail! Are you?!",\
                                "【衝撃】ウルタンは引きこもり","【全米が涙】ウルタンはニート",\
                                "**おちばシューターウルタン**\nサブはポイントセンサー、スペシャルはインクアーマーだ"))
            embed = discord.Embed(title="SSーM㊙情報",description=string)
            await channel.send(embed=embed)
            nsyu += 1


@bot.event #反応単語
async def on_message(message):
    

    cont = message.content

    if cont=="!levels": #mee6用
        if message.guild.get_member(159985870458322944) is None:
            await message.channel.send("mee6が入ってないやん！")
            return
        string = requests.get("https://mee6.xyz/api/plugins/levels/leaderboard/"+str(message.guild.id)+"?=1").json()

        ranklist = []
        xplist = []
        strlist = []
        lvlist = []

        for i in range(len(string["players"])):
            ranklist.append(string["players"][i]["username"])
        
        for i in range(len(string["players"])):
            xplist.append(string["players"][i]["xp"])
        
        for i in range(len(string["players"])):
            lvlist.append(string["players"][i]["level"])

        for i in range(len(string["players"])):
            strlist.append(str(i+1).ljust(3," ")+"\t"+str(lvlist[i]).ljust(3," ")+"\t"+str(xplist[i]).ljust(7," ")+str(ranklist[i]))

        
        await message.channel.send("```"+"\n".join(strlist)+"```")
        return

    if message.author.bot:return #botを無視！

    global routcount
    global talklist
    global talkcount
    global nusi
    global bosyuflag
    global bosyulist

    if nusi in message.mentions:
        await message.channel.send("募集者にメンションしました。")
        bosyulist.append(message.author.id)
        return
    

    if "tw:@" in cont: #ツイッター
        s = message.content
        s = s+" "
        m = re.search('\@+[a-zA-Z0-9_]+[\a-zA-Z0-9_]', s)
        string = m.group(0).replace("@","https://twitter.com/")
        await message.channel.send(string)
      
    
    if "漏斗" in cont: #漏斗
        if routcount == 4:
            await message.channel.send(message.author.mention+"誰が漏斗じゃい！")
            routcount = 0
        else:
            routcount+=1
            
    if cont=='かわいくないよ': # かわいくない役職（総合ゲーム）
        if message.guild.id==586914633441607696:
            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='かわいい'))
            await message.author.add_roles(discord.utils.get(message.guild.roles, name='かわいくない'))
    if cont=='やっぱりかわいいよ': #かわいい役職（総合ゲーム）
        if message.guild.id==586914633441607696:
            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='かわいくない'))
            await message.author.add_roles(discord.utils.get(message.guild.roles, name='かわいい'))
            
    if cont.lower()=="!dc" or cont.lower()=="!disconnect" or cont.lower()=="!leave" or cont.lower()=="!dis" or cont.lower()=="!fuckoff":
        #dc反応（いちごおばけ）
        if message.guild.id==480522357467774976:
            await message.channel.send('❌ **I am not connected to a voice channel**, Use the summon command to get me in one')
            
    if bot.user in message.mentions: # 話しかけられたかの判定
        global limit
        if message.author.id in talklist: #著者が話者リストにあるなら、カウントを1増加
            if talkcount[talklist.index(message.author.id)] == limit:
                  talkcount[talklist.index(message.author.id)] = 0
            else:
                  talkcount[talklist.index(message.author.id)] += 1
                  return 
        now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).hour
        print(now)                                        
        if now>=22 or now<=3:
            greet = "おやすみー！"
        elif now>=4 and now<=10:
            greet = "おはよ"
        elif now>=11 and now<=15:
            greet = "こん"
        elif now>=16 and now<=21:
            greet = "こんばんは！"


        string = random.choice(("眠い","はらへった","なに？","返信だるい","こん","ばぶー？","ガハハｗ","うるせぇ、俺が法律だ。","くさそう",\
                      "http://urutan.com","ウルタンリーダーやめろ","ヘイト企業S■ーMは謝罪しろ！","SSーM評判悪いねｗｗｗｗ",\
                      "ウルタンは敗北者","ウルタン政治を許さない","ウルタンくさすぎ","こんなことしてないで勉強したら？w",\
                      "ウルタンは、邪知暴虐の王である。","ウルタンぶりぶりー","わなる","SSーM㊙情報\nウルタンの言っていることの99%は嘘",\
                      "【SS－Mのラジオ番組一覧】\n・ウルタンラジオ（ウルラジ）\n・rootラジオ（ルーラジ）\n・あげパンラジオ（あげラジ）",\
                      "SSーMの人たちは、不安よな。ウルタン、動きません（無能）","SSーMの人たちは、不安よな。ウルタン、動きません（ニート）"))
        await message.channel.send(message.author.mention+" "+greet+"\n"+string)
            
        #----------------------------------------------------------------------------
            
            
        if message.author.id not in talklist: #もし、リストに話者がなければ追加する
            talklist.append(message.author.id)
            talkcount.append(0)
            print(talklist)
            
            
    await bot.process_commands(message)


@bot.command() #プレイ中の表示を変更
async def play(ctx):
      
      string = random.choice(("妖怪ウォッチ4","スプラトゥーン2","大学受験","ウルタン天気予報","ウルタンラジオ","ウルタン不審者","テトリス99","フォートナイト",\
                              "リーグマッチ","ぼっちプラべ","rootラジオ","あげパンラジオ","音楽室"))
      await bot.change_presence(activity=discord.Game(name=string))

@bot.command()
async def summon(ctx):
      voice = ctx.guild.voice_client
      if ctx.author.voice == None:
          await ctx.send("ボイスチャンネルにいないよね？")
          return
      if voice is None:
          vc = ctx.author.voice.channel
          if vc==None:
              await ctx.send("君ボイスチャンネルにいないよね？")
              return
          voice = await vc.connect()
      #voice.play(discord.FFmpegPCMAudio('famipop3.mp3'))
      #player.start()

      #voice.play(discord.FFmpegPCMAudio('famipop2.mp3'))
      #await bot.change_presence(activity=discord.Game(name="famipop3"))

      
@bot.command()
async def dc(ctx):
      voice = ctx.guild.voice_client
      if voice:
          await voice.disconnect()
          #await bot.change_presence(activity=discord.Game(name="ウルタンアンチ"))
      else:
          await ctx.send('❌ **I am not connected to a voice channel**, Use the summon command to get me in one')
          #await bot.change_presence(activity=discord.Game(name="ウルタンアンチ"))
      

@bot.command()
async def decore(ctx,target:str,cont:str):
      string=""
      if target=="b" or target=="bold" or target=="strong" or target=="太字" or target=="太い" or target=="ふとい" or target=="太め" or target=="太":string="**"
      elif target=="i" or target=="italic" or target=="斜体" or target=="斜め" or target=="ななめ": string="*"
      elif target=="s" or target=="strike" or target =="deleted" or target=="取り消し線":string="~~"
      elif target.startswith('取り消'):string="~~"
      elif target=="u" or target=="アンダーライン" or target=="アンダーバー" or target=="下線" or target=="underline":string="__"
      elif target=="コード" or target=="code":string="```"
      elif target=="隠す" or target=="マスク" or target=="mask":string="||"
      await ctx.send(string+cont+string)
      
@bot.command()
async def umekomi(ctx,string1:str,string2:str):
      embed = discord.Embed(title=string1, description=string2,color=0x80ff00)
      embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
      await ctx.send(content=None,embed=embed)

'''
※削除されたコマンドです。
@bot.command() 
async def botsw(ctx):
      global switch
      if switch=="ON":switch="OFF"
      elif switch=="OFF":switch="ON"
      str = random.choice(("妖怪ウォッチ4","スプラトゥーン2","ウルタンくさい","大学受験","ウルタン天気予報","ウルタンラジオ","ウルタン不審者","健康ミネラルウル茶","ウルタン語彙力ない"))
      await bot.change_presence(activity=discord.Game(name=switch+'-'+str))
'''
      
@bot.command() #jsonファイルの読み書きテスト
async def jsontest(ctx,name:str):
      f = open('data1.json','r')
      fdic = json.load(f)
      await ctx.send(fdic[name]['twid'])
      f.close()
      
@bot.command()
async def idwrite(ctx):
      print("あなたのIDは"+str(ctx.author.id)+"です。")
      with open('/tmp/data.txt','a') as f:
            f.write(str(ctx.author.id)+"\n")
      print("書き込みました。")

@bot.command() #画像表示 URL一覧は上記辞書
async def spla(ctx,string:str):
      temp = ""
      temp = imdic.get(string)
      if temp != None:
            await ctx.send('https://pbs.twimg.com/media/'+temp+'.jpg')
      else:
            await ctx.send(string+'は見つかりませんでした')
            
@bot.command()
async def emo5000(ctx,string:str):
      if ctx.guild.id!=568427057076371457:
            await ctx.send('5000兆円絵文字未導入のサーバーです。')
            return
      daku = "<:muddy:598415020023480330>"
      string = string[:75]
      string = string.replace("あ","<:aa:596981155056582666>").replace("い","<:ii:596981205103017994>")\
                     .replace("う","<:uu:596981262451998730>").replace("え","<:ee:596981328575201281>")\
                     .replace("お","<:oo:596981372346695690>").replace("か","<:ka:596981589150400522>")\
                     .replace("き","<:ki:596981681173561344>").replace("く","<:ku:596981731085647872>")\
                     .replace("け","<:ke:596981779626328065>").replace("こ","<:ko:596981856939802625>")\
                     .replace("さ","<:sa:596982045368909834>").replace("し","<:si:596982100305903616>")\
                     .replace("す","<:su:596982151052918794>").replace("せ","<:se:596982205872472074>")\
                     .replace("そ","<:so:596982251233738752>").replace("た","<:ta:596982409292152852>")\
                     .replace("ち","<:ti:596982453088944128>").replace("つ","<:tu:596982489420136448>")\
                     .replace("て","<:te:596982540187860993>").replace("と","<:to:596982584240766978>")\
                     .replace("な","<:na:596982896921673728>").replace("に","<:ni:596982967935565843>")\
                     .replace("ぬ","<:nu:596983019487625216>").replace("ね","<:ne:596983059065208853>")\
                     .replace("の","<:no:596983092925956107>").replace("は","<:ha:596983261503160359>")\
                     .replace("ひ","<:hi:596983308391415809>").replace("ふ","<:hu:596983343195750400>")\
                     .replace("へ","<:he:596983385893634049>").replace("ほ","<:ho:596983424808648704>")\
                     .replace("ま","<:ma:596983793609342976>").replace("み","<:mi:596983834428309504>")\
                     .replace("む","<:mu:596983873317896192>").replace("め","<:me:596983908331946004>")\
                     .replace("も","<:mo:596983953064198144>").replace("や","<:ya:596985071479554049>")\
                     .replace("ゆ","<:yu:596985118737039370>").replace("よ","<:yo:596985157756387358>")\
                     .replace("ら","<:ra:596985291710005248>").replace("り","<:ri:596985334680649730>")\
                     .replace("る","<:ru:596985373293543429>").replace("れ","<:re:596985411704979468>")\
                     .replace("ろ","<:ro:596985455111700489>").replace("わ","<:wa:596985495129423884>")\
                     .replace("を","<:wo:596985533977067525>").replace("ん","<:nn:596985577568731147>")\
                     .replace("ぁ","<:aa:596981155056582666>").replace("ぃ","<:ii:596981205103017994>")\
                     .replace("ぅ","<:uu:596981262451998730>").replace("ぇ","<:ee:596981328575201281>")\
                     .replace("ぉ","<:oo:596981372346695690>").replace("ゃ","<:ya:596985071479554049>")\
                     .replace("ゅ","<:yu:596985118737039370>").replace("ょ","<:yo:596985157756387358>")\
                     .replace("ゎ","<:wa:596985495129423884>").replace("が","<:ka:596981589150400522>"+daku)\
                     .replace("ぎ","<:ki:596981681173561344>"+daku).replace("ぐ","<:ku:596981731085647872>"+daku)\
                     .replace("げ","<:ke:596981779626328065>"+daku).replace("ご","<:ko:596981856939802625>"+daku)\
                     .replace("ざ","<:sa:596982045368909834>"+daku).replace("じ","<:si:596982100305903616>"+daku)\
                     .replace("ず","<:su:596982151052918794>"+daku).replace("ぜ","<:se:596982205872472074>"+daku)\
                     .replace("ぞ","<:so:596982251233738752>"+daku).replace("だ","<:ta:596982409292152852>"+daku)\
                     .replace("ぢ","<:ti:596982453088944128>"+daku).replace("づ","<:tu:596982489420136448>"+daku)\
                     .replace("で","<:te:596982540187860993>"+daku).replace("ど","<:to:596982584240766978>"+daku)\
                     .replace("ば","<:ha:596983261503160359>"+daku).replace("び","<:hi:596983308391415809>"+daku)\
                     .replace("ぶ","<:hu:596983343195750400>"+daku).replace("べ","<:he:596983385893634049>"+daku)\
                     .replace("ぼ","<:ho:596983424808648704>"+daku).replace("ぱ","<:ha:596983261503160359>"+daku)\
                     .replace("ぴ","<:hi:596983308391415809>"+daku).replace("ぷ","<:hu:596983343195750400>"+daku)\
                     .replace("ぺ","<:he:596983385893634049>"+daku).replace("ぽ","<:ho:596983424808648704>"+daku)\
                     .replace("ー","<:__:596969408799309826>").replace("っ","<:tu:596982489420136448>")
      
      #.replace("R",":ReTweet: ").replace("F",":favorite: ").replace("s",":Splat_masaback: ")
      
      await ctx.send(string[:2000])

      '''
      string = string.replace("あ","a").replace("い","i").replace("う","u").replace("え","e").replace("お","o")\
                     .replace("か","ka").replace("き","ki").replace("く","ku").replace("け","ke").replace("こ","ko")\
                     .replace("さ","sa").replace("し","si").replace("す","su").replace("せ","se").replace("そ","so")\
                     .replace("た","ta").replace("ち","ti").replace("つ","tu").replace("て","te").replace("と","to")\
                     .replace("な","na").replace("に","ni").replace("ぬ","nu").replace("ね","ne").replace("の","no")\
                     .replace("は","ha").replace("ひ","hi").replace("ふ","hu").replace("へ","he").replace("ほ","ho")\
                     .replace("ま","ma").replace("み","mi").replace("む","mu").replace("め","me").replace("も","mo")\
                     .replace("や","ya").replace("ゆ","yu").replace("よ","yo").replace("わ","wa").replace("を","wo")\
                     .replace("ん","n").replace("ぁ","xa").replace("ぃ","xi").replace("ぅ","xu").replace("ぇ","xe")\
                     .replace("ぉ","xo").replace("い","i").replace("う","u").replace("え","e").replace("お","o")
       '''
      
      

@bot.command() #チーム生成
async def team(ctx,num:int):
      
      import random
      import math
      sead = [0] * num
      test = 0
      red = math.floor(num/2)
      for i in range(num):
            #初期配列を生成
            sead[i] = random.randrange(2)
      i=0
      for i in range(red):
            test += sead[i]
            #赤チームの現人数はtest=青チームの残り人数（test）、青チームの現人数=赤チームの残り人数（4-test）
    
      start = random.randrange(red)
      i=0
      for i in range(red):
            sead[i+red]=0
      record = 0
      i=0
      while i<red-test:
            sead[red+record+start] = 1
            i+=1
            record += 1
            if start+record==red:
                  record =0
                  start =0
      temp = [""]*num
      for i in range(num):
            if sead[i]==0:
                  temp[i]='参加者['+str(i)+']\tチームA'
            else: temp[i]='参加者['+str(i)+']\tチームB'
            string = "\n".join(temp)
      await ctx.send(ctx.author.mention+'\n'+string)
      


@bot.command() #いらない
async def bosyu(ctx,rule:str,open:str,*,come):

      if ctx.author.id!=519434882460549169:
          return
      global nusi
      global bosyuflag
      global bosyulist

      if rule != "n" and rule!= "r" and rule != "s" and rule!="p":
          await ctx.send("ルールが正しく入力されていません！\n"\
                         "**n**：ナワバリバトル\n"\
                         "**r**：リーグマッチ\n"\
                         "**s**：サーモンラン\n"\
                         "**p**：プライベートマッチ  と指定できます。")
          return

      if open is None:
          await ctx.send("時刻が入力されていません！\n"\
                         "時刻は ```00:00``` のように指定します。")
          return

      match = re.match(r'[0-9]{2}:[0-9]+', open)

      if match is None:
          await ctx.send("時刻が入力されていません！\n"\
                         "時刻は ```00:00```のように指定します。")
          return
      else:
          print(match.group(0))
          shour = re.split(r':', open)[0]
          smin = re.split(r':',open)[1]
          print(smin)

      if int(shour)>=24:
          await ctx.send("存在しない時刻です！\n時刻は00:00～23:59まで指定できます。")
          return
      elif int(smin)>=60:
          await ctx.send("存在しない時刻です！\n分は59まで指定できます。")
          return
      
      #alert = datetime.datetime.strptime(str(args[1]),'%H:%M')

      nowobject = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
      print(nowobject)
      nhour = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).hour
      nmin = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).minute

      

      if rule == "r" or rule=="n": #nawarigu
          headers = {'User-Agent': 'SS-Mbot @shidoro_onn'}
          if rule=="n":
              rulename = "regular"
          else:
              rulename = "league"

          string = requests.get("https://spla2.yuu26.com/"+rulename+"/now",headers=headers).json()
      
          stage1 = string["result"][0]["maps_ex"][0]["image"]
          stage2 = string["result"][0]["maps_ex"][1]["image"]

          stage1_name = string["result"][0]["maps"][0]
          stage2_name = string["result"][0]["maps"][1]

          if stage1_name == "フジツボスポーツクラブ":
              stage1_name = "フジツボ\nスポーツクラブ"
          elif stage2_name == "フジツボスポーツクラブ":
              stage2_name = "フジツボ\nスポーツクラブ"

      if rule == "s":
          headers = {'User-Agent': 'SS-Mbot @shidoro_onn'}

          string = requests.get("https://spla2.yuu26.com/coop/schedule",headers=headers).json()

          stagename = string["result"][0]["stage"]["name"]
          stageim = string["result"][0]["stage"]["image"]
          buki1 = string["result"][0]["weapons"][0]["name"]
          buki2 = string["result"][0]["weapons"][1]["name"]
          buki3 = string["result"][0]["weapons"][2]["name"]
          buki4 = string["result"][0]["weapons"][3]["name"]

      """alert = datetime.datetime.strptime(str(args[1]),'%H:%M')
      ここから画像処理"""

      img = Image.open(rule+".jpg")
      draw = ImageDraw.Draw(img)

      # ！フォントの設定(フォントファイルのパスと文字の大きさ)
      main = ImageFont.truetype(r"GENEILATEGON_V2.TTF", 40)
      stagef = ImageFont.truetype(r"GENEILATEGON_V2.TTF",24)
      timef = ImageFont.truetype(r"LOGOTYPEJP_MP_B_1.1.TTF",50)
      # ？ フォントの設定(フォントファイルのパスと文字の大きさ)

      # ！ 投稿者情報
      draw.text((375, 60), ctx.author.display_name, fill=(0, 0, 0), font=main)
      icon = Image.open(io.BytesIO(requests.get(ctx.author.avatar_url).content))
      icon = mask_circle_solid(icon)
      icon = icon.resize((200,200))
      img.paste(icon,(115,50))

      draw.text((470,185),open+"～",fill=(0,0,0),font=timef)
      
      draw.text((900,665),datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S'),fill=(0,0,0),font=stagef)

      # ？ 投稿者情報

      # ！ ステージ情報
      if rule == "r" or rule == "n":
          s1im = Image.open(io.BytesIO(requests.get(stage1).content))
          s2im = Image.open(io.BytesIO(requests.get(stage2).content))

          s1im = s1im.resize((128,72))
          s2im = s2im.resize((128,72))

          img.paste(s1im,(790,360))
          img.paste(s2im,(790,480))

          draw.text((930,385),stage1_name,fill=(0,0,0),font=stagef)
          draw.text((930,500),stage2_name,fill=(0,0,0),font=stagef)

      elif rule == "s":
          stim = Image.open(io.BytesIO(requests.get(stageim).content))

          stim = stim.resize((311,175))

          img.paste(stim,(890,30))

          draw.text((800,460),buki1+"\n"+buki2+"\n"+buki3+"\n"+buki4+"\n",fill=(0,0,0),font=main)

      # ？ ステージ情報

      # ！ コメント

      come = "\n".join(textwrap.wrap(come,width=13))
      draw.text((160,342),come,fill=(0,0,0),font=main)

      # ？ コメント


      img.save("result.png")
      await ctx.send(file=discord.File('result.png'))
      await ctx.send("```著作権表記\n画像生成時に「源瑛ラテミン」(https://okoneya.jp/font/genei-latin.html) 、"\
                     "「コーポレート・ロゴ」(https://logotype.jp/corporate-logo-font-dl.html)を使用しています。\n"\
                     "Licensed under SIL Open Font License 1.1 (http://scripts.sil.org/OFL)\n"\
                     "© おたもん, © 2014-2019 Adobe Systems Incorporated, All Rights Reserved. © 2008–2019  フォント910\n"\
                     "© 2014 自家製フォント工房 by MM. © 2015 M+ FONTS PROJECT © 2019 転職サイト情報のLOGOTYPE.JP.```")

      if nhour>int(shour):
          await ctx.send("仕様上予約は当日のみ行えます。\n画像のみ生成します、ごめんなさい。\nby作者")
      elif nhour==int(shour) and nmin>int(smin):
          await ctx.send("仕様上予約は当日のみ行えます。\n画像のみ生成します、ごめんなさい。\nby作者")
      else:
          #先に現在時刻を文字列に変換
          nowstr = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d')
          #予定時刻を追記
          nowstr = nowstr+" "+str(shour)+":"+str(smin)+":00 +09:00:00"
          print(nowstr)
          stime = datetime.datetime.strptime(nowstr, '%Y-%m-%d %H:%M:%S %z')
          print(stime)
          #予定と現在の差を計算

          if bosyuflag==0:
              bosyulist.append(ctx.author.id)
              nusi = ctx.guild.get_member(ctx.author.id)
              print(nusi.id)
              bosyuflag = 1
          else:
              await ctx.send("現在"+ctx.guild.get_member(nusi.id).display_name+"さんが募集しています。")
              return

          sa = stime - nowobject
          await asyncio.sleep(sa.total_seconds())

          if rule=="n":temprule="ナワバリバトル"
          elif rule=="r":temprule="リーグマッチ"
          elif rule=="p":temprule="プライベートマッチ"
          else:temprule="サーモンラン"

          await ctx.send("@everyone\n"+ctx.author.mention+"が"+open+"から"+temprule+"を募集しています")

          newlist = []
          for i in range(len(bosyulist)):
              newlist.append(ctx.guild.get_member(bosyulist[i]).display_name)

          newlist = list(set(newlist))

          await ctx.send("現在の参加者一覧\n```"+"\n".join(newlist)+"```合計："+str(len(newlist)))

          bosyuflag=0
          bosyulist = []
          nusi = ""
          newlist = []

def mask_circle_solid(pil_img, background_color=(255,255,255), blur_radius=0, offset=0):
    background = Image.new(pil_img.mode, pil_img.size, background_color)

    offset = blur_radius * 2 + offset
    mask = Image.new("L", pil_img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((offset, offset, pil_img.size[0] - offset, pil_img.size[1] - offset), fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(blur_radius))

    return Image.composite(pil_img, background, mask)

@bot.command() #ピンポンテスト
async def ping(ctx):
    await ctx.send('pong')

@bot.command() #役職配布
async def role(ctx,string:str):
      if string=="testrole":
            target = discord.utils.get(ctx.guild.roles, name=string) in ctx.author.roles
            if target:
                  await ctx.author.remove_roles(discord.utils.get(ctx.guild.roles, name=string))
            else:
                  await ctx.author.add_roles(discord.utils.get(ctx.guild.roles,name=string))

@bot.command() #ウルタントーク
async def urutalk(ctx,string:str):
    member = ctx.guild.get_member(446286203101249567)
    await ctx.send(member.mention+' '+ctx.author.name+'「'+string+'」')

        
@bot.command() #フレンドコード一覧
async def frlist(ctx):
    temp=[]
    for i in frdic:
        temp.append('|      '+i+'     '+str(frdic[i]).ljust(12)+'    |')
    string = "\n".join(temp)
    await ctx.send('--------------------------------------------\n'+'|Friend cords list for '+ctx.author.mention+'!|\n'+string+'\n--------------------------------------------')
        
@bot.command() #フレンドコード検索
async def frc(ctx,cord:str):
    if cord.startswith("ウル"):cord="ウルタン"
    elif cord=="zeppurun":cord="ウルタン"
    elif cord=="リアルくん":cord="リアル"
    elif cord=="ちんちん":cord="ちゅんちゅん"
    elif cord=="ち〇んち〇ん":cord="ちゅんちゅん"
    elif cord=="かろーらたまて":cord="かろーら"
    elif cord=="バナナ":cord="taki"
    elif cord=="ぬらねこ":cord="ぬらねこX"
    elif cord=="ぬら":cord="ぬらねこX"
    elif cord=="ぬぅ？":cord="ぬらねこX"
    elif cord=="ぬぅ?":cord="ぬらねこX"
    await ctx.send(ctx.author.mention+"\n"+frdic.get(cord,cord+' は見つかりませんでした'))

@bot.command() #ウルタンアンチレベリング
async def dcurutan(ctx):
    global urulv
    urulv+=1
    if urulv%10 == 0:
        embed_message = discord.Embed(title='ウルタンアンチレベルが '+str(urulv)+' になりました！', description='ウルタンおつ！',color=7506394)
        await ctx.send(content=None, embed=embed_message)
    
@bot.command() #デバッグ用ウルタンアンチ確認コマンド
async def call(ctx):
    global switch
    global urulv
    await ctx.send('現在のアンチレベル ： '+str(urulv))
    await ctx.send('現在のswitch状態：'+switch)
      
@bot.event #メンバーが入ったとき
async def on_member_join(member):
      if member.guild.id==568427057076371457:
        string = "**このサーバーについて**\n"\
                 "SSーM 本鯖は、ゲームクランSSーMのサーバーです。\n"\
                 "毎週金曜・土曜にスプラトゥーンでプライベートマッチを行うのが活動内容です。\n"\
                 "役職「スプラ2」「フォトナ」「妖怪ウォッチ4」「マリメ2」「SZ」を持っているメンバーは、専用チャンネルに書き込めます。\n"\
                 "管理者からの通知は「 #お知らせ-重要な事 」で告知されます。\n"\
                 "雑談は、「 #総合雑談 」を使ってください。\n"\
                 "「rythm（音楽bot）」や「SSーMbot（鯖支援bot）」は「 #bot操作 」を使ってください。\n"\
                 "これからよろしくお願いします。"
        dm_channel = await member.create_dm()
        await dm_channel.send(string)
        return;
      elif member.guild.id==586914633441607696: #総合ゲーム鯖用設定
        role = discord.utils.get(member.guild.roles, name='かわいい')
      elif member.guild.id==593372280969756682: #作業用鯖用設定
        role = discord.utils.get(member.guild.roles, name='Gewöhnliche')
      else:return
      await member.add_roles(role)
      
@bot.event #メンバーが退出したとき
async def on_member_remove(member):
      guild = member.guild
      target = guild.system_channel
      await target.send(member.name+" さんがサーバーを脱退しました。ありがとうございました。")
      
@bot.event #メンバーがBANされたとき
async def on_member_ban(guild,member):
      guild = member.guild
      target = guild.system_channel
      await target.send(member.name+" さんがサーバーからBANされました。")
            
@bot.command(aliases=['info']) #ヘルプ
async def help(ctx):
      embed=discord.Embed(title="SSーM bot ヘルプ", description="SSーMの支援bot「SSーM bot」の機能についての説明です。", color=0x80ffff)
      embed.add_field(name="**__コマンド__**", value="_コマンド文字列 と送信すると反応します。", inline=False)
      embed.add_field(name="_dcurutan", value="ウルタンアンチレベルを1上げます。（ネタ要素）", inline=False)
      embed.add_field(name="_call", value="ウルタンアンチレベルを表示します。（ネタ要素）", inline=False)
      embed.add_field(name="_frlist", value="登録されているメンバーのフレンドコードリスト。", inline=False)
      embed.add_field(name="_frc メンバー名", value="特定のメンバーのフレンドコード。", inline=False)
      embed.add_field(name="_decore 装飾の種類 文字列",value="文字列を指定の方法で装飾。太字、斜体、取り消し線、マスクなどが可能。",inline="False")
      embed.add_field(name="_Bosyu ルール 時間", value="ルールは、n（ナワバリ）r2（2リグ）r4（4リグ）s（サーモン）f（フェス）を指定し募集します。", inline=False)
      embed.add_field(name="_team 人数", value="与えられた人数に対してランダムに2チームを生成。", inline=False)
      embed.add_field(name="_ping", value="返信テストコマンド", inline=False)
      embed.add_field(name="_role", value="役職半自動配布(試運転)。", inline=False)
      embed.add_field(name="_emo5000 ひらがな",value="文字列を5000兆円絵文字に変換します（SSーM本鯖限定）",inline=False)
      embed.add_field(name="_spla 文字列",value="文字列にパブロとか入れると画像URLをくれます。",inline=False)
      embed.add_field(name="_help", value="このDMを送信します。", inline=False)
      embed.add_field(name="**__その他__**", value="自動変換機能など。メッセージの先頭でなくても反応。", inline=False)
      embed.add_field(name="tw:@ID", value="IDをツイッターのURLに変換します。存在しないIDでも変換しちゃいます…", inline=True)
      embed.add_field(name="漏斗", value="これを送るとたまにしゃべります", inline=True)
      embed.set_footer(text="何か不明な点があれば、わたくし @カッシー/にゅげ#5706 までご連絡くださーい！ｗ")
      dm_channel = await ctx.author.create_dm()
      await dm_channel.send(embed=embed)
      
@bot.command()
async def test(ctx,opt:str):
      global routcount
      global bosyulist
      global nusi
      if opt=="ユーザー":
            string=[]
            i=0
            for i in range(len(bot.users)):
                  string.append(str(bot.users[i]))
            mes = '\n'.join(string)
            await ctx.send(mes)
      if opt=="作業ディレクトリ":
            await ctx.send(os.getcwd())
      if opt=="rout":
            await ctx.send("カウント状況："+str(routcount))
      if opt=="file":
            f = open('/tmp/data.txt','r')
            s=f.read()
            await ctx.send(s)
            f.close()
      if opt=="emoji":
            '''
            i=0
            string = ""
            
            temp = []
            for i in range(61):
                  temp.append(bot.get_emoji(596981155056582666))
            
            await ctx.send("\n".join(temp))
            
            await ctx.send(string)
            '''
            
            await ctx.send(type(bot.get_emoji(596981155056582666)))
      if opt.startswith("c"): #反応カウント変更
            global limit
            limit=int(opt[1])
            print("限界値を"+opt[1]+"に変更しました。")

      if opt=="regular":
            string = requests.get("https://spla2.yuu26.com/regular/now").json()
            #f = open(string,"r")
            #stages = json.load(string)
            await ctx.send(string)
            await ctx.send("現在のステージ："+string["result"][0]["maps_ex"][0]["image"]+"\n"+string["result"][0]["maps_ex"][1]["image"])

      if opt=="everyone":
            #target = discord.utils.get(ctx.guild.roles, id=586914633441607696)
            await ctx.send("@everyone むりだろうけど")
            #await ctx.send(ctx.guild.default_role.mention+" テストです")
      if opt=="bosyudata":
            if nusi is None:
                  await ctx.send("募集はありません。")
                  return
            await ctx.send("現在"+ctx.guild.get_member(nusi.id).display_name+"さんが募集しています。")
            newlist=[]
            for i in range(len(bosyulist)):
              newlist.append(ctx.guild.get_member(bosyulist[i]).display_name)
            newlist = list(set(newlist))
            await ctx.send("\n".join(newlist))
            newlist = []
      
        
bot.run(token)
