#extras
import random
import json
import discord
from discord import command

class raffle():
    '''
    Extension to handle extra commnds die redford
    '''
    @raffle.commands(name="raffle_list")
    def raffle_list(self, ctx):
        #load json data files
        details = "Currently Enrolled:\r\n"
        with open('redford/data/raffledata.json') as r:
            raffd = json.load(r)
            for entry in raffd:
                details += "Ticket#: {entry[tid]}, UserID#: {entry[uid]},\r\n"
                
       # await self.send(details)
    
    @raffle.commands(name="buy")
    def raffle_buy(self, message=1):
        """
        insert ticket numbers 
        """
        with open('redford/data/raffledata.json') as r:
            raffd = json.load(r)
            uid = message.author.userid
            details = "Tickets Bought:\n\r"
            raffc = raffd.count
            i=1
            if(i <= raffc):
                tid = raffc + i
                details += "Ticket#: {tid}, UserID#: {uid},\r\n"
                new = "\{\"tid\":{tid}, \"uid\":{uid}}"
                #insert into json
   
    def raffle_end(self, message)
        raffd = json.load(r)
        winid = random(0,raffd.count)
        details = "Winning Ticket# {winid}\r\n"
        for tid in raffd
            details += "Purchased by: {raffd[{uid}]}"
        