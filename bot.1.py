import discord
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

bot.run("token")
