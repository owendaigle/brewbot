"""
FILE: BrewBot 0.2
VERSION: Rewrite 2.0
AUTHORS: TheRuntingMuumuu, TheTechRobo
LICENSE: ttr please fill out
SOURCE STATUS: Close Source
ABOUT: This is the random brewbot that TTR and TRM are making. It serves absolutely no purpose but it helps me learn about python, coding, and using APIs.
SOURCES: in the comments or in sources.txt
"""

#--Lots of module imports--
import discord
from discord.ext import commands
import sys, traceback
from discord.ext.commands import Bot
from store_data import *
import asyncio, heapq, configparser, logging, discord, random

#--The prefix for the bot--
bot = commands.Bot(command_prefix="brew ")

#--Loads all the additional files using cogs--
initial_extensions = ['fun2', 'system', 'brewcoin2']

for extension in initial_extensions: #runs the amount of times of files to load
    bot.load_extension(extension) #loads
    print(f'\nThe {extension} has loaded')

async def status(): #function for changing the status
    print("\nA stamden has changed the bot status") #console.log
    choices = ["a river","brew out of the faucet"] #what is can be changed to
    await bot.change_presence(activity=discord.Streaming(url="https://www.youtube.com/watch?v=ivSOrKAsPss", name=random.choice(choices))) #changes it, link required for streaming status to work

#--When the bot loads--
@bot.event
async def on_ready():
    print("\n-----------------------------------------------\n<----Hits-Head-on-Cabinet has logged in...---->\n-----------------------------------------------") #tell console bot is logged in
    while True: #repeat forever
        await status()
        await asyncio.sleep(20)

@bot.event
async def on_command_error(ctx, error):
    """
    Does some stuff in case of cooldown error.
    """
    if isinstance(error, commands.CommandOnCooldown):
        potentialMessages = [f'This command is on cooldown, please wait {int(error.retry_after)}s.', f'Searching for more coins to excavate... ({int(error.retry_after)}s)', f'The GPU overheated. Hopefully it did not die, or you may have a hard time finding a new one... {int(error.retry_after)}s.', f'You should not be greedy and mine too many brewcoins... Please try again in {int(error.retry_after)}s.', f'The drill is overheated. You cannot brewcoin yet. Please wait {int(error.retry_after)}s.', f'Bad things may happen if you do not wait {int(error.retry_after)} more seconds before mining again... :ghost:']
        await ctx.send(random.choice(potentialMessages))
        print('\nAn anonymous magcro tried to do a command that was on cooldown')

def TheColoursOfTheRainbow(): #to choose a random RGB value
    colours = []
    for i in range(0,3):
        colours.append(random.randint(0,255))
    return colours



bot.run('ODIzNzIyNDk5MDU3Mzg1NDkz.YFk9Ww.7np2a793tTK4H061CXbu2O_Yh20')