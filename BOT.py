import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os

Bot = commands.Bot(command_prefix = '!')

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
async def prefix(ctx, new = None):
	if new == None:
		await ctx.send(f'My current prefix is {!}')
	else:
		new = f'{new}'
		Bot = commands.Bot(command_prefix = new)
		await ctx.send(f'You changed your prefix to {new}')
				
@Bot.event
async def on_ready():
	print('Bot is ready!')
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('1234567890'))
	
@Bot.event
async def on_message_edit(ctx.message, ctx.message):
	print(f'{ctx.message} changed')
	await ctx.send('Everything is OK!')
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
