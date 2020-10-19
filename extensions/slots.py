# slots
import discord
import logging
import tqdm
try:
    from numpy.random import RandomState
except:
    logging.warning('Could not find numpy.random, using random.SystemRandom')
    from random import SystemRandom as RandomState

logger = logging.getLogger(__name__)


class SlotMachine(object):
    """ A simple, expandable, customizable slotmachine complete with
    identifyable 'jackpot' and 'bonus' symbols.
    """
    def __init__(self, multi=3, size=(5,2), randomState=None):
        base=['⚔','⚖','⚗','⚓']
        jack='⚜'
        bonus='⚡'
        self.jack, self.bonus, self.base = jack, bonus, base
        self.multi, self.size = multi, size
        self.reel = self.buildReel()
        if randomState:
            self.randomState = randomState
        else:
            self.randomState = RandomState()
        self.count = 0
        self.sinceJack = 0
        self.odds = None
        self.lastSpin = None
        
        #bank
        bonus = 100
        #with open('data/econdata.json')
        #bal = b['userid'].bal
        bal=0
        if bal <= 0:
            bal = bonus
                
    def buildReel(self):
        """ Makes the self.reel array """
        logger.info('Building Reel')
        # make reversed copy of 'base'
        rbase = self.base[::-1]
        # append 'bonus' to 'reversed base'
        rbase.append(self.bonus)
        # add 'reversed base'+'bonus' to 'base'
        nbase = rbase + self.base
        # append another 'bonus' to 'new base'
        nbase.append(self.bonus)
        # extend nbase num 'times'
        reel = nbase * int(self.multi)
        # add jackpot symbol to front
        reel.insert(0, self.jack)
        # return 'reel' with extra 'bonus' removed
        return reel[:-1]

    def __call__(self):
        """ Pulls the 'handle' """
        logger.debug('Spinning machine')
        # set empty display
        nCols, nRows = range(self.size[0]), range(self.size[1])
        # pick symbols and fill display
        raw = [[self.reel[i - row] for row in nRows]
               for i in [self.randomState.choice(range(len(self.reel)))
                         for col in nCols]]
        self.count += 1
        self.sinceJack += 1
        # return display (turned 90 so it makes more
        # sense and easier to traverse/read)
        self.lastSpin = [[col[i] for col in raw] for i in range(len(raw[0]))]
        return self.lastSpin

    def checkLine(self, line):
        """ Overwrite to fit your machine """
        if line.count(self.jack) == len(line):
            jackpot = 100 * self.sinceJack
            self.sinceJack = 0
            return jackpot
        elif line.count(self.bonus) == len(line):
            return 20 * sum(self.lastSpin)
        elif line.count(line[0]) == len(line):
            return 10 * sum(self.lastSpin)  
        else: 
            return False

    def calcOdds(self, times=1000000):
        tally = {}
        logger.info('Calculating odds...')
        for i in tqdm.trange(times):
            r = self.checkLine(self.__call__()[0])
            if str(r) not in tally:
                tally[str(r)] = 0
            tally[str(r)] += 1
        self.odds = tally
        self.count = 0
        self.sinceJack = 0


if __name__ == '__main__':
    from sys import argv
    s = SlotMachine()
    if len(argv) > 1:
        s.calcOdds(argv[1])
        print(s.odds)
    else:
        logging.basicConfig(level=logging.INFO)
        r = s()[0]
        print(r)
        print(s.checkLine(r))
        
    #    await ctx.send(s.checkLine(r))