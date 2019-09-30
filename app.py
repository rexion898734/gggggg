import discord
from discord.ext import commands
from discord.ext.commands import Bot
from hq_api import HQApi as hq
import aniso8601
from datetime import datetime
from pytz import timezone
import random
import colorsys
import asyncio
from discord import Game, Embed, Color, Status, ChannelType

api = hq("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI1ODc4OTEzLCJ1c2VybmFtZSI6ImNoZXRhbjE3d3V3dXciLCJhdmF0YXJVcmwiOiJzMzovL2h5cGVzcGFjZS1xdWl6L2RhL2JsdWUucG5nIiwidG9rZW4iOiJXNldmNGIiLCJyb2xlcyI6W10sImNsaWVudCI6IiIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTU2MTg5ODI4NSwiZXhwIjoxNTY5Njc0Mjg1LCJpc3MiOiJoeXBlcXVpei8xIn0.Nqy3wgFtBaA7aef1nRk0cqVirJFNA3bUs8biQElrYzI")

client = commands.Bot(command_prefix="*")
client.remove_command('help')

@client.event
async def on_ready():
    print("I am Ready With HQ")
    while True:
    	await client.change_presence(game=discord.Game(type=1,name="with perfix is *help"))
    	await asyncio.sleep(5)
    	
    	await client.change_presence(game=discord.Game(type=1,name="with *buy"))
    	await asyncio.sleep(5)
    	
    	#await bot.change_presence(activity=discord.Activity(type=1,name="*buy"))
    	#await asyncio.sleep(5)
    	
    	#await bot.change_presence(activity=discord.Activity(type=1,name="with Confetti India!"))
    	#await asyncio.sleep(5)
    	
    	#await bot.change_presence(activity=discord.Activity(type=1,name="with HQ!"))
    	#await asyncio.sleep(5)
    	
    	#await bot.change_presence(activity=discord.Activity(type=1,name="with The Q!"))
    	#await asyncio.sleep(5)
    	
    	#await bot.change_presence(activity=discord.Activity(type=1,name="with My Karma!"))
    	#await asyncio.sleep(5)
    	
    	#await bot.change_presence(activity=discord.Activity(type=1,name="with Jeetoh!"))
    	#await asyncio.sleep(5)
    	
    	#await client.change_presence(activity=discord.Activity(type=2,name="with DRAGON"))
    	#await asyncio.sleep(5)
    	
        #await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'''{len(bot.guilds)} servers'''))
    	#wait asyncio.sleep(5)
    
@client.event
async def on_member_join(member):
    print("In our server" + member.name + " joined just joined")
    await client.send_message(member, 'JOIN TO OUR OFFICIALS SERVER @everyone    Our server is going to no¹ bot server in whole discord.....                 Because--- GAME   ANS TIME   ACCQURACY LOCO  →   7SEC    →   10/10 (CNF) JEETHO →  7SEC    →   8/8  (CNF ) QUREKA → 10MIN  → ALL (CNF) SWOO   →   7SEC    →  10/10(CNF) CONFEETI → 7SEC  → 10/10(9/10) HQ          →   7SEC   →   90% (CNF) SWAIG IQ →  7SEC  →   99%(CNF) SUPER FAST BOT SERVER ............ 7SEC ka matlab→ ( WHEN COUNT 10,9,8,7 -- ANSWER ) @SPARK TRIVIA  JOIN FIRST  https://discord.gg/6XArvCz')
    print("Sent message to " + member.name)

