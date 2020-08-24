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
	e_e = discord.Embed(title = emoji.name, color = discord.Color.green())
	e_e.set_image(url = emoji.url)
	e_e.set_footer(text = 'ID: ' + str(emoji.id))
	await ctx.send(embed = e_e)

@Bot.command()
async def server(ctx):
	server = ctx.guild
	online_members = 0
	bot_members = 0
	bans = await server.bans()
	s_e = discord.Embed(title = server.name, description = server.description, color = discord.Color.green())
	s_e.add_field(name = "Server ID", value = server.id)
	s_e.add_field(name = "Server Owner", value = server.owner.mention)
	for i in range(0, len(server.members)):
		if server.members[i].status == discord.Status.online or server.members[i].status == discord.Status.idle or server.members[i].status == discord.Status.dnd:
			if server.members[i].bot == False:
				online_members += 1
	for i in range(0, len(server.members)):
		if server.members[i].bot == True:
			bot_members += 1
	members = f'<:online:747352635643920385> {online_members} Online<:transparent:747360968773730325><:offline:747355444250542141> {len(server.members) - bot_members} Members'
	s_e.add_field(name = "Members", value = members, inline = False)
	channels = f'<:textchannel:747403102650368032> {len(server.text_channels)} Text<:transparent:747360968773730325><:voicechannel:747410314630266960> {len(server.voice_channels)} Voice'
	s_e.add_field(name = "Channels", value = channels, inline = False)
	s_e.add_field(name = "Roles", value = len(server.roles))
	s_e.add_field(name = "Emojis", value = len(server.emojis))
	if server.region == discord.VoiceRegion('amsterdam'):
		s_e.add_field(name = "Voice Region", value = ":flag_nl: Nethelands", inline = False)
	elif server.region == discord.VoiceRegion('brazil'):
		s_e.add_field(name = "Voice Region", value = ":flag_br: Brazil", inline = False)
	elif server.region == discord.VoiceRegion('dubai'):
		s_e.add_field(name = "Voice Region", value = ":flag_ae: United Arab Emirates", inline = False)
	elif server.region == discord.VoiceRegion('europe'):
		s_e.add_field(name = "Voice Region", value = ":flag_eu: Europe", inline = False)
	elif server.region == discord.VoiceRegion('frankfurt'):
		s_e.add_field(name = "Voice Region", value = ":flag_de: Germany", inline = False)
	elif server.region == discord.VoiceRegion('hongkong'):
		s_e.add_field(name = "Voice Region", value = ":flag_hk: Hong Kong", inline = False)
	elif server.region == discord.VoiceRegion('india'):
		s_e.add_field(name = "Voice Region", value = ":flag_in: India", inline = False)
	elif server.region == discord.VoiceRegion('japan'):
		s_e.add_field(name = "Voice Region", value = ":flag_jp: Japan", inline = False)
	elif server.region == discord.VoiceRegion('london'):
		s_e.add_field(name = "Voice Region", value = ":flag_gb: United Kingdom", inline = False)
	elif server.region == discord.VoiceRegion('russia'):
		s_e.add_field(name = "Voice Region", value = ":flag_ru: Russia", inline = False)
	elif server.region == discord.VoiceRegion('singapore'):
		s_e.add_field(name = "Voice Region", value = ":flag_sg: Singapore", inline = False)
	elif server.region == discord.VoiceRegion('southafrica'):
		s_e.add_field(name = "Voice Region", value = ":flag_za: South Africa", inline = False)
	elif server.region == discord.VoiceRegion('south_korea'):
		s_e.add_field(name = "Voice Region", value = ":flag_kr: South Korea", inline = False)
	elif server.region == discord.VoiceRegion('sydney'):
		s_e.add_field(name = "Voice Region", value = ":flag_au: Australia", inline = False)
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
