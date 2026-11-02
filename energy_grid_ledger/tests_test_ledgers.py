"""
Unit tests for the energy grid ledger.

This module contains unit tests for the `EnergyGridLedger` class,
ensuring that it behaves as expected in various scenarios.
"""

import unittest
from typing import List, Tuple

class TestLedgers(unittest.TestCase):
    def test_empty_ledger(self) -> None:
        """Test an empty ledger."""
        from energy_grid_ledger.ledger import EnergyGridLedger
        ledger = EnergyGridLedger()
        self.assertEqual(ledger.get_events(), [])

    def test_append_event(self) -> None:
        """Test appending a single event to the ledger."""
        from energy_grid_ledger.ledger import EnergyGridLedger
        ledger = EnergyGridLedger()
        event_id = "event-1"
        data = {"power_load": 100}
        ledger.append(event_id, data)
        self.assertEqual(ledger.get_events(), [(event_id, data)])

    def test_append_multiple_events(self) -> None:
        """Test appending multiple events to the ledger."""
        from energy_grid_ledger.ledger import EnergyGridLedger
        ledger = EnergyGridLedger()
        event_ids: List[str] = ["event-1", "event-2"]
        data: Tuple[dict, dict] = ({"power_load": 100}, {"power_load": 200})
        for event_id, ev_data in zip(event_ids, data):
            ledger.append(event_id, ev_data)
        self.assertEqual(ledger.get_events(), [(event_id, ev_data) for event_id, ev_data in zip(event_ids, data)])

    def test_ledger_hash(self) -> None:
        """Test the hash of an empty ledger."""
        from energy_grid_ledger.ledger import EnergyGridLedger
        ledger = EnergyGridLedger()
        self.assertIsNotNone(ledger.get_hash())

if __name__ == "__main__":
    unittest.main()
