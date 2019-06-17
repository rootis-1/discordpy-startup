from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='_')
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


@bot.command()
async def on_message(message):
    if message.content == '@ss-mbot おい':
        reply = f'{message.author.mention} なに'
        await message.channel.send(reply)


bot.run(token)
