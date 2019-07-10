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

bot = commands.Bot(command_prefix='_',help_command=None)
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
urulv = 0
switch = "ON"
routcount = 0

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
    await bot.change_presence(activity=discord.Game(name=switch+'-ウルタンアンチ'))

class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

@bot.event #startswith反応単語
async def on_message(message):
    global switch
    cont = message.content
    global routcount 
    if not cont.startswith('_') and switch == "OFF":
        return
    if message.author == client.user:
        return
    if "tw:@" in cont:
        s = message.content
        s = s+" "
        m = re.search('\@+[a-zA-Z0-9_]+[\a-zA-Z0-9_]', s)
        string = m.group(0).replace("@","https://twitter.com/")
        await message.channel.send(string)
    if message.author.bot:return
    if "漏斗" in cont:
        if routcount == 4:
            await message.channel.send(message.author.mention+"誰が漏斗じゃい！")
            routcount = 0
        else:
            routcount+=1
    if cont.startswith('hellouru'):
        member = message.guild.get_member(446286203101249567)
        await message.channel.send(member.mention+' おはよう')
    if cont.startswith('ばぶ'):
        str = random.choice(("ばぶ","ばぶー","ばぶー！","ばぶ？","ばぶばぶー"))
        await message.channel.send(message.author.mention+' '+str)
    if cont.startswith('ガハハ'):
        await message.channel.send(message.author.mention+' はクソ')
    if cont.startswith('おやす'):
        await message.channel.send(message.author.mention+' おやすみー！')
    if cont.startswith('おは'):
        await message.channel.send(message.author.mention+' おはよう！起きて！朝だよ！カンカンカンカンカンカンカンカンカン')   
    if cont.startswith("ウルタン"):
        str = random.choice(("ばかだ","無能だ","ハゲだ","ごみだ","くさい","頭悪い","気持ち悪い","かわいい"))
        await message.channel.send(message.author.mention+' ウルタン'+str+'ね')
    if cont=='かわいくないよ':
        if message.guild.id==586914633441607696:
            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='かわいい'))
            await message.author.add_roles(discord.utils.get(message.guild.roles, name='かわいくない'))
    if cont=='やっぱりかわいいよ':
        if message.guild.id==586914633441607696:
            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='かわいくない'))
            await message.author.add_roles(discord.utils.get(message.guild.roles, name='かわいい'))
    if cont=='np':
        await message.channel.send('!np')
    if cont.lower()=="!dc" or cont.lower()=="!disconnect" or cont.lower()=="!leave" or cont.lower()=="!dis" or cont.lower()=="!fuckoff":
        await message.channel.send('❌ **I am not connected to a voice channel**, Use the summon command to get me in one')
    
    
        
        
    await bot.process_commands(message)


@bot.command() #プレイ中の表示を変更
async def play(ctx):
      global switch
      str = random.choice(("妖怪ウォッチ4","スプラトゥーン2","ウルタンくさい","大学受験","ウルタン天気予報","ウルタンラジオ","ウルタン不審者","健康ミネラルウル茶","ウルタン語彙力ない"))
      await bot.change_presence(activity=discord.Game(name=switch+'-'+str))
      
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

@bot.command() #botの状態を設定
async def botsw(ctx):
      global switch
      if switch=="ON":switch="OFF"
      elif switch=="OFF":switch="ON"
      str = random.choice(("妖怪ウォッチ4","スプラトゥーン2","ウルタンくさい","大学受験","ウルタン天気予報","ウルタンラジオ","ウルタン不審者","健康ミネラルウル茶","ウルタン語彙力ない"))
      await bot.change_presence(activity=discord.Game(name=switch+'-'+str))
      
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
     
@bot.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.BadArgument):
        await ctx.send("不正な入力です")
@bot.event
async def on_command_error(ctx, error):
    await ctx.send('エラーが発生しました\n'+str(error))

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
async def Bosyu(ctx,rule:str,open:str):
      if rule == "n":rule="ナワバリバトル"
      elif rule == "r2":rule="リーグマッチ（2）"
      elif rule == "r4":rule="リーグマッチ（4）"
      elif rule == "s":rule="サーモンラン"
      elif rule == "f":rule="フェスマッチ（フレンド）"
      else : return;
      embed_message = discord.Embed(title=ctx.author.name+' が'+open+'から'+rule+'を開催！',color=7506394)
      embed_message.set_image(url="https://www.sankei.com/images/news/180503/plt1805030018-p1.jpg")
      await ctx.send(content=None, embed=embed_message)


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
      else:return;
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
            
@bot.command() #ヘルプ
async def help(ctx):
      embed=discord.Embed(title="SSーM bot ヘルプ", description="SSーMの支援bot「SSーM bot」の機能についての説明です。", color=0x80ffff)
      embed.add_field(name="**__コマンド__**", value="_コマンド文字列 と送信すると反応します。", inline=False)
      embed.add_field(name="_botsw", value="botの反応を抑制するかを切り替えます（ONOFFはプレイ中の欄に表示されます）", inline=False)
      embed.add_field(name="_dcurutan", value="ウルタンアンチレベルを1上げます。（ネタ要素）", inline=False)
      embed.add_field(name="_call", value="ウルタンアンチレベルを表示します。（ネタ要素）", inline=False)
      embed.add_field(name="_frlist", value="登録されているメンバーのフレンドコードリスト。", inline=False)
      embed.add_field(name="_frc メンバー名", value="特定のメンバーのフレンドコード。", inline=False)
      embed.add_field(name="_decore 装飾の種類 文字列",value="文字列を指定の方法で装飾。太字、斜体、取り消し線、マスクなどが可能。",inline="False")
      embed.add_field(name="_Bosyu ルール 時間", value="ルールは、n（ナワバリ）r2（2リグ）r4（4リグ）s（サーモン）f（フェス）を指定し募集します。", inline=False)
      embed.add_field(name="_team 人数", value="与えられた人数に対してランダムに2チームを生成。", inline=False)
      embed.add_field(name="_ping", value="返信テストコマンド", inline=False)
      embed.add_field(name="_role", value="役職半自動配布(試運転)。", inline=False)
      embed.add_field(name="_helpbot", value="このDMを送信します。", inline=False)
      embed.add_field(name="**__先頭反応語句__**", value="単語がメッセージの先頭にあった場合に反応します。", inline=False)
      embed.add_field(name="おは", value="返信「おはよう！・・・」", inline=False)
      embed.add_field(name="おやす", value="返信「おやすみー！」", inline=True)
      embed.add_field(name="ばぶ", value="返信「（ランダム）」", inline=True)
      embed.add_field(name="ガハハ", value="返信「はクソ」", inline=True)
      embed.add_field(name="ウルタン", value="返信「ウルタン（ランダム）ね」", inline=True)
      embed.add_field(name="hellouru", value="@ウルタン おはよう", inline=True)
      embed.add_field(name="**__その他__**", value="自動変換機能など。メッセージの先頭でなくても反応。", inline=False)
      embed.add_field(name="tw:@ID", value="IDをツイッターのURLに変換します。存在しないIDでも変換しちゃいます…", inline=True)
      embed.set_footer(text="何か不明な点があれば、わたくし @カッシー/にゅげ#5706 までご連絡くださーい！ｗ")
      dm_channel = await ctx.author.create_dm()
      await dm_channel.send(embed=embed)
      
@bot.command()
async def test(ctx,opt:str):
      global routcount
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

      
        
bot.run(token)
