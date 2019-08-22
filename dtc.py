import discord
import asyncio
import os
import csv
import time

class DTC:

    def __init__(self, client):
        self._client = client
        self.invite_link = 'https://discord.gg/sSeeGPs'
        self.map_channel = '546072336642605056'
        self.HP_channel = '337956200048099328'
        self.announcements_channel = '303367823516893196'
        self.playground = '558128086852567041'

    async def userstats(self, message):
        months = {'nov': 'november', 'dec': 'december', 'jan':'january', 'feb':'february', 'mar':'march', 'apr':'april','may':'may', 'jun':'june','jul':'july','aug':'august','sept':'september','sep':'september','oct':'october'}
        if message.content.lower().startswith('!userstats') or message.content.lower().startswith('!stats'):
            msg = message.content.lower().split(" ")
            if len(msg) == 3:
                notif = ''
                username = msg[1]
                month = msg[2]
                if len(month) == 3 or len(month) == 4:
                    for abbrev in months.keys():
                        if abbrev == month:
                            month=months.get(abbrev)
                filename ='./stats/' + month + '_' + username +'.txt'
                print('Reading from {}'.format(filename))
                if os.path.exists(filename):
                    with open(self.get_path(
                        './stats/' + month + '_' + username +'.txt'), 'r+') as stats_file:
                        for line in stats_file:
                            notif = notif + line
                        await self._client.send_message(message.channel, (notif).format(message.author.display_name))
                else:
                    if month not in ['nov', 'november', 'dec', 'december', 'jan', 'january','feb','february','mar','march','apr','april','may', 'jun','june','jul','july','aug','august','sept','sep','september','oct','october']:
                        await self._client.send_message(message.channel, (
                        "That's not a month, `{}`.").format(message.author.display_name))
                    else:
                        await self._client.send_message(message.channel, (
                        "Try your PoGo trainer name instead. Or did you forget to submit your stats to DTC this month, `{}`?").format(message.author.display_name))
            else:
                await self._client.send_message(message.channel, (
                    ':facepalm: Not how this works, `{}`. Try ' +
                    '!stats [PoGo trainer name] [month] ' +
                    'and then cry at your terrible stats :sob:').format(message.author.display_name))

    def get_path(self, path):
        if not os.path.isabs(path):
            path = os.path.join(os.path.dirname(__file__), path)
        return path

    async def guide(self, message):
        guide_link = 'https://dtc.fyi/gofestguide2019'
        await self._client.send_message(message.channel, guide_link)

    async def merch(self, message):
        merch_link = 'https://dtc.fyi/merch'
        await self._client.send_message(message.channel, merch_link)

    async def patreon(self, message):
        patreon_link = 'https://www.patreon.com/dtcpkmngo'
        await self._client.send_message(message.channel, patreon_link)

    async def map(self, message):
        if message.channel.id == self.map_channel:
            map_link = 'https://map.dtc.fyi'
            await self._client.send_message(message.channel, map_link)

    async def HPgyms(self, message):
        if message.channel.id == self.HP_channel:
            gym_link = 'http://imgur.com/a/O8acycN'
            await self._client.send_message(message.channel, 'Here is a list of gyms in Hyde Park/Woodlawn with their locations and EX eligibility:\n(' + gym_link + ')')

    def get_users():

        startTime = datetime.now().time
        for server in client.servers:
            online = 0
            idle = 0
            offline = 0

            for member in server.members:
                if str(member.status) == 'online':
                    online+=1
                elif str(member.status) == 'idle':
                    idle += 1
        totalUsers = online + idle
        row = [totalUsers, online,idle]
        return row

    async def announcement_count(self, message):
        if message.channel.id == self.announcements_channel:
            channel = message.channel
            time.sleep(30)
            cache_msg = await self._client.get_message(channel, message.id)
            reacts = {react.emoji: react.count for react in cache_msg.reactions}
            online = 0
            online = self.get_users()
            row = [message.content[0:50], message.timestamp, message.author.display_name, len(message.content),len(message.attachments), reacts, online]
            with open('announcement_reacts.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(row)
            return reacts




