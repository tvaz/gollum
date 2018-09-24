#!/home/bots/venv/bin/python

import random
import re
import discord
from discord.ext import commands
from _token import token

bot = commands.Bot(command_prefix="!")
active_riddle = ""
riddles = {"What has roots as nobody sees,\nIs taller than trees\nUp, up it goes,\nAnd yet never grows?":"A mountain",
"Voiceless it cries,\nWingless flutters,\nToothless bites,\nMouthless mutters.":"Wind",
"It cannot be seen, cannot be felt.\nCannot be heard, cannot be smelt.\nIt lies behind stars and under hills,\nAnd empty holes it fills.\nIt comes first and follows after,\nEnds life, kills laughter.":"Dark",
"Alive without breath,\nAs cold as death;\nNever thirsty, ever drinking,\nAll in mail never clinking.":"Fish"}

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

@bot.command()
async def precious():
    answer = "My precious......."
    if random.randint(0, 14) == 14:
        answer = "GOLLUM"
    await bot.say(answer)

@bot.command()
async def riddle():
    global active_riddle
    active_riddle = random.choice(list(riddles.keys()))
    await bot.say(active_riddle)

@bot.command()
async def guess(guess : str):
    global active_riddle
    if active_riddle == "":
        await bot.say("Hobbits got to ask a question first...")
        return
    answer = riddles[active_riddle]
    if answer == guess:
        await bot.say("Yessss....correct...")
        active_riddle = ""
    else:
        phrase = random.choice(["I wonder what hobbitses taste like...", "Wrong wrong wrong!!", "Munch crunch munch..."])
        await bot.say(phrase)

bot.run(token)
