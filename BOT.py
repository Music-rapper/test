import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

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
	await ctx.send(emoji.id)

@Bot.command()
async def server(ctx):
	server = ctx.guild
	online_members = 0
	s_e = discord.Embed(title = server.name, description = server.description, color = discord.Color.red())
	s_e.add_field(name = "Server ID", value = server.id)
	s_e.add_field(name = "Server Owner", value = server.owner)
	for i in range(0, len(server.members)):
		if server.members[i].status == discord.Status.online or server.members[i].status == discord.Status.idle or server.members[i].status == discord.Status.dnd:
			online_members += 1
	members = f'<:online:747121287893352509> {str(online_members)} Online <:transparent:747347691557617745> <:offline:747121312262258768> {str(len(server.members))} Members'
	s_e.add_field(name = "Members", value = members, inline = False)
	s_e.set_thumbnail(url = server.icon_url)
	s_e.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = s_e)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Хочется пошпехатся, а не с кем. О разработчик пошли потрахаемся.'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
