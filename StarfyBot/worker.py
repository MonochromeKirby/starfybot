import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os

bot = commands.Bot(command_prefix="st!")

@bot.event
async def on_ready():
  print(bot.user.name)

@bot.command(pass_context=True)
async def test(ctx):
  await bot.say("Fii~!")

bot.run(os.environ['BOT_TOKEN'])