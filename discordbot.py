from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))
    
    
    
client.on('ready', message =>
{
  client.user.setPresence({ game: { name: '電波人間のRPG Free！' } });  
  console.log('bot is ready!');
});


 
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')


bot.run(token)
