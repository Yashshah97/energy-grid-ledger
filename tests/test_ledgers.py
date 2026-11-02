import unittest
from energy_grid_ledger import ledgers

class TestLedger(unittest.TestCase):
    def test_append(self):
        ledger = ledgers.Ledger()
        event_data1 = {'timestamp': 1643723400, 'data': 'Event data'}
        event_data2 = {'timestamp': 1643723410, 'data': 'Another event'}

        hash1 = ledger.append(event_data1)
        hash2 = ledger.append(event_data2)

        self.assertEqual(ledger.get_events(), [
            {
                'timestamp': 1643723400,
                'data': 'Event data',
                'hash': hash1
            },
            {
                'timestamp': 1643723410,
                'data': 'Another event',
                'hash': hash2
            }
        ])

    def test_get_events(self):
        ledger = ledgers.Ledger()
        event_data = {'timestamp': 1643723400, 'data': 'Event data'}
        ledger.append(event_data)

        self.assertEqual(ledger.get_events(), [
            {
                'timestamp': 1643723400,
                'data': 'Event data',
                'hash': ledgers.Ledger()._calculate_hash(event_data)
            }
        ])

if __name__ == '__main__':
    unittest.main()
