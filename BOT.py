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
async def membercount(ctx):
	guild = ctx.guild
	mention_msg = ''
	
	for i in range(0, len(guild.members)):
		if guild.members[i].bot == False:
			mention_msg += f'{guild.members[i].mention}, '
	else:
		mention_msg -= 2
	mcm_e = discord.Embed(title = 'Server Members', color = discord.Color.from_rgb(255, 0, 0))
	mcm_e.add_field(name = f'Members ({len(guild.members)})', value = mention_msg)
	mcm_e.set_footer(text = f'Caused by: {str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = mcm_e)
				
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('1234567890 :imp:'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
