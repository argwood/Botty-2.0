import discord
import asyncio

class Commands:

    def __init__(self, client):
        self._client = client

    async def help(self, message):

        """
        Usage: Upon user command `!help`, returns a help message with bot functionality to message channel

        Parameters: message (Discord.py message)
        """

        info_msg = (":robot: Hi I'm Botty! Here are some of the things I can do for you: \n\n" +
            "`!dex` to display stats for a particular Pokemon \n" +
            "`!rank` to find the best IVs for PvP\n" +
            "`!invite` to get an invite link to the server \n" +
            "`!friend` to see commands for Botty's Friend List  \n")
        await self._client.send_message(message.channel, info_msg)


