class Character():
    # TODO: Add get_reward(self, event) method
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
