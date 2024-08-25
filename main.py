
import discord
from discord.ext import commands
import random
from random import randint
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)



@bot.command('roll')
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('13d13')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)




bot.run("MTI0MDc1NDI5NzM0MDI5NzMwNg.GS8f68._-6Ykp4jrJ7QO-sjpNnUjWhWAnxou_sgN1oWys")
