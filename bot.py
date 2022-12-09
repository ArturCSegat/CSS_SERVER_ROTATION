import discord
from discord.ext import commands
from server import Server


bot = commands.Bot(command_prefix=":", intents=None)

server = Server(10, 15, "C://steamcmd/css_ds")

@bot.event
async def on_ready():
    server.startServer()
    channel = await bot.get_channel(581159663345860619) # ggez
    await channel.send(f"Server ta on no mapa {server.queue.current_map.name}")

@bot.event
async def on_resumed():
    server.killServer()
    channel = await bot.get_channel(581159663345860619) # ggez
    await channel.send(f"matei o server")


@bot.command
async def skip(ctx):
    server.nextMap()
    await ctx.send(f"Mapa mudado para {server.queue.current_map.name} entra dnv")




bot.run("")

