import discord
import asyncio
import random
import json
import re
import collections, itertools
from dicts import Dicts
import requests
from bs4 import BeautifulSoup

dicts = Dicts()

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
                    try:
                        await self._client.send_message(message.channel, user.mention + ' doesn\'t bite. Their friend code is ``' + choice_code + '``.')
                    except AttributeError:
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
                    await self._client.send_message(message.channel, 'Use the following commands to find friends and add Trainers to your network:\n\n`!friend XXXX XXXX XXXX` to add your Trainer Code\n`!friend <@username>` to search for a Trainer\'s Code\n`!friend remove` to remove your Trainer Code\n`!friend roulette` to roll the dice and get a random Trainer Code')
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
                await self._client.send_message(message.channel, 'Use the following commands to find friends and add Trainers to your network:\n\n`!friend XXXX XXXX XXXX` to add your Trainer Code\n`!friend <@username>` to search for a Trainer\'s Code\n`!friend remove` to remove your Trainer Code\n`!friend roulette` to roll the dice and get a random Trainer Code')

    async def dex(self, message):
        condition = ''
        if len(message.content.lower().split()) == 1:
            await self._client.send_message(message.channel, 'Nope. Use ``!dex [Pokemon] [form]`` to search for typing, movesets, CPs, and more for a specific \'mon.')
        elif len(message.content.lower().split()) == 2:
            pokemon = message.content.lower().split()[1]
        elif len(message.content.lower().split()) == 3 and message.content.lower().split()[2] in ['a', 'alolan']:
            pokemon = message.content.lower().split()[1]
            condition = 'alolan'
        elif len(message.content.lower().split()) == 3 and message.content.lower().split()[2] in ['a','s','d', 'attack', 'speed', 'defense']: #deoxys
            pokemon = message.content.lower().split()[1]
            condition = message.content.lower().split()[2]
            if condition == 'a':
                condition = 'attack'
            elif condition == 's':
                condition = 'speed'
            elif condition == 'd':
                condition = 'defense'
        elif len(message.content.lower().split()) == 3 and message.content.lower().split()[2] in ['altered','origin']: #gira
            pokemon = message.content.lower().split()[1]
            condition = message.content.lower().split()[2]
        elif len(message.content.lower().split()) == 3 and message.content.lower().split()[2] == 'armored':
            pokemon = message.content.lower().split()[1]
            condition = 'armored'
        else:
            await self._client.send_message(message.channel, (
                'Something\'s not quite right, `{}`. Use ``!dex [Pokemon] [form]`` to search for a specific \'mon.').format(message.author.display_name))

        if pokemon in dicts.pokemon:
            dex_number = dicts.pokemon.get(pokemon)

            if condition == 'alolan':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-alolan".format(dex_number)
            elif condition == 'attack':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-attack".format(dex_number)
            elif condition == 'speed':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-speed".format(dex_number)
            elif condition == 'defense':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-defense".format(dex_number)
            elif condition == 'altered':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-altered".format(dex_number)
            elif condition == 'origin':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-origin".format(dex_number)
            elif condition == 'armored':
                site = "https://pokemongo.gamepress.gg/pokemon/{}-armored".format(dex_number)
            else:
                site = "https://pokemongo.gamepress.gg/pokemon/{}".format(dex_number)
            page = requests.get(site)
            soup = BeautifulSoup(page.content, 'html.parser')

            max_cp = soup.find_all(class_="max-cp-number")
            stats = soup.find_all(class_="stat-text")
            types = soup.find_all(class_=("field field--name-field-pokemon-type " +
                                          "field--type-entity-reference " +
                                          "field--label-hidden field__items"))

            female = soup.find_all(class_="female-percentage")
            male = soup.find_all(class_="male-percentage")

            weak_table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="weak-table")
            strength_table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="resist-table")
            weak_list = weak_table.find_all(class_ = "type-img-cell")
            strength_list = strength_table.find_all(class_ = "type-img-cell")

            weaknesses = []
            strengths = []
            for i in range(len(weak_list)):
                weaknesses.append(str(weak_list[i].contents[0]).split('/')[-2][:-5])
            for i in range(len(strength_list)):
                strengths.append(str(strength_list[i].contents[0]).split('/')[-2][:-5])
            quick = []
            legacy_quick = []
            for quick_move in soup.find_all(class_=(
                    "views-field views-field-field-quick-move")):
                quick.append(quick_move.find(class_=(
                    "field field--name-title " +
                    "field--type-string field--label-hidden")))
                legacy_quick.append(quick_move.find(class_=(
                    "has-legacy")))
            charge = []
            legacy_charge = []
            for charge_move in soup.find_all(class_=(
                    "views-field views-field-field-charge-move")):
                charge.append(charge_move.find(class_=(
                    "field field--name-title " +
                    "field--type-string field--label-hidden")))
                legacy_charge.append(charge_move.find(class_=(
                    "has-legacy")))
            legacy_moves = []
            for (legacy_quick, legacy_charge) in zip(legacy_quick, legacy_charge):
                try:
                    if legacy_quick.get_text() == '*':
                        legacy_moves.append(' (Legacy)')
                    else:
                        try:
                            if legacy_charge.get_text() == '*':
                                legacy_moves.append(' (Legacy)')
                            else:
                                legacy_moves.append('')
                        except:
                            legacy_moves.append('')
                except:
                    try:
                        if legacy_charge.get_text() == '*':
                            legacy_moves.append(' (Legacy)')
                        else:
                            legacy_moves.append('')
                    except:
                        legacy_moves.append('')
            offensive_grade = soup.find_all(class_=(
                "views-field views-field-field-offensive-moveset-grade"))
            for index, grade in enumerate(offensive_grade):
                offensive_grade[index] = str(grade.get_text().strip())
            defensive_grade = soup.find_all(class_=(
                "views-field views-field-field-defensive-moveset-grade"))
            for index, grade in enumerate(defensive_grade):
                defensive_grade[index] = str(grade.get_text().strip())
            offensive_moves = sorted(zip(offensive_grade[1:], quick[1:],
                                         charge[1:], legacy_moves[1:]),
                                     key=lambda x: x[0])
            defensive_moves = sorted(zip(defensive_grade[1:], quick[1:],
                                         charge[1:], legacy_moves[1:]),
                                     key=lambda x: x[0])
            title = "%03d" % dex_number + ' | ' + pokemon.upper()
            if condition:
                title += ' (' + condition.upper() + ')'
            elif dex_number == 386: #add normal deoxys title as well
                title += ' (NORMAL)'
            elif dex_number == 487:
                title += ' (ALTERED)'
            table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="minmaxtable")
            rows = table.find_all(lambda tag:tag.name=='tr')
            max_cp_15 = rows[29].find_all('td')[3].contents[0]
            max_cp_20 = rows[39].find_all('td')[3].contents[0]
            max_cp_25 = rows[49].find_all('td')[3].contents[0]
            max_cp_30 = rows[59].find_all('td')[3].contents[0]
            max_cp_35 = rows[69].find_all('td')[3].contents[0]
            max_cp_40 = rows[79].find_all('td')[3].contents[0]
            if len(types[0].get_text().split()) == 1:
                descript = "\n**Type** " + types[0].get_text().split()[0]
            else:
                descript = ("\n**Type** " + types[0].get_text().split()[0] + ' | ' +
                             types[0].get_text().split()[1])
            descript += "\n"
            if len(weaknesses) == 1:
                descript += "\n**Weak Against** " + weaknesses[0].capitalize()
            elif len(weaknesses) == 2:
                descript += ("\n**Weak Against** " + weaknesses[0].capitalize() + ' | ' +
                             weaknesses[1].capitalize())
            elif len(weaknesses) == 3:
                descript += ("\n**Weak Against** " + weaknesses[0].capitalize() + ' | ' +
                             weaknesses[1].capitalize() + ' | ' + weaknesses[2].capitalize())
            elif len(weaknesses) >= 4:
                descript += ("\n**Weak Against** " + weaknesses[0].capitalize() + ' | ' +
                             weaknesses[1].capitalize() + ' | ' + weaknesses[2].capitalize()  + ' | ' + weaknesses[3].capitalize())
            if len(strengths) == 1:
                descript += "\n**Strong Against** " + strengths[0].capitalize()
            elif len(strengths) == 2:
                descript += ("\n**Strong Against** " + strengths[0].capitalize() + ' | ' +
                             strengths[1].capitalize())
            elif len(strengths) == 3:
                descript += ("\n**Strong Against** " + strengths[0].capitalize() + ' | ' +
                             strengths[1].capitalize() + ' | ' + strengths[2].capitalize())
            elif len(strengths) >= 4:
                descript += ("\n**Strong Against** " + strengths[0].capitalize() + ' | ' +
                             strengths[1].capitalize() + ' | ' + strengths[2].capitalize()  + ' | ' + strengths[3].capitalize())
            descript += "\n"
            descript += ("\n**" + stats[0].get_text().split()[0] + '** ' +
                         stats[0].get_text().split()[1] + ' | **' +
                         stats[2].get_text().split()[0] + '** ' +
                         stats[2].get_text().split()[1] + ' | **' +
                         stats[4].get_text().split()[0] +
                         '** ' + stats[4].get_text().split()[1] + '\n')
            try:
                descript += ("**♀** " + female[0].get_text().strip() +
                             "  |  **♂** " + male[0].get_text().strip() + '\n')
            except:
                pass
            descript += ("\n**:100: L40** " + max_cp_40 + ' | **L35** ' + max_cp_35 + ' | **L30** ' + max_cp_30 +
                         '\n**:100: L25** ' + max_cp_25 + ' | **L20** ' + max_cp_20 + ' | **L15** ' + max_cp_15)
            descript += "\n"
            if len(offensive_moves) > 0:

                descript += "\n**Offensive Movesets**"
                for (grade, quick, charge, legacy) in offensive_moves:
                    try:
                        descript += ('\n(' + grade.strip() + ') ' + quick.get_text().strip() +
                             '/' + charge.get_text().strip() + legacy)
                    except:
                        pass
                descript += " \n"
                descript += "\n**Defensive Movesets**"
                for (grade, quick, charge, legacy) in defensive_moves:
                    try:
                        descript += ('\n(' + grade.strip() + ') ' + quick.get_text().strip() +
                                 '/' + charge.get_text().strip() + legacy)
                    except:
                        pass
                descript += "\n"
                if len(soup.find_all(class_=("raid-boss-counters"))) > 0:
                    descript += "\n**Raid Boss Counters**\n"
                    for counter in raid_counters:
                        descript += '\n' + counter.get_text()
                    descript += "\n"
            else:
                quick_moves = soup.find(class_=("primary-move")).find_all(class_=(
                    "field field--name-title field--type-string " +
                    "field--label-hidden"))
                charge_moves = soup.find(class_=("secondary-move")).find_all(
                    class_=("field field--name-title field--type-string " +
                            "field--label-hidden"))
                if soup.find(class_=("pokemon-legacy-quick-moves")) is not None:
                    quick_legacy = soup.find(class_=(
                        "pokemon-legacy-quick-moves")).find_all(class_=(
                            "field field--name-title field--type-string " +
                            "field--label-hidden"))
                if soup.find(class_=(
                        "secondary-move-legacy secondary-move")) is not None:
                    charge_legacy = soup.find(class_=(
                        "secondary-move-legacy secondary-move")).find_all(class_=(
                            "field field--name-title field--type-string " +
                            "field--label-hidden"))
                descript += "\n**Quick Moves**"
                for quick_move in quick_moves:
                    descript += '\n' + quick_move.get_text().strip()
                if soup.find(class_=("pokemon-legacy-quick-moves")) is not None:
                    for legacy_move in quick_legacy:
                        descript += '\n' + legacy_move.get_text().strip() + ' (Legacy)'
                descript += "\n"
                descript += "\n**Charge Moves**"
                for charge_move in charge_moves:
                    descript += '\n' + charge_move.get_text().strip()
                if soup.find(class_=(
                        "secondary-move-legacy secondary-move")) is not None:
                    for legacy_move in charge_legacy:
                        descript += '\n' + legacy_move.get_text().strip() + ' (Legacy)'
                descript += "\n"
                if len(soup.find_all(class_=("raid-boss-counters"))) > 0:

                    descript += "\nRaid Boss Counters\n"
                    for counter in raid_counters:
                        descript += '\n' + counter.get_text()
                    descript += "\n"
            em = discord.Embed(title=title, url=site, description=descript,
                               color=dicts.type_colors[
                                   types[0].get_text().split()[0].lower()])
            if condition == 'alolan':
                em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_61.png').format(dex_number))
            elif dex_number == 386: #deoxys
                if condition == 'attack':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_12.png').format(dex_number))
                elif condition == 'defense':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_13.png').format(dex_number))
                elif condition == 'speed':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_14.png').format(dex_number))
                else:
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_11.png').format(dex_number))
            elif dex_number == 487: #gira
                if condition == 'origin':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_12.png').format(dex_number))
                else:
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_number))
            elif dex_number == 150: #mewtwo
                if condition == 'armored':
                    em.set_thumbnail(url=('https://pokemongo.gamepress.gg/sites/pokemongo/files/styles/240w/public/2019-07/mewtwoArmored.png?itok=LoC_Rd9g'))
                else:
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_number))
            else:
                em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_number))
            em.set_footer(text='Data courtesy of pokemongo.gamepress.gg')
            await self._client.send_message(message.channel, embed=em)
        else:
            await self._client.send_message(message.channel, (
                "That's not any Pokemon I know of, check your spelling " +
                "`{}`").format(message.author.display_name))

    async def rank(self, message):
        split = message.content.lower().split()
        leagues = {'great':1500, 'ultra':2500}
        condition = []
        conditions = ['alolan', 'speed', 's', 'attack', 'a', 'defense', 'd', 'armored', 'origin', 'altered']
        if len(split) > 1: #== 6 or len(split) == 7 or len(split) == 3 or len(split) == 4: #format !rank league pokemon [form] a d s
            #league = split[1]
            if split[1] not in ['great', 'ultra', 'master']:
                league = 'great' # set default league to great
                index = 1
                pokemon = split[index]
            else:
                league = split[1]
                index = 2
                pokemon = split[index]

            if league not in ['great', 'ultra']:
                if 'master' in league:
                    await self._client.send_message(message.channel, 'There is no CP limit in Master League, you want 100% IVs')
                else: await self._client.send_message(message.channel, 'Usage: `!rank League Pokemon [form] Atk Def Sta`')
            #pokemon = split[2]
            if pokemon not in dicts.pokemon:
                await self._client.send_message(message.channel, (
                "That's not any Pokemon I know of, check your spelling " +
                "`{}`").format(message.author.display_name))
            if pokemon in ['mew', 'deoxys', 'celebi']: #pokemon that can't be traded
                miniv = '10'
            else: miniv = '0'
            if len(split) == 2 or (len(split) == 3 and pokemon in split[-1]): # show rank 1
                att_iv = str(15)
                def_iv = str(15)
                sta_iv = str(15)
                site = 'https://gostadium.club/pvp/iv?pokemon=' + pokemon.capitalize() + '&max_cp='+str(leagues[league])+'&min_iv='+miniv+'&att_iv=' + att_iv + '&def_iv=' + def_iv + '&sta_iv=' + sta_iv
            elif any(item in conditions for item in split):#len(split) == 7 or len(split) == 4:
                if pokemon in ['deoxys', 'giratina', 'mewtwo'] or 'alolan' in split: #or (pokemon=='mewtwo' and split[3] == 'armored'):
                    print(split)
                    condition = split[index+1]
                    if condition == 's':
                        condition = 'speed'
                    elif condition == 'a':
                        condition = 'attack'
                    elif condition == 'd':
                        condition = 'defense'

                    if len(split) == 6 or len(split) == 7:
                        att_iv = split[index+2]
                        def_iv = split[index+3]
                        sta_iv = split[index+4]
                    else:
                        att_iv = str(15)
                        def_iv = str(15)
                        sta_iv = str(15)
                    site = 'https://gostadium.club/pvp/iv?pokemon=' + pokemon.capitalize() + '+' + condition.capitalize() + '&max_cp='+str(leagues[league])+'&min_iv='+miniv+'&att_iv=' + att_iv + '&def_iv=' + def_iv + '&sta_iv=' + sta_iv
                else: return self._client.send_message(message.channel, 'Usage: `!rank League Pokemon [form] Atk Def Sta`')
            else:
                try:
                    att_iv = split[index+1]
                    def_iv = split[index+2]
                    sta_iv = split[index+3]
                    site = 'https://gostadium.club/pvp/iv?pokemon=' + pokemon.capitalize() + '&max_cp='+str(leagues[league])+'&min_iv='+miniv+'&att_iv=' + att_iv + '&def_iv=' + def_iv + '&sta_iv=' + sta_iv
                except:
                    return self._client.send_message(message.channel, 'Usage: `!rank League Pokemon [form] Atk Def Sta`')
            page = requests.get(site)
            soup = BeautifulSoup(page.content, 'html.parser')
            rank_table_full = soup.find('table', attrs={'class':'table table-condensed table-striped text-light'})
            ranks = rank_table_full.find_all(lambda tag:tag.name=='td')
            rank = ranks[0].get_text()
            lvl = str(float(ranks[1].get_text()))
            ivs = ranks[2].get_text()
            cp = ranks[3].get_text()
            max_stat = ranks[8].get_text()
            best_lvl = str(float(ranks[10].get_text()))
            best_ivs= ranks[11].get_text()
            best_cp = ranks[12].get_text()
            if len(split) == 2 or len(split) == 3 or (len(split) == 4 and condition in conditions):
                descript = '\n\n'
                descript += '**Ideal IV **' + best_ivs + ' (' + best_cp + ' CP, Lvl ' + best_lvl + ')\n'
            elif len(split) == 7:
                descript = '\n\n'
                descript += '**Rank** ' + rank + '\n**Level** ' + lvl + '\n**IV** ' + ivs + '\n**CP** ' + cp + '\n**% Max** ' + max_stat + '\n\n'
                #descript += '**Rank** ' + rank + '\n**IV** ' + ivs + '\n**Level** ' + lvl + '\n**CP** ' + cp + '\n**% Max** ' + max_stat + '\n\n'
                descript += '**Ideal IV **' + best_ivs + ' (' + best_cp + ' CP, Lvl ' + best_lvl + ')\n'
            else:
                descript = '\n\n'
                descript += '**Rank** ' + rank + '\n**Level** ' + lvl + '\n**IV** ' + ivs + '\n**CP** ' + cp + '\n**% Max** ' + max_stat + '\n\n'
                descript += '**Ideal IV **' + best_ivs + ' (' + best_cp + ' CP, Lvl ' + best_lvl + ')\n'
            title = pokemon.upper()
            if condition:
                title += ' (' + condition.upper() + ')'
            #elif dex_number == 386: #add normal deoxys title as well
            #    title += ' (NORMAL)'
            #elif dex_number == 487:
            #    title += ' (ALTERED)'
            #if len(split) == 6 or len(split) == 7:
                #title += ' | ' + ivs
            em = discord.Embed(title=title, url=site, description=descript, color=0x000000)
            em.set_footer(text='Data courtesy of gostadium.club')
            dex_number = dicts.pokemon.get(pokemon)
            if condition == 'alolan':
                em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_61.png').format(dex_number))
            elif dex_number == 386: #deoxys
                if condition == 'attack':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_12.png').format(dex_number))
                elif condition == 'defense':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_13.png').format(dex_number))
                elif condition == 'speed':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_14.png').format(dex_number))
                else:
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_11.png').format(dex_number))
            elif dex_number == 487: #gira
                if condition == 'origin':
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_12.png').format(dex_number))
                else:
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_number))
            elif dex_number == 150: #mewtwo
                if condition == 'armored':
                    em.set_thumbnail(url=('https://pokemongo.gamepress.gg/sites/pokemongo/files/styles/240w/public/2019-07/mewtwoArmored.png?itok=LoC_Rd9g'))
                else:
                    em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_number))
            else:
                em.set_thumbnail(url=('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_number))
            await self._client.send_message(message.channel, embed=em)
        else:
            await self._client.send_message(message.channel, 'Usage: `!rank League Pokemon [form] Atk Def Sta`')

    async def shiny(self, message):
        condition = ''
        if len(message.content.lower().split()) == 2:
            pokemon = message.content.lower().split()[1]
            if pokemon not in dicts.pokemon:
                return client.send_message(message.channel, (
                "That's not any Pokemon I know of, check your spelling " +
                "`{}`").format(message.author.display_name))
            dex_num = dicts.pokemon.get(pokemon)
            img_url = ('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00.png').format(dex_num)
            shiny_img_url = ('https://raw.githubusercontent.com/ZeChrales/PogoAssets/master/pokemon_icons/pokemon_icon_{0:0=3d}_00_shiny.png').format(dex_num)
            title = pokemon.upper()
            em = discord.Embed(title=title, color=0xffffff)
            em.set_image(url=shiny_img_url)
            em.set_thumbnail(url=img_url)
            await self._client.send_message(message.channel, embed=em)

    async def help(self, message):

        """
        Usage: Upon user command `!help`, returns a help message with bot functionality to message channel

        Parameters: message (Discord.py message)
        """

        info_msg = (":robot: Hi I'm Botty! Here are some of the things I can do for you: \n\n" +
            "`!dex` to display stats for a particular Pokemon \n" +
            "`!rank` to find the best IVs for PvP\n" +
            "`!shiny` to see the shiny version of a particular Pokemon \n" +
            "`!invite` to get an invite link to the server \n" +
            "`!friend` to see commands for Botty's Friend List  \n")
        await self._client.send_message(message.channel, info_msg)


