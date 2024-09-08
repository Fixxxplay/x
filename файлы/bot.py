import discord
from discord.ext import commands
import requests
import os
import random
from random import choice
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())
@bot.command('memprog')
async def mem_prog(message):
    a = os.listdir('images')
    result = random.choice(a)
    with open(f'images/{result}', 'rb') as f:
        pict = discord.File(f)
    await message.send(file = pict)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('memjj')
async def mem_jj(message):
    b = os.listdir('memsjj')
    result = random.choice(b)
    with open(f'memsjj/{result}', 'rb') as f:
        pict = discord.File(f)
    await message.send(file = pict)


@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)


bot.run('')