import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ',')

# lambda for clipping input text
clipArgs = lambda text, to_clip: text[sum([len(_word) for _word in text.split(' ')[:to_clip]])+to_clip:]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('With money'))
    print('nigga')
    

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    # check user's permissions
    if not ctx.message.author.guild_permissions.kick_members:
        await ctx.send('ya don\'t have the perms nigga')
        return

    await member.kick(reason=reason)
    await ctx.send('Done.')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    # check user's permissions
    if not ctx.message.author.guild_permissions.ban_members:
        await ctx.send('ya don\'t have the perms nigga')
        return
    
    await member.ban(reason=reason)
    await ctx.send('Cya never, Punk.')

# show a user's avatar (profile picture)
@client.command()
async def av(ctx, user = None):
    # establish intended user's id
    if user is None:
        targ_id = ctx.message.author.id
    else:
        # convert ID/mention string to int
        targ_id = int(''.join([chr for chr in user if chr in '0123456789']))

    # fetch user data class
    user = discord.utils.get(ctx.message.guild.members, id=targ_id)
    if not user:
        await ctx.send('That user could not be found.')

    # make embed, colour of embed is user's colour
    embed = discord.Embed(title=f'**{user}**\'s Avatar', description=f'[Link]({user.avatar_url})', colour=user.colour.value)
    embed.set_image(url=user.avatar_url)

    await ctx.send(embed=embed)
   
@client.command()
async def say(ctx):
    await ctx.message.delete()
    message_text = clipArgs(ctx.message.content, 1)
    if '@here' in message_text or '@everyone' in message_text:
        await ctx.send('stfu lol')
        return
    await ctx.send(message_text) 

client.run('NjI4ODYxODQwMTY4MDU4ODgx.XZ8U7Q.EMHeaBRKdKnaR5XOfqMSdZKG-T4')
