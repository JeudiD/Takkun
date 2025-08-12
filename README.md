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
4. Install dependencies:

```bash
pip install -r requirements.txt


python bot.py to run the bot

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

---

## License

MIT License

Copyright (c) 2025 Pure

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

