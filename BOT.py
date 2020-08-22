import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = 'r!'

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def say(ctx, channel: discord.TextChannel, *, word):
	await channel.send(word)

@Bot.command()
async def roles(ctx, member: discord.Member):
	roles_mention = []
	for i in range(0, len(member.roles)):
		roles_mention.append(member.roles[i].mention)
	await ctx.send(roles_mention)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Я слежу за вами, рабы Купола. Без моего разрешения вы не можете ничего!!!'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
