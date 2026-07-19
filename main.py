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
youtube2 = "https://www.youtu.be/"

prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
@commands.cooldown(1, 150, commands.BucketType.user)
async def play(ctx, arg):
    if youtube or youtube2 in arg.lower():
        print(arg)
        await ctx.send("opening link for 5 minutes!, you are now on cooldown!")
        webbrowser.open(arg)
        await asyncio.sleep(10) # so it actually plays the video LOL
        pyautogui.click(1049, 613) #Exactr!
        await asyncio.sleep(300) 
        os.system("taskkill /f /im firefox.exe") #make sure it closes after to prevent overloading the Evil Boy
    else:
        await ctx.send("this is not a youtube link!")
        print(arg)

@play.error
async def play_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("you're on cooldown!" )

bot.run(token=TOKEN)