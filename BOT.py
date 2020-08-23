import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = 'r!'

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def channels(ctx):
	channel_list = discord.Guild.text_channels
	await ctx.send(channel_list)

@Bot.command()
async def server(ctx):
	await ctx.send(discord.Guild.name)
	
'''
@Bot.command()
async def say(ctx, channel, *, word = None):
	if channel in channel_id_list or channel == :
		await channel.send(word)
	else:
		if word != None:
			await ctx.send(str(channel) + f' {word}')
		else:
			await ctx.send(channel)
'''
	
@Bot.command()
async def user(ctx, member: discord.Member):
	emb = discord.Embed(title = str(member), description = member.mention, color = member.top_role.color)
	emb.add_field(name = "ID", value = member.id, inline = False)
	emb.add_field(name = "Joined server at", value = str(member.joined_at)[:19], inline = False)
	emb.add_field(name = "Created account at", value = str(member.created_at)[:19], inline = False)
	if member.top_role == member.roles[0]:
		emb.add_field(name = "Highest role", value = member.top_role, inline = False)
	else:
		emb.add_field(name = "Highest role", value = member.top_role.mention, inline = False)
	emb.set_thumbnail(url = member.avatar_url)
	emb.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Я слежу за вами, рабы Купола. Без моего разрешения вы не можете ничего!!!'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
