#   merchant.py
import os
import json
import asyncio
import discord
from discord.ext import commands
import dotenv
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OWNER = os.getenv('DISCORD_OWNER')
PREFX = os.getenv('DISCORD_PREFX')

class RedfordClient(discord.Client):
    """
    Merchant Bot for Discord: 
    redford v0.0.2 by: darkstag
    "Merchant" Cog Extension by: oxygen / Oxygenetic
    ..................................................................
    Any data collected about users is on at an at-will/opt-in basis.
    Remote communications only share content designated by the user.
    Your privacy is important to us, for more information @darkstag#0001
    """
    
    def get_prefix(self, message):
        """Designate our Prefix"""

        prefixes = [PREFX]

        # Check if DM
        if not message.guild:
            #incase we need to change this
            return prefixes

        # in Guild Chat
        return commands.when_mentioned_or(*prefixes)(self, message)

    #load these cogs
    initial_extensions = ['extensions.raffle',
                      'extnensions.slots',
                      'cogs.merchant.merchant',
                      'cogs.merchant.hunting',
                      'cogs.merchant.loading',
                      'cogs.merchant.membership',
                      'cogs.merchant.services'
                      ]

    bot = commands.Bot(command_prefix=get_prefix, description='A Rewrite Cog Example')

    # Here we load our extensions(cogs) listed above in [initial_extensions].
    if __name__ == '__main__':
        for extension in initial_extensions:
            bot.load_extension(extension)

    async def on_ready(self):
        #load json data files
        with open('redford/data/guilddata.json') as g:
            guilds = json.load(g)
        with open('redford/data/userdata.json') as u:
            users = json.load(u)
        #with open('data/relaydata.json') as r:
        #    relays = json.load(r)
        #with open('data/commdata') as c:
         #   cmds = json.load(c)
        
        conns = discord.utils.get(client.guilds)
        #connct = conns.count
        #guildct = guilds.count
        #i=0
        #for conn in conns:
        #    i=+1
        #    print(f'{conn.name}({conn.id}) allowed ✓\n')
        #    await self.send(
        #        f'{self.guildname} connected to REDFORD'    
        #    )
        #print(f'{i} guilds connected')
        client_id = "625008879411003403"
        print(f'https://discordapp.com/oauth2/authorize?client_id={client_id}&scope=bot&permissions=8')
        
    async def on_join(self):                
        await client.send(
            f'{client.member}({client.member.id}) has joined {client.guildname}'
        )
    
client = RedfordClient()
client.run(TOKEN) 