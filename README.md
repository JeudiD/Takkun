# Takkun — Lofi Radio Discord Bot

A minimal Discord bot that streams chill lofi beats 24/7 in a voice channel. Perfect for background vibes and study sessions.

## Features

- Auto joins a designated voice channel (like AFK)  
- Streams continuous lofi music via a URL or local playlist  
- Minimal commands: join, leave, and status  
- Lightweight and reliable — designed to run nonstop  

## Setup

1. Clone or download this repo  
2. Create a `.env` file in the project folder with your bot token:
TOKEN=your_bot_token_here

3. Make sure you have Python 3.10+ installed  


## Commands

- `tjoin` — Bot joins your current voice channel  
- `tplay` — Play lofi radio 
- `tleave` — Bot leaves the voice channel  

## Requirements

- Python 3.10 or higher  
- discord.py  
- python-dotenv  
- FFmpeg installed and added to your system PATH (for streaming audio)  
- Python's built-in `logging` module (no extra install needed)

## Notes

- The bot requires **Connect** and **Speak** permissions in the voice channel  
- Make sure to enable **Message Content Intent** in the Discord Developer Portal for your bot  
- The bot uses Python’s built-in `logging` module for runtime information and debugging  
- Ensure FFmpeg is installed and properly added to your system PATH to handle audio streaming  


## Attribution

If you use or modify this bot, a simple shout-out or mention would be appreciated but is not required. Thanks for supporting my work!


