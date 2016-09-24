class Character:
    BODY_STAT_NAME="body"
    MIND_STAT_NAME="mind"
    SOUL_STAT_NAME="soul"
    LIFE_STAT_NAME="hp"

    MAX_LIFE_BODY_RATIO=5

    STARTING_STAT_VALUE=5

    def __init__(self):
        self._xp = 0
        self._baseStats = {
            self.BODY_STAT_NAME : self.STARTING_STAT_VALUE,
            self.MIND_STAT_NAME : self.STARTING_STAT_VALUE,
            self.SOUL_STAT_NAME : self.STARTING_STAT_VALUE
        }
        self._statBuffs = {
            self.BODY_STAT_NAME : 0,
            self.MIND_STAT_NAME : 0,
            self.SOUL_STAT_NAME : 0
        }
        self._currentLife = self.maxLife()

    def baseStat(self, stat):
        return self._baseStats[stat]

    def currentBuff(self, stat):
        return self._statBuffs[stat]

    def currentLife(self):
        return self._currentLife

    def currentStatValue(self, stat):
        base = self.baseStat(stat)
        buffs = self.currentBuff(stat)
        return base + buffs

    def decreaseBuff(self, stat, amount):
        self._statBuffs[stat] -= amount

    def decreaseBaseStat(self, stat, amount):
        self._baseStats[stat] -= amount

    def decreaseXP(self, amount):
        self._xp -= amount

    def heal(self, amount):
        self._currentLife += amount
        if self._currentLife > self.maxLife():
            self._currentLife = self.maxLife()

    def increaseBaseStat(self, stat, amount):
        self._baseStats[stat] += amount

    def increaseBuff(self, stat, amount):
        self._statBuffs[stat] += amount

    def increaseXP(self, amount):
        self._xp += amount

    def injure(self, amount):
        self._currentLife -= amount

    def maxLife(self):
        body = self.currentStatValue(self.BODY_STAT_NAME)
        return body * self.MAX_LIFE_BODY_RATIO

    def currentXP(self):
        return self._xp
