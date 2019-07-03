import discord
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


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
    if message.content.startswith('口が悪いね、残念だがここでお別れだ'):
        await message.channel.send('もちろんy')
    if message.content.startswith('ダブルアップ'):
        await message.channel.send('どちらの穴に入るか、「右」か「左」で決めよう！')
    if message.content.startswith('右'):
        str = random.choice(("はずれー！！懲りずに、また挑戦してみてね！","当たり！次の穴を選んでね！"))
        await message.channel.send(str)
    if message.content.startswith('左'):
        str = random.choice(("残念、そっちはハズレの穴なんだ","当たり！次の穴を選んでね！"))
        await message.channel.send(str)
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
