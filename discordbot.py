import discord
from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='_')
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']
urulv = 0

'''
@bot.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='ウルタンアンチ'))
'''
@bot.event
async def on_message(message):
    
    if message.author == client.user:
        return
   
    if message.content.startswith('hellouru'):
        member = message.guild.get_member(446286203101249567)
        await message.channel.send(member.mention+' おはよう')

    if message.content.startswith('ばぶ'):
        str = random.choice(("ばぶ","ばぶー","ばぶー！","ばぶ？","ばぶばぶー"))
        await message.channel.send(message.author.mention+' '+str)
    elif message.content.startswith('ガハハ'):
        await message.channel.send(message.author.mention+' はクソ')
        
    if message.content.startswith('urutest'):
        member = message.guild.get_member(446286203101249567)
        await message.channel.send(member.mention+' '+member.author.name+'「おはよう」')

        
    await bot.process_commands(message)


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
async def dcurutan(ctx):
    global urulv
    urulv+=1
    
    if urulv%10 == 0:
        embed_message = discord.Embed(title='ウルタンアンチレベルが '+str(urulv)+' になりました！', description='ウルタンおつ！',color=7506394)
        await ctx.send(content=None, embed=embed_message)
    
@bot.command()
async def call(ctx):
    global urulv
    await ctx.send('現在のアンチレベル ： '+urulv)
        
bot.run(token)
