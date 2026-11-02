import unittest
from energy_grid_ledger import events

class TestEvent(unittest.TestCase):

    def test_init(self):
        event = events.Event("123", 1643723400, {"key": "value"})
        self.assertEqual(event.id, "123")
        self.assertEqual(event.timestamp, 1643723400)
        self.assertEqual(event.data, {"key": "value"})

    def test_repr(self):
        event = events.Event("123", 1643723400, {"key": "value"})
        self.assertEqual(repr(event), "Event(id='123', timestamp=1643723400, data={'key': 'value'})")

    def test_eq(self):
        event1 = events.Event("123", 1643723400, {"key": "value"})
        event2 = events.Event("123", 1643723400, {"key": "value"})
        self.assertTrue(event1 == event2)
        self.assertFalse(events.Event("456", 1643723400, {"key": "value"}) == event1)

    def test_hash(self):
        event = events.Event("123", 1643723400, {"key": "value"})
        self.assertEqual(hash(event), hash((event.id, event.timestamp, event.data)))

if __name__ == "__main__":
    unittest.main()
