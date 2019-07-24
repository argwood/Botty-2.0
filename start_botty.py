import os
import discord
import asyncio
import commands

'''
Botty Lite - a sassy but smart Discord bot for Pokemon GO

Provide bot token as environment variable:
    export TOKEN='my_token_here'

Usage:
    python3 start_botty.py
'''

client = discord.Client()

try:
    token = os.environ['TOKEN']
except KeyError:
    print('Make sure you\'ve provided your bot token as an environment variable. Use: export TOKEN = \'my_token_here\'.')
    client.close()

_botty = commands.Commands(client)

@client.event
async def on_ready():
    print('Waking up Botty...')
    print('Currently running on Discord.py version {}. Botty runs best on version 0.16.12.'.format(discord.__version__))

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

if __name__ == "__main__":

    try:
        client.run(token)
    except:
        client.close()
