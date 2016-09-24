class Character:
    BODY_STAT_NAME="body"
    MIND_STAT_NAME="mind"
    SOUL_STAT_NAME="soul"
    LIFE_STAT_NAME="hp"

    MAX_LIFE_BODY_RATIO=5

    STARTING_STAT_VALUE=5

    def __init__(self):
        self.xp = 0
        self.baseStats = {
            self.BODY_STAT_NAME : self.STARTING_STAT_VALUE,
            self.MIND_STAT_NAME : self.STARTING_STAT_VALUE,
            self.SOUL_STAT_NAME : self.STARTING_STAT_VALUE
        }
        self.statBuffs = {
            self.BODY_STAT_NAME : 0,
            self.MIND_STAT_NAME : 0,
            self.SOUL_STAT_NAME : 0
        }
        self.currentLife = self.maxLife()

    def addXP(self, xp):
        self.xp += xp

    def baseStat(self, stat):
        return self.baseStats[stat]

    def buffStat(self, stat, amount):
        self.statBuffs[stat] += amount

    def buffsOn(self, stat):
        return self.statBuffs[stat]

    def debuffStat(self, stat, amount):
        self.statBuffs[stat] -= amount

    def decreaseBaseStat(self, stat, amount):
        self.baseStats[stat] -= amount

    def heal(self, amount):
        self.currentLife += amount
        if self.currentLife > self.maxLife():
            self.currentLife = self.maxLife()

    def increaseBaseStat(self, stat, amount):
        self.baseStats[stat] += amount

    def injure(self, amount):
        self.currentLife -= amount

    def maxLife(self):
        body = self.statValue(self.BODY_STAT_NAME)
        return body * self.MAX_LIFE_BODY_RATIO

    def removeXP(self, xp):
        self.xp -= xp

    def statValue(self, stat):
        base = self.baseStat(stat)
        buffs = self.buffsOn(stat)
        return base + buffs
