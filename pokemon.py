import random

class Pokemon:
  def __init__(self, name, exp=0, level, poke_type, is_ko=False):
    self.name = name
    self.level = level
    self.poke_type = poke_type
    self.max_health = self.level * 20
    self.current_health = current_health
    self.is_ko = is_ko

  def __repr__(self):
    return "Pokemon info: {}, current level: {}, type: {}, maximun health: {},
     current health: {}.\n".format(self.name, self.level, self.poke_type, self.max_health,
      self.current_health)

  def lose_health(self, damage):
    health_rem = self.current_health - damage
    # Check pokemon still has health.
    if health_rem > 0:
      self.current_health = health_rem
      print(f"{self.name.title()} has {health_rem} remaining.")
    else:
      self.knock_out()

  def knock_out(self):
    if self.current_health <= 0:
      print(f"{self.name.title()} has been knocked out.")
      self.is_ko = True

  def revive_pokemon(self):
    self.current_health = round(self.max_health / 2)
    self.is_ko = True
    print(f"{self.name.title()} has been revived with 50% health.")

  def regen_health(self, val):
    val = int(val)
    # Check if sum of val and current health greater than total allow health.
    self.current_health += val
    print(f"{self.name} now has {self.current_health}")
    # time.sleep(1) between print statements to simulate healing over time. Potion?
    pass

  def attack(self, other):
      bonus_dmg = 5
      for p_type in self.poke_type:
          for o_p_type in other.poke_type:
            if self.level < 10:
                # Refactor dmg/poke_type code below into function. DRY
    			if (p_type == 'fire' and o_p_type == 'grass') \
    				or (t == 'grass' and o_p_type == 'water') \
    				or (t == 'water' and o_p_type == 'fire'):
    				damage = (random.randint(1, 6) * 5) + bonus_dmg
    		    elif (p_type == 'grass' and o_p_type == 'fire') \
    			    or (p_type == 'fire' and o_p_type == 'water') \
    			    or (p_type == 'water' and o_p_type == 'grass'):
                    damage = (random.randint(1, 6) * 5) - bonus_dmg

            elif (self.level > 9) and (self.level < 20):
    			if (t == 'fire' and y == 'grass') \
    				or (t == 'grass' and y == 'water') \
    				or (t == 'water' and y == 'fire'):
    				damage = (random.randint(6, 11) * 5) + bonus_dmg
    		    elif (t == 'grass' and y == 'fire') \
    			    or (t == 'fire' and y == 'water') \
    			    or (t == 'water' and y == 'grass'):
                    damage = (random.randint(6, 11) * 5) - bonus_dmg

            elif (self.level > 20) and (self.level < 30):
                if (t == 'fire' and y == 'grass') \
    				or (t == 'grass' and y == 'water') \
    				or (t == 'water' and y == 'fire'):
    				damage = (random.randint(11, 21) * 5) + bonus_dmg
    		    elif (t == 'grass' and y == 'fire') \
    			    or (t == 'fire' and y == 'water') \
    			    or (t == 'water' and y == 'grass'):
                    damage = (random.randint(11, 21) * 5) - bonus_dmg
            else:
                if (t == 'fire' and y == 'grass') \
    				or (t == 'grass' and y == 'water') \
    				or (t == 'water' and y == 'fire'):
    				damage = (random.randint(30, 50) * 5) + bonus_dmg
    		    elif (t == 'grass' and y == 'fire') \
    			    or (t == 'fire' and y == 'water') \
    			    or (t == 'water' and y == 'grass'):
                    damage = (random.randint(30, 50) * 5) - bonus_dmg

    if self.type.lower() == 'fire':
      pass


class Legendary(Pokemon):
    def __init__(self, name, exp=0, level, poke_type, current_health, is_ko=False):
        super().__init__(self, level=5)
