import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Arabian Shop is online: {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Arabian Shop Bot is working!")

@bot.command()
async def shop(ctx):
    embed = discord.Embed(
        title="Arabian Shop",
        description="مرحباً بك في متجر Arabian Shop!\n\nنظام بيع وشراء متعدد التجار.\n\nطرق الدفع بانتظار التفعيل.",
        color=0xD4AF37
    )
    await ctx.send(embed=embed)

if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN is missing!")

bot.run(TOKEN)
