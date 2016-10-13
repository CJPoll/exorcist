import unittest

from src.actor.equipment import Equipment
from src.actor.equipment import EquipmentManager
from src.actor.equipment_type import EquipmentType



class TestEquipment(unittest.TestCase):

	setUp(self){
		self.weapon = Equipment("Short Sword","shortsw.png",0,1,0,EquipmentType.WEAPON)
		self.armor = Equipment("Leather Armor","ltarmor.png",1,0,1,EquipmentType.ARMOR)
		self.nothing = EquipmentManager().NOTHING
		self.actor
		self.total = {1,1,1}
	}
	
	def test_equipment_equip_weapon(self):
		self.actor = EquipmentManager().equip(self.actor,self.weapon)
		self.weapon.assertEquals(self.actor.weapon)

	def test_equipment_equip_armor(self):
		self.actor = EquipmentManager().equip(self.actor,self.armor)
		self.armor.assertEquals(self.actor.armor)


	def test_equipment_dequip_weapon(self):
		self.actor = EquipmentManager().dequip(self.actor,self.weapon)
		self.nothing.assertEquals(self.actor.weapon)

	def test_equipment_dequip_weapon(self):
		self.actor = EquipmentManager().dequip(self.actor,self.weapon)
		self.nothing.assertEquals(self.actor.armor)

	def test_equipment_sumEquipment():
		self.total.assertEquals(EquipmentManager().sumEquipment(self.actor))




