import random
from characters import Player, Monster


OTHER_EVENTS = [
    {
        "description": "Other event 1, choose 1 ",
        "choices": {"1": True, "2": False},
        "exp": 1,
        "gold": 1
    },
    {
        "description": "Other event 2, choose 1 ",
        "choices": {"1": True, "2": False},
        "exp": 3,
        "gold": 4
    },
    {
        "description": "Other event 3, choose 1 ",
        "choices": {"1": True, "2": False},
        "exp": 5,
        "gold": 9
    }
]

BATTLE_EVENTS = [
    {
        "description": "Hey, fighting is coming, choose a skill: "
    }

]

class BaseEvent():
    def __init__(self, exp=0, gold=0, items=None, *args, **kwargs):
        self.exp = exp
        self.gold = gold
        self.items = items or []


class Battle(BaseEvent):
    def __init__(self, description, player, monster, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = description
        self.choices = player.skills
        self.player = player
        self.monster = monster

    def get_user_input(self):
        while True:
            user_input = input(self.description).lower()
            if user_input in self.choices:
                return self.choices[user_input]

    def basic_fight(self, chosen_skill):
        # if chosen_skill.name is "run"
        #     TODO: make this a special case
        dmg_dealt = chosen_skill()
        self.monster.take_dmg(dmg_dealt)
        if self.monster.is_alive():
            dmg_dealt = self.monster.deal_dmg()
            self.player.take_dmg(dmg_dealt)
        else:
            return(self.player.name, "wins the combat")

    def take_place(self):
        # TODO: Print description just once at the beginning and then print
        # player skills in get_user_input
        while self.player.is_alive() and self.monster.is_alive():
            chosen_skill = self.get_user_input()
            print(chosen_skill)
            if chosen_skill:
                self.basic_fight(chosen_skill)
        # TODO: Give player exp/gold after winning?


class EventOther(BaseEvent):
    def __init__(self, description, choices, player, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = description
        self.choices = choices
        self.player = player

    def get_user_input(self):
        while True:
            user_input = input(self.description).lower()
            if user_input in self.choices:
                return self.choices[user_input]

    def take_place(self):
        result = self.get_user_input()
        if result:
            self.player.gold += self.gold
            self.player.exp += self.exp
            print("Gained gold:", self.player.gold, "and exp:",self.player.exp)


def create_other_event(player, events=OTHER_EVENTS):
    if not events:
        return None
    random_num = random.randint(0, (len(events)-1))
    random_dict = events[random_num]
    random_event = EventOther(
        description=random_dict["description"],
        choices= random_dict["choices"],
        player=player,
        exp=random_dict["exp"],
        gold=random_dict["gold"]
    )
    return random_event

def create_random_event(player, events=OTHER_EVENTS):
    # TODO: Make this create battles or other events randomly
    # TODO: Consider "popping" so that we run out of events in the end
    # if cointoss:
    event = create_other_event(player, events=OTHER_EVENTS)
    # else:
    # event = create_battle_event()
    return event
