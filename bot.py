import os
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")  # Make sure your .env has DISCORD_TOKEN=your_token

# Bot prefix
bot = commands.Bot(command_prefix="t", intents=discord.Intents.all())

# Path to the downloaded audio file
AUDIO_FILE = "lofi.mp3"  # Place your lofi.mp3 in the same folder as this bot

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with a ball of yarn, Meow!"))

@bot.command()
async def play(ctx):
    """Join VC and start playing music on loop."""
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        vc = ctx.voice_client or await channel.connect()

        if not vc.is_playing():
            def after_playing(error):
                # Play again after finishing
                if not error:
                    vc.play(discord.FFmpegPCMAudio(AUDIO_FILE), after=after_playing)

            vc.play(discord.FFmpegPCMAudio(AUDIO_FILE), after=after_playing)
            await ctx.send("🎵 Playing Lofi on loop in your channel!")
        else:
            await ctx.send("❌ Music is already playing.")
    else:
        await ctx.send("❌ You are not in a voice channel!")

@bot.command()
async def stop(ctx):
    """Stop the music and disconnect."""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("⏹ Music stopped and disconnected.")
    else:
        await ctx.send("❌ Not connected to a voice channel.")

bot.run(TOKEN)
