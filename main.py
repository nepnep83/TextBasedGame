import time
import random
from colorama import Fore

available_weapons = ["Fists, Rusty Knife"]
player_name = input(f'{Fore.BLUE}please input your username before continuing 'f'{Fore.WHITE}')
Tutorial = 0
player = 0
room_count = 0
gained_exp = 0
win = "a"
req_exp = 10
player_exp = 0
room10 = 0
player_level = 1
item_mult = 1
weapon = ("Gauntlets")
current_monst = "a"
player_health = 20
max_health = 20
level_mult = player_level * 1.05


class Weapons():
  def melee(player_weapon, level_mult):
    global item_mult
    global melee_dmg
    melee_dmg = float(player_weapon) * float(item_mult) * float(level_mult)

    
  def ranged():
    global ranged_dmg
    global item_mult

  def magic():
    global magic_dmg
    global level_mult
        

  def DOT():
    global magic_dmg
    global melee_dmg
    global DOT_pois
    global DOT_fire
    global DOT_bleed
    global DOT_dmg


class monsters():
  def goblin():
    global item_mult
    global monster_level
    global mons_health
    global mons_dmg
    monster_level = player_level + random.randint(-1, 2)
    if monster_level < 1:
      monster_level = 1
    monster_level_mult = monster_level * 1.02
    mons_health = 10 * monster_level_mult
    def mons_dmg():
      global mons_dmg
      mons_dmg = random.randint(1, 2) * monster_level_mult
    mons_dmg()

  
def weapon_dmg():
  global player_weapon
  global weapon
  weapons = {
    'Fists': random.randint(1, 3),
    'Rusty knife': random.randint(2, 4),
    "Shortsword": random.randint(5, 7),
    "Longsword": random.randint(10, 15),
    'Gauntlets': random.randint(1000, 1500),
  }
  player_weapon = weapons[weapon]

  
def chosen_weapon():
    global player_weapon
    global weapon
    print("What weapon would you like?")
    weapon = input(available_weapons).capitalize()

def battle():
  global player_exp
  global gained_exp
  global mons_health
  global player_health
  global mons_dmg
  global melee_dmg
  global player_weapon
  global level_mult
  while mons_health >= 1:
    weapon_dmg()
    Weapons.melee(player_weapon, level_mult)
    mons_health -= melee_dmg
    print(f"{Fore.CYAN}you did", round(melee_dmg), "damage.")
    print(f"{Fore.YELLOW}the monster has", round(mons_health)," health left")
    time.sleep(1)
    if mons_health >= 1:
      player_health -= mons_dmg
      print(f"{Fore.RED}you took", round(mons_dmg), "damage.")
      print(f"{Fore.LIGHTGREEN_EX}you have", round(player_health),"health left.")
      time.sleep(1)
      if player_health <= 0:
        print (f'{Fore.RED}You died')
        quit()
    if mons_health < 1:
      gained_exp = random.randint(monster_level - 1, monster_level + 2)
      if gained_exp < 1:
        gained_exp = 1
        player_exp += gained_exp
      else:
        player_exp += gained_exp
      print("You killed the monster! well done.")
      time.sleep(1)
      print("you gained", gained_exp, "exp points")
      time.sleep(1)
      player_lvl()
      print("You have", player_exp, "exp")
      print("you healed 10 health" f'{Fore.BLUE}')
      Weapon_change = input ("Would you like to change your weapon?").capitalize()
      gained_exp = 0
      player_health += 10
      if Weapon_change == 'Yes' or Weapon_change == 'yes' or Weapon_change == 'Y' or Weapon_change == 'y':
        chosen_weapon()
      if player_health > max_health:
        player_health = max_health
        time.sleep(2)


def player_lvl():
    global player_level
    global level_mult
    global req_exp
    global player_exp
    if player_exp >= req_exp:
        player_level += 1
        print("You leveled up! you are now level", player_level)
        player_exp -= req_exp
        player_hth()
        req_exp = (req_exp * random.randint(15, 20)) / 10


def player_hth():
    global player_health
    global max_health
    max_health = (player_level * 10) + 10
    player_health = max_health


def tutorial():
    global Tutorial
    print(f'{Fore.LIGHTGREEN_EX}\nEach room will have different challenges you have to complete. ')
    time.sleep(5)
    print("\nThis could be fighting monsters, solving puzzles or finding specified items. ")
    time.sleep(6)
    print("\nLEVEL 1 GOBLIN SPAWNED \nThis is a goblin, goblins are one of the weakest monsters in the game.")
    time.sleep(5)
    print("\nEach monster has different health, damage and resistances. ")
    time.sleep(4)
    print("\ndespithe the goblin being one of the weakest monsters, all monsters scale with level aswell as the items they have so don't underestimate anything you fight.")
    time.sleep(11)
    print("\nWith the right equiptment a higher level goblin can be quite strong so don't underestimate them.")
    time.sleep(7)
    print("\nEvery non-boss monster you fight has a chance to drop the items they hold. ")
    time.sleep(5)
    print('\nWell enough talking, lets try fighting a monster!')
    time.sleep(4)
    Tutorial = 0
    Room_1()


def Start():
    global player
    global Tutorial
    player = 1

    print(f"{Fore.BLUE}welcome to the game",player_name + "! You have entered your first room. ")
    time.sleep(5)
    Tutorial = input("would you like to try the tutorial? " f'{Fore.WHITE}')
    if Tutorial == "Y" or Tutorial == "y" or Tutorial == "yes" or Tutorial == "Yes":
        Tutorial = 1
        print(f"{Fore.BLUE}Okay time to begin the tutorial. ")
        time.sleep(4)
    else:
        Tutorial = 0
        print("Okay time to begin the game. ")


def Room_1():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_2():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_3():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_4():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_5():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_6():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_7():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_8():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_9():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    room_count += 1


def Room_10():
    global room_count
    monsters.goblin()
    print("LEVEL", monster_level, "GOBLIN SPAWNED")
    time.sleep(2)
    #weap = input("please select your weapon.")
    battle()

    global room10
    room_count += 1
    room10 += 1


while win != "win":
    if Tutorial == 1:
        tutorial()
    if player == 0:
        Start()
    else:
        player = random.randint(1, 2)
        if player == 1:
            Room_1()
        elif player == 2:
            Room_2()
        elif player == 3:
            Room_3()
        elif player == 4:
            Room_4()
        elif player == 5:
            Room_5()
        elif player == 6:
            Room_6()
        elif player == 7:
            Room_7()
        elif player == 8:
            Room_8()
        elif player == 9:
            Room_9()
        elif player == 10:
            if room_count >= 5:
                Room_10()
            else:
                print("")
    while room10 == 1:
        room10 += 1
        print("You have finished the game!")
        cont = input("Would you like to continue playing?")
        if cont == "Y" or cont == "y" or cont == "yes" or cont == "Yes":
            print("The game will now continue.")
        else:
            print("Thanks for playing, the game will now end.")
            win = "win"