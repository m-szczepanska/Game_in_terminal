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
            print("if result")

def create_random_event(player):
    random_event = EventOther(
        description='what to do',
        choices={"1": True, "2": False},
        player=player,
        exp=1,
        gold=1
    )
    return random_event
