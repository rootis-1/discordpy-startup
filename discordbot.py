import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/',help_command=None)
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
async def nox(ctx):
    await ctx.send('世界は残酷だ。ありふれたジャンク情報に魅了され、それらに没頭した者から、淘汰されてしまう。常に取捨選択をしなければならない。ないがしろにされた取捨選択は積み重なり、やがてその量によって、その人の人生の価値が決まる。「塵も積もれば山となる」とはまさにこのことだ。')
    
@bot.command()
async def root(ctx):
    await ctx.send('誰が漏斗じゃい')
 
@bot.command()
async def dc(ctx):
    await ctx.send('fuck')
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')

@bot.command() #ヘルプ
async def help(ctx):
    embed=discord.Embed(title="いちごおばけbot", description="いちごおばけbotについての説明です。", color=0x80ffff)
    embed.add_field(name="/help", value="この文章を送信します。まあこの文章を読めてる時点で/helpって打ってるんだよね君", inline=False)
    embed.add_field(name="/(コマンド)で反応する単語一覧", value="dc、root、m、いちごおばけ、noxのどれかを打つと反応します", inline=False)
    embed.add_field(name="おはよう、まいにち過疎", value="特定の文章を返します", inline=False)
    
    
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed)

               
@bot.event
async def on_message(message):
            
    if message.content.startswith('!dc'):
        await message.channel.send('❌ **I am not connected to a voice channel**, Use the summon command to get me in one')
    
    if message.content == "あ":
        await message.channel.send('意味のある発言をしようとは思わないの？？')
    if message.content.startswith('おはよう'):
        await message.channel.send('言動には注意すべきだ。発言者本人は発せられたその言葉の意味や意図をよく考えないで使っているかもしれないが、あらゆる行動に意味を持つように、その言葉を発した意味も当然存在する筈だ。言葉の意味を失わない為に、また、今後は反射的な発言をしないように、今一度、その発言の意味を深く考えてみてはどうだろうか。')
    if message.author.bot==True:return
    if message.content.startswith('まいにち過疎'):
        await message.channel.send('わかる')
    await bot.process_commands(message)
 
bot.run(token)
