import random


OTHER_EVENTS = [
    {
        "description": "what to do now",
        "choices": {"1": True, "2": False},
        "exp": 1,
        "gold": 1
    },
    {
        "description": "what ",
        "choices": {"1": True, "2": False},
        "exp": 3,
        "gold": 4
    },
    {
        "description": "three ",
        "choices": {"1": True, "2": False},
        "exp": 5,
        "gold": 9
    }
]


class BaseEvent():
    def __init__(self, exp=0, gold=0, items=None, *args, **kwargs):
        self.exp = exp
        self.gold = gold
        self.items = items or []


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
            # TODO: Make this self.player.get_reward(self)
            self.player.gold += self.gold
            self.player.exp += self.exp
            print("gold ", self.player.gold)


def create_random_event(player, events=OTHER_EVENTS):
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
