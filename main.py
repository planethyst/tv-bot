import discord
from os import getenv
from discord.ext import commands
import webbrowser
from dotenv import load_dotenv

load_dotenv()
TOKEN = getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True


youtube = "https://www.youtube.com/watch?v="

prefix = "!"
bot = commands.Bot(command_prefix=prefix, intents=intents)


@bot.command()
async def play(ctx, arg):
    if youtube in arg.lower():
        print(arg)
        webbrowser.open(arg)
    else:
        await ctx.send("this is not a youtube link!")
        print(arg)

bot.run(token=TOKEN)