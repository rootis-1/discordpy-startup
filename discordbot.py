
import discord
from discord.ext import commands
import os
import traceback
import random
import json
import math
import base64
import re
import asyncio

bot = commands.Bot(command_prefix='/',help_command=None)
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event #FalseCommand
async def on_command_error(ctx, error):
    print(error)
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('そんなコマンドないよ？出直してきな？')
    elif isinstance(error,commands.UserInputError):
        await ctx.send('コマンド情報の取得に失敗しました。')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name='new電波人間のRPG'))

    
@bot.command()
async def m(ctx):
    await ctx.send('まいにち過疎')
    
@bot.command()
async def root(ctx):
    await ctx.send('誰が漏斗じゃい')
 
@bot.command()
async def dc(ctx):
    await ctx.send('fuck')
    
@bot.command()
async def r(ctx):
    await ctx.send('(´・υ・｀)')
    
    
@bot.command()
async def いちごおばけ(ctx):
    await ctx.send('さいつお！')
    
@bot.command()
async def わたる(ctx):
    wataru = ["伊藤","安藤","黒船来","鴨浦","浅村","出雲","浅井","泉","藤原","斎藤","お前は俺の","喋れよ","出野"]
    choice = random.choice(wataru)
    await message.channel.send(choice+"航")
    
#@bot.command()
#async def start(ctx):
    #await ctx.send('待たせたな！')
    
@bot.command()
async def wau(ctx):
    await ctx.send("""いちごおばけとは
日本のゲームソフト開発会社ジニアスソノリティが2014年7月23日にニンテンドー3ds用ソフトとして無料配信したゲーム『電波人間のRPG free』に登場する敵キャラクターだ。
ステージ1の最初の敵としては妥当なhpと攻撃力。技も単体攻撃のみと特徴は無い。
しかし筆頭すべき点として、無効化する事のできない行動停止技「なめる」を使用する事がある。普通に戦うぶんにはあまり気にならないが、この
「無効化する事のできない行動停止技」、これを扱うモンスターは非常に少なく、その殆どはステージ後半に出現する強力な敵である。
そんな中最初に登場するいちごおばけがこの技を会得している事は偉業なのではないだろうか。
また、いちごおばけ型のモンスターは他にも多種登場する。
v1.0のメインラスボスのいるステージ9の雑魚敵として現れるおばけホイップやイベントステージに出現するチョコホイップ。
ストーリー後半に登場するくさったいちご、くさりきったいちご。
又、その他色々なステージにいちごおばけ型のモンスターは出現している。最早「電波人間のRPG free」における看板モンスターと言っても過言では無いだろう。
最後に、ステージ1に登場するいちごおばけの特徴を置いてこの文章を締めようと思う。
Lv1、HPは8(乱数で前後)、弱点属性は土水光。そして闇属性に耐性を持つ。
ドロップ品は2Gとたまにキズぐすり、稀にぜんかいキズぐすりを落とす。
アンテナ「捕まえる」で使用する場合はAP1で「ひっかく」を使う
以上、いちごおばけについての解説を終わる。""")
    
@bot.command(aliases=['exp'])
async def 経験値(ctx,lv:int,*args):
    
    f = open("other/data.txt","r")
    items = f.readlines()
    target = int(items[lv-1])
    f.close()
    
    expdown = 0
    
    if len(args)>0:
        expdown = int(args[0])/100
        
    explist = [str(math.floor(target*(1-i*0.01)*(1-expdown))) for i in range(8)]
    l = []
   
    for i in range(8):
        l.append(chr((i+65))+"\t"+explist[i])
        
    embed=discord.Embed(title="経験値の一覧", description="各属に当てはまる可能性のある体格", color=0x80ffff)
    embed.add_field(name="A", value="回避0 最大型", inline=False)
    embed.add_field(name="B", value="回避0 準大／中間／準速／最速", inline=False)
    embed.add_field(name="C", value="回避3 最大型／準大-1／準準大-1／準準速-2／準速-2", inline=False)
    embed.add_field(name="D", value="回避3 準大-2／準準大2／準準速-1／準速-1／最速", inline=False)
    embed.add_field(name="E", value="回避6 最大／準大-2／中間-2／中間-3", inline=False)
    embed.add_field(name="F", value="回避6 準大-1／中間-1／準速／最速", inline=False)
    embed.add_field(name="G", value="回避10 最大／中間／最速\n回避15 最大／中間", inline=False)
    embed.add_field(name="H", value="回避15 最速", inline=False)
    
    await ctx.send(embed=embed)
    await ctx.send("【"+str(lv)+" Lv】\n```"+"\n".join(l)+"```")
    
