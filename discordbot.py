import discord
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='#')
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
    if message.content.startswith("ばぶー"):
        await channel.send(message.author.mention+"ばぶー！")
        
    if message.content.startswith("うーん"):
        await channel.send(message.author.mention+"うーん")
        
    if message.content.startswith("ガハハｗ"):
        await channel.send(message.author.mention+"はクソ")


bot.run(token)
