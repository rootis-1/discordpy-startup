import discord
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
ducount = 0


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
async def dc(ctx):
    await ctx.send('fuck')
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')
       
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
    if message.content.startswith('口が悪いね、残念だがここでお別れだ'): 
        await message.channel.send('もちろんy')
        
    if message.content.startswith('ダブルアップ'): #初回
        ducount = 0 #リスタート
        embed = discord.Embed(title="どちらの穴に入るか、「右」か「左」で決めよう！（１回目）", description="\n\t●\t●\n",color=0x80ff00)
        await message.channel.send(content=None,embed=embed)
        ducount = 1
        
    if (message.content.startswith('右')or message.content.startswith('左'))and ducount<5 and ducount!=0: #5回まで
        rand = random.randrange(2)
        if rand==0:
            await message.channel.send("はずれー！！懲りずに、また挑戦してみてね！")
            ducount = 0
            return;
        if rand==1:
            embed = discord.Embed(title="当たり！次の穴を選んでね！（"+str(ducount)+"回目）",description="\n\t●\t●\n",color=0x80ff00)
            await message.channel.send(content=None,embed=embed)
            
    if (message.content.startswith('真ん中')or message.content.startswith('右')or message.content.startswith('左'))and ducount==5: #最終回
        rand = random.randrange(3)
        if rand==0 or rand==1:
            await message.channel.send("はずれー！！懲りずに、また挑戦してみてね！")
            ducount = 0
            return;
        if rand==2:
            await message.channel.send(message.author.mention+" おめでとう")
            
            
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
