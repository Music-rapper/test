import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
import time

prefix = 'r!'

Bot = commands.Bot(command_prefix = prefix)

@Bot.command()
async def hello(ctx):
    	await ctx.send(f"Hello {ctx.author.mention}")
	
@Bot.command()
async def prefix(ctx, value):
	prefix = value

@Bot.command()
async def user(ctx, member: discord.Member):
	emb = discord.Embed(title = str(member), description = member.mention, color = member.top_role.color)
	emb.add_field(name = 'Id', value = member.id, inline = False)
	emb.set_thumbnail(member.avatar_url)
	emb.set_footer(text = f'Caused by:{str(ctx.author)}', icon_url = ctx.author.avatar_url)
	await ctx.send(embed = emb)
	
	
@Bot.event
async def on_ready():
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Playing with developer'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
