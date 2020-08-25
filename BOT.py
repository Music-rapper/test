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
	
def calculator(num):
	
	num = str(num)
	
	if num[8:10] == '01':
		day = num[8:10] + 'st'
	elif num[8:10] == '02':
		day = num[8:10] + 'nd'
	elif num[8:10] == '03':
		day = num[8:10] + 'rd'
	elif num[8:10] == '04' or num[8:10] == '05' or num[8:10] == '06' or num[8:10] == '07' or num[8:10] == '08' or num[8:10] == '09':
		day = num[8:10] + 'th'
	elif num[8:10] == '21' or num[8:10] == '31':
		day = num[8:10] + 'st'
	elif num[8:10] == '22':
		day = num[8:10] + 'nd'
	elif num[8:10] == '23':
		day = num[8:10] + 'rd'
	else:
		day = num[8:10] + 'th'
		
	if num[5:7] == '01':
		month = ' February '
	elif num[5:7] == '02':
		month = ' January '
	elif num[5:7] == '03':
		month = ' March '
	elif num[5:7] == '04':
		month = ' April '
	elif num[5:7] == '05':
		month = ' May '
	elif num[5:7] == '06':
		month = ' June '
	elif num[5:7] == '07':
		month = ' July '
	elif num[5:7] == '08':
		month = ' August '
	elif num[5:7] == '09':
		month = ' September '
	elif num[5:7] == '10':
		month = ' October '
	elif num[5:7] == '11':
		month = ' November '
	elif num[5:7] == '12':
		month = ' December '
		
	date = day + month + f'{num[2:4]} '
	
	now_year = int(str(datetime.date.today())[0:4])
	year = int(num[0:4])

	
	now_month = int(str(datetime.date.today())[5:7])
	month = int(num[5:7])
	
	if now_month == 1 or now_month == 3 or now_month == 5 or now_month == 7 or now_month == 8 or now_month == 10 or now_month == 12:
		day_bonus = 31
	elif now_month == 2:
		day_bonus = 28
	else:
		day_bonus = 30
	
	now_day = int(str(datetime.date.today())[8:10])
	day = int(num[8:10])
	week = 0
	
	if now_day < day:
		now_month -= 1
		now_day += day_bonus
		day = now_day - day
	else:
		day = now_day - day
	
	if now_month < month:
		now_year -= 1
		now_month += 12
		month = now_month - month
	else:
		month = now_month - month
	
	while day // 7:
		week += 1
		day -= 7
	
	year = now_year - year
	
	if year == 0:
		if month == 0:
			if week == 0:
				if day == 0:
					msg = 'Today'
				elif day == 1:
					msg = '1 day ago'
				else:
					msg = f'{day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 week ago'
				elif day == 1:
					msg = '1 week and 1 day ago'
				else:
					msg = f'1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{week} weeks ago'
				elif day == 1:
					msg = f'{week} weeks and 1 day ago'
				else:
					msg = f'{week} weeks and {day} days ago'
		elif month == 1:
			if week == 0:
				if day == 0:
					msg = '1 month ago'
				elif day == 1:
					msg = '1 month and 1 day ago'
				else:
					msg = f'1 month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 month and 1 week ago'
				elif day == 1:
					msg = '1 month, 1 week and 1 day ago'
				else:
					msg = f'1 month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 month {week} weeks ago'
				elif day == 1:
					msg = f'1 month, {week} weeks and 1 day ago'
				else:
					msg = f'1 month, {week} weeks and {day} days ago'
					
		else:
			if week == 0:
				if day == 0:
					msg = f'{month} month ago'
				elif day == 1:
					msg = f'{month} month and 1 day ago'
				else:
					msg = f'{month} month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{month} month and 1 week ago'
				elif day == 1:
					msg = f'{month} month, 1 week and 1 day ago'
				else:
					msg = f'{month} month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{month} month and {week} weeks ago'
				elif day == 1:
					msg = f'{month} month and {week} weeks and 1 day ago'
				else:
					msg = f'{month} month and {week} weeks and {day} days ago'
					
	elif year == 1:
		if month == 0:
			if week == 0:
				if day == 0:
					msg = '1 year ago'
				elif day == 1:
					msg = '1 year and 1 day ago'
				else:
					msg = f'1 year and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 year and 1 week ago'
				elif day == 1:
					msg = '1 year, 1 week and 1 day ago'
				else:
					msg = f'1 year, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 year and {week} weeks ago'
				elif day == 1:
					msg = f'1 year, {week} weeks and 1 day ago'
				else:
					msg = f'1 year, {week} weeks and {day} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					msg = '1 year and 1 month ago'
				elif day == 1:
					msg = '1 year, 1 month and 1 day ago'
				else:
					msg = f'1 year, 1 month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = '1 year, 1 month and 1 week ago'
				elif day == 1:
					msg = '1 year, 1 month, 1 week and 1 day ago'
				else:
					msg = f'1 year, 1 month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 year, 1 month and {week} weeks ago'
				elif day == 1:
					msg = f'1 year, 1 month, {week} weeks and 1 day ago'
				else:
					msg = f'1 year, 1 month, {week} weeks and {day} days ago'
					
		else:
			if week == 0:
				if day == 0:
					msg = f'1 year and {month} month ago'
				elif day == 1:
					msg = f'1 year, {month} month and 1 day ago'
				else:
					msg = f'1 year, {month} month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'1 year, {month} month and 1 week ago'
				elif day == 1:
					msg = f'1 year, {month} month, 1 week and 1 day ago'
				else:
					msg = f'1 year, {month} month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'1 year, {month} month and {week} weeks ago'
				elif day == 1:
					msg = f'1 year, {month} month, {week} weeks and 1 day ago'
				else:
					msg = f'1 year, {month} month, {week} weeks and {day} days ago'
	else:
		if month == 0:
			if week == 0:
				if day == 0:
					msg = f'{year} years ago'
				elif day == 1:
					msg = f'{year} years and 1 day ago'
				else:
					msg = f'{year} years and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{year} years and 1 week ago'
				elif day == 1:
					msg = f'{year} years, 1 week and 1 day ago'
				else:
					msg = f'{year} years, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{year} years and {week} weeks ago'
				elif day == 1:
					msg = f'{year} years, {week} weeks and 1 day ago'
				else:
					msg = f'{year} years, {week} weeks and {day} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					msg = f'{year} years and 1 month ago'
				elif day == 1:
					msg = f'{year} years, 1 month and 1 day ago'
				else:
					msg = f'{year} years, 1 month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{year} years, 1 month and 1 week ago'
				elif day == 1:
					msg = f'{year} years, 1 month, 1 week and 1 day ago'
				else:
					msg = f'{year} years, 1 month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{year} years, 1 month and {week} weeks ago'
				elif day == 1:
					msg = f'{year} years, 1 month, {week} weeks and 1 day ago'
				else:
					msg = f'{year} years, 1 month, {week} weeks and {day} days ago'
					
		else:
			if week == 0:
				if day == 0:
					msg = f'{year} years and {month} month ago'
				elif day == 1:
					msg = f'{year} years, {month} month and 1 day ago'
				else:
					msg = f'{year} years, {month} month and {day} days ago'
					
			elif week == 1:
				if day == 0:
					msg = f'{year} years, {month} month and 1 week ago'
				elif day == 1:
					msg = f'{year} years, {month} month, 1 week and 1 day ago'
				else:
					msg = f'{year} years, {month} month, 1 week and {day} days ago'
					
			else:
				if day == 0:
					msg = f'{year} years, {month} month and {week} weeks ago'
				elif day == 1:
					msg = f'{year} years, {month} month and {week} weeks and 1 day ago'
				else:
					msg = f'{year} years, {month} month and {week} weeks and {day} days ago'
	
	info = date + f'({msg})'
	
	return info

