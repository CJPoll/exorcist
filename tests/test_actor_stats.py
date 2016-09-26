import unittest

from src.actor.stats import ActorStats
from src.actor.stat_names import StatNames

class TestActorStats(unittest.TestCase):
	def setUp(self):
		self.stats = ActorStats()
		self.stats._xp = 250
		self.body = StatNames.BODY

	def test_increase_xp(self):
		self.stats.increaseXP(250)
		self.assertEqual(self.stats.currentXP(), 500)

	def test_decrease_xp(self):
		self.stats.decreaseXP(250)
		self.assertEqual(self.stats.currentXP(), 0)

	def test_increase_base_stat(self):
		self.stats.increaseBaseStat(self.body, 5)
		self.assertEqual(self.stats.baseStat(self.body), 10)

	def test_decrease_base_stat(self):
		self.stats.decreaseBaseStat(self.body, 5)
		self.assertEqual(self.stats.baseStat(self.body), 0)

	def test_increase_buff(self):
		self.stats.increaseBuff(self.body, 5)
		self.assertEqual(self.stats.currentBuff(self.body), 5)

	def test_decrease_buff(self):
		self.stats.increaseBuff(self.body, 5)
		self.stats.decreaseBuff(self.body, 3)
		self.assertEqual(self.stats.currentBuff(self.body), 2)

	def test_total_stat(self):
		self.stats.increaseBuff(self.body, 5)
		self.stats.decreaseBuff(self.body, 3)
		self.assertEqual(self.stats.currentStatValue(self.body), 7)

	def test_max_hp(self):
		self.assertEqual(self.stats.maxLife(), 25)

	def test_injure_player(self):
		self.assertEqual(self.stats.currentLife(), 25)
		self.stats.injure(5)
		self.assertEqual(self.stats.currentLife(), 20)

	def test_heal_player(self):
		self.assertEqual(self.stats.currentLife(), 25)
		self.stats.injure(5)
		self.assertEqual(self.stats.currentLife(), 20)
		self.stats.heal(5)
		self.assertEqual(self.stats.currentLife(), 25)

	def test_cant_overheal(self):
		self.assertEqual(self.stats.currentLife(), 25)
		self.stats.injure(5)
		self.assertEqual(self.stats.currentLife(), 20)
		self.stats.heal(10)
		self.assertEqual(self.stats.currentLife(), 25)