@bot.command()
async def hp(ctx,an:str,lv:int,*args):
    
    f = open("other/anhp.txt","r")
    items = f.readlines()
    
    items = [i.replace("\n","") for i in items]
    
    if an in items:
        p = items.index(an)
    else:
        await ctx.send("そのアンテナのステータスは記録されていません。")
        f.close()
        return
    f.close()
    
    f = open("other/hps.txt","r")
    items = f.readlines()
    
    renga = 1
    if len(args)>=1:
        if args[0] == "+":
            renga = 1.15
    
    if items[p].startswith("ー"):
        await ctx.send("そのアンテナのステータスは記録されていません。")
        f.close()
        return
    else:
        target = int(items[p]) #そのアンテナのLv1最大型
        n = target/40
        print(n)
             
        f = open("other/hp.txt","r")
        items = f.readlines()
             
        #await ctx.send(str(math.floor(n*int(items[lv-1]))))
        
        i = 0
        string = []
        
        for i in range(1,11):
            string.append(str(i).ljust(5)+str(math.floor(((1-0.067*(i-1))*n*int(items[lv-1])*renga))))
        
        f.close()
        await ctx.send("【アンテナ "+an+" の "+str(lv)+" Lvの体格ごとHP】\n"+"```"+"\n".join(string)+"```")
        #0.067を引いていく。HP2は((1-(0.067*(2-1)))*hp)

    
    
@bot.command()
async def リサイクル(ctx,rare:int):
    if rare==9:
        rand=0
    elif rare>1 and rare<10:
        rand = random.randrange(0,10) #レア度の上下調整
        
        if rand==1:
            rand=-1
        elif rand==9:
            rand=1
        else:rand=0
        
        rare += rand
    elif rare<=1:
        rare = 1
        rand = random.randrange(0,10)
        
        if rand<=4:
            rand=0
        else:
            rand=1
            
        rare += rand
    elif rare>=10:
        rare = 10
        rand = random.randrange(0,10)
        
        if rand<=4:
            rand=0
        else:
            rand=-1
            
        rare += rand
        
    resrand = random.randrange(0,2) #レア度ごとに2つのセリフがあるので、それを選択（0のとき1つめ、1のとき2つめ）
        
    res1 = ["んー、こういうこともあるよね。","ちょっと残念？","はい、どうぞ～。","かんせ～い！","すごい、すごーい！","ほわぁ！大成功だよ！"]
    res2 = ["ができたわ。","ができたわ。","ができたわよ。","ができたわ。","ができたわ！","ができたー！"]
    
    fname = "rare/rare"+str(rare)+".txt" #ファイルのパス
    f = open(fname,"r") #ファイルの読み込み
    items = f.readlines() #ファイル.readlines()で行ごとにリスト化
    f.close()
    
    result = items[random.randrange(0,len(items))]
    result = result.replace("\n","") #readlinesは各行の改行コードを読んでしまうため改行コードを消去
    
    await ctx.send(ctx.author.mention + res1[(3+resrand+2*rand)-1] + " ☆" + str(rare) + "の\n**" + result + "**ができたわ。")

