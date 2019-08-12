import discord
from discord.ext import commands
import os
import traceback
import random
import json
import math
import base64
import re
gold = 0

bot = commands.Bot(command_prefix='/',help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
ducount = 0
starter = 0
startname = ""

'''
@bot.event #FalseCommand
async def on_command_error(ctx, error):
    await ctx.send('そんなコマンドないよ？出直してきな？')
''' 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='電波人間のRPG free'))

    
@bot.command()
async def m(ctx):
    await ctx.send('まいにち過疎')

@bot.command()
async def nox(ctx):
    await ctx.send('世界は残酷だ。ありふれたジャンク情報に魅了され、それらに没頭した者から、淘汰されてしまう。常に取捨選択をしなければならない。ないがしろにされた取捨選択は積み重なり、やがてその量によって、その人の人生の価値が決まる。「塵も積もれば山となる」とはまさにこのことだ。')
    
@bot.command()
async def root(ctx):
    await ctx.send('誰が漏斗じゃい')
 
@bot.command()
async def dc(ctx):
    await ctx.send('fuck')
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')
    
@bot.command(aliases=['exp'])
async def 経験値(ctx,lv:int):
    
    f = open("other/data.txt","r")
    items = f.readlines()
    target = int(items[lv-1])
    f.close()
    
    explist = [str(math.floor(target*(1-i*0.01))) for i in range(8)]
    l = []
    
    for i in range(8):
        l.append(chr((i+65))+"\t"+explist[i])
        
    embed=discord.Embed(title="経験値の一覧", description="各属に当てはまる可能性のある体格", color=0x80ffff)
    embed.add_field(name="A", value="回避0 最大型", inline=False)
    embed.add_field(name="B", value="回避0 準大／中間／準速／最速", inline=False)
    embed.add_field(name="C", value="回避3 最大型／準大-1／準準大-1／準準速-2／準速-2", inline=False)
    embed.add_field(name="D", value="回避3 準大-2／準準大2／準準速-1／準速-1／最速", inline=False)
    embed.add_field(name="E", value="回避6 最大／準大-2／中間-2／中間-3", inline=False)
    embed.add_field(name="F", value="回避6 準大-1／中間-1／準速／最速", inline=False)
    embed.add_field(name="G", value="回避10 最大／中間／最速\n回避15 最大／中間", inline=False)
    embed.add_field(name="H", value="回避15 最速", inline=False)
        
    await ctx.send("【"+str(lv)+" Lv】\n```"+"\n".join(l)+"```")
    
    await ctx.send(embed=embed)
    
    
@bot.command()
async def リサイクル(ctx,rare:int):
    if rare>1 and rare<10:
        rand = random.randrange(-1,2) #レア度の上下調整
        rare += rand
    elif rare<=1:
        rare = 1
        rand = random.randrange(0,2) #下限なので0か1。
        rare += rand
    elif rare>=10:
        rare = 10
        rand = random.randrange(-1,1) #上限なので-1か0。
        rare += rand
        
    resrand = random.randrange(0,2) #レア度ごとに2つのセリフがあるので、それを選択（0のとき1つめ、1のとき2つめ）
        
    res1 = ["んー、こういうこともあるよね。","ちょっと残念？","はい、どうぞ～。","かんせ～い！","すごい、すごーい！","ほわぁ！大成功だよ！"]
    res2 = ["ができたわ。","ができたわ。","ができたわよ。","ができたわ。","ができたわ！","ができたー！"]
    
    fname = "rare/rare"+str(rare)+".txt" #ファイルのパス
    f = open(fname,"r") #ファイルの読み込み
    items = f.readlines() #ファイル.readlines()で行ごとにリスト化
    f.close()
    
    result = items[random.randrange(0,len(items))]
    result = result.replace("\n","") #readlinesは各行の改行コードを読んでしまうため改行コードを消去
    
    await ctx.send(ctx.author.mention + res1[(3+resrand+2*rand)-1] + " ☆" + str(rare) + "の\n**" + result + "**ができたわ。")


