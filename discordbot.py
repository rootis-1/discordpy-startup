import discord
from discord.ext import commands
import os
import traceback
import random
import math

bot = commands.Bot(command_prefix='_')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
urulv = 0

frdic={"ウルタン":"7274-0692-4516","デコピン【R】":"0857-0883-1787","鮪":"5987-3991-4481","千秋":"1153-1958-7503","リアル":"2707-5632-2995",
      "流星(Light)":"4668-6953-1391","闇":"2996-3936-5864","ゆっくりはやくタロウ":"1396-6888-2293","あげパン":"1792-7753-6891",
      "ログ":"8566-2988-4961","ちゅんちゅん":"6001-3499-3328","goa":"2589-2017-2410","taki":"2321-8536-1233","りある":"3518-6462-4899",
      "カービィ":"5558-7760-9399","カッシー":"5542-3638-4894","さいつお":"6222-8498-7799","root-1":"2917-4595-2298","かろーら":"1193-9378-7413"}

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='ウルタンアンチ'))
    

@bot.event #startswith反応単語
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content.startswith('hellouru'):
        member = message.guild.get_member(446286203101249567)
        await message.channel.send(member.mention+' おはよう')
    if message.content.startswith('ばぶ'):
        str = random.choice(("ばぶ","ばぶー","ばぶー！","ばぶ？","ばぶばぶー"))
        await message.channel.send(message.author.mention+' '+str)
    if message.content.startswith('ガハハ'):
        await message.channel.send(message.author.mention+' はクソ')
    if message.content.startswith('おやす'):
        await message.channel.send(message.author.mention+' おやすみー！')
    if message.content.startswith('おは'):
        await message.channel.send(message.author.mention+' おはよう！起きて！朝だよ！カンカンカンカンカンカンカンカンカン')   
    if message.content.startswith("ウルタン"):
        str = random.choice(("ばかだ","無能だ","ハゲだ","ごみだ","くさい","頭悪い","気持ち悪い","かわいい"))
        await message.channel.send(message.author.mention+' ウルタン'+str+'ね')
    if message.content=='かわいくないよ':
        if message.guild.id==586914633441607696:
            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='かわいい'))
            await message.author.add_roles(discord.utils.get(message.guild.roles, name='かわいくない'))
        
        
    await bot.process_commands(message)

@bot.command() #プレイ中の表示を変更
async def play(ctx):
      str = random.choice(("ウルタンくさい","ウルタン受験落ちました","ウルタン天気予報","ウルタンラジオ","ウルタンドットコム","ウルタンハム太郎",
                          "ウルタンばぶー","ウルタン不審者","ウルタン健康ミネラルむぎ茶","ウルタンは語彙力ないよ"))
      await bot.change_presence(activity=discord.Game(name=str))

@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
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


@bot.command()
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
    await ctx.send(ctx.author.mention)
    if cord.startswith("ウル"):cord="ウルタン"
    elif cord=="zeppurun":cord="ウルタン"
    elif cord=="リアルくん":cord="リアル"
    elif cord=="ちんちん":cord="ちゅんちゅん"
    elif cord=="ち〇んち〇ん":cord="ちゅんちゅん"
    elif cord=="かろーらたまて":cord="かろーら"
    await ctx.send(frdic.get(cord,cord+' は見つかりませんでした'))

@bot.command() #ウルタンアンチレベリング
async def dcurutan(ctx):
    global urulv
    urulv+=1
    if urulv%10 == 0:
        embed_message = discord.Embed(title='ウルタンアンチレベルが '+str(urulv)+' になりました！', description='ウルタンおつ！',color=7506394)
        await ctx.send(content=None, embed=embed_message)
    
@bot.command() #デバッグ用ウルタンアンチ確認コマンド
async def call(ctx):
    global urulv
    await ctx.send('現在のアンチレベル ： '+str(urulv))
      
@bot.event
async def on_menber_join(menber):
      if menber.guild.id==586914633441607696:
        role = discord.utils.get(ctx.guild.roles, name='かわいい')
        await ctx.author.add_roles(role)
        
bot.run(token)
