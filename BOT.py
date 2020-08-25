import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time
import datetime

prefix = '!'

Bot = commands.Bot(command_prefix = prefix)

#Bot.remove_command('help')

'''
@Bot.command()
async def help(ctx, command = None):
	me = ctx.guild.me
	h_e = discord.Embed(title = f'{me.name} Bot Commands', color = discord.Color.from_rgb(255, 0, 0))
	h_e.add_field(name = f'{prefix}avatar', value = 'Give you someone\'s avatar that you can easily download.', inline = False)
	h_e.add_field(name = f'{prefix}emoji', value = 'Give information about custom emoji.', inline = False)
	h_e.set_thumbnail(url = me.avatar_url)
	h_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = h_e)
'''	

@Bot.command()
async def role(ctx, role = None):
	
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
				
	r_e = discord.Embed(title = 'Role information', color = discord.Color.from_rgb(255, 0, 0))
	r_e.add_field(name = 'Name', value = role.name)
	r_e.add_field(name = 'ID', value = role.id)
	r_e.add_field(name = 'Mention', value = f'`{role.mention}`')
	r_e.add_field(name = 'Color', value = role.color)
	r_e.add_field(name = 'Members', value = f'`{role.mention}`')
	await ctx.send(embed = r_e)
				
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('1234567890 :imp:'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
