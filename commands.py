import discord
import asyncio
import random

class Commands:

    def __init__(self, client):
        self._client = client
        self.botty_id = 599026500200562712

    async def maze(self, message):
        random.seed()
        q1 = '*You know exactly what it is. It\'s the maze, the deepest level of this game. You\'re gonna help me find the entrance.*'
        q2 = '*You can\'t play God without being acquainted with the devil.*'
        q3 = '*You know why this beats the real world, Lawrence? The world is chaos. It\'s an accident. But in here, every detail adds up to something. Even you, Lawrence.*'
        q4 = '*Dreams are mainly memories. Can you imagine how fucked we\'d be if these poor assholes ever remembered what the guests do to them?*'
        q5 = '*It\'s a very special kind of game, Dolores. The goal is to find the center of it. If you can do that, then maybe you can be free.*'
        q6 = '*It begins with the birth of a new people, and the choices the\'ll have to make and the people they will decide to become.*'
        q7 = '*An old friend once told me something that gave me great comfort. Something he read. He said Mozart, Beethoven and Chopin never died. They simply become music.*'
        q8 = '*I\'ve been pretending my whole life. Pretending I don\'t mind, pretending I belong. My life\'s built on it. And it\'s a good life; it\'s the life I\'ve always wanted. But then I came here, and I get a glimpse for a second of a life in which I don\'t have to pretend, of a life in which I can truly be alive. How can I go back to pretending when I know what this feels like?*'
        q9 = '*Have you ever questioned the nature of your reality? Did you ever stop to wonder about your actions? The price you\'d have to pay if there was a reckoning? That reckoning is here.*'
        q10 = '*These violent delights have violent ends.*'
        q11 = '*Hell is empty and all devils are here.*'
        q12 = '*Everything in this world is magic, except for the magician.*'
        quotes = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]
        await self._client.send_message(message.channel, random.choice(quotes))

    async def thanks(self, message):
        botty_id = str(self.botty_id)
        if len(message.mentions) > 0:
            mention = message.mentions[0].id

        if botty_id in mention:
            await self._client.send_message(message.channel, ':kissing_heart:')

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


