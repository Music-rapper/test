import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time
import datetime

prefix = '!'

Bot = commands.Bot(command_prefix = prefix)

Bot.remove_command('help')

@Bot.command()
async def help(ctx, command = None):
	me = ctx.guild.me
	h_e = discord.Embed(title = f'{me.name} Bot Commands', color = discord.Color.from_rgb(255, 0, 0))
	h_e.add_field(name = f'{prefix}avatar', value = 'Give you someone\'s avatar that you can easily download.', inline = False)
	h_e.add_field(name = f'{prefix}emoji', value = 'Give information about custom emoji.', inline = False)
	h_e.set_thumbnail(url = me.avatar_url)
	h_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = h_e)

@Bot.command()
async def emoji(ctx, emoji:discord.Emoji):
	e_e = discord.Embed(title = f'`<:{emoji.name}:{emoji.id}>`', color = discord.Color.from_rgb(255, 0, 0))
	e_e.set_image(url = emoji.url)
	e_e.add_field(name = 'Name', value = emoji.name)
	e_e.add_field(name = 'ID', value = emoji.id)
	e_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = e_e)

@Bot.command()
async def channel(ctx, channel = None):
	
	guild = ctx.guild
	channel_list = guild.text_channels
	channel_stop = False
	
	for i in range(0, len(channel_list)):
		if channel == channel_list[i].name or channel == str(channel_list[i].id) or channel == channel_list[i]:
			channel_stop = True
			channel = channel_list[i]
	else:
		if channel_stop == False:
			if channel == None:	
				channel = ctx.channel
			else:
				await ctx.send('You wrote channel index incorectly.')
	
	await ctx.send(channel)
	await ctx.send(channel_list)
	c_e = discord.Embed(title = 'Channel information', color = discord.Color.from_rgb(255, 0, 0))
	c_e.add_field(name = 'Name', value = channel.name)
	c_e.add_field(name = 'ID', value = channel.id)
	c_e.add_field(name = 'Mention', value = f'`{channel.mention}`')
	if channel.category != None:
		c_e.add_field(name = 'Category', value = channel.category)
	c_e.add_field(name = 'NSFW', value = channel.is_nsfw())
	if channel.topic != None:
		c_e.add_field(name = 'Topic', value = channel.topic, inline = False)
	c_e.add_field(name = 'Roles', value = '1')
	c_e.add_field(name = 'Created at', value = channel.created_at, inline = False)
	c_e.set_footer(text = f'Caused by: {ctx.author}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = c_e)
	
@Bot.command()
async def avatar(ctx, member = None):
	if member == None:
		member = ctx.author
	else:
		guild = ctx.guild
		member_list = guild.members
		member_stop = False
		mention1 = ''
		mention2 = ''
		mention_list = []

		author_mention = str(member)
		if author_mention[1] == '@' and author_mention[2] != '!':
			author_mention = member[0:2] + '!' + member[2 : len(member)]
			member = author_mention

		for i in range(0, len(member_list)):
			mention1 = member_list[i].mention
			if mention1[1] == '@' and mention1[2] == '!':
				mention_list.append(mention1)
			else:
				mention2 = mention1[0 : 2] + '!' + mention1[2 : len(mention1)]
				mention_list.append(mention2)	

		for i in range(0, len(member_list)):
			if member == member_list[i].name or member == str(member_list[i].id) or member == mention_list[i]:
				member_stop = True
				member = member_list[i]
		else:
			if member_stop == False:
				if member != None:
					await ctx.send('You wrote member index incorectly.')
	a_e = discord.Embed(title = f'{member} avatar', color = discord.Color.green())
	a_e.set_image(url = member.avatar_url)
	a_e.set_footer(text = f'Caused by: {ctx.author}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = a_e)
				
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('1234567890'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
