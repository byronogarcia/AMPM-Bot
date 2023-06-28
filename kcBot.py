# bot.py

import os
import discord
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.typing = False

TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!',intents=intents)
# bot = commands.Bot(command_prefix='!')

@bot.command(name='kcls', help='not helping you')
async def chooseQuoteKC(ctx):
	kc_quotes = [
		'classic KC :rofl:',
		'you are changing the game!! :rofl:',
		'now this, is gonna turn my world upside down :rofl:',
		'hack my life why don\'t ya! :rofl:',
		'now this is pod racing :rofl:',
		'fanta? More like fonta (i like fonts)',
		'asklsdfjklaeh'
	]

	response = random.choice(kc_quotes)
	await ctx.send(response)

@bot.command(name='frizz', help='not helping you')
async def chooseQuoteFR(ctx):
	frizz_quotes = [
		'whats up fuckers',
		'good evening fuckers',
		'good morning fuckers',
		'good night fuckers',
		'sleep tight fuckers'
	]

	response = random.choice(frizz_quotes)
	await ctx.send(response)

bot.run(TOKEN)