@bot.command(name="ダブルアップ")
async def double_up(ctx):
    """
    「ダブルアップチャンス！」を開始します。
    """
    depth = 1 # 現在の階層

    HOLE = "\N{HOLE}\N{VARIATION SELECTOR-16}"
    LEFT_ARROW = "\N{LEFTWARDS BLACK ARROW}\N{VARIATION SELECTOR-16}"
    RIGHT_ARROW = "\N{BLACK RIGHTWARDS ARROW}\N{VARIATION SELECTOR-16}"
    TOP_ARROW = "\N{UPWARDS BLACK ARROW}\N{VARIATION SELECTOR-16}"
    emojis = [LEFT_ARROW,RIGHT_ARROW] # 通常の穴選択用絵文字リスト
    final_emojis = [LEFT_ARROW,TOP_ARROW,RIGHT_ARROW] # 最後の穴選択用絵文字リスト


    def gold_check(msg):
        # 掛け金の入力チェック用
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.isdecimal()

    embed = discord.Embed(title="ダブルアップ",description=f"{ctx.author.mention} 掛け金を入力してください。",color=0x0000ff)
    await ctx.send(embed=embed)

    try:
        gold_msg = await bot.wait_for("message",check=gold_check,timeout=30.0)
    except asyncio.TimeoutError:
        embed = discord.Embed(title="エラー",
            description=f"{ctx.author.mention} 掛け金の正常な入力が確認されませんでした。コマンドの処理を終了します。",
            color=0xff0000)
        await ctx.send(embed=embed)
        return

    gold = int(gold_msg.content)
    embed = discord.Embed(title=f"どちらの穴に入るか選ぼう！（{depth}回目）",
        description=f"{HOLE}\t{HOLE}\n{LEFT_ARROW}\t{RIGHT_ARROW}",color=0x00ff00)
    embed.set_footer(text=f"掛け金：{gold * 2} G")

    game_msg = await ctx.send(embed=embed) # ゲーム用メッセージ。以降はこれを編集してゲームを表現する。

    while depth < 5:
        await game_msg.edit(embed=embed)

        for emoji in emojis:
            await game_msg.add_reaction(emoji) # 穴選択用絵文字でリアクションする

        def hole_check(reaction,user):
            # 穴の入力チェック用
            react_msg = reaction.message
            are_same_msgs = react_msg.id == game_msg.id and react_msg.channel == game_msg.channel # メッセージの同一性
            return are_same_msgs and user == ctx.author and str(reaction.emoji) in emojis

        try:
            hole_react,user = await bot.wait_for("reaction_add",check=hole_check,timeout=30.0)
        except asyncio.TimeoutError:
            embed = discord.Embed(title="エラー",
                description=f"{ctx.author.mention} 穴の選択が正常に行われませんでした。コマンドの処理を終了します。",
                color=0xff0000)
            await ctx.send(embed=embed)
            return
        
        if random.randrange(2) == 0:
            # 2分の1の確率ではずれを引く
            embed = discord.Embed(title=f"はずれー！！",
                description=f"{ctx.author.mention} 懲りずに、また挑戦してみてね！",color=0x00ff00)
            await ctx.send(embed=embed)
            return

        depth += 1
        gold *= 2

        await hole_react.remove(user)
        embed = discord.Embed(title=f"当たり！次の穴を選んでね！（{depth}回目）",
            description=f"{ctx.author.mention}\n{HOLE}\t{HOLE}\n{LEFT_ARROW}\t{RIGHT_ARROW}",
            color=random.randrange(0xffffff))
        embed.set_footer(text=f"次の掛け金：{gold * 2} G")
        
    embed = discord.Embed(title=f"当たり！次の穴が最後！（{depth}回目）",
        description=f"{HOLE}\t{HOLE}\t{HOLE}\n{LEFT_ARROW}\t{TOP_ARROW}\t{RIGHT_ARROW}",
        color=random.randrange(0xffffff))
    embed.set_footer(text=f"掛け金：{gold * 2} G")
    await game_msg.edit(embed=embed)
    await game_msg.clear_reactions() # 最後は中間にもう一つ穴が追加されるので、全てのリアクションを削除しておく

    for emoji in final_emojis:
        await game_msg.add_reaction(emoji)

    def hole_check_final(reaction,user):
        # 最後の穴の入力チェック用
        react_msg = reaction.message
        are_same_msgs = react_msg.id == game_msg.id and react_msg.channel == game_msg.channel
        return are_same_msgs and user == ctx.author and str(reaction.emoji) in final_emojis

    try:
        await bot.wait_for("reaction_add",check=hole_check_final,timeout=30.0)
    except asyncio.TimeoutError:
        embed = discord.Embed(title="エラー",
            description=f"{ctx.author.mention} 穴の選択が正常に行われませんでした。コマンドの処理を終了します。",
            color=0xff0000)
        await ctx.send(embed=embed)
        return

    if random.randrange(3) != 2:
        # 3分の2の確率ではずれを引く
        embed = discord.Embed(title="はずれ。",
            description=f"{ctx.author.mention} 君たちは一体今までにいくら貢いだんだろうね",color=0x00ff00)
        await ctx.send(embed=embed)
        return

    gold *= 2

    embed = discord.Embed(title="おめでとう！",
        description=f"{ctx.author.mention} **{gold}** G入手したよ！\n達成できたのは今回で…何回目だったっけ",color=0x0000ff)
    await ctx.send(embed=embed)


