from characters import Character
from events import create_random_event

jimmy = Character(
    name='James',
    hp=[100, 100],
    dmg=[50, 80]
)
while True:
   event = create_random_event(jimmy)
   event.take_place()
