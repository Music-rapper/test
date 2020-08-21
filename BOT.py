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
async def roles(ctx, member: discord.Member):
	role_list = ''
	for i in range(0, len(member.roles)):
		role_list += f'{member.roles[i]} '
	await ctx.send(role_list)

@Bot.command()
async def role(ctx, member: discord.Member):
	role = f"{member.roles}"
	await ctx.send(role[9:27])
	
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
	await Bot.change_presence(status = discord.Status.dnd, activity = discord.Game('Playing with developer'))
	
token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))
