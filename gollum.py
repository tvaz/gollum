#!/home/bots/venv/bin/python

import random
import re
import discord
from discord.ext import commands
from _token import token
import json
import logging
import datetime

logger = logging.getLogger("gollum")
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch_format = logging.Formatter('%(asctime)s - %(message)s')
logger.addHandler(ch)
log_file = "/home/bots/gollum/gollum_" + datetime.datetime.today().strftime("%m_%d") + ".log"
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
fh_format = logging.Formatter('%(asctime)s - %(lineno)d - %(levelname)-8s - %(message)s')
fh.setFormatter(fh_format)
logger.addHandler(fh)

bot = commands.Bot(command_prefix="!")
active_riddle = ""
riddles = {}

with open('/home/bots/gollum/riddles.json') as riddle_data:
	riddles = json.load(riddle_data)

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
    logger.info("Asking the following riddle...")
    active_riddle = random.choice(list(riddles.keys()))
    logger.info(active_riddle)
    await bot.say(active_riddle)

@bot.command()
async def guess(guess : str):
    global active_riddle
    logger.debug("Recieved guess for Active riddle:")
    logger.debug(active_riddle)
    logger.debug("The guess was:    "+guess)
    if active_riddle == "":
        logger.debug("Guess was empty!")
        await bot.say("Hobbits got to ask a question first...")
        return
    answer = riddles[active_riddle]
    logger.debug("Expected answer was:   " + answer)
    if answer == guess:
        logger.debug("Success!")
        await bot.say("Yessss....correct...")
        active_riddle = ""
    else:
        logger.debug("Failure")
        phrase = random.choice(["Wrong wrong wrong!!", "Munch crunch munch..."])
        await bot.say(phrase)

bot.run(token)
