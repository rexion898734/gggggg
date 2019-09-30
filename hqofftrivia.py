#from HQApi 
import HQApi
from HQApi.exceptions import ApiResponseError
import random
import requests
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import random
import aiohttp
import csv
import json
import datetime
import string
import aniso8601
from datetime import datetime
from pytz import timezone


client = Bot(command_prefix='+')
client.remove_command('help')

#token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI2MDkzMjkzLCJ1c2VybmFtZSI6Im5hbWVzZEo0MjUiLCJhdmF0YXJVcmwiOiJodHRwczovL2Nkbi5wcm9kLmh5cGUuc3BhY2UvZGEvZ29sZC5wbmciLCJ0b2tlbiI6bnVsbCwicm9sZXMiOltdLCJjbGllbnQiOiJBbmRyb2lkLzEuMzkuMCIsImd1ZXN0SWQiOm51bGwsInYiOjEsImlhdCI6MTU2NTg2MDQxMSwiZXhwIjoxNTczNjM2NDExLCJpc3MiOiJoeXBlcXVpei8xIn0.EHLKDZpFsf-JIY_nPyWbtIo0HwPIuqWKYYdusQKC-o8'
api = HQApi()

@client.event
async def on_ready():
    print("Logged in as " + client.user.name)
    print("I'm ready")

@client.command(pass_context=True,no_pm=True)
async def nexthq(ctx):
    api = HQApi()
    show = api.get_show()
    time = show["nextShowTime"]
    tm = aniso8601.parse_datetime(time)
    x =  tm.strftime("%Y-%m-%d %H:%M:%S")
    x_ind = tm.astimezone(timezone("Asia/Kolkata"))
    x_in = x_ind.strftime("%Y-%m-%d %H:%M:%S")
    prize = show["nextShowPrize"]
    stype = show["upcoming"][0]["showType"]+show["upcoming"][0]["gameType"]
    await client.say(f"**Time For Next HQ in UTC ** --> {x} \n\n **Time For HQ in Indain TimeZone** --> {x_in} \n\n **Prize of Next HQ** --> {prize} \n\n **Type of HQ game** --> {stype}")

@client.command(pass_context=True,no_pm=True)
async def myhq(ctx,username:str):
    api = HQApi('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjI2MjAwODQzLCJ1c2VybmFtZSI6Im5hbWVzWm4zNTAiLCJhdmF0YXJVcmwiOiJodHRwczovL2Nkbi5wcm9kLmh5cGUuc3BhY2UvZGEvZ3JlZW4ucG5nIiwidG9rZW4iOm51bGwsInJvbGVzIjpbXSwiY2xpZW50IjoiQW5kcm9pZC8xLjM5LjAiLCJndWVzdElkIjpudWxsLCJ2IjoxLCJpYXQiOjE1Njc4NTM5OTgsImV4cCI6MTU3NTYyOTk5OCwiaXNzIjoiaHlwZXF1aXovMSJ9.i9-MgZ1gS8MHhe7-az-yorIWhDiO5I_uHEgDirA7fF0')
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
async def phone(ctx,num:str):
    try:
        api2 = HQApi()
        method = "sms"
        details[ctx.message.author.id] = {}
        details[ctx.message.author.id]["num"] = num
        otp = api2.send_code(num,method)
        details[ctx.message.author.id]["v_id"]  = otp["verificationId"]
        await client.say("***__You will get a <otp> One Time Password! on ur Phone__*** \n\n **__``Now use +code <otp>``__**")
    except: 
        await client.say("**Rate Limit Exceeded**")
def rand():
    ran = random.randint(3,5)
    x = "1234567890"
    name = "Test"
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
        api3 = HQApi()
        v_id = details[ctx.message.author.id]["v_id"]
        cnf = api3.confirm_code(v_id,code)
        if cnf["auth"] ==  None:
            ran = random.randint(3,6)
            await client.say("`No Account found from HQ...That's Why I am creating New account and apply Swipe`")
            ref = ""
            name = rand()
            y = api3.register(v_id, name, ref)
            print(y)
            await client.say(f"Account has been created with username {name}")
            details[ctx.message.author.id]["auth"] = y["auth"]["authToken"]
            tst = await client.say("Starting Swipe")
            api = HQApi(details[ctx.message.author.id]["auth"])
            x = api.easter_egg()
            if "errorCode" in x:
                await client.say("No Swipe for you... Sry ¯\_(ツ)_/¯ " )
            elif "data" in x:
                await client.edit_message(tst,"Hurre... That's all you got your life in your account")
            
        details[ctx.message.author.id]["auth"] = cnf["auth"]["authToken"]
        tst = await client.say("Starting Swipe")
        api = HQApi(details[ctx.message.author.id]["auth"])
        x = api.easter_egg()
        if "errorCode" in x:
            await client.say(x["error"])
        elif "data" in x:
            await client.edit_message(tst,"Hurre... That's all you got your life in your account")
    else:
        await client.say("Please Use Number first")

client.run("NjIxNjk3Mzg1MTIyMzY1NDQw.XYNh4g.0I2MCCWW1vtLo6Qb2yKRDsHn3VE")
