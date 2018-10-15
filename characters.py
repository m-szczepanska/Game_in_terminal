from random import randint


class Character():
    def __init__(self, name, hp, dmg, exp=0, gold=0, lvl=1, items=None):
        """Args:
            name - String
            hp - List, [current_hp, max_hp],
            dmg - List, [min_dmg, max_dmg],
            exp - Integer
            lvl - Integer
            gold - Integer
        """
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.exp = exp
        self.gold = gold
        self.lvl = lvl
        self.items = items or []

    def __repr__(self):
        return str({
            "Name: {}".format(self.name),
            "Hit Points (hp): {}/{}".format(self.hp[0], self.hp[1]),
            "Damage: {}-{}".format(self.dmg[0], self.dmg[1]),
            "Experience: {}".format(self.exp),
            "Gold: {}".format(self.gold),
            "Level: {}".format(self.lvl)
        })

    def is_alive(self):
        return self.hp[0] > 0

    def deal_dmg(self, dmg_modifiers=[0, 0]):
        """
        Args:
            dmg_modifiers: list (of ints) - list describing whether we deal
                more or less dmg
        Returns:
            dmg_dealt: int
        """
        actual_dmg = [
            self.dmg[0] + dmg_modifiers[0], self.dmg[1] + dmg_modifiers[1]
        ]
        dmg_dealt = randint(actual_dmg[0], actual_dmg[1]) #Randomly chosen damage
        print("{} hits for {} damage.".format(self.name, dmg_dealt), end=' ')
        return dmg_dealt

    def take_dmg(self, dmg_taken, hp_modifiers=[0, 0]):
        self.hp[0] += hp_modifiers[0]
        self.hp[1] += hp_modifiers[1]
        self.hp[0] -= dmg_taken
        print("{} takes {} damage and has {}/{} hit points now.".format(
            self.name, dmg_taken, self.hp[0], self.hp[1])
        )

    def get_stats(self):
        return str({
            "Name: {}".format(self.name),
            "Hit Points (hp): {}/{}".format(self.hp[0], self.hp[1]),
            "Damage: {}-{}".format(self.dmg[0], self.dmg[1]),
            "Experience: {}".format(self.exp),
            "Gold: {}".format(self.gold),
            "Level: {}".format(self.lvl)
        })


class Player(Character):
    # TODO: Add get_reward(self, event) method
    def __init__(
            self,
            name,
            hp,
            dmg,
            exp=0,
            gold=0,
            lvl=1,
            items=None,
            skills=None):

        super().__init__(name, hp, dmg, exp, gold, lvl, items)
        self.skills = skills

        for skill_name, skill in skills.items():
            skill.player = self
            setattr(self, skill_name, skill)


    def gain_exp(self, exp):
        self.exp += exp
        print("You gain {} exp. You have {} exp now.".format(exp, self.exp))
        self.player_level_up()

    def player_level_up(self):
        exp_to_level = 4 * self.lvl
        if self.exp >= exp_to_level:
            self.exp -= exp_to_level
            self.dmg[1] += 3
            self.lvl += 1
            self.hp[1] += 10
            self.hp[0] = self.hp[1]
            print("Level up! You can deal to {} damage now!".format(self.dmg[1]))
            self.get_stats()
        else:
            lack_of = exp_to_level - self.exp
            print(f"{lack_of} exp points to next level")


class Monster(Character):
    pass  # TODO: this will be useful later
