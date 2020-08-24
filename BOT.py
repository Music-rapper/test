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
async def server(ctx):
	server = ctx.guild
	online_members = 0
	inactive_members = 0
	busy_members = 0
	bot_members = 0
	bans = await server.bans()
	s_e = discord.Embed(title = server.name, description = server.description, color = discord.Color.green())
	s_e.add_field(name = "Server ID", value = server.id)
	s_e.add_field(name = "Server Owner", value = server.owner.mention)
	for i in range(0, len(server.members)):
		if server.members[i].status == discord.Status.online:
			if server.members[i].bot == False:
				online_members += 1
		elif server.members[i].status == discord.Status.idle:
			if server.members[i].bot == False:
				inactive_members += 1
		elif server.members[i].status == discord.Status.dnd:
			if server.members[i].bot == False:
				busy_members += 1
	for i in range(0, len(server.members)):
		if server.members[i].bot == True:
			bot_members += 1
	members = (f'<:online:747352635643920385> {online_members} Online<:transparent:747360968773730325><:idle:747490969984958544> {inactive_members} Inactive'
		   +f'<:transparent:747360968773730325><:dnd:747492056087134289> {busy_members} Busy<:transparent:747360968773730325>'
		   +f'/n<:offline:747355444250542141> {len(server.members) - bot_members} Members')
	s_e.add_field(name = "Members", value = members, inline = False)
	channels = f'<:textchannel:747403102650368032> {len(server.text_channels)} Text<:transparent:747360968773730325><:voicechannel:747410314630266960> {len(server.voice_channels)} Voice'
	s_e.add_field(name = "Channels", value = channels, inline = False)
	s_e.add_field(name = "Roles", value = len(server.roles))
	s_e.add_field(name = "Emojis", value = f':grinning: {len(server.emojis)}')
	
	if str(server.created_at)[8:10] == '01':
		server_day = str(server.created_at)[9:10] + 'st'
	elif str(server.created_at)[8:10] == '02':
		server_day = str(server.created_at)[9:10] + 'nd'
	elif str(server.created_at)[8:10] == '03':
		server_day = str(server.created_at)[9:10] + 'rd'
	elif (str(server.created_at)[8:10] == '04' or str(server.created_at)[8:10] == '05' or str(server.created_at)[8:10] == '06'
	      or str(server.created_at)[8:10] == '07' or str(server.created_at)[8:10] == '08' or str(server.created_at)[8:10] == '09'):
		server_day = str(server.created_at)[9:10] + 'th'
	elif str(server.created_at)[8:10] == '21' or str(server.created_at)[8:10] == '31':
		server_day = str(server.created_at)[8:10] + 'st'
	elif str(server.created_at)[8:10] == '22':
		server_day = str(server.created_at)[8:10] + 'nd'
	elif str(server.created_at)[8:10] == '23':
		server_day = str(server.created_at)[8:10] + 'rd'
	else:
		server_day = str(server.created_at)[8:10] + 'th'
		
	if str(server.created_at)[5:7] == '01':
		server_month = ' February '
	elif str(server.created_at)[5:7] == '02':
		server_month = ' January '
	elif str(server.created_at)[5:7] == '03':
		server_month = ' March '
	elif str(server.created_at)[5:7] == '04':
		server_month = ' April '
	elif str(server.created_at)[5:7] == '05':
		server_month = ' May '
	elif str(server.created_at)[5:7] == '06':
		server_month = ' June '
	elif str(server.created_at)[5:7] == '07':
		server_month = ' July '
	elif str(server.created_at)[5:7] == '08':
		server_month = ' August '
	elif str(server.created_at)[5:7] == '09':
		server_month = ' September '
	elif str(server.created_at)[5:7] == '10':
		server_month = ' October '
	elif str(server.created_at)[5:7] == '11':
		server_month = ' November '
	elif str(server.created_at)[5:7] == '12':
		server_month = ' December '
		
	server_date = server_day + server_month + str(server.created_at)[2:4]
	
	now_time_year = str(datetime.date.today())[0:4]
	now_time_year = int(now_time_year)
	server_time_year = str(server.created_at)[0:4]
	server_time_year = int(server_time_year)
	
	now_time_month = str(datetime.date.today())[5:7]
	now_time_month = int(now_time_month)
	server_time_month = str(server.created_at)[5:7]
	server_time_month = int(server_time_month)
	
	if (now_time_month == 1 or now_time_month == 3 or now_time_month == 5 or now_time_month == 7
	    or now_time_month == 8 or now_time_month == 10 or now_time_month == 12):
		day_bonus = 31
	elif now_time_month == 2:
		day_bonus = 28
	else:
		day_bonus = 30
	
	now_time_day = str(datetime.date.today())[8:10]
	now_time_day = int(now_time_day)
	server_time_day = str(server.created_at)[8:10]
	server_time_day = int(server_time_day)
	week = 0
	
	if now_time_day < server_time_day:
		now_time_month -= 1
		now_time_day += day_bonus
		day = now_time_day - server_time_day
	else:
		day = now_time_day - server_time_day
	
	if now_time_month < server_time_month:
		now_time_year -= 1
		now_time_month += 12
		month = now_time_month - server_time_month
	else:
		month = now_time_month - server_time_month
	
	while day // 7:
		week += 1
		day -= 7
	
	year = now_time_year - server_time_year
	
	if year == 0:
		if month == 0:
			if week == 0:
				if day == 0:
					server_msg = 'Today'
				elif day == 1:
					server_msg = '1 day ago'
				else:
					server_msg = f'{str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 week ago'
				elif day == 1:
					server_msg = '1 week and 1 day ago'
				else:
					server_msg = f'1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(week)} weeks ago'
				elif day == 1:
					server_msg = f'{str(week)} weeks and 1 day ago'
				else:
					server_msg = f'{str(week)} weeks and ' + str(day) + ' days ago'
		elif month == 1:
			if week == 0:
				if day == 0:
					server_msg = '1 month ago'
				elif day == 1:
					server_msg = '1 month and 1 day ago'
				else:
					server_msg = f'1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 month and 1 week ago'
				elif day == 1:
					server_msg = '1 month, 1 week and 1 day ago'
				else:
					server_msg = f'1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'1 month {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'1 month, {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					server_msg = f'{str(month)} month ago'
				elif day == 1:
					server_msg = f'{str(month)} month and 1 day ago'
				else:
					server_msg = f'{str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{month} month and 1 week ago'
				elif day == 1:
					server_msg = f'{month} month, 1 week and 1 day ago'
				else:
					server_msg = f'{month} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'{month} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'{month} month and ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'{month} month and ' + str(week) + f' weeks and {str(day)} days ago'
					
	elif year == 1:
		if month == 0:
			if week == 0:
				if day == 0:
					server_msg = '1 year ago'
				elif day == 1:
					server_msg = '1 year and 1 day ago'
				else:
					server_msg = f'1 year and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 year and 1 week ago'
				elif day == 1:
					server_msg = '1 year, 1 week and 1 day ago'
				else:
					server_msg = f'1 year, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'1 year and {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'1 year, {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'1 year, {str(week)} weeks and ' + str(day) + ' days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					server_msg = '1 year and 1 month ago'
				elif day == 1:
					server_msg = '1 year, 1 month and 1 day ago'
				else:
					server_msg = f'1 year, 1 month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = '1 year, 1 month and 1 week ago'
				elif day == 1:
					server_msg = '1 year, 1 month, 1 week and 1 day ago'
				else:
					server_msg = f'1 year, 1 month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'1 year, 1 month and {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'1 year, 1 month, {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'1 year, 1 month, {str(week)} weeks and ' + str(day) + ' days ago'
					
		else:
			if week == 0:
				if day == 0:
					server_msg = f'1 year and {str(month)} month ago'
				elif day == 1:
					server_msg = f'1 year, {str(month)} month and 1 day ago'
				else:
					server_msg = f'1 year, {str(month)} month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'1 year, {str(month)} month and 1 week ago'
				elif day == 1:
					server_msg = f'1 year, {str(month)} month, 1 week and 1 day ago'
				else:
					server_msg = f'1 year, {str(month)} month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'1 year, {str(month)} month and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'1 year, {str(month)} month, ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'1 year, {str(month)} month, ' + str(week) + f' weeks and {str(day)} days ago'
	else:
		if month == 0:
			if week == 0:
				if day == 0:
					server_msg = f'{str(year)} years ago'
				elif day == 1:
					server_msg = f'{str(year)} years and 1 day ago'
				else:
					server_msg = f'{str(year)} years and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{str(year)} years and 1 week ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 week and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(year)} years and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(week) + f' weeks and {str(day)} days ago'
					
		elif month == 1:
			if week == 0:
				if day == 0:
					server_msg = f'{str(year)} years and 1 month ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 month and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 month and ' + str(day) + ' days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{str(year)} years, 1 month and 1 week ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 month, 1 week and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 month, 1 week and ' + str(day) + ' days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(year)} years, 1 month and ' + str(week) + ' weeks ago'
				elif day == 1:
					server_msg = f'{str(year)} years, 1 month, ' + str(week) + ' weeks and 1 day ago'
				else:
					server_msg = f'{str(year)} years, 1 month, ' + str(week) + f' weeks and {str(day)} days ago'
					
		else:
			if week == 0:
				if day == 0:
					server_msg = f'{str(year)} years and ' + str(month) + ' month ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' +  str(month) + ' month and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(day)} days ago'
					
			elif week == 1:
				if day == 0:
					server_msg = f'{str(year)} years, ' + str(month) + ' month and 1 week ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' + str(month) + ' month, 1 week and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(month) + f' month, 1 week and {str(day)} days ago'
					
			else:
				if day == 0:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks ago'
				elif day == 1:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and 1 day ago'
				else:
					server_msg = f'{str(year)} years, ' + str(month) + f' month and {str(week)} weeks and ' + str(day) + ' days ago'
	
	server_info = server_date + f' ({server_msg})'
	
	s_e.add_field(name = "Created at", value = server_info, inline = False)
	
	if server.region == discord.VoiceRegion('amsterdam'):
		s_e.add_field(name = "Voice Region", value = ":flag_nl: Nethelands")
	elif server.region == discord.VoiceRegion('brazil'):
		s_e.add_field(name = "Voice Region", value = ":flag_br: Brazil")
	elif server.region == discord.VoiceRegion('dubai'):
		s_e.add_field(name = "Voice Region", value = ":flag_ae: United Arab Emirates")
	elif server.region == discord.VoiceRegion('europe'):
		s_e.add_field(name = "Voice Region", value = ":flag_eu: Europe")
	elif server.region == discord.VoiceRegion('frankfurt'):
		s_e.add_field(name = "Voice Region", value = ":flag_de: Germany")
	elif server.region == discord.VoiceRegion('hongkong'):
		s_e.add_field(name = "Voice Region", value = ":flag_hk: Hong Kong")
	elif server.region == discord.VoiceRegion('india'):
		s_e.add_field(name = "Voice Region", value = ":flag_in: India")
	elif server.region == discord.VoiceRegion('japan'):
		s_e.add_field(name = "Voice Region", value = ":flag_jp: Japan")
	elif server.region == discord.VoiceRegion('london'):
		s_e.add_field(name = "Voice Region", value = ":flag_gb: United Kingdom")
	elif server.region == discord.VoiceRegion('russia'):
		s_e.add_field(name = "Voice Region", value = ":flag_ru: Russia")
	elif server.region == discord.VoiceRegion('singapore'):
		s_e.add_field(name = "Voice Region", value = ":flag_sg: Singapore")
	elif server.region == discord.VoiceRegion('southafrica'):
		s_e.add_field(name = "Voice Region", value = ":flag_za: South Africa")
	elif server.region == discord.VoiceRegion('south_korea'):
		s_e.add_field(name = "Voice Region", value = ":flag_kr: South Korea")
	elif server.region == discord.VoiceRegion('sydney'):
		s_e.add_field(name = "Voice Region", value = ":flag_au: Australia")
	elif (server.region == discord.VoiceRegion('us_central') or server.region == discord.VoiceRegion('us_east')
	      or server.region == discord.VoiceRegion('vip_us_east') or server.region == discord.VoiceRegion('us_south')
	      or server.region == discord.VoiceRegion('us_west') or server.region == discord.VoiceRegion('vip_us_west')):
		s_e.add_field(name = "Voice Region", value = ":flag_us: USA")
	s_e.add_field(name = "Bans", value = f'<:banhammer:747471683140452391> {len(bans)}')
	s_e.set_thumbnail(url = server.icon_url)
	s_e.set_footer(text = f"Caused by: {str(ctx.author)}", icon_url = ctx.author.avatar_url)
	await ctx.send(embed = s_e)
	
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Хочется пошпехатся, а не с кем. О разработчик, пошли потрахаемся.'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
