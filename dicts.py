import discord
import asyncio
import json
import re
import collections, itertools

class Dicts:

	pokemon = {}
	type_colors = {}

	with open("pokedex.txt") as f:
		for line in f:
			(key, val) = line.strip().rsplit(' ',1)
			pokemon[key.lower()] = int(val)

	type_colors = {'bug': 0xA8B820,
                'dark': 0x705848,
                'dragon': 0x7038F8,
                'electric': 0xF8D030,
                'fairy': 0xEE99AC,
                'fighting': 0xC03028,
                'fire': 0xF08030,
                'flying': 0xA890F0,
                'ghost': 0x705898,
                'grass': 0x78C850,
                'ground': 0xE0C068,
                'ice': 0x98D8D8,
                'normal': 0xA8A878,
                'poison': 0xA040A0,
                'psychic': 0xF85888,
                'rock': 0xB8A038,
                'steel': 0xB8B8D0,
                'water': 0x6890F0
                }
