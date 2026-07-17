import discord
from discord.ext import commands
import webbrowser




youtube = "https://youtube.com/"
prefix = "!"
bot = commands.Bot(command_prefix=prefix)
bot.run(token=lol)


@bot.command()
async def play(ctx, arg):
    if youtube in arg:
        await webbrowser.open(arg)
    else:
        await ctx.send("this is not a youtube link!")