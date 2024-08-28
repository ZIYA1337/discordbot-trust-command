import discord
from discord.ext import commands
from discord.ext.commands import has_any_role, MissingAnyRole

token = 'your discord token here'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
@has_any_role('moderator', 'admin') #role names that can use this command
async def trust(ctx, member: discord.Member):
    trusted = discord.utils.get(ctx.guild.roles, name = 'trusted') #set the value of name(string type) to the role name that this command will add 
    await member.add_roles(trusted)
    await ctx.send('Success, 成功!')

@trust.error
async def trust_error(ctx, error):
    if isinstance(error, MissingAnyRole):
        error_message = 'No access to the command, 无权限使用该指令'
    else:
        error_message = 'Unknown error, 未知错误'
    await ctx.send(error_message)

bot.run(token)