import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time
import datetime

prefix = '!'

Bot = commands.Bot(command_prefix = prefix)

'''
@Bot.command()
async def join(ctx):
	voice = ctx.author.voice
	if voice == None:
		await ctx.send('You need to be in a voice chat to use that')
	else:
		await voice.channel.connect(timeout = 5)

@Bot.command()
async def leave(ctx):
	voice = ctx.author.voice
	if voice == None:
		await ctx.send('You need to be in a voice chat to use that')
	else:
		guild = ctx.guild
		voice_client = guild.voice_client
		await voice_client.disconnect()
'''

@Bot.command()
async def emoji(ctx, emoji:discord.Emoji):
	e_e = discord.Embed(title = emoji.name, color = discord.Color.green())
	e_e.set_image(url = emoji.url)
	e_e.set_footer(text = 'ID: ' + str(emoji.id))
	await ctx.send(embed = e_e)

@Bot.command()
async def clean(ctx, channel = None, msgs = None):
	if channel == None:
		await ctx.send('These command need argument')
	else:
		stop = False
		guild = ctx.guild
		channel_list = guild.text_channels
		for i in range(0, len(channel_list)):
			if channel == channel_list[i].name or channel == channel_list[i].id or channel == channel_list[i].mention:
				if msgs == None:
					stop = True
					await ctx.send('You don\'t wrote how many messages I need to delete.')
				else:
					stop = True
					channel = channel_list[i]
					deleted = await channel.purge(limit = int(msgs))
					await channel.send(f' Ddeleted {deleted} message(s)')
		else:
			if stop == False:
				deleted = await ctx.channel.purge(limit = int(channel))
				await ctx.send(f' Ddeleted {deleted} message(s)')
				
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Хочется пошпехатся, а не с кем. О разработчик, пошли потрахаемся.'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
