# magic-missile
D&amp;D (5th edition) Magic Missile spell in Python, cast the spell with one die, or a die for each dart, depending on your persuasion

- why ? A wizard overheard some friends shooting-the-breeze about whether magic-missile should be cast with one d20 and the result applied to each dart, or a d20 should be rolled for each dart and result per die rolled applied to each dart. This gave the wizard an itch to scratch and so he wrote some python code.

- For those not familar and left utterly confused, see: https://www.dndbeyond.com/spells/magic-missile

#### Disclaimer, this is code, not magic, unlike magic there may be bugs and silly things lurking.

## Examples of use:

```
wizard@dev magic-missile]$ ./cast_magic_missile.py 
Usage: cast_magic_missile.py <spell-slot level> <spell-mode>
       spell-slot level must be an integer
       spell-mode either 'roll_die' or 'roll_dice'
           roll_die, rolls 1 die and result applied to each dart
           roll_dice, rolls a die for each dart
[wizard@dev magic-missile]$
```

```
wizard@dev magic-missile]$ ./cast_magic_missile.py 0 roll_die
You clearly have no magic ability, and are utterly weak
[wizard@dev magic-missile]$ 
```

```
[wizard@dev magic-missile]$ ./cast_magic_missile.py 1 roll_die
darts_fired: 3
base_damage: 1
damage_per_dart: 2
total_damage: 6
[wizard@dev magic-missile]$
```

```
[wizard@dev magic-missile]$ ./cast_magic_missile.py 3 roll_dice
darts_fired: 5
base_damage_by_dart: {'dart_1': 4, 'dart_2': 2, 'dart_3': 3, 'dart_4': 2, 'dart_5': 4}
total_damage_by_dart: {'dart_1': 5, 'dart_2': 3, 'dart_3': 4, 'dart_4': 3, 'dart_5': 5}
total_damage_all_darts: 20
[wizard@bitdev magic-missile]$ 
```

