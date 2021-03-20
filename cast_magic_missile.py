#!/bin/env python3.9

import sys
from magic_missile import MagicMissile

def usage():
     print("Usage: cast_magic_missile.py <spell-slot level> <spell-mode>")
     print("       spell-slot level must be an integer")
     print("       spell-mode either 'roll_die' or 'roll_dice'")
     print("           roll_die, rolls 1 die and result applied to each dart")
     print("           roll_dice, rolls a die for each dart")
     exit()
  
def main(argv):
    if len(argv) == 2:
        spell_slot_lvl = argv[0]
        spell_mode = argv[1]
        try:
            mm_spell = MagicMissile(spell_slot_lvl, spell_mode)
            for item, value in mm_spell.cast().items():
                print("{}: {}".format(item, value))
        except Exception as e:
            print("Error casting MagicMissile, {}".format(e))
            usage()
    else:
            usage()

if __name__ == '__main__':

    main(sys.argv[1:])