@client.command(pass_context=True,no_pm=True)
async def help(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed=discord.Embed(title="Help Commands", description="HQ LIVES BOT & LOCO COIN", color=0x15ff00 )
    embed.add_field(name="*swipe", value="*e.g.:* `*swipe +1315348829`", inline=False)
    embed.add_field(name="*code", value="*e.g.:* `*code 1234`", inline=False)
    embed.add_field(name="*hquser", value="*e.g.:* `*hquser abcd`", inline=False)
    embed.add_field(name="next Show Time of HQ", value="*e.g.:* `*nexthq`", inline=False)
    embed.add_field(name="for loco+play", value="*e.g.:* `$play +91<number>`", inline=False)
    embed.add_field(name="$code", value="*e.g.:* `$code 1234`", inline=False)
    embed.set_footer(text="MADE BY SPARK")
    await client.say(embed=embed)
    
@client.command(pass_context=True,no_pm=True)
async def nexthq(ctx):
    show = api.get_show()
    time = show["nextShowTime"]
    tm = aniso8601.parse_datetime(time)
    x =  tm.strftime("%Y-%m-%d %H:%M:%S")
    x_ind = tm.astimezone(timezone("Asia/Kolkata"))
    x_in = x_ind.strftime("%Y-%m-%d %H:%M:%S")
    prize = show["nextShowPrize"]
    stype = show["upcoming"][0]["showType"]+show["upcoming"][0]["gameType"]
    await bot.say(f"**Time For Next HQ in UTC ** --> {x} \n\n **Time For HQin Indain TimeZone** --> {x_in} \n\n **Prize of Next HQ** --> {prize} \n\n **Type of HQ game** --> {stype} \n\n **creacted by SPARK** --> {stype}")

@client.command(pass_context=True,no_pm=True)
async def hquser(ctx,username:str):
    userid = api.search(username)["data"]
    if len(userid) == 0:
        await client.say("No Username Found :(")
        return
    userid = userid[0]["userId"]
    usdet = api.get_user(userid)
    name = usdet["username"]
    account_at = usdet["created"]
    a_time = aniso8601.parse_datetime(account_at).strftime("%Y-%m-%d %H:%M:%S")
    t_games = usdet["gamesPlayed"]
    t_wins = usdet["winCount"]
    t_money = usdet["leaderboard"]["total"]
    r_money = usdet["leaderboard"]["unclaimed"]
    c_season = usdet["seasonXp"][0]["name"]
    c_points = usdet["seasonXp"][0]["currentPoints"]
    t_points = usdet["seasonXp"][0]["remainingPoints"]
    c_level = usdet["seasonXp"][0]["currentLevel"]["level"]

    await client.say(f" **Username From HQ ** -- > {name} \n\n **Account created At** --> {a_time} \n\n  **Total games that you played **  --> {t_games} \n\n  **Total Wins in HQ** --> {t_wins} \n\n **Total money you Won ** --> {t_money} \n\n **Unclaimed Money** --> {r_money} \n\n **This Season Name **--> {c_season} \n\n **Current Points** --> {c_points} \n\n **Remaining Points** --> {t_points} \n\n **Your Current Level** --> {c_level}")
details = {}

@client.command(pass_context=True,no_pm=True)
async def swipe(ctx,num:str):
    try:
        api2 = hq("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI1ODc4OTEzLCJ1c2VybmFtZSI6ImNoZXRhbjE3d3V3dXciLCJhdmF0YXJVcmwiOiJzMzovL2h5cGVzcGFjZS1xdWl6L2RhL2JsdWUucG5nIiwidG9rZW4iOiJXNldmNGIiLCJyb2xlcyI6W10sImNsaWVudCI6IiIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTU2MTg5ODI4NSwiZXhwIjoxNTY5Njc0Mjg1LCJpc3MiOiJoeXBlcXVpei8xIn0.Nqy3wgFtBaA7aef1nRk0cqVirJFNA3bUs8biQElrYzI")
        method = "sms"
        details[ctx.message.author.id] = {}
        details[ctx.message.author.id]["num"] = num
        otp = api2.send_code(num,method)
        details[ctx.message.author.id]["v_id"]  = otp["verificationId"]
        await client.say("If the number is your's you will get a One Time Password!. \n\n ** Now use +code <otp>**  \n\n **SPARK")
    except:
        await client.say("wrong input +swipe +1<number> no Indian numbers banned use us numbers  \n\n **MADE BY DRAGON{dev}**")
    
def rand():
    ran = random.randint(3,12)
    x = "1234567890abcdefghijklmnopqrstqvwxyzABCDEFGHIJKLMNOPQRSTQVWXYZ"
    name = ""
    for i in range(ran):
        c = random.choice(x)
        name = name+c
    check = api.check_username(name)
    if not check:
        return name
    else:
        return rand()
    
@client.command(pass_context=True,no_pm=True)
async def code(ctx,code):
    if ctx.message.author.id in details:
        api3 = hq("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI1ODc4OTEzLCJ1c2VybmFtZSI6ImNoZXRhbjE3d3V3dXciLCJhdmF0YXJVcmwiOiJzMzovL2h5cGVzcGFjZS1xdWl6L2RhL2JsdWUucG5nIiwidG9rZW4iOiJXNldmNGIiLCJyb2xlcyI6W10sImNsaWVudCI6IiIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTU2MTg5ODI4NSwiZXhwIjoxNTY5Njc0Mjg1LCJpc3MiOiJoeXBlcXVpei8xIn0.Nqy3wgFtBaA7aef1nRk0cqVirJFNA3bUs8biQElrYzI")
        v_id = details[ctx.message.author.id]["v_id"]
        cnf = api3.confirm_code(v_id,code)
        #if "accessToken" not in api3:
            #return print(api3["error"])
        #await client.say(f'{api3["username"]}\'s access token:\n==============\n{api3["accessToken"]}\n==============')
        if cnf["auth"] ==  None:
            ran = random.randint(3,12)
            await client.say("No Account found from HQ...That's Why I am creating New account and apply Swipe  \n\n **made by-panda{dev} and chetan{dev}**")
            ref = "mahimahesh19"
            name = rand()
            y = api3.register(v_id, name, refferal)
            print(y)
            await client.say("Account has been created with username {name}")
            details[ctx.message.author.id]["auth"] = y["auth"]["authToken"]
            tst = await client.say("Already swiped😋 \n\n **made by-dragon**")
            api = hq(details[ctx.message.author.id]["auth"])
            x = api.easter_egg()
            if "error" in x:
                await client.say("No Swipe for you... Sry ¯\_(ツ)_/¯ " )
            elif "data" in x:
                await client.edit_message(tst,"Hurre... That's all you got your :heartpulse: in your account 😗")
                await client.say(f'{api["username"]}\'s access token:\n==============\n{api["accessToken"]}\n==============')
            
        details[ctx.message.author.id]["auth"] = cnf["auth"]["authToken"]
        tst = await client.say("Already swiped😋 \n\n **made by-dragon**")
        api = hq(details[ctx.message.author.id]["auth"])
        x = api.easter_egg()
        if "error" in x:
            await client.say(x["error"])
        elif "data" in x:
            await client.edit_message(tst,"Hurre... That's all you got your :heartpulse: in your account  \n\n **made by-SPARK**")
    else:
        await client.say("Pleas Use Number first")
        
        
@client.command(pass_context=True,aliases=['servercount'])
async def work(ctx):
     if ctx.message.author.id == "584791464933064705":
             servers = list(client.servers)
             numbers = str(len(client.servers))
             print("Connected on " + str(len(client.servers)) + " servers")
             await client.say("watching `" + str(len(client.servers)) + "` servers!")


@client.command(pass_context = True)
async def buy(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Buy BOT & SCRIPT')
    embed.set_image(url = 'https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif')
    embed.add_field(name = '``if u want bot ur script then contact spark `our server link https://discord.gg/mX9MqE` ',value ='',inline = False)
    await client.send_message(author,embed=embed)
    await client.say('📨 Check DMs To buy ')

@client.command(pass_context = True)
#@commands.has_permissions(kick_members=True)
async def serverlist(ctx):
    for server in client.servers:
        #print(server.name)
        await client.say(server.name) 
        await client.say(server.id)
        #await client.say(server.link)
        
    
client.run("NjI3MDE4MTAyOTQ4NzU3NTI0.XY2iWA.rVkCqRbb8fr2P-NA6jVZSoGn04U")
