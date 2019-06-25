import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='電波人間のRPG free'))

@bot.command()
async def m(ctx):
    await ctx.send('まいにち過疎')
    
@bot.event
async def "#まいにち過疎"(message):
   if message.content.startswith('わかる'):

 
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')


bot.run(token)
