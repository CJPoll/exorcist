from src.actor.stat_names import StatNames

class ActorStats:
	MAX_LIFE_BODY_RATIO=5
	STARTING_STAT_VALUE=5

	def __init__(self):
		self._xp = 0
		self._baseStats = {
			StatNames.BODY : self.STARTING_STAT_VALUE,
			StatNames.MIND : self.STARTING_STAT_VALUE,
			StatNames.SOUL : self.STARTING_STAT_VALUE
		}
		self._statBuffs = {
			StatNames.BODY : 0,
			StatNames.MIND : 0,
			StatNames.SOUL : 0
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
		body = self.currentStatValue(StatNames.BODY)
		return body * self.MAX_LIFE_BODY_RATIO

	def currentXP(self):
		return self._xp
