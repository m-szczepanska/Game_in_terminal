from characters import Character
from events import create_random_event


jimmy = Character(
    name='James',
    hp=[100, 100],
    dmg=[50, 80]
)

while True:
   event = create_random_event(jimmy)
   if not event:
       print(jimmy)
       exit("You won the game!")  # Futureproofing
   event.take_place()
