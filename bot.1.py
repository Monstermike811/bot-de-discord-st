import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saludo(ctx, nombre:str):
    await ctx.send(f"Hola {nombre}, bienvenido a mi servidor")

@bot.command()
async def saludar(ctx):
    await ctx.send(f"Hola {ctx.author.mention}, bienvenido a mi servidor")

@bot.command()
async def suma(ctx, num1:int, num2:int):
    await ctx.send(f"la suma es: {num1 + num2}")

@bot.command()
async def resta(ctx, num1:int, num2:int):
    await ctx.send(f"la resta es: {num1 - num2}")

@bot.command()
async def multiplicar(ctx, num1:int, num2:int):
    await ctx.send(f"la multiplicación es: {num1 * num2}")

@bot.command()
async def dividir(ctx, num1:int, num2:int):
    await ctx.send(f"la división es: {num1 / num2}")

@bot.command()
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    # Joined at can be None in very bizarre cases so just handle that as well
    if member.joined_at is None:
        await ctx.send(f'{member} has no join date.')
    else:
        await ctx.send(f'{member} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command()
async def mem(ctx):
    imagenes = os.listdir("imagenes")
    with open(f'imagenes/{random.choice(imagenes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def animeme(ctx):
    animemes = os.listdir("animemes")
    with open(f'animemes/{random.choice(animemes)}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)

    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

bot.run("token")
