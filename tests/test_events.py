from unittest import TestCase
from unittest.mock import patch

from events import create_random_event, EventOther


# TODO: Add more tests...
class TestEventOthers(TestCase):
    def setUp(self):
        self.events = [
            {
                "description": "testing",
                "choices": {"1": True, "2": False},
                "exp": 150,
                "gold": 15
            }
        ]

    def test_create_random_event(self):
        result = create_random_event(player="test_player", events=self.events)

        self.assertEqual(result.description, self.events[0]['description'])
        self.assertEqual(result.choices, self.events[0]['choices'])
        self.assertEqual(result.exp, self.events[0]['exp'])
        self.assertEqual(result.gold, self.events[0]['gold'])
        self.assertEqual(result.player, "test_player")

    def test_create_random_event_empty_events(self):
        result = create_random_event(player="test_player", events=[])

        self.assertEqual(result, None)

    @patch('events.random')
    def test_not_real_test_just_checking_patch_out(self, random_patched):
        random_patched.randint.return_value = 1
        new_event = {
            "description": "this should happen",
            "choices": {"10": True, "20": False},
            "exp": 300,
            "gold": 60
        }
        self.events.append(new_event)
        result = create_random_event(player="test_player", events=self.events)

        self.assertEqual(result.description, new_event['description'])
        self.assertEqual(result.choices, new_event['choices'])
        self.assertEqual(result.exp, new_event['exp'])
        self.assertEqual(result.gold, new_event['gold'])
        self.assertEqual(result.player, "test_player")
#
    @patch('events.input')
    def test_user_input(self, input_patched):
        input_patched.return_value = "yes"
        result = EventOther(description="desc",
        choices={"yes": "good test", "6": False},
        player="test_player").get_user_input()

        self.assertTrue(result, "good test")


    # @patch('events.EventOther.get_input', return_value='yes')
    # def test_answer_yes(self, input):
    #     self.assertEqual(EventOther(description="desc",
    #     choices={"yes": "good test", "6": False},
    #     player="test_player").get_user_input(), 'good test')
