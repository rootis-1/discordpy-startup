import discord
from discord.ext import commands
import os
import traceback
import random
import json
import math
import base64


bot = commands.Bot(command_prefix='/',help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']
ducount = 0
starter = 0
startname = ""


@bot.event #FalseCommand
async def on_command_error(ctx, error):
    await ctx.send('そんなコマンドないよ？出直してきな？')
 

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
    
@bot.command() #ヘルプ
async def help(ctx):
      embed=discord.Embed(title="いちごおばけbot", description="いちごおばけbotについての説明です。", color=0x80ffff)
      embed.add_field(name="/help", value="この文章を送信します。まあこの文章を読めてる時点で/helpって打ってるんだよね君", inline=False)
      embed.add_field(name="/(コマンド)で反応する単語一覧", value="dc、root、m、いちごおばけ、noxのどれかを打つと反応します", inline=False)
      embed.add_field(name="おはよう、おやすみ、まいにち過疎", value="特定の文章を返します", inline=False)
      embed.add_field(name="ダブルアップ", value="ダブルアップチャンスを開始します。続いて表示される指示に従ってください", inline=False)
      embed.add_field(name="リセット", value="ダブルアップチャンスの状態をリセットします", inline=False)
      dm_channel = await ctx.author.create_dm()
      await dm_channel.send(embed=embed)
       
@bot.command() #ヘルプ
async def help(ctx):
      embed=discord.Embed(title="いちごおばけbot", description="いちごおばけbotについての説明です。", color=0x80ffff)
      embed.add_field(name="/help", value="この文章を送信します。まあこの文章を読めてる時点で/helpって打ってるんだよね君", inline=False)
      embed.add_field(name="/(コマンド)で反応する単語一覧", value="dc、root、m、いちごおばけ、noxのどれかを打つと反応します", inline=False)
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
    if message.content.startswith('口が悪いね、残念だがここでお別れだ'): 
        await message.channel.send('もちろんy')
        
    if message.content.startswith('ダブルアップ'): #初回
        if ducount>0:
            await message.channel.send("もう始まってるよ")
            return;
        if len(message.content.split())==1:
            await message.channel.send("```ダブルアップ 掛け金```\nと送信して掛け金を指定してください。")
            return;
        gold = message.content.split()[1]
        
        gold = re.sub("\\D", "", gold)
        starter = message.author.id
        startname = message.author.name
        ducount = 0 #リスタート
        embed = discord.Embed(title="どちらの穴に入るか、「右」か「左」で決めよう！（１回目）\n掛け金："+gold+"G", description="\n\t●\t●\n",color=0x80ff00)
        await message.channel.send(content=None,embed=embed)
        ducount = 1
        
    if (message.content.startswith('右')or message.content.startswith('左'))and ducount<5 and ducount!=0: #5回まで
        if starter != message.author.id:
            await message.channel.send("現在"+startname+"さんがプレイ中です。順番を待てないお子様なのかな？")
            return;
        rand = random.randrange(2)
        
        rand=1 #デバッグが終わったら削除！
        
        if rand==0:
            await message.channel.send("はずれー！！懲りずに、また挑戦してみてね！")
            ducount = 0
            return;
        if rand==1 and ducount!=4: #4回目以外
            ducount += 1
            embed = discord.Embed(title="当たり！次の穴を選んでね！（"+str(ducount)+"回目）\n掛け金："+gold*ducount+"G",description="\n\t●\t●\n",color=0x80ff00)
            await message.channel.send(content=None,embed=embed)
        elif rand==1 and ducount==4: #4回目のみ（穴数変更）
            ducount += 1
            embed = discord.Embed(title="当たり！次の穴が最後！「左」「真ん中」「右」の中から選ぼう！（"+str(ducount)+"回目）\n掛け金："+gold*ducount+"G",
                                  description="\n\t●\t●\t●\n",color=0x80ff00)
            await message.channel.send(content=None,embed=embed)
     
            
    elif (message.content.startswith('真ん中')or message.content.startswith('右')or message.content.startswith('左'))and ducount==5: #最終回
        if starter != message.author.id:
            await message.channel.send("現在"+startname+"さんがプレイ中です。順番を待てないお子様なのかな？")
            return;
        rand = random.randrange(3)
        if rand==0 or rand==1:
            await message.channel.send("はずれー！！懲りずに、また挑戦してみてね！")
            ducount = 0
            return;
        if rand==2:
            await message.channel.send(message.author.mention+"おめでとう 達成できたのは今回で……何回目だったっけ")
            ducount = 0
            return;
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
    if message.author.bot==True:return;
    if message.content.startswith('まいにち過疎'):
        await message.channel.send('わかる')
    if 564709839859744769 in message.raw_channel_mentions:
        await message.channel.send('まいにち過疎')
    await bot.process_commands(message)
 
bot.run(token)
