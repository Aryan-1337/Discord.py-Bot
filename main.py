import discord
from discord.ext import commands

TOKEN = "OTg5ODIxNDIwMTk0Mzk0MjQz.GWl1WR.P0HPm8jbd1LJLWnuHnFbSZNOD6UFhARqokLEz8"
PREFIX = "."
INTENTS = discord.Intents.all()

client = commands.Bot(command_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
	print(f"{client.user} Is Ready To Go.")


@client.command()
async def ping(ctx):
	await ctx.send(f":ping_pong: My Latency Is {round(client.latency * 1000)} ms.")


client.load_extension("cogs.Moderation")
client.run(TOKEN)