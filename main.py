import discord, json, datetime, random
from discord.ext import commands as cmds

with open('config.json','r') as config:
    config = json.load(config)

bot = cmds.Bot(command_prefix = ':', case_insensitive = True, description = 'Joee\'s discord scamming bot.', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print(f'{bot.user.name}#{bot.user.discriminator} is ready to cause chaos, with the prefix: \'{bot.command_prefix}\'. (UID: {bot.user.id})')
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = 'over some servers!'))
    
@bot.command()
async def embed(ctx):
    user = bot.get_user() # TEMP
    await ctx.reply(user)
    link_to_mask = config['link_to_mask']
    
    embed = discord.Embed(
        title = 'Discord System Message from Wumpus.',
        description = f'Hello {user},\nHere at Discord we are focused on maintaining a safe and secure enviroment for our community.\n\nYour account has been flagged by our auto-moderation bot, and has had several manual reports by unique users.\n\nManual report log from users:',
        color = 0x5865F2
    )
    
    embed.add_field(name = '**·** Harassment', value = f'Unique User Reports: {random.randint(5, 30)}', inline = True)
    embed.add_field(name = '**·** Hate Speech', value = f'Unique User Reports: {random.randint(5, 30)}', inline = True)
    embed.add_field(name = '_ _', value = f'Your actions are in violation of our [Community Guidelines]({link_to_mask} "Discord\'s Community Guidelines. https://discord.com/guidelines/"), therefore we are issuing you a warning. If this behavior continues, we will take further action on your account, up to and including account termination.\n\nSincerely,\nDiscord Trust & Safety Team.', inline = False)
    embed.add_field(name = '_ _', value = f'If you believe this is a mistake, please visit [Discord\'s Account Report Appeals]({link_to_mask} "Discord\'s Account Report Appeals. https://support.discord.com/hc/en-us/requests/new/").\n', inline = False)
    embed.set_footer(text = 'Official messages from discord will always have a BOT tag next to it\'s username.', icon_url = 'https://i.imgur.com/75WC2s4.png')
    
    await user.send(embed = embed)

bot.run(config['bot_token'])
