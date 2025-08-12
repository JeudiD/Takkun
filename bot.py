import os
import logging
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'
)

bot = commands.Bot(command_prefix='t', intents=intents)

@bot.event
async def on_ready():
    logging.info(f"✅ Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run(TOKEN)
