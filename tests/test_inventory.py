import unittest

from src.actor.inventory import ActorInventory


class TestActorInventory(unittest.TestCase):
	def setUp(self):
		self.inventory = ActorInventory()
		self.item = object()
	
	def test_length_on_add(self):
		self.inventory.add_item(self.item)
		self.inventory.add_item(self.item)
		self.inventory.add_item(self.item)
		self.assertEqual(self.inventory.length(), 3)