@bot.command() #ヘルプ
async def help(ctx):
    embed=discord.Embed(title="いちごおばけbot", description="いちごおばけbotについての説明です。", color=0x80ffff)
    embed.add_field(name="/help", value="この文章を送信します。まあこの文章を読めてる時点で/helpって打ってるんだよね君", inline=False)
    embed.add_field(name="/(コマンド)で反応する単語一覧", value="dc、root、m、いちごおばけ等の単語を打つと反応します。他にも反応する単語があるかも？", inline=False)
    embed.add_field(name="/リサイクル レア度", value="リサイクルをします。レア度には1~10の数字を入力してください。", inline=False)
    embed.add_field(name="/ダブルアップ", value="ダブルアップチャンスを開始します。", inline=False)
    embed.add_field(name="おはよう、おやすみ、まいにち過疎", value="特定の文章を返します", inline=False)
    
    dm_channel = await ctx.author.create_dm()
    await dm_channel.send(embed=embed)

               
@bot.event
async def on_message(message):
    
    if message.content.startswith('?uranai'):  #botの書き方が下手糞！
        uranai = ["おみくじ？どーでもいいけど大吉っていう文字列出しとけば気が楽になるんでしょ？はい、大吉。","""大吉をあげたいところだけど…、仕方ない。
本当はこんな事したくないんだけどね…？中吉だよ。""","""占って欲しいんだね？
…君もわかっているはずさ。この占いがランダムに生成されるだけのシステムに過ぎない事を。それでも君たちは求める。何故だろうね。僕には理解できないよ。
ああ、そうそう、忘れてたよ。小吉。これで満足かい？""","""大吉が欲しい？文面のみの情報に全てを委ねるのかい？君は。全く、そんな訳ないだろう？
いいかい？運なんて所詮、心の拠り所に過ぎないのさ。例え君が何かに失敗したとき、君はそれを運のせいにする事ができる。
さあ、受け取りたまえ。君の失敗を、このおみくじに全て押し付けるんだ。凶だよ。"""]
        choice = random.choice(uranai)
        await message.channel.send(choice)
    if message.content.startswith('ごめん'):
        yurusu = ["赦しましょう","赦しましょう","赦しません"]
        choice = random.choice(yurusu)
        await message.channel.send(choice)
    if message.content.startswith('〆'):
        simeru = ["勝手に〆ないで貰えるかな？","勝手に〆ないで貰えるかな？","勝手に〆ないで貰えるかな？","便乗して〆"]
        choice = random.choice(simeru)
        await message.channel.send(choice)
    if message.content.startswith('?slot'):
        await message.channel.send("""|:poop:|:laughing:|:poop:|
Boo :weary:""")          
    if message.content.startswith('!dc'):
        await message.channel.send('❌ **I am not connected to a voice channel**, Use the join command to get me in one')
    if message.content.startswith('おやすみ'):
        await message.channel.send(message.author.name+'、おやすみ、だって？どうせまだ寝ないだろう？')
    if message.content.startswith('||'):
        await message.channel.send('これからもそうやって真実を隠し続けるんだろうね')
    if message.content.startswith('〜'):
        await message.channel.send('ー')
    if message.content.startswith('おはよう'):
        await message.channel.send('言動には注意すべきだ。発言者本人は発せられたその言葉の意味や意図をよく考えないで使っているかもしれないが、あらゆる行動に意味を持つように、その言葉を発した意味も当然存在する筈だ。言葉の意味を失わない為に、また、今後は反射的な発言をしないように、今一度、その発言の意味を深く考えてみてはどうだろうか。')
    if message.author.bot==True:return
    if message.content.startswith('まいにち過疎'):
        await message.channel.send('わかる')
    if 564709839859744769 in message.raw_channel_mentions:
        await message.channel.send('まいにち過疎')
    await bot.process_commands(message)
  
 
bot.run(token)
