import discord
from discord.ext import commands
import random, os
import requests

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
async def Contaminado(ctx):
    list_images = os.listdir('ImagenesBotEcologistaContaminante')
    img_name = random.choice(list_images)
    with open(f'ImagenesBotEcologistaContaminante/{img_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

@bot.command()
async def NoContaminado(ctx):
    list_images = os.listdir('ImagenesBotEcologistaNoContaminante')
    img_name = random.choice(list_images)
    with open(f'ImagenesBotEcologistaNoContaminante/{img_name}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

bot.run("token")
