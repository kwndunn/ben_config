# Sample configuration parser for Ben

# set up our parser and import our configuration file
from configparser import ConfigParser
parser = ConfigParser()
parser.read('monsters.conf')

# create an empty dictionary to hold our monster list
monsters = {}

# define our Monster class
class Monster(object):
    # these values are required when the object is created
    def __init__(self, name, max_hp, weapon):
        self.name = name
        self.max_hp = max_hp
        self.weapon = weapon

# loop over the list of monsters
for monster in parser.sections():
    # create a new instance of a Monster and store it in the monsters list
    monsters[monster] = Monster(
            name = monster,
            max_hp = parser.get(monster, "max_hp"),
            weapon = parser.get(monster, "weapon")
    )

# this basically does the following for each of the monsters
# monsters["Slime"] = Monster(
#     name = "Slime",
#     max_hp = 2
#     weapon = slime
#)


# print out a table of monsters
# \t represents a tab
print("----------------------")
print("Name\tHP\tWeapon")
print("----------------------")

# our monster objects are values stored in the monsters dictionary
# here we loop over them and print their attributes
for monster in monsters.values():
    # the first {} is filled in by the first variable after format and so on
    print("{}\t{}\t{}\t".format(monster.name, monster.max_hp, monster.weapon))
