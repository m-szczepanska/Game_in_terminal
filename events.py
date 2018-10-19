import random
from characters import Player, Monster
from monsters_list import MONSTERS_DICT


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

BATTLE_DESCRIPTS = [
    "First fight. Choose a skill to fight : ",
    "Gonna fight, choose skill: ",
    "Let your pigge fight: ",
    "Let's go: ",
    "Fifth fight: "
]


class BaseEvent():
    def __init__(self, exp=0, gold=0, items=None, *args, **kwargs):
        self.exp = exp
        self.gold = gold
        self.items = items or []


class Battle(BaseEvent):
    check_list = []

    def __init__(self, description, player, monster, battle_ongoing=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.description = description
        self.choices = player.skills
        self.player = player
        self.monster = monster
        self.battle_ongoing = battle_ongoing

    def first_print_skills_during_battle(self):
        print(f"Fight's ahead, choose a skill to beat the {self.monster.name}")
        for skill, skill_name in self.player.skills.items():
            print(skill, "--", skill_name)
        return ">> "
    def another_print_skills_during_battle(self):
        print(f"{self.monster.name} is unbeaten yet. Choose skill to fight: ")
        for skill, skill_name in self.player.skills.items():
            print(skill, "--", skill_name)
        return ">> "

    def get_user_input(self):
        while True:
            if self.monster.name in self.check_list:
                user_input = input(self.another_print_skills_during_battle()).lower()
                if user_input in self.choices:
                    return self.choices[user_input]
            else:
                user_input = input(self.first_print_skills_during_battle()).lower()
                if user_input in self.choices:
                    self.check_list.append(self.monster.name)
                    return self.choices[user_input]

    def basic_fight(self, chosen_skill):
        if chosen_skill.name == 'Run':
            print("You ran away")
            self.battle_ongoing = False
        else:
            dmg_dealt = chosen_skill()
            self.monster.take_dmg(dmg_dealt)
            if self.monster.is_alive():
                dmg_dealt = self.monster.deal_dmg()
                self.player.take_dmg(dmg_dealt)

    def take_place(self):
        # TODO: Print description just once at the beginning and then print
        while self.player.is_alive() and self.monster.is_alive() and self.battle_ongoing:
            chosen_skill = self.get_user_input()
            self.basic_fight(chosen_skill)
        if self.monster.is_alive() == False:
            print("you won the battle")
            self.player.gain_exp(self.monster.exp)
            self.player.gold += self.monster.gold
            print(
                "Gained gold:", self.monster.gold, "and exp:", self.monster.gold
            )

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
            self.player.gain_exp(self.gold)
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

def choose_battle(player, MONSTERS_DICT, BATTLE_DESCRIPTS):
    if not MONSTERS_DICT:
        return None
    # random_num = random.randint(0, (len(MONSTERS_DICT)-1))
    chosen_monster = MONSTERS_DICT[0]
    # random_monster = MONSTERS_DICT[random_num]
    MONSTERS_DICT.pop(0)
    chosen_descript = BATTLE_DESCRIPTS[0]
    BATTLE_DESCRIPTS.pop(0)
    battle_event = Battle(
        chosen_descript,
        player=player,
        monster=Monster(
            name=chosen_monster["name"],
            hp=chosen_monster["hp"],
            dmg=chosen_monster["damage"],
            exp=chosen_monster["exp"],
            gold=chosen_monster["gold"]
        ),
        exp=chosen_monster["exp"],
        gold=chosen_monster["gold"]
    )
    return battle_event

def create_random_event(player, BATTLE_DESCRIPTS, MONSTERS_DICT, OTHER_EVENTS):
    battle_or_other_event = random.choice(["Battle", "Other_event"])
    if battle_or_other_event == "Other_event":
        event = create_other_event(player, events=OTHER_EVENTS)
    else:
        event = choose_battle(player, MONSTERS_DICT, BATTLE_DESCRIPTS)
    return event