@bot.command() #ヘルプ
async def help(ctx):
    embed=discord.Embed(title="いちごおばけbot", description="いちごおばけbotについての説明です。", color=0x80ffff)
    embed.add_field(name="/help", value="この文章を送信します。まあこの文章を読めてる時点で/helpって打ってるんだよね君", inline=False)
    embed.add_field(name="/(コマンド)で反応する単語一覧", value="dc、root、m、いちごおばけ、noxのどれかを打つと反応します", inline=False)
    embed.add_field(name="/リサイクル レア度", value="リサイクルをします。レア度には1~10の数字を入力してください。", inline=False)
    embed.add_field(name="おはよう、おやすみ、まいにち過疎", value="特定の文章を返します", inline=False)
    embed.add_field(name="ダブルアップ", value="ダブルアップチャンスを開始します。続いて表示される指示に従ってください", inline=False)
    embed.add_field(name="リセット", value="ダブルアップチャンスの状態をリセットします", inline=False)
    
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed)

               
@bot.event
async def on_message(message):
    '''
    <ducountが>
     0→スタート（１個目の穴を聞く）countを1に
     1→1個目の穴の答えを受け取／２個目の穴を聞く countを2に
     2→2個目の穴の答えを受け取／３個目の穴を聞く countを3に
     3→3個目の穴の答えを受け取／４個目の穴を聞く countを4に
     4→4個目の穴の答えを受け取／５個目の穴を聞く（！ここだけ三択！） countを5に
     5→5個目の穴の答えを受け取／おめでとう
    '''
    global ducount
    global starter
    global startname
    global gold
    if message.content.startswith('口が悪いね、残念だがここでお別れだ'): 
        await message.channel.send('もちろんy')
        
    if message.content.startswith('ダブルアップ'): #初回
        if ducount>0:
            await message.channel.send("もう始まってるよ")
            return
        if len(message.content.split())==1:
            await message.channel.send("```ダブルアップ 掛け金```\nと送信して掛け金を指定してください。")
            return
        string = message.content.split()[1]
        
        if re.search("[0-9]",string):
            gold = re.sub("\\D", "", string)
            gold = int(gold)
            gold *= 2
        else:
            await message.channel.send("```ダブルアップ 掛け金```\nと送信して掛け金を**半角数字で**指定してください。")
            return
        
        if gold == 0:
            await message.channel.send("1以上の金額を入力してください！")
        starter = message.author.id
        startname = message.author.name
        ducount = 0 #リスタート
        embed = discord.Embed(title="どちらの穴に入るか、「右」か「左」で決めよう！（１回目）\n次の掛け金："+str(gold)+"G", description="\n\t●\t●\n",color=0x80ff00)
        await message.channel.send(content=None,embed=embed)
        ducount = 1
        
    if (message.content.startswith('右')or message.content.startswith('左'))and ducount<5 and ducount!=0: #5回まで
        
        if starter != message.author.id:
            await message.channel.send("現在"+startname+"さんがプレイ中です。順番を待てないお子様なのかな？")
            return
        rand = random.randrange(2)
        
        if rand==0:
            await message.channel.send("はずれー！！懲りずに、また挑戦してみてね！")
            ducount = 0
            return
        if rand==1 and ducount!=4: #4回目以外
            ducount += 1
            gold *= 2
            embed = discord.Embed(title="当たり！次の穴を選んでね！（"+str(ducount)+"回目）\n次の掛け金："+str(gold)+"G",description="\n\t●\t●\n",color=0x80ff00)
            await message.channel.send(content=None,embed=embed)
        elif rand==1 and ducount==4: #4回目のみ（穴数変更）
            ducount += 1
            gold *= 3
            embed = discord.Embed(title="当たり！次の穴が最後！「左」「真ん中」「右」の中から選ぼう！（"+str(ducount)+"回目）\n次の掛け金："+str(gold)+"G",
                                  description="\n\t●\t●\t●\n",color=0x80ff00)
            await message.channel.send(content=None,embed=embed)
     
            
    elif (message.content.startswith('真ん中')or message.content.startswith('右')or message.content.startswith('左'))and ducount==5: #最終回
        if starter != message.author.id:
            await message.channel.send("現在"+startname+"さんがプレイ中です。順番を待てないお子様なのかな？")
            return
        rand = random.randrange(3)
        
        if rand==0 or rand==1:
            await message.channel.send("はずれ。君たちは一体今までにいくら貢いだんだろうね")
            ducount = 0
            return
        if rand==2:
            await message.channel.send(message.author.mention+"おめでとう **"+str(gold)+"** G入手したよ！\n達成できたのは今回で……何回目だったっけ")
            ducount = 0
            return
    if (message.content.startswith('右')or message.content.startswith('左'))and ducount==0:	
            await message.channel.send('今日も良い天気だね')
        
    if message.content=='リセット':
        ducount = 0
        starter = 0
        startname = ""
        await message.channel.send("リセットしたよ？後悔のないようにね？")
            
    if message.content.startswith('!dc'):
        await message.channel.send('❌ **I am not connected to a voice channel**, Use the summon command to get me in one')
    if message.content.startswith('おやすみ'):
        await message.channel.send(message.author.name+' Gute Nacht, gute Träume')
    if message.content.startswith('おはよう'):
        await message.channel.send('言動には注意すべきだ。発言者本人は発せられたその言葉の意味や意図をよく考えないで使っているかもしれないが、あらゆる行動に意味を持つように、その言葉を発した意味も当然存在する筈だ。言葉の意味を失わない為に、また、今後は反射的な発言をしないように、今一度、その発言の意味を深く考えてみてはどうだろうか。')
    if message.author.bot==True:return
    if message.content.startswith('まいにち過疎'):
        await message.channel.send('わかる')
    if 564709839859744769 in message.raw_channel_mentions:
        await message.channel.send('まいにち過疎')
    await bot.process_commands(message)
 
bot.run(token)
