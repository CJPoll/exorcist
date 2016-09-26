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
		self.inventory.add(TestItem("Mighty Axe"))
		self.inventory.add(TestItem("Mighty Sword"))
		doubles = map(lambda item: item.name, self.inventory)
		self.assertTrue("Mighty Sword" in doubles)
		self.assertTrue("Mighty Axe" in doubles)

	def test_max_size(self):
		self.inventory.add(TestItem("Mighty Axe"))
		self.inventory.add(TestItem("Mighty Shield"))
		self.inventory.add(TestItem("Mighty Helm"))
		with self.assertRaises(InventoryFullException):
			self.inventory.add(TestItem("Mighty Sword"))
