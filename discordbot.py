import discord
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='_')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ウルタンは(ctx):
    rand = random.randrange(5)

    if rand == 0:
        await ctx.send('くさい')
    elif rand == 1:
        await ctx.send('ばか')
    elif rand == 2:
        await ctx.send('暇人')
    elif rand == 3:
        await ctx.send('ひきこもり')
    elif rand == 4:
        await ctx.send('かわいい')


@client.event
async def on_message(message):
    print('message')
    if message.content=='ばぶー':
        m = message.author.mention+"ばぶー！"
        await channel.send(m)
        
    if message.content=='うーん':
        m = message.author.mention+"うーん"
        await channel.send(m)
        
    if message.content=='ガハハｗ':
        m = message.author.mention+"はクソ"
        await channel.send(m)


bot.run(token)
client.run(token)
