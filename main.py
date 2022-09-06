import discord
from discord.ext import commands

TOKEN = "OTg5ODIxNDIwMTk0Mzk0MjQz.GgJ5QQ.V4U6zFOnw7Ix6k9w24ln2W3m2xrU6f3gSnh-KU"
PREFIX = "."
INTENTS = discord.Intents.all()

client = commands.Bot(command_prefix=PREFIX, intents=INTENTS)


@client.event
async def on_ready():
	print(f"{client.user} Is Ready To Go.")


@client.command()
async def ping(ctx):
	await ctx.send(f":ping_pong: My Latency Is {round(client.latency * 1000)} ms.")


client.run(TOKEN)