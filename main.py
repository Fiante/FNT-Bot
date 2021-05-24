import platform

import clear as clear
import discord
from discord.ext import commands, tasks
from utils import *
from functions import *
import os

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix="!f ", intents=intents)
game = Game()



@Bot.event
async def on_ready():
    await Bot.change_presence(activity=discord.Game(name='!f by Fiante'))
    print("Ben Hazırım. Öyleyse Başlayalım.")





@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="yeni-gelenler")
    await channel.send(f"{member} Aramıza Hoşgeldin Dostum!")
    print(f"{member} Aramıza Hoşgeldin Dostum!")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="gidenler")
    await channel.send(f"{member} Aramızdan Ayrıldı!")
    print(f"{member} Aramızdan Ayrıldı!")


@Bot.event
async def on_command_error(ctx, error):
    await ctx.send(error)


@Bot.command(aliases=["zar"])
async def fnt(ctx, *args):
    if "roll" in args:
        await ctx.send(game.roll_dice())
    else:
        await ctx.send('Ben Hazırım. Öyleyse Başlayalım!')


@Bot.command()
@commands.has_role("Admin")
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@Bot.command()
@commands.has_role("Admin")
async def kick(ctx, member: discord.Member, *args, reason="Yok"):
    await member.kick(reason=reason)


@Bot.command()
@commands.has_role("Admin")
async def ban(ctx, member: discord.Member, *args, reason="Yok"):
    await member.ban(reason=reason)


@Bot.command()
@commands.has_role("Admin")
async def load(ctx, extension):
    Bot.load_extension(f'cogs.{extension}')


@Bot.command()
@commands.has_role("Admin")
async def unload(ctx, extension):
    Bot.unload_extension(f'cogs.{extension}')


@Bot.command()
@commands.has_role("Admin")
async def reload(ctx, extension):
    Bot.unload_extension(f'cogs.{extension}')
    Bot.load_extension(f'cogs.{extension}')


for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        Bot.load_extension(f'cogs.{filename[:-3]}')

Bot.run(TOKEN)
