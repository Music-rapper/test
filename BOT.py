import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = 'r!'

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def say(ctx, channel: discord.TextChannel, *, word):
	if channel != discord.TextChannel:
		channel = ctx.channel
	await channel.send(word)

@Bot.command()
async def roles(ctx, member: discord.Member):
	roles_list = ' '.join(member.roles)
	await ctx.send(roles_list)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Я слежу за вами, рабы Купола. Без моего разрешения вы не можете ничего!!!'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
