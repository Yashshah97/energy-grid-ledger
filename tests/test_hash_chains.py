import unittest
from energy_grid_ledger import hash_chains

class TestHashChain(unittest.TestCase):
    def test_hash_chain_append(self):
        ledger = hash_chains.HashChain()
        new_hash = ledger.append("Event 1")
        self.assertIsInstance(new_hash, str)
        self.assertEqual(ledger.get_log(), [("a" * 64, "Event 1")])

    def test_hash_chain_append_multiple_events(self):
        ledger = hash_chains.HashChain()
        new_hash_1 = ledger.append("Event 1")
        new_hash_2 = ledger.append("Event 2")
        self.assertEqual(ledger.get_log(), [(new_hash_1, "Event 1"), (new_hash_2, "Event 2")])

    def test_hash_chain_append_event_not_string(self):
        ledger = hash_chains.HashChain()
        with self.assertRaises(ValueError):
            ledger.append(123)

if __name__ == "__main__":
    unittest.main()
