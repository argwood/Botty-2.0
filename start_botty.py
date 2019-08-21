import os
import discord
import asyncio
import commands
from dtc import DTC

'''
Botty - a sassy but smart Discord bot for Pokemon GO

Provide bot token as environment variable:
    export TOKEN='my_token_here'

By default, DTC-specific functions are turned off.
Use 'dtc=True' with caution.

Usage:
    python3 start_botty.py
'''

dtc = True

client = discord.Client()

try:
    token = os.environ['TOKEN']
except KeyError:
    print('Make sure you\'ve provided your bot token as an environment variable. Use: export TOKEN = \'my_token_here\'.')
    client.close()

_botty = commands.Commands(client)
if dtc:
    _dtc = DTC(client)

@client.event
async def on_ready():
    print('Waking up Botty...')
    print('Currently running on Discord.py version {}. Botty runs best on version 0.16.12.'.format(discord.__version__))
    await client.change_presence(game=discord.Game(name='with your emotions'))

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        await _botty.help(message)
    elif message.content.startswith('!invite'):
        await _botty.invite(message)
    elif message.content.startswith('!maze'):
        await _botty.maze(message)
    elif message.content.lower().startswith('thanks'):
        await _botty.thanks(message)
    elif message.content.startswith('!friend'):
        await _botty.friend(message)
    elif message.content.startswith('!dex'):
        await _botty.dex(message)
    elif message.content.startswith('!rank'):
        await _botty.rank(message)
    elif message.content.startswith('!shiny'):
        await _botty.shiny(message)

    if dtc:
        if message.content.startswith('!stats') or message.content.startswith('!userstats'):
            await _dtc.userstats(message)
        elif message.content.startswith('!guide'):
            await _dtc.guide(message)
        elif message.content.startswith('!merch'):
            await _dtc.merch(message)
        elif message.content.startswith('!patreon'):
            await _dtc.patreon(message)
        elif message.content.startswith('!map'):
            await _dtc.map(message)
        elif message.content.lower().startswith('where is ') or message.content.lower().startswith('where\'s'):
            await _dtc.HPgyms(message)
        elif ('303367823516893196' in message.channel.id):
            await _dtc.announcement_count(message)

if __name__ == "__main__":

    try:
        client.run(token)
    except:
        client.close()
