import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
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
    if message.author.bot==True:return;
    if message.content.startswith('まいにち過疎'):
        await message.channel.send('わかる')
    if 564709839859744769 in message.raw_channel_mentions:
        await message.channel.send('まいにち過疎')
    await bot.process_commands(message)

bot.run(token)
