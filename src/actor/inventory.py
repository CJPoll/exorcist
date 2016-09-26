class InventoryFullException(Exception):
	pass

class ActorInventory():
	def __init__(self, max_size):
		self.items = set()
		self.max_size = max_size

	def __iter__(self):
		return iter(self.items)

	def add(self, item):
		if self.length() >= self.max_size:
			raise InventoryFullException
		self.items.add(item)

	def contains(self, item):
		return item in self.items

	def length(self):
		return len(self.items)

	def remove(self, item):
		self.items.remove(item)
