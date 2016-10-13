import collections
from src.actor.equipment_type import EquipmentType

Equipment = collections.namedTuple('Equipment','name image body mind soul type');

class EquipmentManager():
	NOTHING = Equipment("Nothing","nothing.png",0,0,0,"")

	def equip(actor,equipment):
		if(equipment.type == EquipmentType.ARMOR):
			actor.armor = equipment
		else:
			actor.weapon = equipment
		return actor


	def dequip(actor,equipment):
		if(equipment.type == EquipmentType.ARMOR):
			actor.armor = NOTHING
		else:
			actor.weapon = NOTHING
		return actor	
 
	def sumEquipment(actor):
		weapon = actor.weapon
		armor = actor.armor
		mind = weapon.mind + armor.mind
		body = weapon.body + armor.body
		soul = weapon.soul + armor.soul
		buffs = {
			mind,
			body,
			soul
		}
		
		return buffs




