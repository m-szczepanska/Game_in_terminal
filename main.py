from characters import Character, Player, Monster
from events import create_random_event, Battle, BATTLE_EVENTS


# TODO: Move skills to another file; they actually were but I hav issues
# with it so now they're temporarily here.
class Skill:
    def __repr__(self):
        raise NotImplementedError

    def __call__(self):
        raise NotImplementedError


class Run(Skill):
    def __repr__(self):
        return "Run"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] -= 1
        return self.player.deal_dmg(dmg_modifiers=[0, 0])


class Poop(Skill):
    def __repr__(self):
        return "Poop"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[0, 2])


class Bomb(Skill):
    def __repr__(self):
        return "Bomb"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] -= 3
        return self.player.deal_dmg(dmg_modifiers=[3, 3])


class Hide(Skill):
    def __repr__(self):
        return "Hide"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] += 2
        return self.player.deal_dmg(dmg_modifiers=[0, 0])


class Tangle(Skill):
    def __repr__(self):
        return "Tangle"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[3, 0])


class FigureThisOut(Skill):
    def __repr__(self):
        return "FigureThisOut"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[0, 2])


class Protect(Skill):
    def __repr__(self):
        return "Protect"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] += 3
        return self.player.deal_dmg(dmg_modifiers=[0, 0])


# Make player choose their skills
# Not in player class since we show choices before player instance is created
def show_choices(choice_dict):
    result = ''
    for pig, skill in choice_dict.items():
        result += f"-- {pig} with skill: {skill}\n"
    return result

def player_type_choice():
    choice_dict = { # dict with piggies to choose
        "aguti": Hide(),
        "long-haired": Tangle(),
        "skinny": FigureThisOut(),
        "wire-haired": Protect()
    }
    # basic skills for every pig
    skills = {"bomb": Bomb(), "poop": Poop(), "run": Run()}
    while True:
        user_input = input(
            f"what kind of pig do you choose?\n{show_choices(choice_dict)}"
        ).lower()
        if user_input in choice_dict:
            skills["special"] = choice_dict[user_input]
            print(
                f"Your pig is {user_input} with 4 skills:\n"
                f"{show_choices(skills)}"
            )
            return skills

chosen_skills = player_type_choice()

# Create player
player_name = "bob"  # hardcoded for ease of testing
player = Player(
    name = player_name,
    hp=[100, 100],
    dmg=[5, 20],
    skills=chosen_skills
)
monster_1 = Monster(
    "Bearer of Silence",
    hp=[30, 30],
    dmg=[7, 7],
    exp=2,
    gold=9,
    lvl=1,
    items=None
)

battle = Battle(
    BATTLE_EVENTS[0]["description"],
    player=player,
    monster=monster_1,
    exp=monster_1.exp,
    gold=monster_1.gold
)

# Play game
while True:
    event = create_random_event(player)
    battle.take_place()
    if not event:
        print(player)
        exit("You won the game!")  # Futureproofing
    event.take_place()
