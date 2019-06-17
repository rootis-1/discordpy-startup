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
    if client.user in message.mentions: # 話しかけられたかの判定
        if message.content == 'おい':
            reply = f'{message.author.mention} なに' # 返信メッセージの作成
            await message.channel.send(reply) # 返信メッセージを送信


bot.run(token)
