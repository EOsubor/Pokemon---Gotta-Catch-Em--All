class Pokemon:
  def __init__(self, name, level, poke_type, current_health, is_ko=False):
    self.name = name
    self.level = level
    self.poke_type = poke_type
    self.max_health = self.level * 5
    self.current_health = current_health
    self.is_ko = is_ko

  def lose_health(self, damage):
    health_rem = self.current_health - damage
    if health_rem > 0:
      self.current_health = health_rem
      print(f"{self.name.title()} has {health_rem} remaining.")
    else:
      self.knock_out()

  def knock_out(self):
    if self.current_health == 0:
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

  def attack(self, pokemon):
    if self.level < 10:
      self.damage = random.randint(1, 5)
    elif (self.level > 9) and (self.level < 20):
      self.damage = random.randint(5, 10)
    elif (self.level > 20) and (self.level < 30):
      self.damage = random.randint(10, 20)
    else:
      self.damage = random.randint(30, 50)

    if self.type.lower() == 'fire':
      pass
