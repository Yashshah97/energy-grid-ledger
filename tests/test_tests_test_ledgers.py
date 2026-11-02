import unittest
from energy_grid_ledger import tests_test_ledgers

class TestTestLedgers(unittest.TestCase):
    def test_import(self) -> None:
        """Test importing the `tests_test_ledgers` module."""
        self.assertIsNotNone(tests_test_ledgers)

if __name__ == "__main__":
    unittest.main()
