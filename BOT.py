import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

bot_prefix = ['!']

Bot = commands.Bot(command_prefix = bot_prefix)

@Bot.command()
async def members(ctx):
	guild = discord.utils.get(Client.guilds, guild__name = ctx.guild.name)
	print(guild.members)

@Bot.command()
async def inrole(ctx, role = None):
	if role == None:
		ctx.send('You didn\'t write role')
	else:
		guild = ctx.guild
		role_list = guild.roles
		role_stop = 0
	
		for i in range(0, len(role_list)):
			if role == role_list[i].name or role == str(role_list[i].id) or role == role_list[i].mention:
				role_stop = True
				role = role_list[i]
		else:
			if role_stop == False:	
				await ctx.send('You didn\'t write role index.')
	ir_e = dicord.Embed(color = role.color)
	ir_m = ''
	for i in range(0, len(role.members)):
		ir_m += role.members[i].mention + '\n'
	ir_e.add_field(name = f'People with role {role.mention}: {len(role.members)}', value = ir_m)
				
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('1234567890'))
	
'''
@Bot.event
async def on_message_edit(before: discord.Message, after: discord.Message):
	channel = discord.utils.get(before.guild.text_channels, name = 'лог')
	ed_e = discord.Embed(title = 'Message Edited')
	await channel.send(before.content)
	await channel.send(after.content)

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
	
@Bot.event
async def on_member_join(member: discord.Member):
	channel = discord.utils.get(member.guild.text_channels, name = 'bot')
	await channel.send(f'{member.mention} joined to the server')
	
@Bot.event
async def on_member_remove(member: discord.Member):
	channel = discord.utils.get(member.guild.text_channels, name = 'bot')
	await channel.send(f'{member.mention} leaved the server')
'''
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