@Bot.command()
async def channel(ctx, channel = None):
	
	guild = ctx.guild
	role_list = guild.roles
	r_roles_quantity = 0
	r_roles_msg = ''
	w_roles_quantity = 0
	w_roles_msg = ''
	channel_list = guild.text_channels
	channel_stop = False
	
	for i in range(0, len(channel_list)):
		if channel == channel_list[i].name or channel == str(channel_list[i].id) or channel == channel_list[i].mention:
			channel_stop = True
			channel = channel_list[i]
	else:
		if channel_stop == False:
			if channel == None:	
				channel = ctx.channel
			else:
				await ctx.send('You wrote channel index incorectly.')
	
	for i in range(0, len(role_list)):
		if channel.overwrites_for(role_list[0]).read_messages == False:
			if role_list[i].permissions.read_messages == True:
				if (channel.overwrites_for(role_list[i]).read_messages == True or role_list[i].permissions.administrator == True
				    or channel.overwrites_for(role_list[i]).read_messages == None):
					r_roles_quantity += 1
					r_roles_msg += role_list[i].mention
					r_roles_msg += ', '
			else:
				if channel.overwrites_for(role_list[i]).read_messages == True or role_list[i].permissions.administrator == True:
					r_roles_quantity += 1
					r_roles_msg += role_list[i].mention
					r_roles_msg += ', '
		else:
			if role_list[i].permissions.read_messages == True:
				if channel.overwrites_for(role_list[i]).read_messages != False:
					r_roles_quantity += 1
					r_roles_msg += role_list[i].mention
					r_roles_msg += ', '
			else:
				if channel.overwrites_for(role_list[i]).read_messages == True:
					r_roles_quantity += 1
					r_roles_msg += role_list[i].mention
					r_roles_msg += ', '
	else:
		r_roles_msg = r_roles_msg[0: len(r_roles_msg) - 2]
		
	for i in range(0, len(role_list)):
		if channel.overwrites_for(role_list[0]).send_messages == False:
			if role_list[i].permissions.send_messages == True:
				if (channel.overwrites_for(role_list[i]).send_messages == True or role_list[i].permissions.administrator == True
				    or channel.overwrites_for(role_list[i]).send_messages == None):
					w_roles_quantity += 1
					w_roles_msg += role_list[i].mention
					w_roles_msg += ', '
			else:
				if channel.overwrites_for(role_list[i]).send_messages == True or role_list[i].permissions.administrator == True:
					w_roles_quantity += 1
					w_roles_msg += role_list[i].mention
					w_roles_msg += ', '
		else:
			if role_list[i].permissions.send_messages == True:
				if channel.overwrites_for(role_list[i]).send_messages != False:
					w_roles_quantity += 1
					w_roles_msg += role_list[i].mention
					w_roles_msg += ', '
			else:
				if channel.overwrites_for(role_list[i]).send_messages == True:
					w_roles_quantity += 1
					w_roles_msg += role_list[i].mention
					w_roles_msg += ', '
	else:
		w_roles_msg = w_roles_msg[0: len(w_roles_msg) - 2]
	
	c_e = discord.Embed(title = 'Channel information', color = discord.Color.from_rgb(255, 0, 0))
	c_e.add_field(name = 'Name', value = channel.name)
	c_e.add_field(name = 'ID', value = channel.id)
	c_e.add_field(name = 'Mention', value = f'`{channel.mention}`')
	if channel.category != None:
		c_e.add_field(name = 'Category', value = channel.category)
	c_e.add_field(name = 'NSFW', value = channel.is_nsfw())
	if channel.topic != None:
		c_e.add_field(name = 'Topic', value = channel.topic, inline = False)
	role = ctx.author.roles[0]
	c_e.add_field(name = f'Roles that can read this channel ({r_roles_quantity})', value = r_roles_msg, inline = False)
	c_e.add_field(name = f'Roles that can write in this channel ({w_roles_quantity})', value = w_roles_msg, inline = False)
	c_e.add_field(name = 'Created at', value = calculator(channel.created_at), inline = False)
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
