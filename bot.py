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

#-------------------------------------------------
# empty command

# command name is frizz, below is example of how to use it
# !frizz 
@bot.command(name='frizz', help='n/a')
async def chooseQuoteFR(ctx):
	frizz_quotes = [
		'whats up'
        # put phrases in quotation marks
        # multiple phrases can be separated by comma 

        # 'new phrase'
	]
    
    # quote will be picked randomly after command is used
	response = random.choice(frizz_quotes) 
     
    # wait to see if bot will work
	await ctx.send(response)

#-------------------------------------------------


# Example function with random phrases
@bot.command(name='kcls', help='n/a')
async def chooseQuoteKC(ctx):
	kc_quotes = [
		'classic KC :rofl:',
		'you are changing the game!! :rofl:',
		'now this, is gonna turn my world upside down :rofl:',
		'hack my life why don\'t ya! :rofl:'
	]

	response = random.choice(kc_quotes)
	await ctx.send(response)


# Main function displaying use of APIs
@bot.command(name='disneymovie', help='Get a random Disney movie')
async def get_disney_movie(ctx):
    # disney movie online api I found
    url = 'https://apidisneymovies.bsite.net/api/v1/movies/all'
    response = requests.get(url)
    
    # uses available information - title, year, image, and rating
    # excludes movie ID
    if response.status_code == 200:
        movies = response.json()
        if movies:
            movie = random.choice(movies)
            movie_title = movie.get('title', 'Unknown Title')
            movie_rating = movie.get('rating', 'No rating available')
            movie_year = movie.get('year', 'Unknown Year')
            movie_image = movie.get('image', None) # embed
            
            # backgound for message with image
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


