from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
    
    
await client.change_presence(activity=discord.Game(name='電波人間のRPG Free'))

 
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')


bot.run(token)
