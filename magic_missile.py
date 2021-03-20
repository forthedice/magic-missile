
import random

class MagicMissile:

    def __init__(self, spell_slot_lvl, spell_mode):
        try:
            self.lvl = int(spell_slot_lvl)
        except:        
            raise TypeError("spell_slot_level should be an integer")
        if spell_mode == "roll_die" or spell_mode == "roll_dice":
            self.mode = spell_mode
        else:
            raise Exception("spell_mode should be 'roll_die', or 'roll_dice'")


    def _dart_num(self):
        if self.lvl == 0:
            print("You clearly have no magic ability,\
 and are utterly weak")
            exit()
        elif self.lvl == 1:
            return 3
        else:
            bonus = self.lvl - 1          
            return (3 + bonus) 

    def _attack_damage(self):
        for x in range(1):
            return random.randint(1, 4)

    def _damage_roll_die(self):
        dart_num = self._dart_num()
        base_damage = self._attack_damage()
        damage_per_dart = (base_damage + 1)
        total_damage = damage_per_dart * dart_num
        return { "darts_fired": dart_num, 
                 "base_damage": base_damage, 
                 "damage_per_dart": damage_per_dart, 
                 "total_damage": total_damage  }

    def _damage_roll_dice(self):
        dart_num = self._dart_num()
        base_damage_per_dart = {}
        total_damage_per_dart = {}
        for dart in range(dart_num):
            damage = self._attack_damage()
            base_damage_per_dart["dart_{}".format(dart + 1)]\
                = (damage)
            total_damage_per_dart["dart_{}".format(dart + 1)]\
                = (damage + 1)
        total_damage = sum(total_damage_per_dart.values())
        return { "darts_fired": dart_num,
                 "base_damage_by_dart": base_damage_per_dart,
                 "total_damage_by_dart": total_damage_per_dart,
                 "total_damage_all_darts": total_damage }
         
    def cast(self):
        if self.mode == "roll_die":
            return self._damage_roll_die()
        elif self.mode == "roll_dice":
            return self._damage_roll_dice()

