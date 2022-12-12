import discord
from discord.ext import commands
from server import Server

intents = discord.Intents.all()
intents.message_content = True

ggez_id = 581159663345860619

bot = commands.Bot(command_prefix=":", intents=intents)

server = Server(10, 15, "C://steamcmd/css_ds")

@bot.event
async def on_ready():
    server.startServer()
    await bot.get_channel(ggez_id).send(f"Server ta on no mapa {server.queue.current_map.name}")

@bot.event
async def on_resumed():
    server.killServer()
    await bot.get_channel(ggez_id).send(f"matei o server")


@bot.command()
async def skip(ctx):
    server.nextMap()
    await ctx.send(f"Mapa mudado para {server.queue.current_map.name} entra dnv")




bot.run("")

