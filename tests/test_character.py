import unittest
from src.character import Character
from src.enums import Stats

class TestCharacter(unittest.TestCase):
	def setUp(self):
		self.character = Character()
		self.character._xp = 250
		self.body = Stats.BODY

	def test_increase_xp(self):
		self.character.increaseXP(250)
		self.assertEqual(self.character.currentXP(), 500)

	def test_decrease_xp(self):
		self.character.decreaseXP(250)
		self.assertEqual(self.character.currentXP(), 0)

	def test_increase_base_stat(self):
		self.character.increaseBaseStat(self.body, 5)
		self.assertEqual(self.character.baseStat(self.body), 10)

	def test_decrease_base_stat(self):
		self.character.decreaseBaseStat(self.body, 5)
		self.assertEqual(self.character.baseStat(self.body), 0)

	def test_increase_buff(self):
		self.character.increaseBuff(self.body, 5)
		self.assertEqual(self.character.currentBuff(self.body), 5)

	def test_decrease_buff(self):
		self.character.increaseBuff(self.body, 5)
		self.character.decreaseBuff(self.body, 3)
		self.assertEqual(self.character.currentBuff(self.body), 2)

	def test_total_stat(self):
		self.character.increaseBuff(self.body, 5)
		self.character.decreaseBuff(self.body, 3)
		self.assertEqual(self.character.currentStatValue(self.body), 7)

	def test_max_hp(self):
		self.assertEqual(self.character.maxLife(), 25)

	def test_injure_player(self):
		self.assertEqual(self.character.currentLife(), 25)
		self.character.injure(5)
		self.assertEqual(self.character.currentLife(), 20)

	def test_heal_player(self):
		self.assertEqual(self.character.currentLife(), 25)
		self.character.injure(5)
		self.assertEqual(self.character.currentLife(), 20)
		self.character.heal(5)
		self.assertEqual(self.character.currentLife(), 25)

	def test_cant_overheal(self):
		self.assertEqual(self.character.currentLife(), 25)
		self.character.injure(5)
		self.assertEqual(self.character.currentLife(), 20)
		self.character.heal(10)
		self.assertEqual(self.character.currentLife(), 25)
