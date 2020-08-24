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
	e_e = discord.Embed(description = emoji.name, color = discord.Color.green())
	e_e.set_thumbnail(url = emoji.url)
	e_e.set_footer(text = 'ID: ' + str(emoji.id))
	await ctx.send(embed = e_e)

@Bot.command()
async def server(ctx):
	server = ctx.guild
	online_members = 0
	s_e = discord.Embed(title = server.name, description = server.description, color = discord.Color.dark_red())
	s_e.add_field(name = "Server ID", value = server.id)
	s_e.add_field(name = "Server Owner", value = server.owner)
	for i in range(0, len(server.members)):
		if server.members[i].status == discord.Status.online or server.members[i].status == discord.Status.idle or server.members[i].status == discord.Status.dnd:
			online_members += 1
	members = f'<:online:747352635643920385> {str(online_members)} Online <:transparent:747348899139944488> <:offline:747355444250542141> {str(len(server.members))} Members'
	s_e.add_field(name = "Members", value = members, inline = False)
	s_e.set_thumbnail(url = server.icon_url)
	s_e.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = s_e)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Хочется пошпехатся, а не с кем. О разработчик, пошли потрахаемся.'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
