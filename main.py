from characters import Character, Player, Monster
from events import create_random_event, BATTLE_DESCRIPTS, OTHER_EVENTS
from monsters_list import MONSTERS_DICT


# TODO: Move skills to another file; they actually were but I hav issues
# with it so now they're temporarily here.
class Skill:
    def __repr__(self):
        raise NotImplementedError

    def __call__(self):
        raise NotImplementedError


class Run(Skill):
    name = 'run'

    def __repr__(self):
        return "Run"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] -= 1
        print("run away")


class Poop(Skill):
    name = 'poop'
    def __repr__(self):
        return "Poop"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[0, 2])


class Bomb(Skill):
    name = 'bomb'
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


class Charm(Skill):
    def __repr__(self):
        return "Charm"

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


def player_type_choice():
    choice_dict = { # dict with piggies to choose
        "aguti": Hide(),
        "long-haired": Tangle(),
        "skinny": Charm(),
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

# Make player choose their skills
# Not in player class since we show choices before player instance is created
def show_choices(choice_dict):
    result = ''
    for pig, skill in choice_dict.items():
        result += f"-- {pig} with skill: {skill}\n"
    return result


chosen_skills = player_type_choice()

# Create player
player_name = "bob"  # hardcoded for ease of testing
player = Player(
    name = player_name,
    hp=[100, 100],
    dmg=[5, 20],
    skills=chosen_skills
)

# Play game
while True:
    event = create_random_event(
        player,
        BATTLE_DESCRIPTS,
        MONSTERS_DICT,
        events=OTHER_EVENTS
    )
    if not event:
        print(player)
        exit("You won the game!")  # Futureproofing
    event.take_place()
