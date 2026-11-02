import unittest
from energy_grid_ledger import core

class TestCoreModule(unittest.TestCase):

    def test_create_event(self):
        event = core.create_event(1643723400, {'key': 'value'})
        self.assertIsInstance(event, core.Event)
        self.assertEqual(event.timestamp, 1643723400)
        self.assertEqual(event.data, {'key': 'value'})

    def test_create_ledger(self):
        ledger = core.create_ledger()
        self.assertIsInstance(ledger, core.Ledger)

    def test_add_event_to_ledger(self):
        ledger = core.create_ledger()
        event = core.create_event(1643723400, {'key': 'value'})
        ledger.add_event(event)
        self.assertEqual(len(ledger.events), 1)
        self.assertEqual(ledger.events[0].hash, event.hash)

    def test_get_event_from_ledger(self):
        ledger = core.create_ledger()
        event = core.create_event(1643723400, {'key': 'value'})
        ledger.add_event(event)
        retrieved_event = ledger.get_event(0)
        self.assertEqual(retrieved_event.timestamp, 1643723400)
        self.assertEqual(retrieved_event.data, {'key': 'value'})

if __name__ == '__main__':
    unittest.main()
