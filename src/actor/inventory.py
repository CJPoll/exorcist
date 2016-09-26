class ActorInventory():
	def __init__(self):
		self.items = []

	def add_item(self, item):
		self.items.append(item)

	def length(self):
		return len(self.items)
