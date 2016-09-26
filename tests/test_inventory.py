import unittest

from src.actor.inventory import ActorInventory
from src.actor.inventory import InventoryFullException

class TestItem():
	def __init__(self, name):
		self.name = name

class TestActorInventory(unittest.TestCase):
	def setUp(self):
		self.inventory = ActorInventory(3)

	def test_length_on_add(self):
		self.inventory.add(TestItem("Mighty Axe"))
		self.assertEqual(self.inventory.length(), 1)

	def test_length_on_remove(self):
		axe = TestItem("Mighty Axe")
		self.inventory.add(axe)
		self.inventory.add(TestItem("Magic Mirror"))
		self.inventory.remove(axe)
		self.assertEqual(self.inventory.length(), 1)

	def test_containse_on_add(self):
		axe = TestItem("Mighty Axe")
		self.assertFalse(self.inventory.contains(axe))
		self.inventory.add(axe)
		self.assertTrue(self.inventory.contains(axe))

	def test_contains_on_remove(self):
		axe = TestItem("Mighty Axe")
		self.inventory.add(axe)
		self.inventory.remove(axe)
		self.assertFalse(self.inventory.contains(axe))

	def test_iterable(self):
		self.inventory.add(1)
		self.inventory.add(2)
		doubles = map(lambda x: x * 2, self.inventory)
		self.assertEqual(doubles, [2, 4])

	def test_max_size(self):
		axe = TestItem("Mighty Axe")
		self.inventory.add(axe)
		self.inventory.add(axe)
		self.inventory.add(axe)
		with self.assertRaises(InventoryFullException):
			self.inventory.add(axe)
