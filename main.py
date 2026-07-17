import discord
import asyncio
import os
from discord.ext import commands
import webbrowser
from dotenv import load_dotenv
import pyautogui 

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True


youtube = "https://www.youtube.com/"

prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def play(ctx, arg):
    if youtube in arg.lower():
        print(arg)
        await ctx.send("opening link for 5 minutes!")
        webbrowser.open(arg)
        await asyncio.sleep(10) # so it actually plays the video LOL
        pyautogui.click(700, 500)
        await asyncio.sleep(300)
        os.system("taskkill /f /im firefox.exe") #make sure it closes after to prevent overloading the Evil Boy
    else:
        await ctx.send("this is not a youtube link!")
        print(arg)

bot.run(token=TOKEN)