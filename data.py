import discord

def  init():
    global bot_token
    global self_bot_token
    global message
    global embed
    global output_channel
    global input_channels
    global command_channel

    global game_in_session
    global counter_public_1
    global counter_public_2
    global counter_public_3
    global counter_private_1
    global counter_private_2
    global counter_private_3
    global counter1
    global counter2
    global counter3
    global weight
    global weight_time
    global seconds_elapsed

bot_token = 'NjA2NDQ0MDUyODc5MjQ1MzUy.XULJeg.CJ11f8rQ4K6Jn6w0R6yadCb_g6k'
self_bot_token = "NTM3MDkwNzYzMzk0MjUyODEw.XUHMng.EQtjn3gfmK8-D1ZxjHlOLr2N4io"
embed = None
embed_best = None

#trivia-answers
output_channel = discord.Object(id= '606392979212468224')

input_hq_private  = [
    "593990638916075520",
    "590583414541910018",
    "605443517069656084",
	"588070986554015764",
	"496855838703616032",
	"532833017706577930",
	"544381529829146645",
    "558136902885048329",
    "566979656083963918", # answers1
    "559442345674670082", #answers2
    '559357612068700183' #trivia-answers
]
input_hq_public = ['606392979212468224']
command_channel = '606392979212468224' #trivia-answers
admin_chat = '606392979212468224' # answers2

game_in_session = False
counter_public_1 = 0
counter_public_2 = 0
counter_public_3 = 0
counter_private_1 = 0
counter_private_2 = 0
counter_private_3 = 0
counter1 = 0
counter2 = 0
counter3 = 0
weight = 5
weight_time = 1
wronggone1 = 0
wronggone2 = 0
wronggone3 = 0

seconds_elapsed = 0
