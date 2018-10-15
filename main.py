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
    name = 'Run'

    def __repr__(self):
        return 'Run away from the battle'

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] -= 1
        return self.player.deal_dmg(dmg_modifiers=[0, 0])


class Poop(Skill):
    name = 'Poop'
    def __repr__(self):
        return 'Max damage points + 2'

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[0, 2])


class Bomb(Skill):
    name = 'bomb'
    def __repr__(self):
        return "Max and min damage points + 3 and you hurt yourself for 3 damage"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] -= 3
        return self.player.deal_dmg(dmg_modifiers=[3, 3])


class Hide(Skill):
    name = 'hide'
    def __repr__(self):
        return "Min hit points + 2"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        self.player.hp[0] += 2
        return self.player.deal_dmg(dmg_modifiers=[0, 0])


class Tangle(Skill):
    name = "tangle"
    def __repr__(self):
        return "Min damage points + 3"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[3, 0])


class Charm(Skill):
    name = "charm"
    def __repr__(self):
        return "Max damage points + 2"

    def __call__(self):
        if not hasattr(self, 'player'):
            raise Exception("Player was not assigned to this skill")

        return self.player.deal_dmg(dmg_modifiers=[0, 2])


class Protect(Skill):
    name="protect"
    def __repr__(self):
        return "Min hit points + 3"

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
            f"what kind of pig do you choose?"
            f"\n{show_choices(choice_dict, mode=1)}").lower()
        if user_input in choice_dict:
            special_skill = choice_dict[user_input].name
            skills[special_skill] = choice_dict[user_input]
            print(
                f"\nYour pig is {user_input} with 4 skills:\n"
                f"{show_choices(skills, mode=2)}"
            )
            return skills

# Make player choose their skills
# Not in player class since we show choices before player instance is created
def show_choices(choice_dict, mode):
    result = ''
    if mode == 1:
        for pig, skill in choice_dict.items():
            result += f"-- {pig} with a skill: {skill.name}\n"
    else:
        for pig, skill in choice_dict.items():
            result += f"-- {pig}: {skill}\n"
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

    # battle.take_place()
    if not event:
        print(player)
        exit("You won the game!")  # Futureproofing
    event.take_place()
