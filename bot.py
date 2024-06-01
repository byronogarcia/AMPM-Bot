# bot.py

import os
import discord
import random
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.members = True
intents.typing = False

# APP_ID = ""
# SERVER_ID = "SERVER_ID"
TOKEN = os.getenv('DISCORD_TOKEN')

# url with app ID
# url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands'

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
		'asklsdfjklaeh'
	]

	response = random.choice(kc_quotes)
	await ctx.send(response)

@bot.command(name='frizz', help='not helping you')
async def chooseQuoteFR(ctx):
	frizz_quotes = [
		'whats up',
		# 'good evening fuckers',
		# 'good morning fuckers',
		# 'good night fuckers',
		# 'sleep tight fuckers'
	]

	response = random.choice(frizz_quotes)
	await ctx.send(response)

@bot.command(name='disneymovie', help='Get a random Disney movie')
async def get_disney_movie(ctx):
    url = 'https://apidisneymovies.bsite.net/api/v1/movies/all'
    response = requests.get(url)
    
    if response.status_code == 200:
        movies = response.json()
        if movies:
            movie = random.choice(movies)
            movie_title = movie.get('title', 'Unknown Title')
            movie_rating = movie.get('rating', 'No rating available')
            movie_year = movie.get('year', 'Unknown Year')
            movie_image = movie.get('image', None) # embed
            
            embed = discord.Embed(title=movie_title, color=discord.Color.blue())
            embed.add_field(name="Release Year", value=movie_year,inline=True)
            
            if movie_image:
                embed.set_image(url=movie_image)
            
            await ctx.send(embed=embed)
        else:
            await ctx.send("No movies found.")
    else:
        await ctx.send("Failed to fetch Disney movies.")

bot.run(TOKEN)


