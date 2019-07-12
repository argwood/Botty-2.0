import discord
import asyncio
import random
import json
import re
import collections, itertools

class Commands:

    def __init__(self, client):
        self._client = client
        self.botty_id = 599026500200562712
        self.invite_link = 'https://discord.gg/sSeeGPs'

    async def invite(self, message):
        await self._client.send_message(message.channel, self.invite_link)

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

    async def friend(self, message):
        with open('friend_list.json') as f:
            friend_list = json.load(f)

        if message.content.startswith('!friend list'):
            ordered_list = collections.OrderedDict(friend_list)
            await self._client.send_message(message.channel, 'Sorry, this command was removed due to lack of use and extreme channel-ruining :poop:. \n\n')
        else:
            length = len(message.content.split())
            if length>1 and len(message.mentions) == 0:
                if message.content.split()[1].startswith('remove'):
                    author_discrim = str(message.author)
                    if author_discrim in friend_list:
                        del friend_list[author_discrim]
                        await self._client.send_message(message.channel, 'You have been removed from the Friend List.')
                    else:
                        await self._client.send_message(message.channel, 'You are not currently in the Friend List, `{}`. Use ``!friend <Friend Code>`` to add yourself.'.format(message.author.display_name))
                    with open('friend_list.json', 'w') as f:
                        json.dump(friend_list, f)
                elif message.content.split()[1].startswith('roulette'):
                    random.seed()
                    choice = random.choice(list(friend_list))
                    user = discord.utils.get(message.server.members,name = choice[:-5], discriminator = choice[-4:])
                    choice_code = friend_list.get(str(choice))
                    await self._client.send_message(message.channel, user.mention + ' doesn\'t bite. Their friend code is ``' + choice_code + '``.')
                elif length == 4:
                    if str(message.content.split()[1].startswith('[')): # if they input their code with brackets
                        code_to_add = str((message.content.split()[1]).replace('[',''))+str(message.content.split()[2])+str((message.content.split()[3]).replace(']',''))
                    else: # if they input their code with spaces
                        code_to_add = str(message.content.split()[1])+str(message.content.split()[2])+str(message.content.split()[3])
                    author_name = str(message.author.display_name)
                    author_id = str(message.author.id)
                    author_discrim = str(message.author)
                    if author_discrim not in friend_list:
                        friend_list_add = {author_discrim:code_to_add}
                        friend_list.update(friend_list_add)
                        with open('friend_list.json', 'w') as f:
                            json.dump(friend_list, f)
                            await self._client.send_message(message.channel, 'You have been added to the Friend List with code ``' + code_to_add + '``')
                    else:
                        await self._client.send_message(message.channel, 'You have already been added to the Friend List. Try ``!friend remove`` if you want to edit your code.')
                elif not message.content.split()[1][0].isalpha(): # only adds codes if they are numeric
                    if str(message.content.split()[1].startswith('[')):
                        code_to_add = re.sub("\[|\]","",str(message.content.split()[1]))
                    author_name = str(message.author.display_name)
                    author_id = str(message.author.id)
                    author_discrim = str(message.author)
                    if author_discrim not in friend_list:
                        friend_list_add = {author_discrim:code_to_add}
                        friend_list.update(friend_list_add)
                        with open('friend_list.json', 'w') as f:
                            json.dump(friend_list, f)
                        await self._client.send_message(message.channel, 'You have been added to the Friend List with code ``' + code_to_add + '``')
                    else:
                        await self._client.send_message(message.channel, 'You have already been added to the Friend List. Try ``!friend remove`` if you want to edit your code.')
                else:
                    await self._client.send_message(message.channel, 'Use the following commands to find friends and add Trainers to your network:\n\n`!friend <code>` to add your Trainer Code\n`!friend <@username>` to search for a Trainer\'s Code\n`!friend remove` to remove your Trainer Code\n`!friend roulette` to roll the dice and get a random Trainer Code')
            elif length>1 and len(message.mentions) == 1:
                friend_discrim = str(message.mentions[0])
                friend_name = message.mentions[0].display_name
                friend_id = message.mentions[0].id
                if friend_discrim in friend_list:
                    friend_code = friend_list.get(str(friend_discrim))
                    await self._client.send_message(message.channel, friend_name + '\'s friend code is ``' + friend_code + '``. Please play nicely.')
                else:
                    await self._client.send_message(message.channel, 'Sorry, `{}`. '.format(message.author.display_name) + friend_name + ' has not provided a Trainer Code. Go send them a DM or make friends IRL.')
            else:
                await self._client.send_message(message.channel, 'Use the following commands to find friends and add Trainers to your network:\n\n`!friend <code>` to add your Trainer Code\n`!friend <@username>` to search for a Trainer\'s Code\n`!friend remove` to remove your Trainer Code\n`!friend roulette` to roll the dice and get a random Trainer Code')

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


